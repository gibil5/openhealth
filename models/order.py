# -*- coding: utf-8 -*-
#
# 	Order 
# 
#

from openerp import models, fields, api

import jxvars
import app_vars
import ord_vars
import order_funcs

import appfuncs
import mac_funcs

import cosvars



import datetime


class sale_order(models.Model):
	
	#_name = 'openhealth.order'
	_inherit='sale.order'
	




	name = fields.Char(
			string="Presupuesto #"
		)







	# Consistency 

	#subtotal = fields.Float(
	#		string = 'Sub-total', 
			#required=True, 
	#	)

	#method = fields.Selection(
	#		string="Medio", 
	#		selection = ord_vars._payment_method_list, 			
	#		required=True, 
	#	)

	# Number of paymethods  
	#pm_complete = fields.Boolean(
	#							default = False, 
	#							readonly=False,
								#string="Pm Complete",
								#compute="_compute_pm_complete",
	#)








	# Payment Method 
	x_payment_method = fields.Many2one(

			'openhealth.payment_method',

			string="Pagos", 
		)





	# Open Treatment
	@api.multi 
	def open_treatment(self):

		print 
		print 'Open Treatment'


		ret = self.treatment.open_myself()

		return ret 
	# open_treatment





	# Open Myself
	@api.multi 
	def open_myself(self):

		print 
		print 'Open Myself'

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










	# Partner 
	partner_id = fields.Many2one(

			'res.partner',
		
			string = "Cliente", 	

			required=True, 
		)



	# Family 
	x_family = fields.Selection(
			string = "Tipo", 	

			default='product',
			
			selection = jxvars._family_list, 
		)










	# Doctor name  
	#x_doctor_name = fields.Char(
	

	doctor_name = fields.Char(
									default = 'generic doctor',
						)
	



	#compute="_compute_x_doctor_name",
	#@api.multi
	#@api.depends('x_doctor')

	#def _compute_x_doctor_name(self):
	#	for record in self:
	#		record.x_doctor_name = record.x_doctor.name 




	# Doctor name  
	x_partner_name = fields.Char(
									default = 'generic partner',
									#compute="_compute_x_partner_name",
	)
	
	#@api.multi
	#@api.depends('partner_id')

	#def _compute_x_partner_name(self):
	#	for record in self:
	#		record.x_partner_name = record.partner_id.name 














	margin = fields.Float(
			string="Margen"
		)

	validity_date = fields.Char(
			string="Fecha de expiración"
		)











	# Number of paymethods  
	#pm_complete = fields.Boolean(
	#							default = False, 
	#							readonly=False,
								#string="Pm Complete",
								#compute="_compute_pm_complete",
	#)
	
	#@api.multi
	#@api.depends('pm_total')

	#def _compute_pm_complete(self):
	#	print 'Compute Pm Complete'
	#	for record in self:
	#		if record.pm_total == record.x_amount_total: 
	#			print 'Equal !'
	#			record.pm_complete = True
				#record.state = 'payment'
	#		else:
	#			print 'Not Equal'
	#		print record.pm_total
	#		print record.x_amount_total
	#		print record.pm_complete
	#		print record.state





	# Payment Complete
	x_payment_complete = fields.Boolean(
								#default = False, 
								#readonly=False,
								#string="Pm Complete",
	)





	@api.multi 
	def x_reset(self):

		print 
		print 'jx'
		print 'Reset'



		#self.procedure_ids.unlink()
		self.x_payment_method.unlink()
	
		#self.x_sale_document = False
		self.x_sale_document.unlink()




		#self.x_appointment.unlink()
		#self.x_appointment = False
		#self.x_appointment.x_machine = False
#jz
		if self.x_appointment.x_machine != False:
			self.x_appointment.x_machine = False




		#self.pre_state = 'draft'
		self.state = 'draft'			# This works. 
		self.x_confirmed = False

		print 
		print 
		print 

	# x_reset














	# Comprobante 
	x_sale_document = fields.Many2one(
			'openhealth.sale_document',
			#string="Comprobante de pago", 
			string="Comprobante", 
			#required=True, 
			compute='_compute_x_sale_document', 
		)


	@api.multi
	#@api.depends('state')

	def _compute_x_sale_document(self):
		for record in self:

			#doc = record.env['openhealth.sale_document'].search_count([
			#															('order','=', record.id),
			#															])

			doc = record.env['openhealth.sale_document'].search([
																		('order','=', record.id),
																],
																#order='appointment_date desc',
																limit=1,)
			record.x_sale_document = doc















	@api.multi 
	def x_create_invoice(self):

		print 
		print 
		print 
		print 'jx'
		print 'X Create Invoice'
		print 
		print 
		print 

	# x_create_invoice






	@api.multi 
	#def create_invoice(self):
	#def action_view_sale_advance_payment_inv(self):
	#def sale_advance_payment_inv(self):
	#def invoice_create(self):
	def action_invoice_create(self, grouped=False, final=False):

		print 
		print 'jx'
		print 'Action Invoice Create - Local'

		print 
		print 
		print 

	# x_create_invoice





#jz
	# state 
	state = fields.Selection(

			#selection = ord_vars._state_list, 
			selection = ord_vars._x_state_list, 

			string='Estado',	

			readonly=False,

			default='draft',


			#copy=False, 
			#index=True, 
			#track_visibility='onchange', 
			#compute="_compute_state",
			)



	#@api.multi
	#@api.depends('state')

	#def _compute_state(self):
	#	for record in self:

	#		record.state = 'draft'

	#		if	record.env['openhealth.payment_method'].search_count([('order','=', record.id),]):	
	#			if record.x_amount_total == record.pm_total:			
	#				record.state = 'payment'


	#		if	record.env['openhealth.sale_document'].search_count([('order','=', record.id),]):
	#			record.state = 'proof'



			#if record.x_sale_document  and  	(record.x_machine != False		or 		record.x_family == 'consultation'):
			#if (record.x_machine != False	or 	record.patient.name == False) and record.x_sale_document:
			#if record.x_machine != False:
			#	record.state = 'machine'



	#		if record.x_confirmed != False:
	#			record.state = 'sale'

	# _compute_state







	#@api.onchange('state')
	#def _onchange_state(self):
	#	print 
	#	print 
	#	print 'On change State'
		
	#	if self.pm_total != self.x_amount_total:
	#		self.state = 'draft'

	#	print self.state	
	#	print 
	#	print 



	x_confirmed = fields.Boolean(
			default=False, 
		)






	# Payment Method 
	#x_payment_method = fields.One2many(
	#		'openhealth.payment_method',
	#		'order',		
	#		string="Pagos", 
	#	)

	#@api.onchange('x_payment_method')
	#def _onchange_x_payment_method(self):
	#	print 
	#	print 
	#	print 'On change - Payment Method'
	#	print self.x_payment_method	
	#	total = 0.0
	#	for pm in self.x_payment_method:
	#		total = total + pm.subtotal
	#	self.pm_total = total
	#	print 
	#	print 














	# Total of Payments
	pm_total = fields.Float(
								#string="Total",
								
								#compute="_compute_pm_total",
	)
	


	#@api.onchange('pm_total')
	#def _onchange_pm_total(self):
	#	print 
	#	print 
	#	print 'On change - Pm Total'
	#	print self.pm_total
	#	print self.x_amount_total
	#	print self.state
	#	if self.pm_total == self.x_amount_total:
	#		self.state = 'payment'
	#	print self.state	
	#	print 
	#	print 





	@api.multi
	#@api.depends('x_payment_method')

	def _compute_pm_total(self):

		print 
		print 
		print 'Compute - Pm Total'


		for record in self:

			total = 0.0
			for pm in record.x_payment_method:
				total = total + pm.subtotal


			record.pm_total = total

			#record.pm_complete = True
			record.x_payment_complete = True


			print record.name
			print 'pm_total: ', record.pm_total
			print 'x_amount_total: ', record.x_amount_total

			#print 'pm_complete: ', record.pm_complete
			print 'x_payment_complete: ', record.x_payment_complete

			print 


		print
		print





	# Target 
	x_target = fields.Selection(
			string="Target", 

			#selection = jxvars._target_list, 
			selection = app_vars._target_list, 

			compute='_compute_x_target', 
		)




	#@api.multi
	@api.depends('x_doctor')

	def _compute_x_target(self):
		for record in self:

			#if record.x_doctor.name != False: 
			if record.treatment.name != False: 
				record.x_target = 'doctor'

			#if record.x_therapist.name != False: 
			if record.cosmetology.name != False: 
				record.x_target = 'therapist'









	# Machine Required  
	x_machine_req = fields.Char(

			string='Sala req.',

			compute='_compute_x_machine_req', 
		)

	#@api.multi
	@api.depends('x_product')

	def _compute_x_machine_req(self):
		for record in self:

			tre = record.x_product.x_treatment

			mac = cosvars._hash_tre_mac[tre]

			record.x_machine_req = mac






	# Product
	x_product = fields.Many2one(
			'product.template',			
			string="Producto",
			
			#required=True, 
			
			compute='_compute_x_product', 
			)


	#@api.multi
	@api.depends('order_line')

	def _compute_x_product(self):
		for record in self:

			flag = False

			for line in record.order_line:
				product = line.product_id.id
				flag = True 

			if flag: 
				record.x_product = product







	# Doctor 
	x_doctor = fields.Many2one(
			'oeh.medical.physician',
			string = "Médico", 	
		)



	#x_therapist = fields.Many2one(

			#'openhealth.therapist',
	#		'oeh.medical.physician',

	#		domain = [						
	#					('x_therapist', '=', True),
	#				],
	
	#		string = "Terapeuta", 	
	#	)








# ----------------------------------------------------------- Relational ------------------------------------------------------

	# Consultation 									# Deprecated ? 
	consultation = fields.Many2one(
			'openhealth.consultation',
			string="Consulta",
			ondelete='cascade', 
	#		compute='_compute_consultation_cos', 
		)



	#@api.multi
	#@api.depends('x_appointment')
	#def _compute_consultation_cos(self):
	#	for record in self:
	#		consultation = self.env['openhealth.consultation.cos'].search([
	#																		('patient', '=', record.patient.name), 
																			#('x_type', '=', 'procedure'),
																			#('x_target', '=', record.x_target),	
	#																		('doctor', '=', record.x_doctor.name), 
	#																	],
	#																		order='appointment_date desc',
	#																		limit=1,)
	#		record.consultation_cos = consultation





	# Appointment 
	x_appointment = fields.Many2one(
			'oeh.medical.appointment',
			
			string='Cita', 

			#required=True, 
			compute='_compute_x_appointment', 
			)



	@api.multi
	#@api.depends('x_appointment')

	def _compute_x_appointment(self):
		for record in self:


			if record.x_family == 'procedure':
				app = self.env['oeh.medical.appointment'].search([
																	('patient', '=', record.patient.name), 
																	('x_type', '=', 'procedure'),
																	#('x_target', '=', record.x_target),	
																	('doctor', '=', record.x_doctor.name), 
																],
																	order='appointment_date desc',
																	limit=1,
																)
				record.x_appointment = app




			#if record.x_target == 'doctor': 
			#	app = self.env['oeh.medical.appointment'].search([
			#														('patient', '=', record.patient.name), 
			#														('x_type', '=', 'procedure'),
			#														('x_target', '=', record.x_target),
			#														('doctor', '=', record.x_doctor.name), 
			#												],
			#												order='appointment_date desc',
			#												limit=1,)


			#else:		# therapist 
			#	app = self.env['oeh.medical.appointment'].search([
			#														('patient', '=', record.patient.name), 
			#														('x_type', '=', 'procedure'),
			#														('x_target', '=', record.x_target),

			#														('x_therapist', '=', record.x_therapist.name), 
			#												],
			#												order='appointment_date desc',
			#												limit=1,)

			













	# Amount total 
	x_amount_total = fields.Float(
			string = "Total",
			compute="_compute_x_amount_total",
		)


	@api.multi
	#@api.depends('x_payment_method')

	def _compute_x_amount_total(self):
		for record in self:
			sub = 0.0

			for line in record.order_line:

				sub = sub + line.price_subtotal 
			
			record.x_amount_total = sub







	x_partner_vip = fields.Boolean(
			'Vip', 

			#readonly=True
			
			default=False, 

			compute="_compute_partner_vip",
			)

	@api.multi

	def _compute_partner_vip(self):
		for record in self:
			#print 
			#print 'jx'
			#print 'Compute Partner Vip'
			rec_set = self.env['sale.order'].search([
															('partner_id','=', record.partner_id.id),
															('state','=', 'sale'),
														]) 
			for rec in rec_set:
				#print rec
				for line in rec.order_line:
					#print line
					#print line.name 
					if line.name == 'Tarjeta VIP':
						#print 'Gotcha !!!'
						record.x_partner_vip = True 
					
					#print 
			#print 
			#print 
			#print 


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
























# ---------------------------------------------- Create PM --------------------------------------------------------

	@api.multi 
	def create_payment_method(self):

		print 
		print 'Create Payment Method'



		#nr_pm = self.env['openhealth.payment_method'].search_count([('order','=', self.id),]) 
		#name = 'Pago ' + str(nr_pm + 1)
		name = 'Pago'
		method = 'cash'



		#total = self.x_amount_total
		balance = self.x_amount_total - self.pm_total

		
		#print nr_pm
		print name
		print method
		print 




		# Create 
		#if payment_method_id == False:
		self.x_payment_method = self.env['openhealth.payment_method'].create({
																				'order': self.id,

																				'name': name,
																			
																				'method': method,
																			
																				'subtotal': balance,
																			

																				'pm_total': self.pm_total,
																			
																				'total': self.x_amount_total,

																				'balance': balance, 
																			})
		payment_method_id = self.x_payment_method.id 



#jz
		# State - Change
		print 'State changes'
		self.state = 'payment'
		print self.state
		print 




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
							'form': {'action_buttons': True, }
							},


				'context': {
							'default_order': self.id,

							'default_name': name,
							'default_method': method,
							'default_subtotal': balance,
							'default_total': self.x_amount_total,
							'default_pm_total': self.pm_total,
							}
				}

	# create_payment_method








# ---------------------------------------------- Create Sale Document --------------------------------------------------------

	@api.multi 
	def create_sale_document(self):
		print 
		print 'Create Sale Document'


		# Search 
		sale_document_id = self.env['openhealth.sale_document'].search([('order','=',self.id),]).id



		# Create 
		if sale_document_id == False:

			sale_document = self.env['openhealth.sale_document'].create({
																			'order': self.id,
																			'total': self.x_amount_total, 
																			'partner': self.partner_id.id,				
																		})
			sale_document_id = sale_document.id 


		self.sale_document = sale_document_id




		# State
		print 'State changes'
		self.state = 'proof'
		print self.state
		print 




		return {
				'type': 'ir.actions.act_window',
				'name': ' New sale_document Current', 

				'view_type': 'form',
				'view_mode': 'form',	
				'target': 'current',


				'res_model': 'openhealth.sale_document',				
				'res_id': sale_document_id,


				'flags': 	{
							#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
							'form': {'action_buttons': True, }
							},


				'context': {
							'default_order': self.id,
							'default_total': self.x_amount_total,
							'default_partner': self.partner_id.id,
							}
				}

	# create_sale_document












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























	x_payment_method_code = fields.Char(

			string="Código", 
						
			#required=True, 
		)






	x_ruc = fields.Char(

			string="RUC", 
						
			#required=True, 
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
	#x_chief_complaint = fields.Selection(
	#		string = 'Motivo de consulta', 
	#		selection = jxvars._chief_complaint_list, 
	#		)


























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
			string="Tratamiento", 
		)




	cosmetology = fields.Many2one(
			'openhealth.cosmetology',
			ondelete='cascade', 			
			string="Cosmiatría", 
		)

















	
	patient = fields.Many2one(
		
			'oeh.medical.patient',

			string='Paciente', 
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







# ----------------------------------------------------------- Create order lines - Target ------------------------------------------------------

	@api.multi 
	def x_create_order_lines_target(self, target):

		print 
		print 
		print 'Create order lines - Target'
		
		order_id = self.id



		# Order - Search
		product = self.env['product.template'].search([

														#('x_family','=', 'private'),
														('x_name_short','=', target),

												])

		print product
		print product.id
		
		product_id = product.id


		price_unit = product.list_price



		x_price_vip = product.x_price_vip
		product_uom = product.uom_id.id
		#x_price = product.price


		#ret = self.create_line(order_id, product)
		#print ret

		ol = self.order_line.create({

										'product_id': product_id,
										
										'order_id': order_id,

										
										#'consultation':consultation.id,
										
										'state':'draft',


										'name': target,


										'price_unit': price_unit,

										'x_price_vip': x_price_vip,
										
										#'x_price': x_price,


										#'product_uom': se.service.uom_id.id, 
										'product_uom': product_uom, 
									})

		print
		print 

		return self.nr_lines




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

	



	# For Ooor compatibility - Commented : BEGIN


	# Total 
	#x_price_total = fields.Float(
	#		string="Total",
	#		default=5.0,

	#		compute="_compute_x_price_total",
	#	)

	#x_price_vip_total = fields.Float(
	#		string="Total Vip",
	#		default=3.0,

	#		compute="_compute_x_price_vip_total",
	#	)

	
	#@api.multi
	#def _compute_x_price_total(self):
	#	for record in self:			
	#		total = 0 
	#		for line in record.order_line:
	#			total = total + line.x_price_wigv 
	#		record.x_price_total = total 


	# For Ooor compatibility 
	#@api.multi
	#def _compute_x_price_vip_total(self):
	#	for record in self:			
	#		total = 0 
	#		for line in record.order_line:
	#			total = total + line.x_price_vip_wigv
	#		record.x_price_vip_total = total 


	# For Ooor compatibility - Commented : END






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





# ----------------------------------------------------------- Button - Update Order ------------------------------------------------------
	@api.multi 
	def update_order(self):

		print 
		print 'jx'
		print 'Update Order'

		order_id = self.id



		# Appointment 
		appointment = self.env['oeh.medical.appointment'].search([ 	
																	('patient', 'like', self.patient.name),	

																	#('doctor', 'like', self.physician.name), 	
																	#('x_therapist', 'like', self.x_therapist.name), 	
																	('doctor', 'like', self.x_doctor.name), 	
																	
																	('x_type', 'like', 'procedure'), 
																], 
																	order='appointment_date desc', limit=1)

		appointment_id = appointment.id

		print appointment
		print appointment_id


		self.x_appointment = appointment_id
		print self.x_appointment
		print 
		print 




		# Lines 
		ret = self.order_line.unlink()

		# Cosmetology 
		for service in self.cosmetology.service_ids:
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


		#print 'x_state', self.x_state



		#if self.x_doctor.name != False   and   self.x_machine == False:
		if self.x_doctor.name != False   and   self.x_machine == False	 and 	self.x_machine_req != 'consultation':
			
			print 'Warning: Sala no Reservada !'


		else:
			print 'Success !!!'

			#self.x_state = 'sale'
			#self.x_confirmed = True 



			# State is changed here ! 
			res = super(sale_order, self).action_confirm()

		#else: 
			

		
		#res = super(sale_order, self).action_confirm()
		#Write your logic here
		
		print
	# action_confirm
	








# ----------------------------------------------------------- Buttons - Order  ------------------------------------------------------

	@api.multi
	def remove_myself(self):  

		print 
		print 
		print 'Remove Myself'
		
		print self.name 

		self.x_reset()
		
		self.unlink()



		#self.x_appointment.x_machine = 'none'

		#order_id = self.id
		#print "id: ", order_id
		

		# Search 
		#rec_set = self.env['sale.order'].browse([order_id])
		#print "rec_set: ", rec_set


		# Write
		#ret = rec_set.write({
		#						'state': 'draft',
								#'x_machine': 'none',
		#					})
		#print ret

		#for rec in rec_set:
		#	rec.x_reset


		
		# Unlink 
		#ret = rec_set.unlink()
		#print "ret: ", ret
		

		print 
		print 
	# remove_myself






# ----------------------------------------------------------- Nr Mac Clones  ------------------------------------------------------

	@api.multi 
	def get_nr_mc(self):

		nr_mac_clones =	self.env['oeh.medical.appointment'].search_count([
																			('appointment_date','=', self.x_appointment.appointment_date),
																			
																			#('x_machine','=', self.x_machine),
																			('x_machine','=', self.x_appointment.x_machine),
																		]) 
		return nr_mac_clones




# ----------------------------------------------------------- Button - Reseve Machine  ------------------------------------------------------

	@api.multi 
	def reserve_machine(self):

		print
		print 
		print 'jx'
		print 'Reserve Machine'
		print 


		date_format = "%Y-%m-%d %H:%M:%S"
		duration = self.x_appointment.duration 
		delta = datetime.timedelta(hours=duration)



		# Easiest first 
		#self.x_appointment.x_machine = self.x_machine_req






		#m_list = ['laser_co2_1', 'laser_co2_2', 'laser_co2_3']

		m_dic = {
					'consultation':			[], 


					'laser_co2_1': 			['laser_co2_1', 'laser_co2_2', 'laser_co2_3'], 

					'laser_excilite': 		['laser_excilite'], 
				
					'laser_m22': 			['laser_m22'], 



					'laser_triactive': 		['laser_triactive'], 
					
					'chamber_reduction': 	['chamber_reduction'], 
					
					'carboxy_diamond': 		['carboxy_diamond'], 
			}



		m_list = m_dic[self.x_machine_req]

		ad_str = self.x_appointment.appointment_date


		k = 1.
		out = False 



		while not out		and  	  k < 6: 		



			for x_machine_req in m_list: 



				if not out: 				
					self.x_appointment.appointment_date = ad_str

					self.x_appointment.x_machine = x_machine_req

					nr_mc = self.get_nr_mc()



					print k
					print self.x_appointment.appointment_date				
					print nr_mc



					if nr_mc == 1:		# Success - Get out 
						out = True 



					print out 
					print 




			if not out: 	# Error - Change the date 
				ad = datetime.datetime.strptime(self.x_appointment.appointment_date, date_format) 
				ad_dt = delta + ad
				ad_str = ad_dt.strftime("%Y-%m-%d %H:%M:%S")

				k = k + 1.

				



	# reserve_machine





# ----------------------------------------------------------- Button - Reseve Machine  ------------------------------------------------------

	@api.multi 
	def reserve_machine_old(self):

		print 'jx'
		print 'Reserve Machine - Old'

		#self.x_machine = 'laser_co2_1'


		
		# Create Machine
		appointment_date = 	self.x_appointment_date
		doctor_name = 		self.x_doctor.name
		doctor_id = 		self.x_doctor.id
		patient_id = 		self.patient.id
		treatment_id = 		self.treatment.id
		duration = 			self.x_duration


		x_machine_old = 	self.x_machine




		#start_machine = 	self.x_machine
		start_machine = 	self.x_machine_req





		# New 
		#x_machine = appfuncs.search_machine(self, appointment_date, doctor_name, duration)
		#x_machine = appfuncs.search_machine(self, appointment_date, doctor_name, duration, start_machine)
		x_machine = mac_funcs.search_machine(self, appointment_date, doctor_name, duration, start_machine)
		

		


		self.x_machine = x_machine 
		self.x_appointment.x_machine = x_machine





		# If Sucess create Machine Appointment
		if x_machine != False:


			# Create Appointment - Machine 
			app = self.env['oeh.medical.appointment'].create(
															{
																'appointment_date': appointment_date,

																'patient': 		patient_id,																	

																'x_type': 		'procedure',

																'duration': 	duration,
																																
																'x_create_procedure_automatic': False, 

																'x_machine': 	x_machine,



							                    				#'x_target': 	'machine',
							                    				'x_target': 	self.x_target,


																'doctor': 		doctor_id,

																'treatment': 	treatment_id, 
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








	#----------------------------------------------------------- Quick Button ------------------------------------------------------------

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




#sale_order()


