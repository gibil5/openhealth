# -*- coding: utf-8 -*-
#
# 	payment_method 
# 
#

from openerp import models, fields, api

import ord_vars


class payment_method(models.Model):
	
	_name = 'openhealth.payment_method'

	#_inherit='openhealth.sale_document'




	name = fields.Char(
			#string="Medio de Pago", 
			string="Pagos", 
			
			#required=True, 
			#readonly=True, 

			compute='_compute_name', 
		)

	#@api.depends()
	@api.multi

	def _compute_name(self):
		for record in self:
			record.name = 'PA-' + str(record.id) 






	# Counters
	#counter_receipt = fields.Many2one(
	#		'openhealth.counter',
	#		string="Counter", 
	#		required=True, 
	#	)






	# Date created 
	date_created = fields.Datetime(
			string="Fecha", 
			#readonly=True,
			required=True, 
			)




	# Open Myself
	@api.multi 
	def open_myself(self):
		print 
		print 'Open Myself'
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








	# Partner 
	partner = fields.Many2one(
			'res.partner',
			string = "Cliente", 	
			required=True, 
		)




	# Create Saledoc
	@api.multi 
	def create_saledoc(self):
		print 'Create Saledoc'

		ret = ''

		if self.saledoc == 'receipt':
			ret = self.create_receipt()

		return ret 





	# Create Receipt
	@api.multi 
	def create_receipt(self):
		print 
		print 'Create Receipt'




		# Search 
		receipt_id = self.env['openhealth.receipt'].search([
																('payment_method', '=', self.id),
																#('sale_document','=',self.id),
															]).id


		# Create 
		if receipt_id == False:


			receipt = self.env['openhealth.receipt'].create({
																'payment_method': self.id,
																#'sale_document': self.id,
																'partner': self.partner.id,
																'order': self.order.id,
																'total': self.total,

																'date_created': self.date_created,

																'counter': self.saledoc_code,																
														})
			receipt_id = receipt.id 




		self.receipt = receipt_id

		return {
				'type': 'ir.actions.act_window',
				'name': ' New Receipt Current', 

				'view_type': 'form',
				'view_mode': 'form',	
				'target': 'current',

				'res_model': 'openhealth.receipt',				
				'res_id': receipt_id,

				'flags': 	{
							#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
							'form': {'action_buttons': True, }
							},

				'context': {
							'default_payment_method': self.id,
							#'default_order': self.order.id,
							'default_total': self.total,
							'default_partner': self.partner.id,
							'default_date_created': self.date_created,


							'default_counter': self.saledoc_code,
							}
				}

	# create_receipt







	receipt = fields.Many2one(
			'openhealth.receipt',
			string = "Boleta", 			
			#ondelete='cascade', 
		)

	invoice = fields.Many2one(
			'openhealth.invoice',
			string = "Factura", 			
			#ondelete='cascade', 
		)

	advertisement = fields.Many2one(
			'openhealth.advertisement',
			string = "Canje publicidad", 			
			#ondelete='cascade', 
		)

	sale_note = fields.Many2one(
			'openhealth.sale_note',
			string = "Nota de venta", 			
			#ondelete='cascade', 
		)

	ticket_receipt = fields.Many2one(
			'openhealth.ticket_receipt',
			string = "Ticket Boleta", 			
			#ondelete='cascade', 
		)

	ticket_invoice = fields.Many2one(
			'openhealth.ticket_invoice',
			string = "Ticket Factura", 			
			#ondelete='cascade', 
		)






	_saledoc_list = [

				('receipt', 			'Boleta'),
				('invoice', 			'Factura'),

				('advertisement', 		'Canje Publicidad'),
				#('sale_note', 			'Nota de Venta'),
				('sale_note', 			'Canje NV'),

				('ticket_receipt', 		'Ticket Boleta'),
				('ticket_invoice', 		'Ticket Factura'),

				#('none', 				'Ninguno'),

			]
	

	saledoc = fields.Selection(
			#string="Documento de venta", 
			string="Documento de Pago", 

			selection=_saledoc_list, 
			
			#default='receipt', 
		)





	# Sale doc code 
	saledoc_code = fields.Char(

			string="No", 
		
			readonly=False, 

			#compute="_compute_saledoc_code",
		)


	@api.onchange('saledoc')
	
	def _onchange_saledoc(self):
		print
		print 'onchange - Saledoc'

		ctr = 0 

		if self.saledoc  == 'receipt':
			pre = 'BO-'

			counter = self.env['openhealth.counter'].search([('name', 'like', 'receipt')])
			ctr = counter.value
			#self.counter_receipt = counter


		if self.saledoc  == 'invoice':
			pre = 'FA-'

		if self.saledoc  == 'advertisement':
			pre = 'CA-'

		if self.saledoc  == 'sale_note':
			pre = 'NV-'
			
		if self.saledoc  == 'ticket_receipt':
			pre = 'TB-'
			
		if self.saledoc  == 'ticket_invoice':
			pre = 'TF-'

		if self.saledoc  == 'none':
			pre = 'NO-'

		self.saledoc_code = ctr 



	#@api.multi
	@api.depends('saledoc')

	def _compute_saledoc_code(self):
		for record in self:

			receipt_ctr = '00001'

			pre = 'x'

			if record.saledoc  == 'receipt':
				pre = 'BO-'


			if record.saledoc  == 'invoice':
				pre = 'FA-'

			if record.saledoc  == 'advertisement':
				pre = 'CA-'

			if record.saledoc  == 'sale_note':
				pre = 'NV-'
			
			if record.saledoc  == 'ticket_receipt':
				pre = 'TB-'
			
			if record.saledoc  == 'ticket_invoice':
				pre = 'TF-'

			if record.saledoc  == 'none':
				pre = 'NO-'

			if pre != 'x':
				code = receipt_ctr
				record.saledoc_code = pre + code






	# Consistency 

	#subtotal = fields.Float(
	#		string = 'Sub-total', 
	#		required=True, 
	#	)

	#method = fields.Selection(
	#		string="Medio", 
	#		selection = ord_vars._payment_method_list, 			
	#		required=True, 
	#	)




















	# state 
	_state_list = [
					('draft', 'Inicio'),

					('payment', 'Pagado'),

					('done', 'Completo'),
					
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

			print 'Compute State'

			record.state = 'draft'


			#if	record.env['openhealth.sale_document'].search_count([('order','=', record.id),]):
			#	record.state = 'proof'

			if record.balance == 0.0:
				record.state = 'payment'


			if	record.env['openhealth.receipt'].search_count([('payment_method','=', record.id),]):
				record.state = 'done'

		print record.state
		print 




	nr_pm = fields.Integer(

			compute="_compute_nr_pm",
		)

	@api.multi
	#@api.depends('date_order')

	def _compute_nr_pm(self):
		print
		print 'PML - compute nr pm'
		print 

		for record in self:
			nr = record.env['openhealth.payment_method_line'].search_count([('payment_method','=', record.id),]) 
			record.nr_pm = nr + 1




	# Create Pm
	@api.multi 
	def create_pm_line(self):

		print 
		print 'Create Pm Line'



		
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







	# Payment Method 
	pm_line_ids = fields.One2many(

			'openhealth.payment_method_line',

			'payment_method',		
			string="Pago #", 
		)







	# Open Order
	@api.multi 
	def open_order(self):

		print 
		print 'Open order'


		ret = self.order.open_myself()

		return ret 
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




	total = fields.Float(
			string = 'Total a pagar', 
			required=True, 
		)



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








	balance = fields.Float(
			string = 'Saldo', 
			required=True, 
			readonly=True, 

			compute="_compute_balance",
		)

	@api.multi
	#@api.depends('total', 'pm_total')
	def _compute_balance(self):

		print 'Compute Balance'
		
		for record in self:
			record.balance = record.total - record.pm_total 

			#if record.balance == 0.0:
			#if record.total == record.pm_total:
			#	print 'Gotcha'
			#	record.state = 'done'
			#	print record.state  

		print 





	# On change - Balance
	#@api.onchange('balance')
	
	#def _onchange_balance(self):
		
	#	print 'Onchange Balance'

		#if self.balance == 0.0:
	#	if self.total == self.pm_total:
	#		print 'Gotcha'
	#		self.state = 'done'
	#		print self.state  





	# ----------------------------------------------------------- CRUD ------------------------------------------------------

	# Create 
	@api.model
	def create(self,vals):

		print 
		print 'jx'
		print 'Payment Method - Create Override'
		print 
		print vals
		print 
	



		#order = vals['order']
		#nr_pm = self.env['openhealth.payment_method'].search_count([('order','=', order),]) 
		#name = 'MP-' + str(nr_pm + 1)
		#vals['name'] = name



		#Write your logic here
		res = super(payment_method, self).create(vals)
		#Write your logic here

		return res

