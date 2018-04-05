# -*- coding: utf-8 -*-
#
# 	PaymentMethod 
# 

from openerp import models, fields, api
from . import ord_vars

class PaymentMethod(models.Model):
	
	#_inherit='openhealth.sale_document'

	_name = 'openhealth.payment_method'







# ----------------------------------------------------------- Constants ------------------------------------------------------
	# States 
	READONLY_STATES = {
		'draft': 		[('readonly', False)], 
		'payment': 		[('readonly', True)], 
		'generated': 	[('readonly', True)], 
		'done': 		[('readonly', True)], 	
	}



# ----------------------------------------------------------- Primitives ------------------------------------------------------


	# Comment 
	comment = fields.Text(

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
			string="Documento de Pago", 
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







	# Dni
	dni = fields.Char(
			'DNI', 

		)


	# Firm
	firm = fields.Char(
			'Razón social',

		)


	# Ruc
	ruc = fields.Char(
			'Ruc', 

		)




	# Partner 
	partner = fields.Many2one(
			'res.partner',
			string = "Cliente", 
			required=True, 

			readonly=True, 
		)







# ----------------------------------------------------------- On changes ------------------------------------------------------

	# On change Sale Doc 
	@api.onchange('saledoc')
	def _onchange_saledoc(self):
		#print 'jx'
		#print 'onchange - Saledoc'

		# State 
		#if self.balance == 0.0		and		self.saledoc != False:
		if self.balance == 0.0:
			self.state = 'payment'




		# Generate Name
		pre = {
				'receipt':	'BO-1-', 
				'invoice':	'FA-1-', 
				'advertisement':	'CP-1-', 
				'sale_note':		'CN-1-', 
				'ticket_receipt':	'TKB-1-', 
				'ticket_invoice':	'TKF-1-', 
		}


		counter = self.env['openhealth.counter'].search([('name', '=', self.saledoc)])


		name = pre[self.saledoc] + str(counter.value).rjust(4, '0')


		#self.saledoc_code = name














	# Total Paid
	pm_total = fields.Float(
			string = 'Total pagado', 
			required=True, 

			default=0, 
			compute="_compute_pm_total",
		)

	@api.multi
	#@api.depends('total', 'pm_total')
	def _compute_pm_total(self):
		for record in self:

			pm_total = 0

			for line in record.pm_line_ids:
				s = line.subtotal
				pm_total = pm_total + s

			record.pm_total = record.pm_total + pm_total







	# Balance 
	balance = fields.Float(
			string = 'Saldo', 
			required=True, 
			readonly=True, 

			compute="_compute_balance",
		)

	@api.multi
	#@api.depends('total', 'pm_total')
	def _compute_balance(self):

		#print 'Compute Balance'
		
		for record in self:
			record.balance = record.total - record.pm_total 

			#if record.balance == 0.0:
			#if record.total == record.pm_total:
				#print 'Gotcha'
				#record.state = 'done'
				#print record.state  













	# Name 
	name = fields.Char(
			string="Pagos", 			
			#required=True, 
			#readonly=True, 

			compute='_compute_name', 
		)

	#@api.depends()
	@api.multi
	def _compute_name(self):
		for record in self:
			#record.name = 'PA-' + str(record.id) 
			#record.name = str(record.id) 
			record.name = 'PA-' + str(record.id).zfill(6)


























	confirmed = fields.Boolean(
			default=False, 
			readonly=True, 

			string="Confirmado", 
		)












	# Open Myself
	@api.multi 
	def open_myself(self):
		#print 
		#print 'Open Myself'
		payment_method_id = self.id  



		return {
				# Mandatory 
				'type': 'ir.actions.act_window',
				'name': 'Open payment method Current',


				# Window action 
				'res_model': 'openhealth.payment_method',
				'res_id': payment_method_id,


				# Views 
				"views": [[False, "form"]],
				'view_mode': 'form',
				'target': 'current',


				#'view_id': view_id,
				#"domain": [["patient", "=", self.patient.name]],
				#'auto_search': False, 

				'flags': {
						'form': {'action_buttons': True, }
						#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
				},			

				'context':   {

				}
			}
	# open_myself
























	


















	# state 
	_state_list = [
					('draft', 'Inicio'),

					('payment', 'Pagado'),

					('generated', 'Generado'),
					
					('done', 'Confirmado'),

					#('cancel', 'Cancelled'),
				]


	state = fields.Selection(

			selection = _state_list, 	

			string='Estado',	

			#readonly=False,
			default='draft',

			compute="_compute_state",
			)


	@api.multi
	@api.depends('state')

	def _compute_state(self):
		for record in self:

			#print 'Compute State'

			record.state = 'draft'


			#if	record.env['openhealth.sale_document'].search_count([('order','=', record.id),]):
			#	record.state = 'proof'




			#if record.balance == 0.0 	and 	record.state == 'generated': 
			#if record.balance == 0.0:
			if record.balance == 0.0		and		record.saledoc != False:
				record.state = 'payment'











			if record.confirmed:
				record.state = 'done'




		#print record.state
		#print 




	nr_pm = fields.Char(

			compute="_compute_nr_pm",
		)

	@api.multi
	#@api.depends('date_order')

	def _compute_nr_pm(self):
		#print
		#print 'PML - compute nr pm'
		#print 

		for record in self:
			
			nr = record.env['openhealth.payment_method_line'].search_count([('payment_method','=', record.id),]) 

			record.nr_pm = str(nr + 1)




	# Create Pm
	@api.multi 
	def create_pm_line(self):

		#print 
		#print 'Create Pm Line'



		
		#nr_pm = self.env['openhealth.payment_method_line'].search_count([('payment_method','=', self.id),]) 
		#name = 'Pago #'
		#name = '# ' + str(nr_pm + 1)
		#name = str(nr_pm + 1)
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

		#ret = self.order.open_myself()
		#return ret 

	# open_order















	order = fields.Many2one(
			'sale.order',
			string="Presupuesto",
			ondelete='cascade', 
			required=True, 
			readonly=True, 
		)














	vspace = fields.Char(
			' ', 
			readonly=True
			)


















	# On change - Balance
	#@api.onchange('balance')
	
	#def _onchange_balance(self):
		
		#print 'Onchange Balance'

		#if self.balance == 0.0:
	#	if self.total == self.pm_total:
			#print 'Gotcha'
	#		self.state = 'done'
			#print self.state  









# ----------------------------------------------------------- Actions ------------------------------------------------------









	# Open Order
	@api.multi 
	def open_order(self):


		self.confirmed = True 
		#self.order.state = 'sale' 

		ret = self.order.open_myself()

		return ret 
	# open_order








	# ----------------------------------------------------------- CRUD ------------------------------------------------------




	# Write 
	@api.multi
	def write(self,vals):

		print 'jx'
		print 'Payment Method  - Write'
		#print 
		print vals
		#print self.partner.name



		#if vals['dni'] != False: 
		if 'dni' in vals: 
			dni = vals['dni']
			#print self.partner.x_dni
			self.partner.x_dni = dni 
			#print self.partner.x_dni


		#if vals['ruc'] != False: 
		if 'ruc' in vals: 
			ruc = vals['ruc']
			#print self.partner.x_ruc
			self.partner.x_ruc = ruc 
			#print self.partner.x_ruc


		if 'firm' in vals: 
			firm = vals['firm']
			#print self.partner.x_firm
			self.partner.x_firm = firm 
			#print self.partner.x_firm

		#print



		#Write your logic here
		res = super(PaymentMethod, self).write(vals)
		#Write your logic here

		return res






	# Create 
	@api.model
	def create(self,vals):

		#print 
		#print 'jx'
		#print 'Payment Method - Create Override'
		#print 
		#print vals
		#print 
		


		#order = vals['order']
		#nr_pm = self.env['openhealth.payment_method'].search_count([('order','=', order),]) 
		#name = 'MP-' + str(nr_pm + 1)
		#vals['name'] = name




		#total = vals['total']




		#Write your logic here
		res = super(PaymentMethod, self).create(vals)
		#Write your logic here

		return res

