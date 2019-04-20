# -*- coding: utf-8 -*-
#
# 	Quotation 
# 

from openerp import models, fields, api
from datetime import datetime





#------------------------------------------------------------------------
class Order(models.Model):
	
	#_name = 'openhealth.order'
	_inherit = 'sale.order'

		
	order_line  = fields.One2many(
			'sale.order.line',
			'order_id',
			domain = [
						('id', '=', '3201'),
			#			('doctor', '=', PHYSICIAN),
			],
	)
	
	
	
	def get_domain_order_line(self,cr,uid,ids,context=None):

		context = 'laser_co2'
		print 
		print context
		print 

		#return {
		#	'warning': {
		#		'title': "Laser",
		#		'message': context,
		#}}

		mach = []
		lids = self.pool.get('product.template').search(cr,uid,[('x_treatment', '=', context)])
		return {'domain':{'service':[('id','in',lids)]}}
		
		
	


	name = fields.Char(
			string = 'Order #',
			#string = 'Procedimiento #',
	)
			
	consultation = fields.Many2one('openhealth.consultation',
			ondelete='cascade', 
	)
			

	patient = fields.Many2one(
			'oeh.medical.patient',
			#string="Patient", 
			string="Paciente", 
			#required=True, 

	        #default='This is the actual model',

			index=True
	)
			
			
			
	#partner_invoice_id = fields.Many2one(
	#		'res.partner',
	#		required=False, 
	#)
	
	#partner_shipping_id = fields.Many2one(
	#		'res.partner',
	#		required=False, 			
	#)
	
	pricelist_id = fields.Many2one(
			'product.pricelist',
			required=False, 					
	)


	currency_id = fields.Many2one(
			'res.currency',
			required=False, 					
	)



	#products = fields.One2many(
	#products = fields.Many2one(
	#		'product.template',
	#		)
			
			
	#x_nex = fields.Char(
	#	default='nex',
	#)





	#state_changes = fields.Char(
	#		default='a',
	#		compute='_compute_state_changes', 
	#		)

	#@api.depends('state')	
	#def _compute_state_changes(self):
	#	print
	#	print 'jx'
	#	for record in self:
	#		record.state_changes = 'b'
	#		print record.state_changes










	#_state_list = [
    #     			('draft', 'Quotation'),
	#				('sent', 'Quotation Sent'),
	#				('sale', 'Sale Order'),
	#				('done', 'Done'),
	#				('cancel', 'Cancelled'),
    #     	   ]

	
	


	# State changes
	#@api.onchange('state')
	#def _onchange_state(self):
		
	#	print 
	#	print 'jx'
	#	print 'Order - State change'
	#	print self.state
		
		#self.x_state = 'b'
		
	#	name = 'name',

	#	patient = self.patient
		
	#	print patient
		
		#return {
		#	'warning': {
		#		'title': "Order - State",
		#		'message': self.state + ' ' + patient.name,
		#}}
		
		
		
	#	print self.consultation.treatment.procedure_ids
		
	#	self.consultation.treatment.procedure_ids.create({
			
	#										'name': 'name',
	#										'patient': patient.name,
											
											#'product_id': se.service.id,
											#'product_uom': se.service.uom_id.id,
											#'order_id': order_id,
											#'order_id': 33,
		#									'order_id': consultation_id,
	#									})

		
	#	print 
		

		
# 13 Nov 2016

			#print 'copy'
			#if not self.x_copy_created:			
			#if not self.x_copy_created  and  self.state == 'draft':			
				#ret = self.copy({
				#				#'state':'sale',
				#				'state':'sent',
				#			})	
				#self.x_copy_created = True
			#print ret 

	
	

# 19 Nov 2016

	# Price Subtotal 

	#x_price_subtotal_wigv = fields.Float(
	#		string="Subtotal",

	#		compute="_compute_x_price_subtotal_wigv",
	#	)

	#@api.multi
	#@api.depends('price_subtotal')
	
	#def _compute_x_price_subtotal_wigv(self):
	#	for record in self:
	#		record.x_price_subtotal_wigv = math.ceil(record.price_subtotal * 118.0)








	#x_mark = fields.Char(
	#	default='mark',
	#)

	#product_id = fields.Many2one(
	#	'product.product',
	#	'order_line',
	#	domain = [
	#				('type', '=', 'service'),
	#				('x_treatment', '=', 'laser_co2'),
	#			],

	#	)






# 10 Jan 2017
# Create Machine

		m_list = ['laser_co2_1', 'laser_co2_2', 'laser_co2_3']
		idx = 0 

		x_machine = m_list[idx]


		appointment_date = app.appointment_date 
		doctor = app.doctor
		duration = app.duration

		ret = 1 

		#if True: 
		if appointment_date != False: 

			while not ret == 0:
	

				print 'jx'
				print 'Create Machine'
				print self.patient
				print self.x_doctor
				print 

				app = self.env['oeh.medical.appointment'].search([ 	
															('patient', 'like', self.patient.name),		
															('doctor', 'like', self.x_doctor.name), 	
															('x_type', 'like', 'procedure'), 
															#('state', 'like', 'pre_scheduled'), 
														], 
															order='appointment_date desc', limit=1)


				print app

				#x_machine = 'laser_co2_1'
				#duration = 0.5
				#doctor = self.x_doctor
				#appointment_date = 


				# Check for collisions 
				#ret, doctor_name, start, end = appfuncs.check_for_collisions(self, self.appointment_date, self.doctor, self.duration, self.x_machine)
				#ret, doctor_name, start, end = appfuncs.check_for_collisions(self, app.appointment_date, app.doctor, app.duration, x_machine)
				ret, doctor_name, start, end = appfuncs.check_for_collisions(self, appointment_date, doctor, duration, x_machine)

			
				if ret != 0:	# Error 

					#x_machine = False

					x_machine = m_list[idx]

					idx = idx + 1
					if idx == 3:
						idx = 0




					return {
							'warning': {
									'title': "Error: Colisión !",
									'message': 'La sala ya está reservada: ' + start + ' - ' + end + '.',
						}}




				else: 			# Success 

					print 'Success !'

					app = self.env['oeh.medical.appointment'].create(
																	{
																		'appointment_date': app.appointment_date,

																		'doctor': app.doctor.id,			
																		'patient': app.patient.id,	
																		'treatment': app.treatment.id,	

																		'duration': app.duration,
																		'x_type': 'procedure',
																		'x_create_procedure_automatic': False, 

																		'x_machine': x_machine,
																	}
																)
					print app
					print 
					print 








# 13 Jan 2017
		if 'state' in vals:
			state = vals['state']
			#print state
			#print 'state: ', self.state
			#print 'patient: ', self.patient.name
			#print 'doctor: ', self.x_doctor.name
			#print 'order_line: ', self.order_line


			#if state == 'draft':
			if state == 'sale':
			
				for line in self.order_line:
					product_id = line.product_id

					# If Service 
					if product_id.type == 'service':
						#print product_id.type
						#print product_id.name

						appointment = self.env['oeh.medical.appointment'].search([ 	
															('doctor', 'like', self.x_doctor.name), 	
															('patient', 'like', self.patient.name),		
															('x_type', 'like', 'procedure'), 
															#('state', 'like', 'pre_scheduled'), 
														], 
														order='appointment_date desc', limit=1)

						appointment_id = appointment.id

						print appointment  
						print appointment_id  



						# Self 
						self.x_appointment_date = appointment.appointment_date
						self.x_doctor_name = appointment.doctor.name
						self.x_duration = appointment.duration 





						# Create Machine
						appointment_date = appointment.appointment_date
						doctor_name = self.x_doctor.name
						doctor_id = self.x_doctor.id
						patient_id = self.patient.id
						treatment_id = self.treatment.id

						duration = 0.5


						x_machine = appfuncs.search_machine(self, appointment_date, doctor_name, duration)
	



						if x_machine != False:


							self.x_machine = x_machine 


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
						else:
						
							ret = -1
							#return {	'warning': 	{'title': "Error: Colisión !",
							#			'message': 	'La sala ya está reservada.',   
										#' + start + ' - ' + end + '.',
							#			}}
	




						# Write 
						#rec_set = self.env['oeh.medical.appointment'].browse([appointment_id])
						#ret = rec_set.write({
						#						'state': 'Scheduled',
						#					})
						#print ret 

				




		#ret = treatment_funcs.create_procedure_go(self)




		#Write your logic here
		#res = False
		#if ret != -1:
		#	res = super(sale_order, self).write(vals)








# 12 May 2017



	#@api.multi
	#@api.depends('x_state')
	#def _compute_state(self):
	#	for record in self:
	#		record.state = record.x_state



	#@api.onchange('x_state')
	#def _onchange_x_state(self):
	#	print 
	#	print 
	#	print 'On change x State'
	#	self.state = self.x_state
	#		print 'Gotcha !!!'
	#	print 
	#	print 








	# x_state
	x_state = fields.Selection(

			selection = ord_vars._x_state_list, 

			string='x Estado',	
			default='draft',	
			compute="_compute_x_state",
	)

	@api.multi
	#@api.depends('state')

	def _compute_x_state(self):
		for record in self:

			if record.state == 'draft':
				record.x_state = record.state

			if	record.env['openhealth.payment_method'].search_count([('order','=', record.id),]):	
				if record.x_amount_total == record.pm_total:			
					record.x_state = 'payment'

			if	record.env['openhealth.sale_document'].search_count([('order','=', record.id),]):
				record.x_state = 'proof'

			if (record.x_machine != False	or 	record.patient.name == False) and record.x_sale_document:
				record.x_state = 'machine'

			if record.state == 'sale':
				record.x_state = 'sale'









# 16 May 

# ----------------------------------------------------------- CRUD ------------------------------------------------------


# Create - Deprecated ? 
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




# Write - Deprecated ?
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




# 22 May

				x_type = ''

				if record.x_sale_document.receipt != False:
					x_type = 'receipt'

				if record.x_sale_document.invoice != False:
					x_type = 'invoice'

				if record.x_sale_document.advertisement != False:
					x_type = 'advertisement'

				if record.x_sale_document.sale_note != False:
					x_type = 'sale_note'

				if record.x_sale_document.ticket_receipt != False:
					x_type = 'ticket_receipt'

				if record.x_sale_document.ticket_invoice != False:
					x_type = 'ticket_invoice'

				record.x_sale_document_type = x_type







# CRUD
	@api.model
	def unlink(self,vals):
		print 
		print 'Order - Unlink - Override'
		print 
		print vals
		print 
	
	
		#print self.state
		#self.state = 'draft'
		#print self.state


		#Write your logic here
		res = super(sale_order).unlink(vals)
		#Write your logic here
		return res






# 17 Jun 2017

	# Comprobante 
	#x_sale_document = fields.Many2one(
	#		'openhealth.sale_document',
	#		string="Comprobante", 
			#required=True, 
	#		compute='_compute_x_sale_document', 
	#	)

	#@api.multi
	#@api.depends('state')
	#def _compute_x_sale_document(self):
	#	for record in self:
	#		doc = record.env['openhealth.sale_document'].search([('order','=', record.id),],
																#order='appointment_date desc',
	#															limit=1,)
	#		record.x_sale_document = doc

	# Sale Document Type 
	#x_sale_document_type = fields.Selection(
	#		selection = ord_vars._sale_doc_type_list, 
	#		string="Comprobante Tipo", 
			#required=True, 
	#		compute='_compute_x_sale_document_type', 
	#	)
	#@api.multi
	#@api.depends('state')
	#def _compute_x_sale_document_type(self):
	#	for record in self:
	#		if record.x_sale_document != False: 
	#			record.x_sale_document_type = record.x_sale_document.x_type






	#@api.multi 
	#def x_create_invoice(self):
		#print 
		#print 
		#print 
		#print 'jx'
		#print 'X Create Invoice'
		#print 
		#print 
		#print 
	# x_create_invoice

	#@api.multi 
	#def action_invoice_create(self, grouped=False, final=False):
		#print 
		#print 'jx'
		#print 'Action Invoice Create - Local'
		#print 
		#print 
		#print 
	# x_create_invoice





# State
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
	#	#print 
	#	#print 
	#	#print 'On change State'		
	#	if self.pm_total != self.x_amount_total:
	#		self.state = 'draft'
	#	#print self.state	
	#	#print 
	#	#print 





# Payment Method 
	#x_payment_method = fields.One2many(
	#		'openhealth.payment_method',
	#		'order',		
	#		string="Pagos", 
	#	)

	#@api.onchange('x_payment_method')
	#def _onchange_x_payment_method(self):
	#	#print 
	#	#print 
	#	#print 'On change - Payment Method'
	#	#print self.x_payment_method	
	#	total = 0.0
	#	for pm in self.x_payment_method:
	#		total = total + pm.subtotal
	#	self.pm_total = total
	#	#print 
	#	#print 





# Therapist
	#x_therapist = fields.Many2one(
			#'openhealth.therapist',
	#		'oeh.medical.physician',
	#		domain = [						
	#					('x_therapist', '=', True),
	#				],
	#		string = "Terapeuta", 	
	#	)






# Consultation 									# Deprecated ? 
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









# ----------------------------------------------------------- Create order lines - Target ------------------------------------------------------

# Update Lines 	- DEPRECATED !
	#@api.multi 
	#def update_order_lines(self):
	#	ret = self.x_create_order_lines()
	#	return 1

# Remove - DEPRECATED !
	#@api.multi 
	#def remove_order_lines(self):
	#	ret = self.order_line.unlink()
	#	return ret 



# Create Order Lines 
	#@api.multi 
	#def x_create_order_lines(self):
	#	order_id = self.id
		# co2
	#	for se in self.consultation.service_co2_ids:
	#		ret = self.create_line(order_id, se)
		# 'excilite'
	#	for se in self.consultation.service_excilite_ids:
	#		ret = self.create_line(order_id, se)
		#print 'ipl'
	#	for se in self.consultation.service_ipl_ids:
	#		ret = self.create_line(order_id, se)
		#print 'ndyag'
	#	for se in self.consultation.service_ndyag_ids:
	#		ret = self.create_line(order_id, se)
		#print 'medical'
	#	for se in self.consultation.service_medical_ids:
	#		ret = self.create_line(order_id, se)
		#print 'cosmetology'
	#	for se in self.cosmetology.service_ids:
	#		ret = self.create_line(order_id, se)
		#print 'out'
	#	return self.nr_lines



# ----------------------------------------------------------- Create Line ------------------------------------------------------

	#@api.multi 
	#def create_line(self, order_id, se):
	#	product_id = se.service.id
	#	name = se.name_short
	#	x_price_vip = se.service.x_price_vip
	#	x_price = se.service.list_price
	#	if self.x_partner_vip and x_price_vip != 0.0:
	#		price_unit = x_price_vip
	#	else:
	#		price_unit = x_price
	#	if self.nr_lines == 0:
	#		ol = self.order_line.create({
	#									'product_id': product_id,
	#									'order_id': order_id,
	#									'state':'draft',
	#									'name': name,
	#									'price_unit': price_unit,
	#									'x_price_vip': x_price_vip,
	#									'x_price': x_price,
	#									'product_uom': se.service.uom_id.id, 
	#								})
	#	else:
	#		order_line_id = self.env['sale.order.line'].search([
	#															('order_id', 'like', order_id),
	#															('name', 'like', name),
	#															]).id
	#		rec_set = self.env['sale.order.line'].browse([
	#														order_line_id																
	#													])			
	#		ol = rec_set.write({
	#								'price_unit': price_unit,
	#							})
	#	return 1





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



