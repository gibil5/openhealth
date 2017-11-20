# -*- coding: utf-8 -*-
#
# 	payment_method 
# 
#

from openerp import models, fields, api



from . import ord_vars



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
			#record.name = 'PA-' + str(record.id) 
			#record.name = str(record.id) 
			record.name = 'PA-' + str(record.id).zfill(6)






	# DNI
	dni = fields.Char(
			'DNI', 
			compute='_compute_dni', 
		)

	@api.multi
	#@api.depends('')

	def _compute_dni(self):
		for record in self:

			#print 'jx'
			#print 'Compute Dni'
			record.dni = record.partner.x_dni
			#print 





	# Firm
	firm = fields.Char(
			'Razón social',
			compute='_compute_firm', 
		)

	@api.multi
	#@api.depends('')
	def _compute_firm(self):
		for record in self:

			record.firm  = record.partner.x_firm







	# Ruc
	ruc = fields.Char(
			'Ruc', 
			compute='_compute_ruc', 
		)

	@api.multi
	#@api.depends('')
	def _compute_ruc(self):
		for record in self:

			record.ruc = record.partner.x_ruc









	# Order name 
	@api.multi 
	def order_name(self):
		#print
		#print 'jx'
		

		#print self.invoice.name 
		#print self.receipt.name 
		#print self.advertisement.name 
		#print self.ticket_invoice.name 
		#print self.ticket_receipt.name


		if self.invoice.name != False:
			self.order.name = self.invoice.name

		if self.receipt.name != False:
			self.order.name = self.receipt.name
	
		if self.advertisement.name != False:
			self.order.name = self.advertisement.name

		if self.sale_note.name != False:
			self.order.name = self.sale_note.name

		if self.ticket_invoice.name != False:
			self.order.name = self.ticket_invoice.name

		if self.ticket_receipt.name != False:
			self.order.name = self.ticket_receipt.name


		#print self.order.name 
		#print 



	confirmed = fields.Boolean(
			default=False, 
			readonly=True, 

			string="Confirmado", 
		)



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








	# Partner 
	partner = fields.Many2one(
			'res.partner',
			string = "Cliente", 	
			required=True, 
		)
















	# Receipt
	receipt = fields.Many2one(
			'openhealth.receipt',
			string = "Boleta", 			
			#ondelete='cascade', 

			compute="_compute_receipt",
		)

	@api.multi
	#@api.depends('saledoc')

	def _compute_receipt(self):
		for record in self:
			record.receipt = record.env['openhealth.receipt'].search([('payment_method', '=', record.id),])

	


	# Invoice
	invoice = fields.Many2one(
			'openhealth.invoice',
			string = "Factura", 			
			#ondelete='cascade', 

			compute="_compute_invoice",
		)

	@api.multi
	#@api.depends('saledoc')

	def _compute_invoice(self):
		for record in self:
			record.invoice = record.env['openhealth.invoice'].search([('payment_method', '=', record.id),])




	# Advertisement
	advertisement = fields.Many2one(
			'openhealth.advertisement',
			string = "Canje publicidad", 			
			#ondelete='cascade', 

			compute="_compute_advertisement",
		)
	@api.multi
	#@api.depends('saledoc')

	def _compute_advertisement(self):
		for record in self:
			record.advertisement = record.env['openhealth.advertisement'].search([('payment_method', '=', record.id),])




	# Sale note 
	sale_note = fields.Many2one(
			'openhealth.sale_note',
			string = "Nota de venta", 			
			#ondelete='cascade', 

			compute="_compute_sale_note",
		)
	@api.multi
	#@api.depends('saledoc')

	def _compute_sale_note(self):
		for record in self:
			record.sale_note = record.env['openhealth.sale_note'].search([('payment_method', '=', record.id),])




	# Ticket Receipt
	ticket_receipt = fields.Many2one(
			'openhealth.ticket_receipt',
			string = "Ticket Boleta", 			
			#ondelete='cascade', 

			compute="_compute_ticket_receipt",
		)
	@api.multi
	#@api.depends('saledoc')

	def _compute_ticket_receipt(self):
		for record in self:
			record.ticket_receipt = record.env['openhealth.ticket_receipt'].search([('payment_method', '=', record.id),])




	# Ticket Invoice
	ticket_invoice = fields.Many2one(
			'openhealth.ticket_invoice',
			string = "Ticket Factura", 			
			#ondelete='cascade', 

			compute="_compute_ticket_invoice",
		)
	@api.multi
	#@api.depends('saledoc')

	def _compute_ticket_invoice(self):
		for record in self:
			record.ticket_invoice = record.env['openhealth.ticket_invoice'].search([('payment_method', '=', record.id),])







	
	# Saledoc 
	saledoc = fields.Selection(
			#string="Documento de venta", 
			string="Documento de Pago", 

			#selection=_saledoc_list, 
			selection=ord_vars._sale_doc_type_list, 
			
			#default='receipt', 
			#required=True, 
		)





	# Sale doc code 
	saledoc_code = fields.Char(
			string="No", 
			readonly=False, 

			#compute="_compute_saledoc_code",
		)

	@api.onchange('saledoc')
	
	def _onchange_saledoc(self):

		#print
		#print 'onchange - Saledoc'

		pre = {
				'receipt':	'BO-1-', 
				'invoice':	'FA-1-', 

				'advertisement':	'CP-1-', 
				'sale_note':		'CN-1-', 

				'ticket_receipt':	'TKB-1-', 
				'ticket_invoice':	'TKF-1-', 
		}


		counter = self.env['openhealth.counter'].search([('name', '=', self.saledoc)])

		out = False 



		while not out:

			ctr = counter.value
			name = pre[self.saledoc] + str(ctr).rjust(4, '0')
		

			model = ord_vars._dic_model[self.saledoc]
			count = self.env[model].search_count([
												('name','=', name),
											]) 
			if count == 0:
				out = True
			else:
				counter.increase()



		self.saledoc_code = name














	# state 
	_state_list = [
					('draft', 'Inicio'),

					('payment', 'Pagado'),

					('generated', 'Documento generado'),
					
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

			if record.balance == 0.0:
				record.state = 'payment'


			if	record.env['openhealth.receipt'].search_count([('payment_method','=', record.id),])			or \
				record.env['openhealth.invoice'].search_count([('payment_method','=', record.id),])			or \
				record.env['openhealth.advertisement'].search_count([('payment_method','=', record.id),])	or \
				record.env['openhealth.sale_note'].search_count([('payment_method','=', record.id),])		or \
				record.env['openhealth.ticket_receipt'].search_count([('payment_method','=', record.id),])	or \
				record.env['openhealth.ticket_invoice'].search_count([('payment_method','=', record.id),]):
				
				#record.state = 'done'
				record.state = 'generated'

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







	# Payment Method 
	pm_line_ids = fields.One2many(

			'openhealth.payment_method_line',

			'payment_method',		
			string="Pago #", 
		)







	# Open Order
	@api.multi 
	def open_order(self):

		#print 
		#print 'Open order'

		self.confirmed = True 


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

		#print 'Compute Balance'
		
		for record in self:
			record.balance = record.total - record.pm_total 

			#if record.balance == 0.0:
			#if record.total == record.pm_total:
				#print 'Gotcha'
				#record.state = 'done'
				#print record.state  

		#print 





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

	# Create Sale Proof
	@api.multi 
	def create_saleproof(self):



		print 'jx'
		print 'Create Sale proof'



		# Search in the Model dic
		model = ord_vars._dic_model[self.saledoc]
		print model 



		# The model is valid 
		if model != False: 



			# Search it exists 
			proof = self.env[model].search([
												('payment_method', '=', self.id),
											])

			# Create 
			if proof.id == False:
				print 'create'


				count = self.env[model].search_count([('name','=', self.saledoc_code),])
				print count


				if count != 0: 

					proof = self.env[model].create({
														'name': self.saledoc_code,

														'payment_method': self.id,
														'order': self.order.id,
														'partner': self.partner.id,
																
														'total': self.total,
														'date_created': self.date_created,
												})
					#proof.save


			proof_id = proof.id 
			print proof
			print self.saledoc_code
			print self.id
			print self.order
			print self.partner
			print self.total
			print self.date_created
			print


			return {}


			return {
					'type': 'ir.actions.act_window',
					'name': ' New Proof Current', 

					'view_type': 'form',
					'view_mode': 'form',	
					'target': 'current',

					'res_model': model,
					'res_id': proof_id,

					'flags': 	{
									#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
									'form': {'action_buttons': True, }
								},

					'context': {
								'default_name': self.saledoc_code,

								'default_payment_method': self.id,
								'default_order': self.order.id,
								'default_partner': self.partner.id,
								'default_total': self.total,		
								'default_date_created': self.date_created,
							}
				}




	# create_saleproof




	# ----------------------------------------------------------- CRUD ------------------------------------------------------

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


		#Write your logic here
		res = super(payment_method, self).create(vals)
		#Write your logic here

		return res

