# -*- coding: utf-8 -*-
#
# 	PaymentMethod 


from openerp import models, fields, api
from . import ord_vars

class PaymentMethod(models.Model):
	
	#_inherit='openhealth.sale_document'
	_name = 'openhealth.payment_method'




# ----------------------------------------------------------- Computes ------------------------------------------------------

	# Name 
	name = fields.Char(
			string="Pagos", 

			compute='_compute_name', 
		)
	@api.multi
	def _compute_name(self):

		for record in self:
			record.name = 'PA-' + str(record.id).zfill(6)



	# state 
	state = fields.Selection(
			selection = [
							('draft', 'Inicio'),
							('paid', 'Pagado'),
							('done', 'Confirmado'),
						], 
			string='Estado',	
			default='draft',

			compute="_compute_state",
		)


	@api.multi
	#@api.depends('state')
	def _compute_state(self):

		for record in self:
			record.state = 'draft'
			if record.balance == 0.0		and		record.saledoc != False:
				record.state = 'paid'
			if record.confirmed:
				record.state = 'done'








	# Balance 
	balance = fields.Float(
			string = 'Saldo', 
			#required=True, 
			readonly=True, 

			default=0, 

			#compute="_compute_balance",
		)

	#@api.multi
	#def _compute_balance(self):		
	#	for record in self:
	#		record.balance = record.total - record.pm_total 







	# Nr Payments
	nr_pm = fields.Char(

			default=2, 

			#compute="_compute_nr_pm",
		)

	#@api.multi
	#@api.depends('date_order')
	#def _compute_nr_pm(self):
	#	for record in self:
	#		nr = record.env['openhealth.payment_method_line'].search_count([('payment_method','=', record.id),]) 
	#		record.nr_pm = str(nr + 1)






	@api.onchange('pm_line_ids')
	def _onchange_pm_line_ids(self):

		pm_total = 0
		
		ctr = 1

		for line in self.pm_line_ids:
				pm_total = pm_total + line.subtotal
				ctr = ctr + 1 

		self.balance = self.total - pm_total 
		self.nr_pm = ctr









# ----------------------------------------------------------- Actions ------------------------------------------------------
	# go_back
	@api.multi 
	def go_back(self):
		self.confirmed = True 
		return self.order.open_myself() 
	# go_back








# ----------------------------------------------------------- Constants ------------------------------------------------------
	# States 
	READONLY_STATES = {
		'draft': 		[('readonly', False)], 
		'payment': 		[('readonly', True)], 
		#'generated': 	[('readonly', True)], 
		'done': 		[('readonly', True)], 	
	}





# ----------------------------------------------------------- Primitives ------------------------------------------------------



	# Order 
	order = fields.Many2one(
			'sale.order',
			string="Venta",
			ondelete='cascade', 
			required=True, 
			readonly=True, 
		)









	# Total 
	total = fields.Float(
			string = 'Total a pagar', 
			required=True, 

			#states=READONLY_STATES, 
		)



	# Date created 
	date_created = fields.Datetime(
			string="Fecha", 
			required=True, 

			#states=READONLY_STATES, 
		)



	# Saledoc 
	saledoc = fields.Selection(
			string="Tipo", 
			selection=ord_vars._sale_doc_type_list, 
			
			#states=READONLY_STATES, 
		)



	# Pm Lines 
	pm_line_ids = fields.One2many(
			'openhealth.payment_method_line',
			'payment_method',
			string="Pago #", 
			
			#states=READONLY_STATES, 
		)



	confirmed = fields.Boolean(
			default=False, 
			readonly=True, 
			string="Confirmado", 
		)











	# Partner 
	partner = fields.Many2one(
			'res.partner',
			string = "Cliente", 
			required=True, 
			readonly=True, 
		)
	dni = fields.Char(
			'DNI', 
		)
	firm = fields.Char(
			'Razón social',
		)
	ruc = fields.Char(
			'Ruc', 
		)





	# Vspace 
	vspace = fields.Char(
			' ', 
			readonly=True
		)



	# Comment 
	#comment = fields.Text()




# ----------------------------------------------------------- On changes ------------------------------------------------------

	# On change Sale Doc 
	@api.onchange('saledoc')
	def _onchange_saledoc(self):

		# State 
		if self.balance == 0.0:
			self.state = 'paid'



		# Generate Name
		#pre = {
		#		'receipt':	'BO-1-', 
		#		'invoice':	'FA-1-', 
		#		'advertisement':	'CP-1-', 
		#		'sale_note':		'CN-1-', 
		#		'ticket_receipt':	'TKB-1-', 
		#		'ticket_invoice':	'TKF-1-', 
		#}
		#counter = self.env['openhealth.counter'].search([('name', '=', self.saledoc)])
		#name = pre[self.saledoc] + str(counter.value).rjust(4, '0')
		#self.saledoc_code = name











	# Create Pm
	@api.multi 
	def create_pm_line(self):

		#print 
		#print 'Create Pm Line'

		name = self.nr_pm

		method = 'cash'
		
		balance = self.balance

		payment_method_id = self.id

		return {
				'type': 'ir.actions.act_window',
				'name': ' New PM Line Current', 
				'view_type': 'form',
				'view_mode': 'form',	
				#'target': 'current',
				'target': 'new',
				#'target': 'inline',
				'res_model': 'openhealth.payment_method_line',				
				#'res_id': payment_method_id,
				'flags': 	{
							#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
							'form': {'action_buttons': True, }
							},
				'context': {
							'default_payment_method': payment_method_id,
							'default_name': name,
							'default_method': method,
							'default_subtotal': balance,
							#'default_payment_method_id', payment_method_id,
							#'default_order': self.id,
							#'default_total': self.x_amount_total,
							#'default_pm_total': self.pm_total,
						}
				}
	# create_pm_line











	# ----------------------------------------------------------- CRUD ------------------------------------------------------

	# Write 
	@api.multi
	def write(self,vals):

		print 'jx'
		print 'Payment Method  - Write'
		#print 
		print vals
		#print self.partner.name



		# Update Partner 
		if 'dni' in vals: 
			dni = vals['dni']
			self.partner.x_dni = dni 

		if 'ruc' in vals: 
			ruc = vals['ruc']
			self.partner.x_ruc = ruc 

		if 'firm' in vals: 
			firm = vals['firm']
			self.partner.x_firm = firm 



		#Write your logic here
		res = super(PaymentMethod, self).write(vals)
		#Write your logic here

		return res




	# Create 
	@api.model
	def create(self,vals):
		#print 'Payment Method - Create Override'
		#print vals
		
		#Write your logic here
		res = super(PaymentMethod, self).create(vals)
		#Write your logic here

		return res

