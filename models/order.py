# -*- coding: utf-8 -*-
#
# 	Order 
# 
#

from openerp import models, fields, api

import jxvars
import appfuncs

import app_vars

import ord_vars


import order_funcs



class sale_order(models.Model):
	
	#_name = 'openhealth.order'
	_inherit='sale.order'
	




	#@api.multi 
	#def create_sale_document(self):
	#	print 
	#	print 'Create Sale Document'





	# Doctor 
	x_doctor = fields.Many2one(
			'oeh.medical.physician',
			string = "Médico", 	
		)

	x_therapist = fields.Many2one(
			'openhealth.therapist',
			string = "Terapeuta", 	
		)







	partner_id = fields.Many2one(

			'res.partner',
		
			string = "Cliente", 	

			required=True, 
		)








	amount_total = fields.Float(

			string = "Total",

			compute="_compute_amount_total",
		)

	@api.multi
	#@api.depends('x_payment_method')

	def _compute_amount_total(self):

		for record in self:

			sub = 0.0

			for line in record.order_line:
				sub = sub + line.price_subtotal 

			record.amount_total = sub







	x_partner_vip = fields.Boolean(
			'Vip', 

			#readonly=True
			
			default=False, 

			compute="_compute_partner_vip",
			)

	@api.multi
	#@api.depends('x_payment_method')

	def _compute_partner_vip(self):
		for record in self:

			print 
			print 'jx'
			print 'Compute Partner Vip'
			#count = self.env['sale.order'].search_count([
			#												('partner_id','=', record.partner_id.id),
			#												('state','=', 'sale'),
			#											]) 


			rec_set = self.env['sale.order'].search([
															('partner_id','=', record.partner_id.id),
															('state','=', 'sale'),
														]) 

			for rec in rec_set:
				print rec

				for line in rec.order_line:
					print line
					print line.name 

					if line.name == 'Tarjeta VIP':
						print 'Gotcha !!!'
						record.x_partner_vip = True 
					
					print 

			print 


			#if count > 0:
			#	record.x_partner_vip = True 
			#else:				
			#	record.x_partner_vip = False 


			print 
			print 


# ---------------------------------------------- Event --------------------------------------------------------


	event_ids = fields.One2many(

			'openhealth.event',
		
			'order',		

			string="Eventos", 
		)




	x_cancel = fields.Boolean(
			string='', 
			default = False
		)

	x_cancel_reason = fields.Char(
			string='Motivo de anulación', 
		)

	x_cancel_owner = fields.Char(
			string='Quién anula', 
		)



	@api.multi 
	def cancel_order(self):
		print 
		print 'Cancel'
		self.x_cancel = True

		#ret = self.create_event()
		ret = order_funcs.create_event(self)

		return(ret)



	@api.multi 
	def activate_order(self):
		print 
		print 'Cancel'
		self.x_cancel = False





# ----------------------------------------------------------- Number ofs ------------------------------------------------------


	# Number of saledocs  
	nr_saledocs = fields.Integer(
			string="Documentos de venta",
			compute="_compute_nr_saledocs",
	)
	@api.multi
	def _compute_nr_saledocs(self):
		for record in self:

			receipt =			self.env['openhealth.receipt'].search_count([('order','=', record.id),]) 

			invoice =			self.env['openhealth.invoice'].search_count([('order','=', record.id),]) 

			advertisement =		self.env['openhealth.advertisement'].search_count([('order','=', record.id),]) 

			sale_note =			self.env['openhealth.sale_note'].search_count([('order','=', record.id),]) 
			
			ticket_receipt =	self.env['openhealth.ticket_receipt'].search_count([('order','=', record.id),]) 
			
			ticket_invoice =	self.env['openhealth.ticket_invoice'].search_count([('order','=', record.id),]) 

			record.nr_saledocs= receipt + invoice + advertisement + sale_note + ticket_receipt + ticket_receipt







	# Number of paymethods  
	nr_pay_methods = fields.Integer(
			string="Documentos de venta",
			compute="_compute_nr_pay_methods",
	)
	@api.multi
	def _compute_nr_pay_methods(self):

		for record in self:

			pm = self.env['openhealth.payment_method'].search_count([('order','=', record.id),]) 

			record.nr_pay_methods = pm







	# Number of paymethods  
	pm_total = fields.Float(
								string="Total",
								compute="_compute_pm_total",
	)
	
	#@api.multi
	@api.depends('x_payment_method')

	def _compute_pm_total(self):

		for record in self:

			total = 0.0

			for pm in record.x_payment_method:

				total = total + pm.subtotal


			record.pm_total = total








	# Number of paymethods  
	pm_complete = fields.Boolean(
								string="Pm Complete",
								default = False, 
								
								compute="_compute_pm_complete",
	)
	

	@api.multi
	#@api.depends('pm_total')

	def _compute_pm_complete(self):

		for record in self:
			
			if (record.pm_total != record.amount_total)		or 	 (record.nr_saledocs == 0) : 
				record.pm_complete = False

			else:
				record.pm_complete = True







# ---------------------------------------------- Create PM --------------------------------------------------------
	@api.multi 
	def create_payment_method(self):

		print 
		print 'Create Payment Method'



		nr_pm = self.env['openhealth.payment_method'].search_count([('order','=', self.id),]) 

		name = 'Pago ' + str(nr_pm + 1)

		method = 'cash'

		
		print nr_pm
		print name
		print method
		print 

		return {
				'type': 'ir.actions.act_window',
				'name': ' New PM Current', 

				'view_type': 'form',
				'view_mode': 'form',	
				'target': 'current',


				'res_model': 'openhealth.payment_method',				
				#'res_id': receipt_id,


				'flags': 	{
							#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
							'form': {'action_buttons': True, }
							},

				'context': {
							'default_order': self.id,
							'default_name': name,
							'default_method': method,
							}
				}

	# create_payment_method







# ---------------------------------------------- Create Receipt --------------------------------------------------------
	@api.multi 
	def create_receipt(self):
		print 
		print 'Create Receipt'


		# Search 
		receipt_id = self.env['openhealth.receipt'].search([('order','=',self.id),]).id

		# Create 
		if receipt_id == False:

			receipt = self.env['openhealth.receipt'].create({
																'order': self.id,
																'total': self.amount_total, 

																'partner': self.partner_id.id,				
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
							'default_order': self.id,
							'default_total': self.amount_total,

							'default_partner': self.partner_id.id,
							}
				}

	# create_receipt





# ---------------------------------------------- Create Invoice --------------------------------------------------------
	@api.multi 
	def create_invoice(self):
		print 
		print 'Create Invoice'


		# Search 
		invoice_id = self.env['openhealth.invoice'].search([('order','=',self.id),]).id

		# Create 
		if invoice_id == False:

			invoice = self.env['openhealth.invoice'].create({
																'order': self.id,
																'total': self.amount_total, 
																'ruc': self.x_ruc,	

																'partner': self.partner_id.id,	
													})
			invoice_id = invoice.id 



		self.x_invoice = invoice_id


		return {
				'type': 'ir.actions.act_window',
				'name': ' New invoice Current', 

				'view_type': 'form',
				'view_mode': 'form',	
				'target': 'current',


				'res_model': 'openhealth.invoice',				
				'res_id': invoice_id,


				'flags': 	{
							#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
							'form': {'action_buttons': True, }
							},


				'context': {
							'default_order': self.id,
							'default_total': self.amount_total,
							'default_ruc': self.x_ruc,

							'default_partner': self.partner_id.id,
							}
				}

	# create_invoice





# ---------------------------------------------- Create advertisement --------------------------------------------------------
	@api.multi 
	def create_advertisement(self):
		print 
		print 'Create advertisement'


		# Search 
		advertisement_id = self.env['openhealth.advertisement'].search([('order','=',self.id),]).id

		# Create 
		if advertisement_id == False:

			advertisement = self.env['openhealth.advertisement'].create({
																'order': self.id,
																'total': self.amount_total, 

																'partner': self.partner_id.id,	
													})
			advertisement_id = advertisement.id 


		self.x_advertisement = advertisement_id


		return {
				'type': 'ir.actions.act_window',
				'name': ' New advertisement Current', 

				'view_type': 'form',
				'view_mode': 'form',	
				'target': 'current',


				'res_model': 'openhealth.advertisement',				
				'res_id': advertisement_id,


				'flags': 	{
							#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
							'form': {'action_buttons': True, }
							},


				'context': {
							'default_order': self.id,
							'default_total': self.amount_total,

							'default_partner': self.partner_id.id,
							}
				}

	# create_advertisement






# ---------------------------------------------- Create Sale Note --------------------------------------------------------
	@api.multi 
	def create_sale_note(self):
		print 
		print 'Create Sale Note'



		# Search 
		sale_note_id = self.env['openhealth.sale_note'].search([('order','=',self.id),]).id

		# Create 
		if sale_note_id == False:

			sale_note = self.env['openhealth.sale_note'].create({
																'order': self.id,
																'total': self.amount_total, 

																'partner': self.partner_id.id,	
													})
			sale_note_id = sale_note.id 



		self.x_sale_note = sale_note_id


		return {
				'type': 'ir.actions.act_window',
				'name': ' New sale_note Current', 

				'view_type': 'form',
				'view_mode': 'form',	
				'target': 'current',


				'res_model': 'openhealth.sale_note',				
				'res_id': sale_note_id,


				'flags': 	{
							#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
							'form': {'action_buttons': True, }
							},


				'context': {
							'default_order': self.id,
							'default_total': self.amount_total,

							'default_partner': self.partner_id.id,
							}
				}

	# create_sale_note









# ---------------------------------------------- Create Ticket Receipt  --------------------------------------------------------
	@api.multi 
	def create_ticket_receipt(self):
		print 
		print 'Create Ticekt Receipt'

		# Search 
		ticket_receipt_id = self.env['openhealth.ticket_receipt'].search([('order','=',self.id),]).id

		# Create 
		if ticket_receipt_id == False:

			ticket_receipt = self.env['openhealth.ticket_receipt'].create({
																'order': self.id,
																'total': self.amount_total, 

																'partner': self.partner_id.id,	
													})
			ticket_receipt_id = ticket_receipt.id 



		self.x_ticket_receipt = ticket_receipt_id


		return {
				'type': 'ir.actions.act_window',
				'name': ' New ticket_receipt Current', 

				'view_type': 'form',
				'view_mode': 'form',	
				'target': 'current',


				'res_model': 'openhealth.ticket_receipt',				
				'res_id': ticket_receipt_id,


				'flags': 	{
							#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
							'form': {'action_buttons': True, }
							},


				'context': {
							'default_order': self.id,
							'default_total': self.amount_total,

							'default_partner': self.partner_id.id,
							}
				}

	# create_ticket_receipt








# ---------------------------------------------- Create Ticket Invoice --------------------------------------------------------
	@api.multi 
	def create_ticket_invoice(self):
		print 
		print 'Create Ticket Invoice'


		# Search 
		ticket_invoice_id = self.env['openhealth.ticket_invoice'].search([('order','=',self.id),]).id

		# Create 
		if ticket_invoice_id == False:

			ticket_invoice = self.env['openhealth.ticket_invoice'].create({
																'order': self.id,
																'total': self.amount_total, 

																'partner': self.partner_id.id,	
													})
			ticket_invoice_id = ticket_invoice.id 



		self.x_ticket_invoice = ticket_invoice_id


		return {
				'type': 'ir.actions.act_window',
				'name': ' New ticket_invoice Current', 

				'view_type': 'form',
				'view_mode': 'form',	
				'target': 'current',


				'res_model': 'openhealth.ticket_invoice',				
				'res_id': ticket_invoice_id,


				'flags': 	{
							#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
							'form': {'action_buttons': True, }
							},


				'context': {
							'default_order': self.id,
							'default_total': self.amount_total,

							'default_partner': self.partner_id.id,
							}
				}

	# create_ticket_invoice









# ---------------------------------------------- Vars --------------------------------------------------------

	#x_receipt = fields.One2many(
	receipt = fields.Many2one(

		'openhealth.receipt',
		
		#'order',

		string='Boleta de venta',
		)



	#x_invoice = fields.One2many(
	x_invoice = fields.Many2one(

		'openhealth.invoice',
		
		#'order',

		string='Factura',
		)




	x_advertisement = fields.Many2one(
		'openhealth.advertisement',		
		string='Canje',
		)

	x_sale_note = fields.Many2one(
		'openhealth.sale_note',		
		string='Nota de venta',
		)

	x_ticket_receipt = fields.Many2one(
		'openhealth.ticket_receipt',		
		string='Ticket Boleta',
		)

	x_ticket_invoice = fields.Many2one(
		'openhealth.ticket_invoice',		
		string='Ticket Factura',
		)











	x_sales_document = fields.Selection(

			string="Documento de venta", 

			selection = ord_vars._sale_docs_list, 
						
			#required=True, 

			#compute='_compute_x_machine', 
		)





	#x_payment_method = fields.Selection(
	#		selection = ord_vars._payment_method_list, 			
	#	)



	x_payment_method = fields.One2many(
			'openhealth.payment_method',
			'order',		

			string="Medios de pago", 
		)





	x_payment_method_code = fields.Char(

			string="Código", 
						
			#required=True, 
		)






	x_ruc = fields.Char(

			string="RUC", 
						
			#required=True, 
		)








	x_appointment = fields.Many2one(
			'oeh.medical.appointment',
			
			#string='Appointment #'
			string='Cita', 

			#required=False, 
			#required=True, 
			compute='_compute_x_appointment', 
			)






	# Family 
	x_family = fields.Selection(

			selection = jxvars._family_list, 
		)



	# Machine 
	x_machine = fields.Selection(
			#string="Máquina", 
			string="Sala", 
			#selection = jxvars._machines_list, 
			selection = app_vars._machines_list, 
			
			compute='_compute_x_machine', 
			#required=True, 
		)






	x_appointment_date = fields.Datetime(
			string="Fecha", 
			#readonly=True,

			compute='_compute_x_appointment_date', 
			#required=True, 
			)


	x_duration = fields.Float(
			string="Duración (h)", 
			#readonly=True, 

			compute='_compute_x_duration', 
			#required=True, 		
			)




	#@api.multi
	#@api.depends('x_appointment')
	#def _compute_x_doctor(self):
	#	for record in self:
	#		record.x_doctor = record.x_appointment.doctor





	@api.multi
	#@api.depends('x_appointment')

	def _compute_x_appointment(self):
		for record in self:


			app = self.env['oeh.medical.appointment'].search([
																	('doctor', '=', record.x_doctor.name), 
																	('patient', '=', record.patient.name), 

																	('x_type', '=', 'procedure'),
																	('x_target', '=', 'doctor'),


																	#('appointment_date', 'like', dt), 
																	#('x_machine', '=', x_machine),
															],
															order='appointment_date desc',
															limit=1,)



			record.x_appointment = app



	#@api.multi
	@api.depends('x_appointment')

	def _compute_x_appointment_date(self):
		for record in self:
			record.x_appointment_date = record.x_appointment.appointment_date



	#@api.multi
	@api.depends('x_appointment')

	def _compute_x_duration(self):
		for record in self:
			record.x_duration = record.x_appointment.duration



	#@api.multi
	@api.depends('x_appointment')

	def _compute_x_machine(self):
		for record in self:
			record.x_machine = record.x_appointment.x_machine








	# Chief complaint 
	x_chief_complaint = fields.Selection(
			string = 'Motivo de consulta', 

			selection = jxvars._chief_complaint_list, 
			)











	_state_list = [
        			#('pre-draft', 'Pre-Quotation'),

        			#('draft', 'Quotation'),
        			#('sent', 'Quotation Sent'),
        			#('sale', 'Sale Order'),
        			#('done', 'Done'),
        			#('cancel', 'Cancelled'),
					#('pre-draft', 	'Presupuesto consulta'),


        			('draft', 		'Presupuesto'),
        			
        			('sent', 		'Presupuesto enviado'),
        			('sale', 		'Facturado'),
        			('done', 		'Completo'),
        			('cancel', 		'Cancelado'),
        		]


	state = fields.Selection(
			selection = _state_list, 

			#string='Status', 			
			string='Estado',	
			
			#readonly=True, 
			readonly=False, 

			#default='draft'
			#copy=False, 
			#index=True, 
			#track_visibility='onchange', 
			)


	#jxx
	@api.onchange('state')

	def _onchange_state(self):

		print 
		print 
		print 'On change State'

		if self.state == 'sale':	

			print 'Gotcha !!!'

		print 
		print 











	vspace = fields.Char(
			' ', 
			readonly=True
			)
	
	
	order_line = field_One2many=fields.One2many(
		'sale.order.line',
		'order_id',

		#string='Order',
		#compute="_compute_order_line",
		)


	#@api.multi
	#@api.depends('x_partner_vip')
	
	#def _compute_order_line(self):
	#	for record in self:
	#		print 'compute_order_line'
	#		print record.x_partner_vip 
	#		ret = record.update_order_lines()
	#		print ret 







# ----------------------------------------------------------- Relationals ------------------------------------------------------

	treatment = fields.Many2one(
			'openhealth.treatment',
			ondelete='cascade', 
		)


	cosmetology = fields.Many2one(
			'openhealth.cosmetology',
			ondelete='cascade', 			
			string="Cosmiatría", 
		)




	consultation = fields.Many2one(
			'openhealth.consultation',
			string="Consulta",
			ondelete='cascade', 
		)














	
	patient = fields.Many2one(
			'oeh.medical.patient',

			string='Paciente', 
	)
	
	
	
	x_state = fields.Char(
		default='a',
	)
	

	#x_copy_created = fields.Boolean(
	#	default=False,
	#)

		

	
	
	
	
	
	
	# Nr lines 
	nr_lines = fields.Integer(
			
			default=0,

			string='Nr líneas',
			
			compute='_compute_nr_lines', 
			#required=True, 
			)

	@api.multi
	#@api.depends('order_line')
	
	def _compute_nr_lines(self):
		for record in self:
			#record.name = 'SE00' + str(record.id) 
			#record.nr_lines = 0
			
			ctr = 0
			for l in record.order_line:
				ctr = ctr + 1
			record.nr_lines = ctr 
			
	
	
	
	
	
	# Order lines 

	@api.multi 
	def clean_order_lines(self):
		
		if self.state == 'draft':
			ret = self.remove_order_lines()







	# On change - Vip 

	#@api.onchange('x_partner_vip')
	
	#def _onchange_x_partner_vip(self):
		#print 'onchange'

		#name = self.name 		
		#order_id = self.env['sale.order'].search([('name', 'like', name)]).id

		#print self.id
		#print self.name
		#print order_id 

		#ret = self.update_order_lines(order_id)
		#print ret 

		#print 




	# Update Lines 
	@api.multi 
	def update_order_lines(self):

		print 
		print 'update_order_lines'

		#ret = self.remove_order_lines()

		ret = self.x_create_order_lines()

		return 1



	# Remove 
	@api.multi 
	def remove_order_lines(self):
		ret = self.order_line.unlink()
		return ret 





# ----------------------------------------------------------- Create Line ------------------------------------------------------

	@api.multi 
	def create_line(self, order_id, se):
		print 'create line'

		product_id = se.service.id
		name = se.name_short


		# Consultation 
		consultation = self.consultation
		print consultation 
		print consultation.id



		x_price_vip = se.service.x_price_vip
		x_price = se.service.list_price

		if self.x_partner_vip and x_price_vip != 0.0:
			price_unit = x_price_vip
		else:
			price_unit = x_price


		#print product_id
		#print order_id
		#print name
		#print price_unit
		#print se.service.uom_id.id
		#print 



		if self.nr_lines == 0:
			print 'create new'

			ol = self.order_line.create({

										'product_id': product_id,
										
										'order_id': order_id,

										
										'consultation':consultation.id,
										
										#'state':'pre-draft',
										'state':'draft',


										'name': name,

										'price_unit': price_unit,

										'x_price_vip': x_price_vip,
										
										'x_price': x_price,

										'product_uom': se.service.uom_id.id, 
									})

		else:
			print 'update existing'

			order_line_id = self.env['sale.order.line'].search([
																('order_id', 'like', order_id),
																('name', 'like', name),
																]).id
			print order_line_id


			rec_set = self.env['sale.order.line'].browse([
															order_line_id																
														])
			print rec_set 

			#ol = self.order_line.create({
			#ol = self.order_line.write(1, order_line_id, 
			
			ol = rec_set.write({
									#'product_id': product_id,
									#'order_id': order_id,
									#'name': name,
									'price_unit': price_unit,
									#'product_uom': se.service.uom_id.id, 
								})


		return 1




# ----------------------------------------------------------- Create order lines ------------------------------------------------------

	@api.multi 
	def x_create_order_lines(self):
		print 
		print 'Create order lines'
		
		
		order_id = self.id


		print 
		print 'co2'
		for se in self.consultation.service_co2_ids:
			print se 
			
			ret = self.create_line(order_id, se)



		print 
		print 'excilite'
		for se in self.consultation.service_excilite_ids:
			print se 

			ret = self.create_line(order_id, se)


		
		print 
		print 'ipl'
		for se in self.consultation.service_ipl_ids:
			print se 

			ret = self.create_line(order_id, se)



		print 
		print 'ndyag'
		for se in self.consultation.service_ndyag_ids:
			print se 

			ret = self.create_line(order_id, se)



		print 
		print 'medical'
		for se in self.consultation.service_medical_ids:
			print se 

			ret = self.create_line(order_id, se)





		print 
		print 'cosmetology'
		for se in self.cosmetology.service_ids:
			print se 

			ret = self.create_line(order_id, se)







		print 'out'

		return self.nr_lines

	



	# Total 
	x_price_total = fields.Float(
			string="Total",
			default=5.0,

			compute="_compute_x_price_total",
		)

	x_price_vip_total = fields.Float(
			string="Total Vip",
			default=3.0,

			compute="_compute_x_price_vip_total",
		)

	

	@api.multi
	#@api.depends('x_price')
	
	def _compute_x_price_total(self):
		for record in self:			
			total = 0 

			for line in record.order_line:
				#total = total + line.price_total 
				total = total + line.x_price_wigv 

			record.x_price_total = total 



	@api.multi
	#@api.depends('x_price_vip')
	
	def _compute_x_price_vip_total(self):
		for record in self:			
			total = 0 

			for line in record.order_line:
				total = total + line.x_price_vip_wigv

			record.x_price_vip_total = total 






# ----------------------------------------------------------- Button - Update Lines ------------------------------------------------------
	@api.multi 
	#def update_line(self, order_id, product_id, name, list_price, uom_id):
	def update_line(self, order_id, product_id, name, list_price, uom_id, x_price_vip):


		print 'update existing'

		#line_id = self.env['sale.order.line'].search([
		#														('order_id', 'like', order_id),
		#														('name', 'like', name),
		#												]).id
			
		#print order_line_id
		#rec_set = self.env['sale.order.line'].browse([
		#												order_line_id																
		#											])
		#print rec_set 
		#ol = rec_set.write({
									#'product_id': product_id,
									#'order_id': order_id,
									#'name': name,
		#						'price_unit': price_unit,
									#'product_uom': se.service.uom_id.id, 
		#					})



		order = self.env['sale.order'].search([
															('id', '=', order_id),
															#('name', 'like', name),
													])
		print order 

		print order.id
		print product_id
		print name 
		print uom_id

		line = order.order_line.create({
											'order_id': order.id,

											'product_id': product_id,

											'name': name,

											'product_uom': uom_id, 


											#'price_unit': product_price_unit,
											'x_price_vip': x_price_vip, 

											'x_partner_vip': self.x_partner_vip
										})
		print line
		print 

		return line
	# update_line



	@api.multi 
	def update_order(self):

		print 
		print 'jx'
		print 'Update Order'

		order_id = self.id


		#order.order_line.unlink
		ret = self.order_line.unlink()


		for service in self.consultation.service_co2_ids:
			print service

			line = self.update_line(	
										order_id, 
										service.service.id, 
										service.service.x_name_short, 
										service.service.list_price, 
										service.service.uom_id.id,

										service.service.x_price_vip
									)
			print 
		
		for service in self.consultation.service_excilite_ids:
			print service
			line = self.update_line(	
										order_id, 
										service.service.id, 
										service.service.x_name_short, 
										service.service.list_price, 										
										service.service.uom_id.id,

										service.service.x_price_vip
									)

		for service in self.consultation.service_ipl_ids:
			print service
			line = self.update_line(	order_id, 
										service.service.id, 
										service.service.x_name_short, 
										service.service.list_price, 
										service.service.uom_id.id,

										service.service.x_price_vip
									)

		for service in self.consultation.service_ndyag_ids:
			print service
			line = self.update_line(	order_id, 
										service.service.id, 
										service.service.x_name_short, 
										service.service.list_price, 
										service.service.uom_id.id,

										service.service.x_price_vip
									)

		for service in self.consultation.service_medical_ids:
			print service
			line = self.update_line(	order_id, 
										service.service.id, 
										service.service.x_name_short, 
										service.service.list_price, 
										service.service.uom_id.id,

										service.service.x_price_vip
									)

		print 

	# update_order 




	@api.multi 
	def update_order_lines_app(self):

		print 
		print 'jx'
		print 'Update Order Lines'


		for line in self.order_line:

			print line


			product_id = line.product_id


			# If Service 
			if product_id.type == 'service':



				appointment = self.env['oeh.medical.appointment'].search([ 	
															('doctor', 'like', self.x_doctor.name), 	
															('patient', 'like', self.patient.name),		
															('x_type', 'like', 'procedure'), 
															('x_target', '=', 'doctor'), 
															#('state', 'like', 'pre_scheduled'), 
														], 
														order='appointment_date desc', limit=1)

				appointment_id = appointment.id

				
				print self.x_doctor
				print self.patient

				
				print appointment  
				print appointment_id  



				# Line  
				line.x_appointment_date = appointment.appointment_date
				line.x_doctor_name = appointment.doctor.name
				line.x_duration = appointment.duration 
				
				#line.x_machine_oldachine = appointment.x_machine
				line.x_machine = False


				# Self 
				self.x_appointment = appointment

				#self.x_doctor = appointment.doctor
				#self.x_appointment_date = appointment.appointment_date
				#self.x_duration = appointment.duration
				#self.x_machine = appointment.x_machine 


		print 


	# update_order_lines_app	






	@api.multi 
	def action_confirm(self):
		print 
		print 'jx'
		print 'Action confirm - Over ridden'
		 


		#Write your logic here



		# Validate 
		#if self.x_machine != False:


		print 'x_doctor.name: ', self.x_doctor.name
		print 'x_machine', self.x_machine



		if self.x_doctor.name != False   and   self.x_machine == False:
			print 'Warning: Sala no Reservada !'

		else:
			print 'Success !!!'
			res = super(sale_order, self).action_confirm()

		#else: 
			

		
		#res = super(sale_order, self).action_confirm()
		#Write your logic here
		
		print
	# action_confirm
	


# ----------------------------------------------------------- CRUD ------------------------------------------------------



# Create 
	@api.model
	def create(self,vals):
		print 
		print 'Order - Create - Override'
		print 
		print vals
		print 
	
		#Write your logic here
		res = super(sale_order, self).create(vals)
		#Write your logic here
		return res





# Write 
	@api.multi
	def write(self,vals):

		print 
		print 'Order - Write - Override'
		#print 
		#print vals
		#print 
		#print 




		#if 'x_machine' in vals:
		#	x_machine = vals['x_machine']
		#	print x_machine
		#else:
		#	print 'Error !'
		#	return {
		#				'warning': {
		#							'title': "Error: Sala no Reservada !",
		#							'message': 'jx',
												#'Cita ya existente, con el ' + doctor_name + ": " + start + ' - ' + end + '.',
		#						}}


		#ok = True 
		#if 'x_appointment' in vals:
		#	x_appointment_id = vals['x_appointment']
		#	print x_appointment_id
		#	x_appointment = self.env['oeh.medical.appointment'].search([
		#															('id', '=', x_appointment_id), 
		#														])
		#	print x_appointment
		#	if x_appointment.x_machine == False:
		#		ok = False 
				#ok = True
		#	else:
		#		x_appointment.state = 'Scheduled'
				# Success !!!  
		#		ok = True
		#print 

		#res = 0
		#if ok:
		#	res = super(sale_order, self).write(vals)
		#else:
		#	res = -1
		



		# Confirm 
		if self.x_appointment.x_machine != False: 
			self.x_appointment.state = 'Scheduled'



		res = super(sale_order, self).write(vals)
		#Write your logic here
		print 
		print 

		return res

	# CRUD 



# ----------------------------------------------------------- Buttons - Order  ------------------------------------------------------

	@api.multi
	def remove_myself(self):  

		print 
		print 'Remove Order'


		#self.x_appointment.x_machine = 'none'


		order_id = self.id
		print "id: ", order_id
		

		# Search 
		rec_set = self.env['sale.order'].browse([order_id])
		print "rec_set: ", rec_set

		# Write
		ret = rec_set.write({
								'state': 'draft',
								#'x_machine': 'none',
							})

		
		# Unlink 
		ret = rec_set.unlink()
		print "ret: ", ret
		print 

	# remove_myself





# ----------------------------------------------------------- Button - Reseve Machine  ------------------------------------------------------

	@api.multi 
	def reserve_machine(self):

		print 'jx'
		print 'Reserve Machine'

		#self.x_machine = 'laser_co2_1'


		
		# Create Machine
		appointment_date = 	self.x_appointment_date

		doctor_name = 		self.x_doctor.name
		doctor_id = 		self.x_doctor.id
		patient_id = 		self.patient.id
		treatment_id = 		self.treatment.id
		duration = 			self.x_duration


		x_machine_old = 	self.x_machine
		start_machine = 	self.x_machine





		# New 
		#x_machine = appfuncs.search_machine(self, appointment_date, doctor_name, duration)
		x_machine = appfuncs.search_machine(self, appointment_date, doctor_name, duration, start_machine)
		
		self.x_machine = x_machine 
		self.x_appointment.x_machine = x_machine





		# If Sucess create Machine Appointment
		if x_machine != False:


			# Create Appointment - Machine 
			app = self.env['oeh.medical.appointment'].create(
															{
																'appointment_date': appointment_date,

																'doctor': 		doctor_id,
																'patient': 		patient_id,	
																'treatment': 	treatment_id, 

																'duration': 	duration,
																'x_type': 		'procedure',
																'x_create_procedure_automatic': False, 

																'x_machine': 	x_machine,
							                    				'x_target': 	'machine',
															}
															)



			if app != False:

				# Unlink Old 
				rec_set = self.env['oeh.medical.appointment'].search([
																			('appointment_date', 'like', appointment_date), 
																			('doctor', '=', doctor_name), 
																			('x_machine', '=', x_machine_old),

																			('patient', '=', self.patient.name), 
																	])
				ret = rec_set.unlink()
				print "ret: ", ret




		else:
			print 'Error !'	
			print 			


			return {	'warning': 	{'title': "Error: Colisión !",
						'message': 	'La sala ya está reservada.',   
			#' + start + ' - ' + end + '.',
						}}

	# reserve_machine




#sale_order()


