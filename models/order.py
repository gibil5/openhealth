# -*- coding: utf-8 -*-
#

# 	Order 
# 
# Created: 				26 Aug 2016
#

from openerp import models, fields, api

import datetime
import ord_vars
from num2words import num2words
import math 
from openerp import tools
import count_funcs


class sale_order(models.Model):
	
	_inherit='sale.order'
	


# ----------------------------------------------------------- Deprecated ------------------------------------------------------





# ----------------------------------------------------------- Vars ------------------------------------------------------

	# Serial Number 
	x_serial_nr = fields.Char(
			'Número de serie',
		)


	# Date 
	date_order = fields.Datetime(
		states={	
					'draft': [('readonly', False)], 
					'sent': [('readonly', False)], 
					'sale': [('readonly', True)], 
					'editable': [('readonly', False)], 
				}, 
	)


	# State 
	state = fields.Selection(
			selection = ord_vars._state_list, 
			string='Estado',	
			readonly=False,
			default='draft',
		)


	# For Admin Sale Editing 
	@api.multi
	def state_change(self):  
		if self.state == 'sale': 
			self.state = 'editable'
		elif self.state == 'editable': 
			self.state = 'sale'


	# Pricelist 
	pricelist_id = fields.Many2one(
			'product.pricelist', 
			string='Pricelist', 
			required=True, 
			readonly=True, 
			states={'draft': [('readonly', False)], 'sent': [('readonly', False)]}, 
			help="Pricelist for current sales order.", 
		)


	# Payment Method 
	x_payment_method = fields.Many2one(
			'openhealth.payment_method',
			string="Pago", 
		)



	# Type 
	x_type = fields.Selection(
			[	('receipt', 			'Boleta'),
				('invoice', 			'Factura'),
				('advertisement', 		'Canje Publicidad'),
				('sale_note', 			'Canje NV'),
				('ticket_receipt', 		'Ticket Boleta'),
				('ticket_invoice', 		'Ticket Factura'),	], 
			string='Tipo', 
			required=False,
		)


	# To update type from batch 
	@api.multi
	def update_type_batch(self):
		#print 'update type'
		if self.x_payment_method != False: 
			self.x_type = self.x_payment_method.saledoc
			#print self.x_type






	# Doctor 
	x_doctor = fields.Many2one(
			'oeh.medical.physician',
			string = "Médico",
		)

	x_doctor_uid = fields.Many2one(
			'res.users',
			string = "Médico Uid", 	
			readonly = True,
		)



	# Family 
	x_family = fields.Selection(
			string = "Familia", 	
			selection = [
							('product','Producto'), 
							('consultation','Consulta'), 
							('procedure','Procedimiento'), 
							('cosmetology','Cosmiatría'), 
			], 
			required=False, 
		)



	# Product
	x_product = fields.Char(		
			string="Producto",	
			required=False, 			
		)



	# Nr lines 
	nr_lines = fields.Integer(
			default=0,
			string='Nr líneas',
			required=False, 

			compute='_compute_nr_lines', 
			)

	@api.multi
	#@api.depends('order_line')
	def _compute_nr_lines(self):
		for record in self:			
			ctr = 0
			for l in record.order_line:
				ctr = ctr + 1
			record.nr_lines = ctr 
			
	

	# Partner Vip 
	x_partner_vip = fields.Boolean(
			'Vip', 
			default=False, 

			compute="_compute_partner_vip",
			)

	@api.multi
	def _compute_partner_vip(self):
		for record in self:
			count = self.env['openhealth.card'].search_count([
																('patient_name','=', record.partner_id.name),
														]) 
			if count == 0:
				record.x_partner_vip = False 
			else:	
				record.x_partner_vip = True 




# ----------------------------------------------------------- Primitives ------------------------------------------------------

	# Treatment 
	treatment = fields.Many2one(
			'openhealth.treatment',
			ondelete='cascade', 
			string="Tratamiento",
			readonly=False, 
		)


	@api.onchange('x_doctor')
	def _onchange_x_doctor(self):

		if self.x_doctor.name != False: 

			treatment = self.env['openhealth.treatment'].search([															
																	('patient', '=', self.patient.name), 
																	('physician', '=', self.x_doctor.name), 
													],
														order='write_date desc',
														limit=1,
													)
			self.treatment = treatment



	# Cosmetology 
	cosmetology = fields.Many2one(
			'openhealth.cosmetology',
			ondelete='cascade', 			
			string="Cosmiatría", 
		)



	# For User Interface 
	vspace = fields.Char(
			' ', 
			readonly=True
		)



# ----------------------------------------------------------- Relationals ------------------------------------------------------


# ----------------------------------------------------- Create Order Line ------------------------------------------------------------

	# Buttons  - Agregar Producto Servicio
	@api.multi
	def open_product_selector(self):  


		# Init Vars 
		context = self._context.copy()		
		order_id = self.id
		x_type = context['x_type']
		res_id = False



		# Search Model 
		res = self.env['openhealth.product.selector'].search([
															],
																#order='write_date desc',
																limit=1,
															)
		#print 'Open Product Selector'
		#print context
		#print context['params']
		#print order_id
		#print res.id
		

		if res.id != False: 
			
			res_id = res.id 

			# Reset 
			res.reset()

			# Initialize 
			res.order_id = order_id
			res.product_uom_qty = 1 
			res.x_type = x_type


		return {
				'type': 'ir.actions.act_window',
				'name': ' New Orderline Selector Current', 
				'view_type': 'form',
				'view_mode': 'form',	
				#'target': 'current',
				'target': 'new',
				'res_id': res_id,
				#'res_model': 'sale.order.line',	
				'res_model': 'openhealth.product.selector',	
				'flags': 	{
								#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
								#'form': {'action_buttons': False, }
								'form': {'action_buttons': False, 'options': {'mode': 'edit'}  }
							},
				'context': {
								'default_order_id': order_id ,
								'default_x_type': x_type ,
							}
				}
	# open_product_selector






# ----------------------------------------------------------- Print Tickets ------------------------------------------------------

	# Total in Words
	x_total_in_words = fields.Char(
			"",
			compute='_compute_x_total_in_words', 
		)

	@api.multi
	#@api.depends('')
	def _compute_x_total_in_words(self):
		for record in self:
			words = num2words(record.amount_total, lang='es')
			if 'punto' in words:
				words = words.split('punto')[0]			
			record.x_total_in_words = words.title()



	# Total in cents 
	x_total_cents = fields.Integer(
			"Céntimos",
			compute='_compute_x_total_cents', 
		)

	@api.multi
	#@api.depends('')
	def _compute_x_total_cents(self):
		for record in self:
			frac, whole = math.modf(record.amount_total)			
			record.x_total_cents = frac * 100



	# Net
	x_total_net = fields.Float(
			"Neto",
			compute='_compute_x_total_net', 
		)

	@api.multi
	#@api.depends('')
	def _compute_x_total_net(self):
		for record in self:
			x = record.amount_total / 1.18
			g = float("{0:.2f}".format(x))
			record.x_total_net = g



	# Tax
	x_total_tax = fields.Float(
			"Impuesto",
			compute='_compute_x_total_tax', 
		)
	@api.multi
	#@api.depends('')
	def _compute_x_total_tax(self):
		for record in self:
			x = record.x_total_net * 0.18
			g = float("{0:.2f}".format(x))
			record.x_total_tax = g





	# My company 
	x_my_company = fields.Many2one(
			'res.partner',
			string = "Mi compañía", 	
			domain = [
						('company_type', '=', 'company'),
					],
			compute="_compute_x_my_company",
		)


	@api.multi
	#@api.depends('partner_id')

	def _compute_x_my_company(self):

		for record in self:
				com = self.env['res.partner'].search([
															#('name', '=', 'Clinica Chavarri'),
															('x_my_company', '=', True),
													],
													order='date desc',
													limit=1,
					)
				record.x_my_company = com 													



	# Date corrected 
	x_date_order_corr = fields.Char(
			string='Order Date Corr', 

			compute="_compute_date_order_corr",
		)

	@api.multi
	#@api.depends('partner_id')

	def _compute_date_order_corr(self):
		for record in self:

			DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
			date_field1 = datetime.datetime.strptime(record.date_order, DATETIME_FORMAT)
			
			date_field2 = date_field1 + datetime.timedelta(hours=-5,minutes=0)
			DATETIME_FORMAT_2 = "%d-%m-%Y %H:%M:%S"
			date_field2 = date_field2.strftime(DATETIME_FORMAT_2)
			record.x_date_order_corr = date_field2






# ----------------------------------------------------------- Primitives ------------------------------------------------------
	
	# Proc Created - For Doctor budget creation 
	x_procedure_created = fields.Boolean(
			default=False, 
		)



	# Partner 
	partner_id = fields.Many2one(
			'res.partner',
			string = "Cliente", 	
			ondelete='cascade', 			

			#required=True, 
			required=False, 
		)




	# Patient 
	patient = fields.Many2one(
			'oeh.medical.patient',
			string='Paciente', 
			#compute='_compute_patient', 
			
			#required=True, 
			required=False, 

			#states={
			#			'cancel': 	[('readonly', True)], 
			#			'done': 	[('readonly', True)], 
			#			'sent': 	[('readonly', True)], 
			#			'sale': 	[('readonly', True)], 
			#		}, 
		)



	# DNI 
	x_partner_dni = fields.Char(
			string='DNI', 
			states={
						'draft': 	[('readonly', False)], 
						'sent': 	[('readonly', True)], 
						'sale': 	[('readonly', True)], 
						'cancel': 	[('readonly', True)], 
						'done': 	[('readonly', True)], 
					}, 
		)



	# Order Line 
	order_line = fields.One2many(
			'sale.order.line', 
			'order_id', 
			string='Order Lines', 
			readonly=False, 
			states={
						'cancel': 	[('readonly', True)], 
						'done': 	[('readonly', True)], 
						'sent': 	[('readonly', True)], 
						'sale': 	[('readonly', True)], 
					}, 
		)





# ----------------------------------------------------------- On Changes ------------------------------------------------------

	# Patient  
	@api.onchange('patient')
	def _onchange_patient(self):	
		if self.patient.name != False: 
			self.partner_id = self.patient.partner_id.id 



	# Partner  
	@api.onchange('partner_id')	
	def _onchange_partner_id(self):		
		if self.partner_id.name != False: 			
			self.x_partner_dni = self.partner_id.x_dni



	# Dni 
	@api.onchange('x_partner_dni')
	def _onchange_x_partner_dni(self):		

		if self.x_partner_dni != False: 
			
			# Partner 
			partner_id = self.env['res.partner'].search([
															('x_dni', '=', self.x_partner_dni),					
												],
													order='write_date desc',
													limit=1,
												)
			self.partner_id = partner_id.id




			# Patient 
			patient = self.env['oeh.medical.patient'].search([
																('x_dni', '=', self.x_partner_dni),					
												],
													order='write_date desc',
													limit=1,
												)
			self.patient = patient.id
	# _onchange_x_partner_dni





# ---------------------------------------------- Cancel - Event creation --------------------------------------------------------

	# Event 
	event_ids = fields.One2many(
			'openhealth.event',
			'order',		
			string="Eventos", 
		)


	x_cancel = fields.Boolean(
			string='', 
			default = False
		)


	@api.multi 
	def cancel_order(self):
		#print 
		#print 'Cancel'
		self.x_cancel = True
		self.state = 'cancel'
		ret = self.create_event()
		return(ret)


	@api.multi 
	def activate_order(self):
		#print 
		#print 'Cancel'
		self.x_cancel = False
		self.state = 'draft'


	@api.multi 
	def create_event(self):
		nr_pm = self.env['openhealth.event'].search_count([('order','=', self.id),]) 
		name = 'Evento ' + str(nr_pm + 1)
		x_type = 'cancel'

		return {
				'type': 'ir.actions.act_window',
				'name': ' New PM Current', 
				'view_type': 'form',
				'view_mode': 'form',	
				'target': 'current',
				'res_model': 'openhealth.event',				
				#'res_id': receipt_id,
				'flags': 	{
								#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
								'form': {'action_buttons': True, }
							},
				'context': {
								'default_order': self.id,
								'default_name': name,
								'default_x_type': x_type,
							}
				}





# ---------------------------------------------- Create Payment Method --------------------------------------------------------

	# Amount total 
	x_amount_total = fields.Float(
			string = "x Total",

			compute="_compute_x_amount_total",
		)

	@api.multi
	def _compute_x_amount_total(self):
		for record in self:
			sub = 0.0
			for line in record.order_line:
				sub = sub + line.price_subtotal 
			#if sub == 0.0:
			#	sub = float(record.x_ruc)
			record.x_amount_total = sub



	@api.multi 
	def create_payment_method(self):

		# Update Descriptors
		self.update_descriptors()

		# Init vars 
		name = 'Pago'
		method = 'cash'
		#balance = self.x_amount_total - self.pm_total
		balance = self.x_amount_total

		# For Receipts and Invoices  
		dni = self.partner_id.x_dni
		firm = self.partner_id.x_firm
		ruc = self.partner_id.x_ruc


		# Create 
		self.x_payment_method = self.env['openhealth.payment_method'].create({
																				'order': self.id,
																				'name': name,																			
																				'method': method,
																				'subtotal': balance,
																				'total': self.x_amount_total,
																				'partner': self.partner_id.id, 
																				'date_created': self.date_order,
																				'dni': dni,
																				'firm': firm,
																				'ruc': ruc,

																				#'saledoc': 'receipt', 
																				#'pm_total': self.pm_total,
																				#'balance': balance, 
																				#'balance': 0, 
																			})
		payment_method_id = self.x_payment_method.id 


		# Create Lines 
		name = '1'
		method = 'cash'
		subtotal = self.x_amount_total
		payment_method = self.x_payment_method.id

		ret = self.x_payment_method.pm_line_ids.create({
																	'name': name,
																	'method': method ,
																	'subtotal': subtotal,
																	'payment_method': payment_method, 
										})
		
		self.state = 'sent'


		return {
				'type': 'ir.actions.act_window',
				'name': ' New PM Current', 
				'view_type': 'form',
				'view_mode': 'form',	
				'target': 'current',
				'res_model': 'openhealth.payment_method',				
				'res_id': payment_method_id,
				'flags': 	{
							#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
							#'form': {'action_buttons': False, }
							'form': {'action_buttons': False, 'options': {'mode': 'edit'}  }
							},
				'context': {
				
							'default_order': self.id,
							'default_name': name,
							'default_method': method,
							'default_subtotal': balance,
							'default_total': self.x_amount_total,
							'default_partner': self.partner_id.id,
							'default_date_created': self.date_order,
							'default_dni': dni,
							'default_firm': firm,
							'default_ruc': ruc,

							#'default_saledoc': 'receipt', 
							#'default_pm_total': self.pm_total,
							}
				}
	# create_payment_method






# ----------------------------------------------------------- Update Descriptors ------------------------------------------------------

	# For batch 
	@api.multi 
	def update_descriptors_all(self):

		orders = self.env['sale.order'].search([
													('state', '=', 'sale'),
											],
												order='date_order desc',
												#limit=2000,
												limit=100,
											)
		#print orders 

		for order in orders: 
			order.update_descriptors()



	# Update Family and Product 
	@api.multi 
	def update_descriptors(self):

		out = False

		for line in self.order_line:

			if not out: 

				# Consultations
				#if line.product_id.categ_id.name == 'Consultas':
				if line.product_id.categ_id.name == 'Consulta':
					self.x_family = 'consultation'
					self.x_product = line.product_id.x_name_ticket
					out = True


				# Procedures
				#elif line.product_id.categ_id.name in ['Quick Laser', 'Laser Co2', 'Laser Excilite', 'Laser M22', 'Medical']: 
				elif line.product_id.categ_id.name in ['Procedimiento', 'Quick Laser', 'Laser Co2', 'Laser Excilite', 'Laser M22', 'Medical']: 
					self.x_family = 'procedure'
					self.x_product = line.product_id.x_name_ticket
					out = True


				# Cosmetology 
				elif line.product_id.categ_id.name == 'Cosmeatria':
					self.x_family = 'cosmetology'
					self.x_product = line.product_id.x_name_ticket
					out = True


				# Products 
				else: 
					self.x_family = 'product'
					self.x_product = line.product_id.x_name_ticket


		#print 
		#print 'Update descriptors'
		#print self.x_family
		#print self.x_product

	#update_descriptors





# ----------------------------------------------------------- Print ------------------------------------------------------

	# Print Ticket
	@api.multi
	def print_ticket(self):
		
		if self.x_type == 'ticket_receipt': 
			name = 'openhealth.report_ticket_receipt_nex_view'
			return self.env['report'].get_action(self, name)
		
		elif self.x_type == 'ticket_invoice': 
			name = 'openhealth.report_ticket_invoice_nex_view'
			return self.env['report'].get_action(self, name)





# ----------------------------------------------------------- Update Appointments ------------------------------------------------------

	# Update Appointment in Treatment 
	@api.multi 
	def update_appointment(self):

		if self.x_family == 'consultation': 
			for app in self.treatment.appointment_ids: 
				if app.x_type == 'consultation': 
					app.state = 'invoiced'

		if self.x_family == 'procedure': 
			for app in self.treatment.appointment_ids: 
				if app.x_type == 'procedure': 
					app.state = 'invoiced'




# ----------------------------------------------------------- Create Card ------------------------------------------------------

	# Create Vip Card 
	@api.multi 
	def create_card(self):

		# Detect 
		card_sale = False 
		order_line = self.order_line
		for line in order_line:
			if line.product_id.x_name_short == 'vip_card':
				card_sale = True


		# If Detected 
		if card_sale:

			
			# Search 
			card = self.env['openhealth.card'].search([ ('patient_name', '=', self.partner_id.name), ], order='date_created desc', limit=1)
			

			# Create
			if card.name == False: 
				card = self.env['openhealth.card'].create({
																	'patient_name': self.partner_id.name,
															})



			# Serarch Pricelist 
			pl = self.env['product.pricelist'].search([
																('name','=', 'VIP'),
															],
															#order='appointment_date desc',
															limit=1,)

			# Update Partner 
			self.partner_id.property_product_pricelist = pl






# ----------------------------------------------------------- Action Confirm ------------------------------------------------------

	# Action confirm 
	@api.multi 
	def action_confirm(self):

		print 
		print 'Action confirm - Overridden'
		 
		

#Write your logic here - Begin

		# Serial Number and Type
		if self.x_payment_method.saledoc != False: 

			print 'Serial number'
			
			self.x_type = self.x_payment_method.saledoc
	 		counter = self.env['openhealth.counter'].search([
																	('name', '=', self.x_type), 
																],
																	#order='write_date desc',
																	limit=1,
																)
			name = count_funcs.get_name(self, counter.prefix, counter.separator, counter.padding, counter.value)
			self.x_serial_nr = name

			counter.increase()				# Here !




		# Doctor User Name - For Sale Reporting 
		if self.x_doctor.name != False: 
			print 'Dr name'
			uid = self.x_doctor.x_user_name.id
			self.x_doctor_uid = uid

#Write your logic here - End 



		# The actual procedure 
		res = super(sale_order, self).action_confirm()
		#Write your logic here
		

		
		# Date must be that of the Sale, not the budget. 
		self.date_order = datetime.datetime.now()



		# Update Descriptors (family and product) 
		self.update_descriptors()



		# Change Appointment State - To Invoiced 
		self.update_appointment()



		# Create Proc 
		#self.treatment.create_procedure()



		# Vip Card 
		self.create_card()




		# Reserve Machine if Procedure 					# Deprecated !
		#if self.x_family == 'procedure': 
		#	self.reserve_machine()



		# Stock Picking - Validate 						# Deprecated !
		#print 'Picking'
		#self.validate_stock_picking()
		#self.do_transfer()
		

	# action_confirm	





	# ----------------------------------------------------------- Reset ------------------------------------------------------
	@api.multi 
	def x_reset(self):
		self.x_payment_method.unlink()
		self.state = 'draft'			# This works. 




	#----------------------------------------------------------- Quick Button - For Treatment ------------------------------------------------------------

	# For Treatments Quick access
	@api.multi
	def open_line_current(self):  

		consultation_id = self.id 

		return {
				'type': 'ir.actions.act_window',
				'name': ' Edit Order Current', 
				'view_type': 'form',
				'view_mode': 'form',
				'res_model': self._name,
				'res_id': consultation_id,
				'target': 'current',
				'flags': {
						#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
						'form': {'action_buttons': True, }
						},
				'context': {}
		}




	#----------------------------------------------------------- Qpen myself ------------------------------------------------------------

	# For Payment Method comeback 
	@api.multi 
	def open_myself(self):

		order_id = self.id  

		return {
			# Mandatory 
			'type': 'ir.actions.act_window',
			'name': 'Open Order Current',
			# Window action 
			'res_model': 'sale.order',
			'res_id': order_id,
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




# ----------------------------------------------------------- Update Order ------------------------------------------------------

	# Update colors (state)
	#@api.multi 
	#def update_order_nex(self):
		#print 
		#print 'Update Order Nex'
		#print 




# ----------------------------------------------------------- Reset - For Treatment   ------------------------------------------------------
	@api.multi
	def remove_myself(self):  
		self.x_reset()
		self.unlink()




# ----------------------------------------------------------- Create order lines ------------------------------------------------------
	
	# For  Budget creation - From Treatment - By Doctors 
	@api.multi 
	def x_create_order_lines_target(self, target, price_manual, price_applied):		
		
		print 
		print 'Create Order Lines with Target'
		print target


		order_id = self.id

		product = self.env['product.product'].search([
														('x_name_short','=', target),
														('x_origin','=', False),
												])
		#print product
		#print product.name
		#print product.x_treatment



# Order line creation  - With the correct price 

		# Manual Price  
		if price_manual != 0: 
			
			#print 'Manual Price'

			ol = self.order_line.create({
											'product_id': product.id,
											'order_id': order_id,										
											'price_unit': price_manual,
											'x_price_manual': price_manual, 
										})

		# Quick Laser 
		#elif product.categ_id.name == 'Quick Laser': 	
		elif product.x_treatment == 'laser_quick': 	
			
			#print 'Quick Laser Price'
			
			price_quick = price_applied

			ol = self.order_line.create({
											'product_id': product.id,
											'order_id': order_id,
											'price_unit': price_quick,
										})

		# Normal case
		else: 
			
			#print 'Normal Price'		
			
			ol = self.order_line.create({
											'product_id': product.id,
											'order_id': order_id,
									})


		return self.nr_lines
	# x_create_order_lines_target	




# ----------------------------------------------------------- Testing Units ------------------------------------------------------

	# Unit Testing 
	@api.multi
	def test_units(self):  

		print 
		print 'Unit Testing Begin'

		self.treatment.create_order('consultation')

		self.test_clean_services()
		self.treatment.create_order('procedure')

		self.update_descriptors_all()

		self.update_type_batch()

		self.state_change()
		self.state_change()

		self.x_type = 'ticket_receipt'
		self.print_ticket()
		self.x_type = 'ticket_invoice'
		self.print_ticket()


		self.cancel_order()
		self.activate_order()
		self.state = 'sale'

		print 
		print 'Unit Testing End'
		print 



	# Clean Services 
	@api.multi
	def test_clean_services(self):  
		for service in self.treatment.service_vip_ids:
			service.state = 'draft'
		for service in self.treatment.service_co2_ids:
			service.state = 'draft'
		for service in self.treatment.service_quick_ids:
			service.state = 'draft'
		for service in self.treatment.service_excilite_ids:
			service.state = 'draft'
		for service in self.treatment.service_ipl_ids:
			service.state = 'draft'
		for service in self.treatment.service_ndyag_ids:
			service.state = 'draft'
		for service in self.treatment.service_medical_ids:
			service.state = 'draft'




