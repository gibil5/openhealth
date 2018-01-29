# -*- coding: utf-8 -*-
#
#
# 	Order 
# 
# Created: 				26 Aug 2016
# Last updated: 	 	29 Sep 2017


from openerp import models, fields, api
import datetime
from . import app_vars
from . import ord_vars
from . import appfuncs
from . import cosvars
from . import treatment_vars
from num2words import num2words


class sale_order(models.Model):
	
	_inherit='sale.order'

	#_name = 'openhealth.order'
	





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
	 		print res_id

 			res.default_code = ''
 			res.product_id = False
 			res.product_uom_qty = 1 
	 		
	 		res.x_type = x_type
	 		
	 		#res.reset()
 			
	 		





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

	# Order Line 
	order_line = fields.One2many(
			'sale.order.line', 
			'order_id', 
			string='Order Lines', 

			readonly=False, 

			#states={
			#			'cancel': 	[('readonly', True)], 
			#			'done': 	[('readonly', True)], 
			#			'sent': 	[('readonly', True)], 
			#			'sale': 	[('readonly', True)], 
			#		}, 
			
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
			
			partner_id = self.env['res.partner'].search([
														#('patient', '=', self.patient.name),			
														('x_dni', '=', self.x_partner_dni),					
												],
													order='write_date desc',
													limit=1,
												)

			print partner_id
			print partner_id.id

			#self.partner_id = partner_id
			self.partner_id = partner_id.id




# ----------------------------------------------------------- Date corrected ------------------------------------------------------

	#date_order = fields.Datetime(string='Order Date', required=True, readonly=True, index=True, states={'draft': [('readonly', False)], 'sent': [('readonly', False)]}, copy=False, default=fields.Datetime.now)


	x_date_order_corr = fields.Datetime(
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



			DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"

			#date_field1 = datetime.strptime(date_field1, DATETIME_FORMAT)
			#date_field2 = datetime.strptime(date_field2, DATETIME_FORMAT)
			#date_field2 = date_field1 + timedelta(hours=5,minutes=30)

			date_field1 = datetime.datetime.strptime(record.date_order, DATETIME_FORMAT)

			#date_field2 = datetime.strptime(date_field2, DATETIME_FORMAT)

			#date_field2 = date_field1 + datetime.timedelta(hours=5,minutes=0)
			date_field2 = date_field1 + datetime.timedelta(hours=-5,minutes=0)


			record.x_date_order_corr = date_field2







# ----------------------------------------------------------- Serial Number ------------------------------------------------------

	# Serial Number 
	x_serial_nr = fields.Char(

			'Número de serie', 

			compute="_compute_x_serial_nr",
		)



	@api.multi
	#@api.depends('partner_id')

	def _compute_x_serial_nr(self):
		for record in self:

			if record.x_payment_method != False: 

				serial_nr = record.x_payment_method.saledoc_code 

				record.x_serial_nr = serial_nr
















	# Patient 
	patient = fields.Many2one(
			'oeh.medical.patient',
			string='Paciente', 


			#compute='_compute_patient', 
		)


	@api.multi
	def _compute_patient(self):

		for record in self:

			patient = self.env['oeh.medical.patient'].search([
																('name', '=', self.partner_id.name), 
														],
														#order='appointment_date desc',
														limit=1,
													)
			
			if patient.name != False:
				record.patient = patient












# ----------------------------------------------------------- Test and Hunt ------------------------------------------------------
	# Test Bug 
	@api.multi 
	def test_bug(self):

		print 'jx'
		print 'Test and Hunt !'

		target_line = 'quick_body_local_cyst_2'
		
		print target_line

		ret = self.x_create_order_lines_target(target_line)
		
		print ret  







# ----------------------------------------------------------- Create order lines ------------------------------------------------------
	#@api.multi 
	#def x_create_order_lines_target(self, target):		
	def x_create_order_lines_target(self, target, price_manual):		

		
		print 
		print 'jx'
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
		print product.id
		print product.name
		print product.x_name_short



		#product_id = product.id
		#price_unit = product.list_price
		#x_price_vip = product.x_price_vip
		#product_uom = product.uom_id.id
		#print product
		#print product.id
		#print product.uom_id.id
		#print 



#jxx
		ol = self.order_line.create({
										'product_id': product.id,
										'order_id': order_id,										

										'x_price_manual': price_manual, 



										#'name': target,
										#'name': product.name,
										#'state':'draft',
										#'price_unit': price_unit,
										#'x_price_vip': x_price_vip,
										#'product_uom': product_uom, 
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
			readonly=True, 
			states={'draft': [('readonly', False)], 'sent': [('readonly', False)]}, 
			help="Pricelist for current sales order.", 
		)















	@api.multi
	def _get_default_doctor(self): 


		#name = 'Dr. Chavarri'
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

			default = _get_default_doctor, 


			states={
						'draft': 	[('readonly', False)], 
						'sent': 	[('readonly', True)], 
						'sale': 	[('readonly', True)], 
						'cancel': 	[('readonly', True)], 
						'done': 	[('readonly', True)], 
					}, 

		)




	x_doctor_uid = fields.Many2one(
			'res.users',
			string = "Médico Uid", 	

			readonly = True, 
			#compute='_compute_x_doctor_uid', 
		)




	#@api.onchange('x_doctor')
	#def _onchange_x_doctor(self):
	#		if self.x_doctor.name != False: 
	#			uid = self.x_doctor.x_user_name.id
	#			self.x_doctor_uid = uid






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















	# Total Net
	x_total_net = fields.Float(

			"Neto",
			compute='_compute_x_total_net', 
		)

	@api.multi
	#@api.depends('')
	def _compute_x_total_net(self):
		for record in self:

			record.x_total_net = record.amount_total * 0.82





	# Total Tax
	x_total_tax = fields.Float(

			"Impuesto",
			compute='_compute_x_total_tax', 
		)

	@api.multi
	#@api.depends('')
	def _compute_x_total_tax(self):
		for record in self:

			record.x_total_tax = record.amount_total * 0.18










	# Total in Words
	x_total_in_words = fields.Char(

			"",
			compute='_compute_x_total_in_words', 
		)

	@api.multi
	#@api.depends('')
	def _compute_x_total_in_words(self):
		for record in self:

			#words = record.total
			words = num2words(record.amount_total, lang='es')

			record.x_total_in_words = words.title() + ' Soles'






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
			
				#print 'jx'
				#print com 
				#print 
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

			compute="_compute_x_type",
		)

	@api.multi
	#@api.depends('partner_id')

	def _compute_x_type(self):
		for record in self:

			if record.x_payment_method != False: 
				record.x_type = record.x_payment_method.saledoc


















	# Type (product or service)
	#x_cancel_reason = fields.Char(
	x_cancel_reason = fields.Selection(
			selection=ord_vars._owner_type_list, 
			#string='Motivo de anulación', 
			string='Tipo', 
		)


	# Product Odoo 
	x_cancel_owner = fields.Char(
			#string='Quién anula', 
			string='Producto', 
		)



	# Categ
	categ = fields.Char(

			'Categoria', 

			compute="_compute_categ",
		)

	@api.multi
	#@api.depends('partner_id')

	def _compute_categ(self):
		for record in self:

			for line in record.order_line:

				#record.categ = line.product_id.name
				record.categ = line.product_id.categ_id.name



	# Product
	product = fields.Char(

			'Producto', 

			compute="_compute_product",
		)

	@api.multi
	#@api.depends('partner_id')

	def _compute_product(self):
		for record in self:

			for line in record.order_line:

				record.product = line.product_id.name







	# Comment 
	comment = fields.Selection(
		[
		('product', 'Product'),
		('service', 'Service'),
		], 
		string='Comment', 
		default='product', 
		readonly=True
	)






	# Deprecated ? 
	#margin = fields.Float(
	#		string="Margen"
	#	)

	validity_date = fields.Char(
			string="Fecha de expiración"
		)




#jz
	# State 
	state = fields.Selection(

			
			#selection = ord_vars._x_state_list, 
			selection = ord_vars._state_list, 
			


			string='Estado',	
			readonly=False,
			default='draft',

			#copy=False, 
			#index=True, 
			#track_visibility='onchange', 
			#compute="_compute_state",
			)








	# Consultation - DEPRECATED ? 
	consultation = fields.Many2one(
			'openhealth.consultation',
			string="Consulta",
			ondelete='cascade', 
		)



	# Ooor 
	x_age = fields.Integer(string='Age', default=52, help='Age of student')

	x_group = fields.Char(string='Group', compute='_compute_x_group', help='Group of student', store=True)

	@api.depends('x_age')
	def _compute_x_group(self):
	
		#self.x_group = 'NA'
		#if self.x_age > 5 and self.x_age <= 10:
		#	self.x_group = 'A'
		#elif self.x_age > 10 and self.x_age <= 12:
		#	self.x_group = 'B'
		#elif self.x_age > 12:
		#	self.x_group = 'C'

		for record in self:
			record.x_group = 'NA'
			if record.x_age > 5 and record.x_age <= 10:
				record.x_group = 'A'
			elif record.x_age > 10 and record.x_age <= 12:
				record.x_group = 'B'
			elif record.x_age > 12:
				record.x_group = 'C'




	# Year
	x_year = fields.Char(
			compute="_compute_x_year",

			string='Year', 

			#store=True, 

			default=False, 
		)

	#@api.multi
	@api.one
	@api.depends('date_order')
	def _compute_x_year(self):
		#print 
		#print 'Compute X Year'

		#date = datetime.datetime.strptime(self.date_order, date_format)
		#self.x_year = date.year
		#print self.x_year
		#print 
		#self.fats = self.name.fats

		for record in self:
			date_format = "%Y-%m-%d %H:%M:%S"
			date = datetime.datetime.strptime(record.date_order, date_format)
			record.x_year = date.year




	# Month 
	x_month = fields.Char(
			string='Month', 
			
			#store=True, 
			required=False, 

			compute="_compute_x_month",
		)

	#@api.multi
	@api.depends('date_order')
	def _compute_x_month(self):
		for record in self:
			#record.x_month = 'jz'

			date_format = "%Y-%m-%d %H:%M:%S"
			date = datetime.datetime.strptime(record.date_order, date_format)
			record.x_month = date.month






	note = fields.Text(
			"Nota",					
		)



	# Doctor name  
	x_doctor_name = fields.Char(
		)
	doctor_name = fields.Char(
								default = 'generic doctor',
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






	# Print Order
	#@api.multi 
	#def print_order(self):
		#print 
		#print 'Print Order'
		#ret = self.treatment.open_myself()
		#return ret 
	# open_treatment














	# Open Treatment
	@api.multi 
	def open_treatment(self):


		#print 
		#print 'Open Treatment'
		#ret = self.treatment.open_myself()



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










	# Partner 
	partner_id = fields.Many2one(
			'res.partner',
			string = "Cliente", 	

			ondelete='cascade', 			

			required=True, 
		)



	# Family 
	x_family = fields.Selection(

			#string = "Tipo", 	
			string = "Familia", 	

			default='product',
			
			#selection = jxvars._family_list, 
			selection = treatment_vars._family_list, 


			#required=True, 
			required=False, 
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
	#	#print 'Compute Pm Complete'
	#	for record in self:
	#		if record.pm_total == record.x_amount_total: 
	#			#print 'Equal !'
	#			record.pm_complete = True
				#record.state = 'payment'
	#		else:
	#			#print 'Not Equal'
	#		#print record.pm_total
	#		#print record.x_amount_total
	#		#print record.pm_complete
	#		#print record.state





	# Payment Complete
	x_payment_complete = fields.Boolean(
								#default = False, 
								#readonly=False,
								#string="Pm Complete",
	)





	@api.multi 
	def x_reset(self):

		#print 
		#print 'jx'
		#print 'Reset'



		#self.procedure_ids.unlink()
		self.x_payment_method.unlink()
	


		#self.x_sale_document_type = False
		#self.x_sale_document.unlink()




		#self.x_appointment.unlink()
		#self.x_appointment = False
		#self.x_appointment.x_machine = False
#jz
		if self.x_appointment.x_machine != False:
			self.x_appointment.x_machine = False




		#self.pre_state = 'draft'
		self.state = 'draft'			# This works. 
		self.x_confirmed = False

		#print 
		#print 
		#print 

	# x_reset







	x_confirmed = fields.Boolean(
			default=False, 
		)




	# Total of Payments
	pm_total = fields.Float(
								#string="Total",
								#compute="_compute_pm_total",
	)
	
	@api.multi
	#@api.depends('x_payment_method')

	def _compute_pm_total(self):
		for record in self:
			total = 0.0
			for pm in record.x_payment_method:
				total = total + pm.subtotal
			record.pm_total = total
			record.x_payment_complete = True
	# _compute_pm_total





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

	@api.multi
	#@api.depends('x_product')

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
			required=False, 
			


			domain = [
						#('x_treatment', '=', 'laser_co2'),						
						('x_origin', '=', False),						
					],



			compute='_compute_x_product', 
		)



	#@api.multi
	@api.depends('order_line')

	def _compute_x_product(self):
		for record in self:

			flag = False



			for line in record.order_line:

				tre = line.product_id.x_treatment



				#if line.product_id.x_treatment == 'laser_co2':
				#if 	line.product_id.x_treatment == 'laser_co2'	or 	line.product_id.x_treatment == 'laser_excilite':
				#if tre == 'laser_co2' 		or 		tre == 'laser_excilite': 
				#if tre == 'laser_co2' 		or 	tre == 'laser_excilite'		or 	tre == 'laser_ipl'		or tre == 'laser_ndyag'	: 

				#if tre == 'laser_co2' 	or 	tre == 'laser_excilite'	or 	tre == 'laser_ipl'	or tre == 'laser_ndyag'		or tre == 'consultation': 
				if  	tre == 'laser_quick'  	or 		tre == 'laser_co2' 	or 	tre == 'laser_excilite'	or 	tre == 'laser_ipl'	or tre == 'laser_ndyag'		or tre == 'consultation': 

					product = line.product_id.id
					flag = True 




			if flag: 
				record.x_product = product







	# Treatment
	x_treatment = fields.Char(
			#string="Tratamiento",
			
			#required=True, 
			required=False, 
			
			compute='_compute_x_treatment', 
			)

	#@api.multi
	@api.depends('x_product')
	def _compute_x_treatment(self):
		for record in self:
			record.x_treatment = record.x_product.x_treatment
	# _compute_x_treatment







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



	@api.multi 
	def cancel_order(self):

		#print 
		#print 'Cancel'
		self.x_cancel = True



		self.state = 'cancel'



		ret = self.create_event()
		#ret = order_funcs.create_event(self)

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



		# Init vars 
		#nr_pm = self.env['openhealth.payment_method'].search_count([('order','=', self.id),]) 
		#name = 'Pago ' + str(nr_pm + 1)
		#total = self.x_amount_total

		name = 'Pago'
		method = 'cash'
		balance = self.x_amount_total - self.pm_total

		


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
																			
																				'pm_total': self.pm_total,
																			
																				'total': self.x_amount_total,

																				'balance': balance, 

																				'partner': self.partner_id.id, 

																				'date_created': self.date_order,

																				#'saledoc': 'receipt', 



																				'dni': dni,
																				'firm': firm,
																				'ruc': ruc,
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
							'default_pm_total': self.pm_total,
							'default_partner': self.partner_id.id,
							'default_date_created': self.date_order,
							#'default_saledoc': 'receipt', 


							'default_dni': dni,
							'default_firm': firm,
							'default_ruc': ruc,
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
			required=False, 
		)






	x_ruc = fields.Char(

			string="RUC", 
						
			#required=True, 
			required=False, 
		)


















	# Machine 
	x_machine = fields.Selection(
			#string="Máquina", 
			string="Sala", 
			#selection = jxvars._machines_list, 
			selection = app_vars._machines_list, 
			
			compute='_compute_x_machine', 
		
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




	closing = fields.Many2one(
			'openhealth.closing',
			ondelete='cascade', 
			string="Cierre", 
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
			required=False, 
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















# ----------------------------------------------------------- Button - Update Lines ------------------------------------------------------
	@api.multi 
	def update_line(self, order_id, product_id, name, list_price, uom_id, x_price_vip):
		order = self.env['sale.order'].search([
															('id', '=', order_id),
															#('name', 'like', name),
													])
		line = order.order_line.create({
											'order_id': order.id,
											'product_id': product_id,
											'name': name,
											'product_uom': uom_id, 
											'x_price_vip': x_price_vip, 
											'x_partner_vip': self.x_partner_vip
										})
		return line
	# update_line





# ----------------------------------------------------------- Button - Update Order ------------------------------------------------------
	@api.multi 
	def update_order(self):

		# Order 
		order_id = self.id

		# Appointment 
		appointment = self.env['oeh.medical.appointment'].search([ 	
																	('patient', 'like', self.patient.name),	
																	('doctor', 'like', self.x_doctor.name), 	
																	('x_type', 'like', 'procedure'), 
																], 
																	order='appointment_date desc', limit=1)
		appointment_id = appointment.id
		self.x_appointment = appointment_id




		# Lines 
		ret = self.order_line.unlink()

		# Cosmetology 
		for service in self.cosmetology.service_ids:
			#print service

			line = self.update_line(	
										order_id, 
										service.service.id, 
										service.service.x_name_short, 
										service.service.list_price, 
										service.service.uom_id.id,
										service.service.x_price_vip
									)
			#print 



		# Doctor 
		#for service in self.consultation.service_co2_ids:
		for service in self.treatment.service_co2_ids:
			#print service

			line = self.update_line(	
										order_id, 
										service.service.id, 
										service.service.x_name_short, 
										service.service.list_price, 
										service.service.uom_id.id,

										service.service.x_price_vip
									)
			#print 
		
		for service in self.consultation.service_excilite_ids:
			#print service
			line = self.update_line(	
										order_id, 
										service.service.id, 
										service.service.x_name_short, 
										service.service.list_price, 										
										service.service.uom_id.id,

										service.service.x_price_vip
									)

		for service in self.consultation.service_ipl_ids:
			#print service
			line = self.update_line(	order_id, 
										service.service.id, 
										service.service.x_name_short, 
										service.service.list_price, 
										service.service.uom_id.id,

										service.service.x_price_vip
									)

		for service in self.consultation.service_ndyag_ids:
			#print service
			line = self.update_line(	order_id, 
										service.service.id, 
										service.service.x_name_short, 
										service.service.list_price, 
										service.service.uom_id.id,

										service.service.x_price_vip
									)

		for service in self.consultation.service_medical_ids:
			#print service
			line = self.update_line(	order_id, 
										service.service.id, 
										service.service.x_name_short, 
										service.service.list_price, 
										service.service.uom_id.id,

										service.service.x_price_vip
									)

		#print 

	# update_order 




	@api.multi 
	def update_order_lines_app(self):

		#print 
		#print 'jx'
		#print 'Update Order Lines'


		for line in self.order_line:

			#print line


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

				
				#print self.x_doctor
				#print self.patient

				
				#print appointment  
				#print appointment_id  



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
		#print 
	# update_order_lines_app	









# ----------------------------------------------------------- Buttons - Order  ------------------------------------------------------

	@api.multi
	def remove_myself(self):  
		#print 
		#print 
		#print 'Remove Myself'
		#print self.name 
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
		

		#print 
		#print 
	# remove_myself






# ----------------------------------------------------------- Nr Mac Clones  ------------------------------------------------------

	@api.multi 
	def get_nr_mc(self):
		nr_mac_clones =	self.env['oeh.medical.appointment'].search_count([
																			('appointment_date','=', self.x_appointment.appointment_date),													
																			('x_machine','=', self.x_appointment.x_machine),
																		]) 
		return nr_mac_clones








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









# ----------------------------------------------------------- Actions ------------------------------------------------------

	# Reserve machine 
	@api.multi 
	def reserve_machine(self):

		print 'jx'
		print 'Reserve Machine'
		print 



		# There is an appointment 
		if self.x_appointment.name == False: 
			print 'There is no Appointment'


		else: 
			date_format = "%Y-%m-%d %H:%M:%S"
			duration = self.x_appointment.duration 
			delta = datetime.timedelta(hours=duration)


			# Easiest first 
			m_dic = {

						'laser_quick': 			['laser_quick'], 

						'laser_co2_1': 			['laser_co2_1', 'laser_co2_2', 'laser_co2_3'], 
						'laser_excilite': 		['laser_excilite'], 
						'laser_m22': 			['laser_m22'], 
						'laser_triactive': 		['laser_triactive'], 
						'chamber_reduction': 	['chamber_reduction'], 
						'carboxy_diamond': 		['carboxy_diamond'], 

						'consultation':			[], 
				}



			print 'x machine req'
			print self.x_machine_req


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

						if nr_mc == 1:		# Success - Get out 
							out = True 

				if not out: 	# Error - Change the date 
					ad = datetime.datetime.strptime(self.x_appointment.appointment_date, date_format) 
					ad_dt = delta + ad
					ad_str = ad_dt.strftime("%Y-%m-%d %H:%M:%S")

					k = k + 1.
		

	# reserve_machine








# ----------------------------------------------------------- Validate Stock Picking ------------------------------------------------------


	@api.multi 
	def do_transfer(self):

		#print 
		print 'jx'
		print 'Do Transfer'

		print self.picking_ids

		for pick in self.picking_ids: 

			#ret = pick.do_new_transfer()
			ret = pick.do_transfer()

			print ret






	# Action confirm 
	@api.multi 
	def validate_stock_picking(self):

		#print 
		print 'jx'
		print 'Validate Stock Picking'


		print self.picking_ids


		for pick in self.picking_ids: 
		
			print pick

			print pick.name 

			ret = pick.force_assign()
			print ret







# ----------------------------------------------------------- Action Confirm ------------------------------------------------------

	# Action confirm 
	@api.multi 
	def action_confirm(self):


		#print 
		print 'jx'
		print 'Action confirm - Overridden'
		 
		



		#Write your logic here - Begin

		# Doctor User Name - For Reporting 
		if self.x_doctor.name != False: 
			uid = self.x_doctor.x_user_name.id
			self.x_doctor_uid = uid



		# Change State - To Invoiced 
		if self.x_family == 'consultation'	or 	self.x_family == 'procedure': 
			if self.x_appointment.name != False: 
				#self.x_appointment.state = 'Scheduled'
				self.x_appointment.state = 'invoiced'



		# Reserve machine 
		if self.x_family == 'procedure': 
			self.reserve_machine()

		#Write your logic here - End 





		# The actual procedure 
		res = super(sale_order, self).action_confirm()
		#Write your logic here
		






		patient_name = self.partner_id.name
		#print patient_name




		# Create Card ? 
		go_card = False 


		order_line = self.order_line
		for line in order_line:

			print line 
			print line.name 


			#if line.name == 'Tarjeta VIP' or line.name == 'TARJETA VIP':
			if line.product_id.x_name_short == 'vip_card':

				print 'gotcha'
				
				go_card = True

				print go_card




		# Create Card 
		if go_card:

			print 'Search VIP Card'


			# Partner pricelist - Vip
			pl = self.env['product.pricelist'].search([
																('name','=', 'VIP'),
															],
															#order='appointment_date desc',
															limit=1,)

			print pl

			self.partner_id.property_product_pricelist = pl




			# Card Search 
			card = self.env['openhealth.card'].search([ ('patient_name', '=', patient_name), ], order='date_created desc', limit=1)
			card_id = card.id
			print card 



			# Card Create 
			if card.name == False: 

				print 'jx'
				print 'Create VIP Card'



				# Card name 
				counter = self.env['openhealth.counter'].search([('name', '=', 'vip')])



				#name = str(counter.value).rjust(8, '0')
				name = counter.total

				counter.increase()

				card = self.env['openhealth.card'].create({
																	'name': name,
																	'patient_name': self.partner_id.name,
															})

				print card
				print name 
				print self.partner_id.name				
				print

			#return{}





		# Validate Stock Picking 
		self.validate_stock_picking()
		self.do_transfer()
	# action_confirm	











	# Print Ticket 
	@api.multi
	def print_ticket(self):

		if self.x_type == 'ticket_receipt': 
			return self.env['report'].get_action(self, 'openhealth.report_ticket_receipt_view')

		elif self.x_type == 'ticket_invoice': 
			return self.env['report'].get_action(self, 'openhealth.report_ticket_invoice_view')

	# print_ticket	









# ----------------------------------------------------------- CRUD ------------------------------------------------------


	@api.multi
	def unlink(self):

		#print 
		#print 'Order - Unlink - Override'
		#print 
		
		for invoice in self:

			if invoice.state not in ('draft', 'cancel'):
				#print 'jx - Warning'				
				#raise Warning(('You cannot delete an invoice which is not draft or cancelled. You should refund it instead. - jx'))
				tra = 1 
				
		return models.Model.unlink(self)






# Write - Deprecated ?
	@api.multi
	def write(self,vals):

		print 'jx'
		print 'CRUD - Order - Write'
		#print 
		#print vals
		#print 
		#print 

		#if vals['x_doctor'] != False: 
		#	print vals['x_doctor']
		#if vals['user_id'] != False: 
		#	print vals['user_id']






		#Write your logic here
		res = super(sale_order, self).write(vals)
		#Write your logic here
		#print 
		#print 


		#if self.x_doctor.name != False: 
		#	uid = self.x_doctor.x_user_name.id	
		#	self.x_doctor_uid = uid


		return res

	# CRUD 


#sale_order()