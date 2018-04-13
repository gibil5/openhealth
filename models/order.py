# -*- coding: utf-8 -*-
#
#
# 	Order 
# 
# Created: 				26 Aug 2016
#

from openerp import models, fields, api
import datetime
import app_vars
import ord_vars
import appfuncs
import cosvars
import treatment_vars
from num2words import num2words
import math 
import time 
from openerp import tools
import count_funcs

class sale_order(models.Model):
	
	_inherit='sale.order'
	#_name = 'openhealth.order'
	






# ----------------------------------------------------------- Deprecated ------------------------------------------------------








# ----------------------------------------------------------- Compute - Solving ------------------------------------------------------

	# Product
	x_product = fields.Char(		
			string="Producto",	
			required=False, 			
		)




# ----------------------------------------------------------- Date Order ------------------------------------------------------

	date_order = fields.Datetime(
		#string='Order Date', 
		#required=True, 
		#readonly=True, 
		#index=True, 

		states={	
					'draft': [('readonly', False)], 
					'sent': [('readonly', False)], 
					'sale': [('readonly', True)], 
					
					'editable': [('readonly', False)], 
				}, 

		#write=['openhealth.roots'], 
		
		#copy=False, 
		#default=fields.Datetime.now
	)




	# State 
	state = fields.Selection(

			selection = ord_vars._state_list, 
			
			string='Estado',	
			readonly=False,
			default='draft',

			#copy=False, 
			#index=True, 
			#track_visibility='onchange', 
			#compute="_compute_state",
		)




	@api.multi
	def state_change(self):  

		print 
		print 'jx'
		print 'State Change'

		print self.state 


		if self.state == 'sale': 
			self.state = 'editable'
		elif self.state == 'editable': 
			self.state = 'sale'


		print self.state 




# ----------------------------------------------------------- Primitives ------------------------------------------------------

	x_confirmed = fields.Boolean(
			default=False, 
		)


	treatment = fields.Many2one(
			'openhealth.treatment',
			ondelete='cascade', 
			string="Tratamiento",

			#readonly=True, 
			readonly=False, 
		)


	@api.onchange('x_doctor')
	def _onchange_x_doctor(self):

		print 'jx'		

		if self.x_doctor.name != False: 
			#uid = self.x_doctor.x_user_name.id
			#self.x_doctor_uid = uid


			treatment = self.env['openhealth.treatment'].search([
															
																	('patient', '=', self.patient.name), 
															
																	('physician', '=', self.x_doctor.name), 
													],
														order='write_date desc',
														limit=1,
													)

			print treatment
			self.treatment = treatment


			#if self.treatment.name != False: 
			#	self.treatment = treatment
			#else: 
			#	self.treatment = False











# ----------------------------------------------------- Create Order Line ------------------------------------------------------------

	@api.multi
	def create_orderline(self):  

		print 
		print 'jx'
		print 'Create Order Line'



		# Init Vars 
		context = self._context.copy()
		
		order_id = self.id

		x_type = context['x_type']

		#print context
		#print context['params']
		#print order_id

		res_id = False




		# Search Model 
		res = self.env['openhealth.product.selector'].search([
																#('patient', '=', self.patient.name),
															],
																#order='write_date desc',
																limit=1,
															)
		if res.id != False: 
			
			res_id = res.id 
			#print res_id




			#res.default_code = ''
			#res.product_id = False
			#res.x_type = x_type
			#res.price_manual_flag = False
			#res.price_manual = 0
			#res.family = False
			#res.treatment = False
			#res.zone = False
			#res.family = False

			#if x_type == 'product': 
			#	res.treatment = False
			#	res.zone = False
			#	res.family = False




			# Reset 
			res.reset()


			# Initialize 
			res.order_id = order_id
			res.product_uom_qty = 1 
			res.x_type = x_type






			
			





		print 
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

	# create_orderline










# ----------------------------------------------------------- Primitives ------------------------------------------------------


	currency_id = fields.Many2one(
			"res.currency", 
			related='pricelist_id.currency_id', 
			string="Currency", 
			readonly=True, 

			#required=True, 
			required=False, 

		)



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



			#record.x_total_in_words = words.title() + ' Soles'
			record.x_total_in_words = words.title()








	#x_total_cents = fields.Float(
	x_total_cents = fields.Integer(

			"Céntimos",

			compute='_compute_x_total_cents', 
		)

	@api.multi
	#@api.depends('')

	def _compute_x_total_cents(self):

		for record in self:

			#frac, whole = math.modf(2.5)
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

			#record.x_total_net = record.amount_total * 0.82
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

			#record.x_total_tax = record.amount_total * 0.18
			x = record.x_total_net * 0.18

			g = float("{0:.2f}".format(x))

			record.x_total_tax = g












	# Proc Created 
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

			
			copy=True, 
		)




	# Patient - For Reporting 
	patient_id = fields.Many2one(
			'oeh.medical.patient',
			string='Paciente', 
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






# ----------------------------------------------------------- On Changes ------------------------------------------------------


	# Patient  
	@api.onchange('patient')
	
	def _onchange_patient(self):	

		print 'jx'
		print 'On Change Patient'
		print 

		#if self.partner_id.name != False	and 	self.x_partner_dni == False: 
		#if self.partner_id.name != False: 
		if self.patient.name != False: 
			
			print 'gotcha !'

			self.partner_id = self.patient.partner_id.id 









	# Partner  
	@api.onchange('partner_id')
	
	def _onchange_partner_id(self):		
		print 'jx'
		print 'On Change Partner'
		print 

		#if self.partner_id.name != False	and 	self.x_partner_dni == False: 
		if self.partner_id.name != False: 
			
			print 'gotcha !'
			self.x_partner_dni = self.partner_id.x_dni





	# Dni 
	@api.onchange('x_partner_dni')
	
	def _onchange_x_partner_dni(self):		
		print 'jx'
		print 'On Change Dni'
		print 

		if self.x_partner_dni != False: 
			


			# Partner 
			partner_id = self.env['res.partner'].search([
															#('patient', '=', self.patient.name),			
															('x_dni', '=', self.x_partner_dni),					
												],
													order='write_date desc',
													limit=1,
												)
			print partner_id
			print partner_id.id
			self.partner_id = partner_id.id




			# Patient 
			patient = self.env['oeh.medical.patient'].search([
																#('patient', '=', self.patient.name),			
																('x_dni', '=', self.x_partner_dni),					
												],
													order='write_date desc',
													limit=1,
												)
			print patient
			print patient.id
			self.patient = patient.id





# ----------------------------------------------------------- Ticket - Date Order Corr ------------------------------------------------------


	#x_date_order_corr = fields.Datetime(
	x_date_order_corr = fields.Char(
		string='Order Date Corr', 
		#required=True, 
		#readonly=True, 
		#index=True, 
		#states={'draft': [('readonly', False)], 'sent': [('readonly', False)]}, 
		#copy=False, 
		#default=fields.Datetime.now


			compute="_compute_date_order_corr",
	)

	@api.multi
	#@api.depends('partner_id')

	def _compute_date_order_corr(self):
		for record in self:

			#record.x_date_order_corr = record.date_order





			#date_field1 = datetime.strptime(date_field1, DATETIME_FORMAT)
			#date_field2 = datetime.strptime(date_field2, DATETIME_FORMAT)
			#date_field2 = date_field1 + timedelta(hours=5,minutes=30)


			DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
			date_field1 = datetime.datetime.strptime(record.date_order, DATETIME_FORMAT)

			#date_field2 = datetime.strptime(date_field2, DATETIME_FORMAT)

			#date_field2 = date_field1 + datetime.timedelta(hours=5,minutes=0)
			date_field2 = date_field1 + datetime.timedelta(hours=-5,minutes=0)




			DATETIME_FORMAT_2 = "%d-%m-%Y %H:%M:%S"

			#date_field2 = datetime.datetime.strptime(date_field2, DATETIME_FORMAT_2)

			date_field2 = date_field2.strftime(DATETIME_FORMAT_2)

			record.x_date_order_corr = date_field2








# ----------------------------------------------------------- Serial Number ------------------------------------------------------

	# Serial Number 
	x_serial_nr = fields.Char(
			'Número de serie', 

			#compute="_compute_x_serial_nr",
		)


	#@api.multi
	#@api.depends('partner_id')
	#def _compute_x_serial_nr(self):
	#	for record in self:
	#		if record.x_payment_method != False: 
	#			serial_nr = record.x_payment_method.saledoc_code 
	#			record.x_serial_nr = serial_nr















# ----------------------------------------------------------- Test and Hunt ------------------------------------------------------







# ----------------------------------------------------------- Create order lines ------------------------------------------------------
	#@api.multi 
	def x_create_order_lines_target(self, target, price_manual, price_applied):		

		
		print 
		print 'Create Order Lines Target'
		print target
		#print 

		order_id = self.id



		#product = self.env['product.template'].search([
		product = self.env['product.product'].search([
														('x_name_short','=', target),
														('x_origin','=', False),
												])
		

		print product
		print product.name
		#print product.id
		#print product.x_name_short
		#print product.categ_id
		#print product.categ_id.name






# Order line creation  - With the correct price 


		# Manual Price  
		if price_manual != 0: 

			print 'Manual Price'

			ol = self.order_line.create({
											'product_id': product.id,
											'order_id': order_id,										

											'price_unit': price_manual,

											'x_price_manual': price_manual, 
										})

		

		
		
		# Quick Laer 
		#elif product.categ_id.name == 'Quick Laser': 	
		elif product.x_treatment == 'laser_quick': 	
		

			print 'Quick Laser Price'

			price_quick = price_applied


			ol = self.order_line.create({
											'product_id': product.id,
											'order_id': order_id,

											'price_unit': price_quick,
										})





		# Normal cases 
		else: 

			print 'Normal Price'		
			

			ol = self.order_line.create({
											'product_id': product.id,
											'order_id': order_id,
									})




		print ol
		print ol.product_id
		print ol.product_id.name 


		return self.nr_lines

	









	








	# Pricelist 
	pricelist_id = fields.Many2one(
			'product.pricelist', 
			string='Pricelist', 

			required=True, 
			#required=False, 
			
			readonly=True, 
			states={'draft': [('readonly', False)], 'sent': [('readonly', False)]}, 
			help="Pricelist for current sales order.", 
		)















	@api.multi
	def _get_default_doctor(self): 

		name = 'Clinica Chavarri'

		doctor = self.env['oeh.medical.physician'].search([
																		('name', '=', name),			
																	],
																	#order='start_date desc',
																	limit=1,
																)
		return doctor.id 




	# Doctor 
	x_doctor = fields.Many2one(

			'oeh.medical.physician',
		
			string = "Médico", 	


			#default = _get_default_doctor, 


			#states={
			#			'draft': 	[('readonly', False)], 
			#			'sent': 	[('readonly', True)], 
			#			'sale': 	[('readonly', True)], 
			#			'cancel': 	[('readonly', True)], 
			#			'done': 	[('readonly', True)], 
			#		}, 

		)




	x_doctor_uid = fields.Many2one(
			'res.users',
			string = "Médico Uid", 	

			readonly = True, 
			#compute='_compute_x_doctor_uid', 
		)










	@api.multi
	#@api.depends('')
	def _compute_x_doctor_uid(self):
		for record in self:
			if record.x_doctor.name != False: 

				#uid = self.env['res.users'].search([
															#('name', '=', 'Paul Canales'),
				#											('name', '=', name),
				#									],
				#									order='date desc',
				#									limit=1,
				#								)

				uid = record.x_doctor.x_user_name.id
				record.x_doctor_uid = uid



























	cr = fields.Char(
			#default='-------------------------------------------------------------------', 
			default='--------------------------------------------------------------', 
		)







	x_authorization = fields.Char(
		)




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

			#required=True, 
			required=False, 


			#compute="_compute_x_type",
		)

	@api.multi
	#@api.depends('partner_id')

	def _compute_x_type(self):
		for record in self:

			if record.x_payment_method != False: 
				record.x_type = record.x_payment_method.saledoc





	@api.multi
	def update_type(self):
		#print 'update type'
		if self.x_payment_method != False: 
			self.x_type = self.x_payment_method.saledoc
			#print self.x_type







	#@api.onchange('x_payment_method')
	#def _onchange_x_payment_method(self):

	@api.onchange('x_serial_nr')
	
	def _onchange_x_serial_nr(self):
	
		print 'jx'
		print 'On change serial nr'
		if self.x_payment_method.saledoc != False: 
			self.x_type = self.x_payment_method.saledoc
			print self.x_type



























	validity_date = fields.Char(
			string="Fecha de expiración"
		)































	# Open Treatment
	@api.multi 
	def open_treatment(self):

		#print 
		#print 'Open Treatment'

		if self.treatment.name != False:
			ret = self.treatment.open_myself()
		elif self.cosmetology.name != False:
			ret = self.cosmetology.open_myself()
		else:
			#print 'This should not happen !'
			ret = 0 

		return ret 
	# open_treatment




	# Open Cosmetology
	#@api.multi 
	#def open_cosmetology(self):
		#print 
		#print 'Open cosmetology'
	#	ret = self.cosmetology.open_myself()
	#	return ret 
	# open_cosmetology










	# Open Myself
	@api.multi 
	def open_myself(self):

		#print 
		#print 'Open Myself'

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












	# Family 
	x_family = fields.Selection(

			#string = "Tipo", 	
			string = "Familia", 	


			#default='product',
			#default='consultation',

			
			#selection = jxvars._family_list, 
			selection = treatment_vars._family_list, 


			#required=True, 
			required=False, 
		)













# ----------------------------------------------------------- Reset ------------------------------------------------------
	@api.multi 
	def x_reset(self):
		self.x_payment_method.unlink()
		self.state = 'draft'			# This works. 
		self.x_confirmed = False
	





# ----------------------------------------------------------- Relational ------------------------------------------------------

	# Appointment 
	x_appointment = fields.Many2one(
			'oeh.medical.appointment',
			
			string='Cita', 

			#required=True, 
			required=False, 

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
																	('doctor', '=', record.x_doctor.name), 
																	#('x_target', '=', record.x_target),	
																],
																	order='appointment_date desc',
																	limit=1,
																)

			#elif record.x_family == 'consultation':			
			elif record.x_family == 'consultation'	or  record.x_family == 'product':			

				app = self.env['oeh.medical.appointment'].search([
																	('patient', '=', record.patient.name), 
																	('x_type', '=', 'consultation'),
																	('doctor', '=', record.x_doctor.name), 
																	#('x_target', '=', record.x_target),	
																],
																	order='appointment_date desc',
																	limit=1,
																)
			
			else:
				app = False



			#if record.x_appointment != False:
			#if record.x_appointment.name != False:
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
			#string = "x Amount Total",
			string = "x Total",
			compute="_compute_x_amount_total",
		)


	@api.multi
	#@api.depends('x_payment_method')

	def _compute_x_amount_total(self):
		for record in self:
			sub = 0.0

			for line in record.order_line:
				sub = sub + line.price_subtotal 

			if sub == 0.0:
				sub = float(record.x_ruc)

			record.x_amount_total = sub







	x_partner_vip = fields.Boolean(
			'Vip', 
			default=False, 

			compute="_compute_partner_vip",
			)

	@api.multi

	def _compute_partner_vip(self):
		for record in self:
			
			#print 
			#print 'jx'
			#print 'Compute Partner Vip'


			#rec_set = self.env['sale.order'].search([
			#												('partner_id','=', record.partner_id.id),
			#												('state','=', 'sale'),
			#											]) 			
			#for rec in rec_set:
			#	for line in rec.order_line:
			#		if line.name == 'Tarjeta VIP':
			#			record.x_partner_vip = True 



			count = self.env['openhealth.card'].search_count([
																('patient_name','=', record.partner_id.name),
														]) 

			#print count 


			if count == 0:
				record.x_partner_vip = False 

			else:	
				record.x_partner_vip = True 


			#print 
			#print 
			#print 






# ---------------------------------------------- Cancel --------------------------------------------------------

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
	# create_event





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

		#print 
		#print 'Create Payment Method'



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



#jz
		# State - Change
		#print 'State changes'

		

		#self.state = 'sale'
		#self.state = 'payment'
		self.state = 'sent'

		

		#print self.state
		#print 




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








# ---------------------------------------------- Create Sale Document --------------------------------------------------------

	@api.multi 
	def create_sale_document(self):
		#print 
		#print 'Create Sale Document'

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
		#print 'State changes'
		self.state = 'proof'
		#print self.state
		#print 




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




















	x_payment_method_code = fields.Char(

			string="Código", 
						
			#required=True, 
			required=False, 
		)






	x_ruc = fields.Char(

			string="RUC", 
						
			#required=True, 
			required=False, 
		)























	x_appointment_date = fields.Datetime(
			string="Fecha", 
			#readonly=True,

			compute='_compute_x_appointment_date', 
			
			#required=True, 
			required=False, 
			)


	x_duration = fields.Float(
			string="Duración (h)", 
			#readonly=True, 

			compute='_compute_x_duration', 
			
			#required=True, 		
			required=False, 
			)










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


















	vspace = fields.Char(
			' ', 
			readonly=True
		)
	








	# Nr treatments 
	nr_treatments = fields.Integer(
			default=0,

			compute='_compute_nr_treatments', 
		)

	@api.multi
	#@api.depends('order_line')
	
	def _compute_nr_treatments(self):
		for record in self:

			nr = record.env['openhealth.treatment'].search_count([
																		('physician', '=', record.x_doctor.name ), 
																	])

			record.nr_treatments = nr






	# Nr cosmetologies 
	nr_cosmetologies = fields.Integer(
			default=0,

			compute='_compute_nr_cosmetologies', 
		)


	@api.multi
	#@api.depends('order_line')
	
	def _compute_nr_cosmetologies(self):
		for record in self:

			nr = record.env['openhealth.cosmetology'].search_count([
																		('physician', '=', record.x_doctor.name ), 
																	])

			record.nr_cosmetologies = nr





# ----------------------------------------------------------- Relationals ------------------------------------------------------

	cosmetology = fields.Many2one(
			'openhealth.cosmetology',
			ondelete='cascade', 			
			string="Cosmiatría", 
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
			#record.name = 'SE00' + str(record.id) 
			#record.nr_lines = 0
			
			ctr = 0
			for l in record.order_line:
				ctr = ctr + 1
			record.nr_lines = ctr 
			
	
	
	
	
	





























# ----------------------------------------------------------- Update Order ------------------------------------------------------

	# Update colors (state)
	@api.multi 
	def update_order_nex(self):


		#print 
		print 
		print 'Update Order Nex'
		print 





# ----------------------------------------------------------- Update Descriptors All ------------------------------------------------------

	# Action confirm 
	@api.multi 
	def update_descriptors_all(self):


		#print 
		print 
		print 'Update descriptors All'
		print 

		orders = self.env['sale.order'].search([
													('state', '=', 'sale'),
													#('date_order', '>=', date_begin),
													#('date_order', '<', date_end),
													#('x_type', '=', x_type),
											],
												#order='x_serial_nr asc',
												order='date_order desc',
												limit=2000,
											)
		print orders 


		for order in orders: 
			order.update_descriptors()







# ----------------------------------------------------------- Update Descriptors ------------------------------------------------------

	# Action confirm 
	@api.multi 
	def update_descriptors(self):


		#print 
		#print 
		#print 'Update descriptors'


		out = False
		for line in self.order_line:

			#print 'Family'

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



		#print self.x_family
		#print self.x_product






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







# ----------------------------------------------------------- Action Confirm ------------------------------------------------------

	# Action confirm 
	@api.multi 
	def action_confirm(self):


		#print 
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





		# Doctor User Name - For Reporting 
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
		if self.x_family == 'consultation'	or 	self.x_family == 'procedure': 
			if self.x_appointment.name != False: 
				self.x_appointment.state = 'invoiced'





		# Reserve Machine if Procedure 
		#if self.x_family == 'procedure': 
		#	self.reserve_machine()




		# Create Proc 
		#self.treatment.create_procedure()






		# Patient 
		patient_name = self.partner_id.name
		#print patient_name





		# Card 
		go_card = False 
		order_line = self.order_line
		for line in order_line:
			print line 
			print line.name 
			#if line.name == 'Tarjeta VIP' or line.name == 'TARJETA VIP':
			if line.product_id.x_name_short == 'vip_card':
				#print 'gotcha'
				go_card = True
				print go_card


		# Create Card 
		if go_card:

			print 'Card'


			# Pricelist Vip - For Partner
			pl = self.env['product.pricelist'].search([
																('name','=', 'VIP'),
															],
															#order='appointment_date desc',
															limit=1,)
			print pl
			self.partner_id.property_product_pricelist = pl





			# Search Card
			card = self.env['openhealth.card'].search([ ('patient_name', '=', patient_name), ], order='date_created desc', limit=1)
			card_id = card.id
			print card 

			# Create Card 
			if card.name == False: 
				card = self.env['openhealth.card'].create({
																	'patient_name': self.partner_id.name,
															})
				#print 'jx'
				#print 'Create VIP Card'
				#print card
				#print card.name
				#print self.partner_id.name				
				#print

			#return{}





		# Stock Picking - Validate 
		#print 'Picking'
		#self.validate_stock_picking()
		#self.do_transfer()
		
	# action_confirm	




