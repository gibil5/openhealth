# -*- coding: utf-8 -*-
#
# 	PaymentMethod 
#
from openerp import models, fields, api


#from . import ord_vars
from . import pm_vars


class PaymentMethod(models.Model):
	
	#_inherit='openhealth.sale_document'
	_name = 'openhealth.payment_method'





# ----------------------------------------------------------- Locked ------------------------------------------------------

	# States 
	READONLY_STATES = {
		'draft': 		[('readonly', False)], 
		#'payment': 	[('readonly', True)], 
		#'generated': 	[('readonly', True)], 
		'sale': 		[('readonly', False)], 
		'done': 		[('readonly', True)], 	
	}



	# Lines 
	pm_line_ids = fields.One2many(
			'openhealth.payment_method_line',
			'payment_method',
			string="Pago #", 
			
			states=READONLY_STATES, 
		)


	# Total 
	total = fields.Float(
			string = 'Total a pagar', 
			required=True, 

			states=READONLY_STATES, 
			
			#states={	
			#		'draft': [('readonly', False)], 
			#		'sale': [('readonly', False)], 
			#		'done': [('readonly', True)], 
			#	}, 
		)


	# Saledoc 
	saledoc = fields.Selection(
			string="Tipo", 

			selection=pm_vars._sale_doc_type_list, 
			
			states=READONLY_STATES, 

			#states={	
			#		'draft': [('readonly', False)], 
			#		'sale': [('readonly', False)], 
			#		'done': [('readonly', True)], 
			#	}, 
		)



	# DNI 
	dni = fields.Char(
			'DNI', 
			states=READONLY_STATES, 
		)


	# Firm 
	firm = fields.Char(
			'Razón social',
			states=READONLY_STATES, 
		)


	# Ruc
	ruc = fields.Char(
			'Ruc', 
			states=READONLY_STATES, 
		)




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

							#('paid', 'Pagado'),
							('sale', 'Pagado'),
							
							#('done', 'Confirmado'),
							('done', 'Completo'),

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
				#record.state = 'paid'
				record.state = 'sale'
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


		# Change Order State to Sent 
		self.order.state = 'sent'
		
		return self.order.open_myself() 
	# go_back













# ----------------------------------------------------------- Primitives ------------------------------------------------------



	# Order 
	order = fields.Many2one(
			'sale.order',
			string="Venta",
			ondelete='cascade', 
			required=True, 
			readonly=True, 
		)












	# Date created 
	date_created = fields.Datetime(
			string="Fecha", 
			required=True, 

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
			#self.state = 'paid'
			self.state = 'sale'

	# _onchange_saledoc












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

		#print 'jx'
		#print 'Payment Method  - Write'
		#print vals
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
	# write 




	# Create 
	@api.model
	def create(self,vals):
		#print 'Payment Method - Create Override'
		#print vals
		
		#Write your logic here
		res = super(PaymentMethod, self).create(vals)
		#Write your logic here

		return res
	# create 

