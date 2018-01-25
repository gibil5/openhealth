# -*- coding: utf-8 -*-
#
#
# 		*** OPEN HEALTH - Patient 
# 
# Created: 				26 Aug 2016
# Last updated: 	 	25 Aug 2017

from openerp import models, fields, api
from datetime import datetime
from . import pat_funcs
from . import pat_vars


class Patient(models.Model):

	_inherit = 'oeh.medical.patient'

	_order = 'write_date desc'







# ----------------------------------------------------------- Not Deprecated ------------------------------------------------------
	

	# Stree2 Char - If Province 
	street2_char = fields.Char(
			string = "Distrito Prov.", 	
			required=False, 
		)


	# Street2 ?
	@api.onchange('street2_char')
	def _onchange_street2_char(self):
		self.street2 = self.street2_char






# ----------------------------------------------------------- On changes ------------------------------------------------------

	# Zip  Street2
	@api.onchange('street2_sel')
	def _onchange_street2_sel(self):
		self.street2 = pat_vars.zip_dic_inv[self.street2_sel]
		self.zip = self.street2_sel




	# Street 
	@api.onchange('street')
	def _onchange_street(self):
		if self.street != False: 
			self.street = self.street.strip().title()



	# Email 
	@api.onchange('email')
	def _onchange_email(self):
		if self.email != False: 
			self.email = self.email.strip().lower()






# ----------------------------------------------------------- Hard wired ------------------------------------------------------



	# READY 

	# Email 
	#email = fields.Char(
	#		string = 'Email',  
	#		placeholder = '',
	#		required=True, 
			#required=False, 
	#	)


	#x_dni = fields.Char(
	#		string = "DNI", 	
			#required=True, 
			#required=False, 
	#	)





	# IN PROG 

	#country_id = fields.Many2one(
	#		'res.country', 
	#		string = 'País', 

	#		default = 175,	# Peru

			#required=False, 
	#		required=True, 
	#	)



	#city = fields.Selection(
	#		selection = pat_vars._city_list, 
	#		string = 'Departamento',  
	#		default = 'lima', 

	#		required=True, 
			#required=False, 
	#	)



	#street2 = fields.Char(
	#		string = "Distrito", 	
			
			#required=True, 
	#		required=False, 
	#	)



	#street2_sel = fields.Selection(
	#		selection = pat_vars._street2_list, 
	#		string = "Distrito", 	
			
			#required=True, 
	#		required=False, 
	#	)






	#street = fields.Char(
	#		string = "Dirección", 	

	#		required=False, 
	#	)






	#zip = fields.Integer(
	#		string = 'Código',  
			#compute='_compute_zip', 

			#required=True, 			
	#		required=False, 			
	#	)


	# Deprecated 
	#@api.multi
	#def _compute_zip(self):
	#	for record in self:
	#		if (record.street2 in pat_vars.zip_dic) and (record.city == 'lima')  :
	#			record.zip=pat_vars.zip_dic[record.street2]
	#		else:
	#			record.zip=0






# ----------------------------------------------------------- Order Report ------------------------------------------------------

	# Estado de cuenta
	x_order_report = fields.Many2one(			
			'openhealth.order.report',		
			string="Estado de cuenta",		
		)



	# Generate 
	@api.multi 
	def generate_order_report(self):
		print 'jx'
		print 'Generate'

		self.remove_order_report()
		
		res_id = self.create_order_report()

		self.update_order_report()




		return {
				'type': 'ir.actions.act_window',
				
				'name': ' New Order Report', 

				'view_type': 'form',

				'view_mode': 'form',	
				
				'target': 'current',

				'res_model': 'openhealth.order.report',				
				
				'res_id': res_id,

				'flags': 	{
								#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
								'form': {'action_buttons': True, }
							},

				'context': {
								#'default_order': self.id,
								#'default_name': name,
								#'default_x_type': x_type,
							}
				}
	# create_event









	# Remove 
	@api.multi 
	def remove_order_report(self):
		print 'jx'
		print 'Remove'

		self.x_order_report = False




	# Create 
	@api.multi 
	def create_order_report(self):
		print 'jx'
		print 'Create'


		#if self.x_order_report != False: 
		#	self.x_order_line_ids.unlink()

		#else: 

		#name = 'Estado de cuenta'
		name = 'EC - ' + self.partner_id.name


		#self.x_order_report = self.env['sale.order'].create(
		order_report_id = self.env['openhealth.order.report'].create(
														{
															'name': name, 

															'partner_id': self.partner_id.id,
																													
															'state':'sale',

															#'subtotal':0,
															#'pricelist_id': self.property_product_pricelist.id,	
															#'patient': self.id,	
															#'x_doctor': self.physician.id,	
															#'treatment': self.id,
															#'x_family': target, 
															#'note': note, 
														}
													).id


		self.x_order_report = order_report_id
		

		return order_report_id






	# Update 
	@api.multi 
	def update_order_report(self):
		print 'jx'
		print 'Update'



		partner_id = self.partner_id.name

		orders = self.env['sale.order'].search([
															('partner_id', '=', partner_id),			
													],
													#order='start_date desc',
													#limit=1,
												)
		#print orders


		for order in orders: 
			#print 
			#print order.name 
			for line in order.order_line: 

				#print line.product_id
				#print line.name
				#print line.price_subtotal
				#print line.create_date



				#ret = self.x_order_report.order_line.create({

				ret = self.x_order_line_ids.create({
															
															'product_id': line.product_id.id,

															'name': line.name,
															
															'price_subtotal': line.price_subtotal,


															'x_date_created': line.create_date,


															#'order_id': self.x_order_report.id,
															'order_report_id': self.x_order_report.id,
													})










	# Estado de cuenta - Lines 
	x_order_line_ids = fields.One2many(

			'sale.order.line',			 
			#'openhealth.order.line.report',			 

			'patient_id', 
		
			string="Estado de cuenta",
		)






	@api.multi
	def _compute_x_order_line_ids(self):
		
		print 'jx'
		print 'Compute Order ids'
		
		
		for record in self:		

			record.x_order_line_ids.unlink()

			partner_id = record.partner_id.name

			orders = self.env['sale.order'].search([
															('partner_id', '=', partner_id),			
													],
													#order='start_date desc',
													#limit=1,
												)
			print orders

			for order in orders: 
				print 
				print order.name 
				for line in order.order_line: 
					print line.product_id
					print line.name
					print line.price_subtotal
					print line.create_date

					#ret = record.x_order_line_ids.create({
					#											'product_id': line.product_id.id,
					#											'name': line.name,
					#											'price_subtotal': line.price_subtotal,
					#									})








# ----------------------------------------------------------- DNI RUC ------------------------------------------------------



	# Test DNI 
	@api.onchange('x_dni')

	def _onchange_x_dni(self):
	
		# For Digits 
		ret = pat_funcs.test_for_digits(self, self.x_dni)
		if ret != 0: 
			return ret
	
		# For Length 
		ret = pat_funcs.test_for_length(self, self.x_dni, 8)
		if ret != 0: 
			return ret




	# Test RUC
	@api.onchange('x_ruc')
	
	def _onchange_x_ruc(self):
		
		# For Digits 
		ret = pat_funcs.test_for_digits(self, self.x_ruc)
		if ret != 0: 
			return ret
		
		# For Length 
		ret = pat_funcs.test_for_length(self, self.x_ruc, 11)
		if ret != 0: 
			return ret








# ----------------------------------------------------------- Quick ------------------------------------------------------

	# Service Quick Ids 
	x_service_quick_ids = fields.One2many(
			'openhealth.service.quick', 
			'patient', 


			compute='_compute_service_quick_ids', 
		)

	@api.multi
	def _compute_service_quick_ids(self):
		
		#print 'jx'
		#print 'Compute service quick ids'
		
		
		for record in self:		
			services = self.env['openhealth.service.quick'].search([
																		('patient', '=', record.name),			
																	],
																	order='create_date asc',
																	#limit=1,
																)
			record.x_service_quick_ids = services













	# Hands 
	x_nr_quick_hands = fields.Integer(

			string='Manos', 
		
			default=0, 
			compute='_compute_nr_quick_hands', 
		)

	@api.multi
	def _compute_nr_quick_hands(self):
		
		zone = 'hands', 

		for record in self:		
			record.x_nr_quick_hands =	self.env['openhealth.service.quick'].search_count([																							
																								('patient', '=', record.name),			
																								('zone', '=', zone),			
																					]) 


	# Body Local 
	x_nr_quick_body_local = fields.Integer(

			string='Localizado Cuerpo', 
		
			default=0, 
			compute='_compute_nr_quick_body_local', 
		)

	@api.multi
	def _compute_nr_quick_body_local(self):
		
		zone = 'body_local', 

		for record in self:		
			record.x_nr_quick_body_local =	self.env['openhealth.service.quick'].search_count([																							
																								('patient', '=', record.name),			
																								('zone', '=', zone),			
																					]) 



	# Face Local 
	x_nr_quick_face_local = fields.Integer(

			string='Localizado Rostro', 
		
			default=0, 
			compute='_compute_nr_quick_face_local', 
		)

	@api.multi
	def _compute_nr_quick_face_local(self):
		
		zone = 'face_local', 

		for record in self:		
			record.x_nr_quick_face_local =	self.env['openhealth.service.quick'].search_count([																							
																								('patient', '=', record.name),			
																								('zone', '=', zone),			
																					]) 







	# Cheekbones 
	x_nr_quick_cheekbones = fields.Integer(

			string='Pómulos', 
		
			default=0, 
			compute='_compute_nr_quick_cheekbones', 
		)

	@api.multi
	def _compute_nr_quick_cheekbones(self):
		
		zone = 'cheekbones', 

		for record in self:		
			record.x_nr_quick_cheekbones =	self.env['openhealth.service.quick'].search_count([																							
																								('patient', '=', record.name),			
																								('zone', '=', zone),			
																					]) 



	# face_all 
	x_nr_quick_face_all = fields.Integer(

			string='Todo Rostro', 
		
			default=0, 
			compute='_compute_nr_quick_face_all', 
		)

	@api.multi
	def _compute_nr_quick_face_all(self):
		
		zone = 'face_all', 

		for record in self:		
			record.x_nr_quick_face_all =	self.env['openhealth.service.quick'].search_count([																							
																								('patient', '=', record.name),			
																								('zone', '=', zone),			
																					]) 




	# face_all_hands 
	x_nr_quick_face_all_hands = fields.Integer(

			string='Todo Rostro Manos', 
		
			default=0, 
			compute='_compute_nr_quick_face_all_hands', 
		)

	@api.multi
	def _compute_nr_quick_face_all_hands(self):
		
		zone = 'face_all_hands', 

		for record in self:		
			record.x_nr_quick_face_all_hands =	self.env['openhealth.service.quick'].search_count([																							
																								('patient', '=', record.name),			
																								('zone', '=', zone),			
																					]) 








	# face_all_neck 
	x_nr_quick_face_all_neck = fields.Integer(

			string='Todo Rostro Cuello', 
		
			default=0, 
			compute='_compute_nr_quick_face_all_neck', 
		)

	@api.multi
	def _compute_nr_quick_face_all_neck(self):
		
		zone = 'face_all_neck', 

		for record in self:		
			record.x_nr_quick_face_all_neck =	self.env['openhealth.service.quick'].search_count([																							
																								('patient', '=', record.name),			
																								('zone', '=', zone),			
																					]) 



	# neck 
	x_nr_quick_neck = fields.Integer(

			string='Cuello', 
		
			default=0, 
			compute='_compute_nr_quick_neck', 
		)

	@api.multi
	def _compute_nr_quick_neck(self):
		
		zone = 'neck', 

		for record in self:		
			record.x_nr_quick_neck =	self.env['openhealth.service.quick'].search_count([																							
																								('patient', '=', record.name),			
																								('zone', '=', zone),			
																					]) 



	# neck_hands 
	x_nr_quick_neck_hands = fields.Integer(

			string='Cuello y Manos', 
		
			default=0, 
			compute='_compute_nr_quick_neck_hands', 
		)

	@api.multi
	def _compute_nr_quick_neck_hands(self):
		
		zone = 'neck_hands', 

		for record in self:		
			record.x_nr_quick_neck_hands =	self.env['openhealth.service.quick'].search_count([																							
																								('patient', '=', record.name),			
																								('zone', '=', zone),			
																					]) 






#cheekbones
#face_all  
#face_all_hands
#face_all_neck
#neck 
#neck_hands  

























	x_nothing = fields.Char(
		'Nothing', 
	)




	# QC - Flag  
	x_flag = fields.Char(

		"Flag",
		
		default = '', 
		store=True, 
	)





	# QC - Number of clones  
	x_nr_clones = fields.Integer(
			"QC - Nrc",

			compute="_compute_x_nr_clones",
	)

	@api.multi
	
	def _compute_x_nr_clones(self):
		for record in self:

			record.x_nr_clones = self.env['oeh.medical.patient'].search_count([
																				('name','=', record.name),
																			]) 

			if record.x_nr_clones > 1:
				record.x_flag = 'error'

			else:
				record.x_flag = ''





	# QC - Lowcase
	x_lowcase = fields.Boolean(

			"QC - Low",

			compute="_compute_x_lowcase",
	)


	@api.multi
	def _compute_x_lowcase(self):
		for record in self:
			#if name != name.upper.strip:
			if record.name != record.name.upper():
				record.x_lowcase = True
				record.x_flag = 'error'
			else:
				record.x_lowcase = False
	#			record.x_flag = ''















	# Commons 
	vspace = fields.Char(
			' ', 
			readonly=True
			)



	x_nationality = fields.Selection(
			[	
				('peruvian', 	'Peruano'),
				('other', 		'Otro'),
			], 
			'Nacionalidad', 
			default="peruvian",
			required=True,  
		)


	x_id_doc = fields.Char(
			'Doc. identidad', 
		)


	x_id_doc_type = fields.Selection(
			[	
				('passport', 		'Pasaporte'),
				('foreigner_card', 	'Carnet de Extranjería'),
				('dni', 			'DNI'),
				('other', 			'Otro'),
			], 
			'Tipo de documento', 
			#default="passport",
			#required=True,  
		)





	#@api.multi
	#def card_purchase(self):  
	#	print 'jx'










	# Spaced 		- ???
	x_spaced = fields.Boolean(
		string="Spaced",
		default=False, 

		compute='_compute_spaced', 
	)

	#@api.multi
	@api.depends('name')

	def _compute_spaced(self):
		for record in self:

			if record.name[0] == ' ':
				record.x_spaced = True








	# Vip 
	x_vip = fields.Boolean(
		string="VIP",
		default=False, 

		#store=True, 			

		compute='_compute_x_vip', 
	)


	#@api.multi
	@api.depends('x_card')

	def _compute_x_vip(self):
		for record in self:

			x_card = record.env['openhealth.card'].search([
															('patient_name','=', record.name),
														],
														#order='appointment_date desc',
														limit=1,)

			if x_card.name != False:
				record.x_vip = True 
	# 







	x_card = fields.Many2one(
			'openhealth.card',
			string = "Tarjeta VIP", 	
			#required=True, 
			compute='_compute_x_card', 

			#store=True, 			
		)


	#@api.multi
	@api.depends('name')

	def _compute_x_card(self):
		for record in self:

			x_card = record.env['openhealth.card'].search([
															('patient_name','=', record.name),
														],
														#order='appointment_date desc',
														limit=1,)

			record.x_card = x_card
	# 













	x_country_name = fields.Char(
			'Pais', 
			required=True, 			
			compute='_compute_x_country_name', 
		)

	#@api.multi
	@api.depends('country_id')

	def _compute_x_country_name(self):
		for record in self:
			record.x_country_name = 'Peru'




	x_year = fields.Char(
			string='Year', 
			required=False, 
		)

	x_month = fields.Char(
			string='Month',

			#required=True, 
			required=False, 
		)



	# Year created  
	x_year_created = fields.Char(
			string='Year created', 
			#default = '', 
			#required=False, 

			index=True, 
			#compute='_compute_x_year_created', 
		)

	#@api.multi
	#@api.depends('x_date_created')

	#def _compute_x_year_created(self):
	#	for record in self:
	#		#print 
	#		#print 'Compute x_year_created'
	#		record.x_year_created = record.x_date_created.split('-')[0]


	@api.onchange('x_date_created')
	
	def _onchange_x_date_created(self):

		self.x_year_created = self.x_date_created.split('-')[0]

		self.x_month_created = self.x_date_created.split('-')[1]






	# Month created
	x_month_created = fields.Char(
			string='Month created', 
			#default = '', 
			#required=True, 

			#compute='_compute_x_month_created', 
		)

	#@api.multi
	#@api.depends('x_date_created')

	#def _compute_x_month_created(self):
	#	for record in self:
	#		#print 
	#		#print 'Compute x_month_created'
	#		record.x_month_created = record.x_date_created.split('-')[1]





	# Date created
	x_date_created = fields.Date(
			string = "Fecha de apertura",
			default = fields.Date.today, 
			#readonly = True, 
			required=True, 
			)


	x_datetime_created = fields.Datetime(
			string = "Apertura",

			##default = fields.Datetime.now, 
			#default = '', 
			
			#readonly = True, 

			#required=True, 
			required=False, 

			#store=True, 
			#compute='_compute_x_datetime_created', 
			)


	#@api.onchange('x_date_created')
	#def _onchange_x_date_created(self):
		#self.x_datetime_created = self.x_date_created  
		#self.x_datetime_created = '10/03/2017 20:00:00'
	#	self.x_datetime_created = '2017-10-03 20:00:00'
	#'%Y-%m-%d %H:%M:%S'


	#@api.multi
	#@api.depends('state')
	#def _compute_x_datetime_created(self):
	#	for record in self:
	#		if record.comment == 'legacy':
				#record.x_datetime_created = record.x_date_created
	#			record.x_datetime_created = ''








	x_status = fields.Char(
			string='Status', 

			default = '00', 

			#required=False, 
			required=True, 
		)



	x_state = fields.Selection(

			selection = pat_vars._state_list, 

			string='Estado', 			

			#default = False, 
			default = 'active', 

			compute='_compute_x_state', 
		)



	@api.multi
	#@api.depends('state')

	def _compute_x_state(self):
		for record in self:
			#print 
			#print 'jx'
			#print 'Compute x_state'

			#record.x_state = treatment_vars._hash_x_state[record.state]

			flag = False


			for treatment in record.treatment_ids:
				if treatment.progress == False: 
					flag = True

			if flag:
				record.x_state = 'incomplete'
			else:
				record.x_state = 'active'

			#print 










	x_first_impression = fields.Char(
			string="Primera impresión", 
			required=False, 
		)





# ----------------------------------------------------------- Autofill ------------------------------------------------------
	
	# Autofill

	x_autofill = fields.Boolean(
		string="Autofill",
		default=False, 
	)

	@api.onchange('x_autofill')
	
	def _onchange_x_autofill(self):

		if self.x_autofill == True:


			#self.x_last_name = 'Revilla Rondon'
			#self.x_first_name = 'Toby'





			self.sex = 'Male'

			self.dob = '1965-05-26'
			
			self.x_dni = '09817194'

			self.email = 'jrevilla55@gmail.com'
			
			self.phone = '4760118'

			self.x_allergies = 'Ninguna'

			self.x_first_contact = 'recommendation'




			self.city = 'arequipa'

			self.street = 'Av. San Borja Norte 610'
			
			#self.street2_sel = 41





			self.comment = 'test'

			self.x_ruc = '09817194123'

			self.x_firm = 'Revilla y Asociados'

			self.mobile = '991960734'



			
			#self.x_last_name = 'Fuchs Vibors'
			#self.x_first_name = 'Hans'
			#self.name = self.x_last_name + ' ' + self.x_first_name
			#self.street2 = 'San Borja'
			#self.zip = 41
			#self.city = 'Lima'
			#self.country_id = 175



# ----------------------------------------------------------- Relational ------------------------------------------------------


	treatment_ids = fields.One2many(
			'openhealth.treatment', 		
			'patient', 
			string="Tratamientos"
			)


	cosmetology_ids = fields.One2many(
			'openhealth.cosmetology', 		
			'patient', 
			string="Cosmiatrías"
			)







	appointment_ids = fields.One2many(
			'oeh.medical.appointment', 
			'patient', 
			
			#ondelete='cascade', 		# No - Very dangerous		

			string = "Citas", 
			)




# ----------------------------------------------------------- Re-definitions ------------------------------------------------------

	age = fields.Char(
			string = "Edad", 		
			)

	
	sex = fields.Selection(

			selection = pat_vars._sex_type_list, 

			string="Sexo",

			#required=True, 
			required=False, 
		)



	# Dictionary - For Reports 
	_dic = {
				'Male':		'Masculino', 
				'Female':	'Femenino', 
				'none':		'Ninguno', 
				'':			'', 
			}





	#x_sex_name = fields.Char(
	#		'Sexo', 
	#		required=True, 
	#		compute='_compute_x_sex_name', 
	#	)
	#@api.multi
	#def _compute_x_sex_name(self):
	#	for record in self:
	#		record.x_sex_name = record._dic[record.sex] 






	# For Ccdata compatibility 

	dob = fields.Date(
			string="Fecha nacimiento",

			#required=True, 
			required=False, 
		)



























	# Phone 1
	#@api.onchange('phone_1')
	#def _onchange_phone_1(self):
	#	ret = pat_funcs.test_for_digits(self, self.phone_1)
	#	if ret != 0: 
	#		return ret



	# Phone 2
	#@api.onchange('phone_2')
	#def _onchange_phone_2(self):
	#	ret = pat_funcs.test_for_digits(self, self.phone_2)
	#	if ret != 0: 
	#		return ret


	# Deprecated ? 
	#phone_1 = fields.Char(
	#	string="Teléfono 1",
		
		#required=True, 
	#	required=False, 
	#	)

	#phone_2 = fields.Char(
	#	string="Teléfono 2",

	#	required=False, 
	#	)





	# Phone 3 - Caregiver 
	@api.onchange('phone_3')
	def _onchange_phone_3(self):
		ret = pat_funcs.test_for_digits(self, self.phone_3)
		if ret != 0: 
			return ret

	# Caregiver 
	phone_3 = fields.Char(
		string="Teléfono",
		required=False, 
		)











	function = fields.Char(
			string = 'Ocupación',  
			placeholder = '',
			#required=True, 
			)





# ----------------------------------------------------------- New fields ------------------------------------------------------



	# Full name
	x_full_name = fields.Char(
		string = "Nombre completo",

		compute='_compute_full_name',
	)
	

	@api.depends('x_first_name', 'x_last_name')
	#@api.multi

	def _compute_full_name(self):
		for record in self:
			if record.x_first_name and record.x_last_name:				
				full = record.x_last_name.lower() + '_' + record.x_first_name.lower()
				full = full.replace (" ", "_")
				full = pat_funcs.strip_accents(full)
				record.x_full_name = full





	x_first_name = fields.Char(
		string = "Nombres", 	
		required=True, 
		default='',		
	)



	x_last_name = fields.Char(
		string = "Apellidos", 	
		required=True, 
		default='',	
	)







	x_date_consent = fields.Date(
			string = "Fecha de consentimiento informado", 	
			default = fields.Date.today, 
			#readonly = True, 
			#required=True, 
			)



	x_active = fields.Boolean(
			string = "Activa", 	
			default = True, 
			#readonly = True, 
			required=True, 
			)






	# Allergies 
	x_allergies = fields.Char(
			string = "Alergias", 

			#required=True, 
			#required=False, 
			)

	@api.onchange('x_allergies')
	def _onchange_x_allergies(self):

		if self.x_allergies != False: 
			self.x_allergies = self.x_allergies.strip().title()




	x_first_contact = fields.Selection(
			selection = pat_vars._first_contact_list, 
			string = '¿ Cómo se enteró ?',
			#default = 'none', 

			#required=True, 
			#required=False, 
			)


	# Caregiver
	x_caregiver_last_name = fields.Char(
			string = 'Apellidos',
			#default = '', 
			#required=True, 
			)

	x_caregiver_first_name = fields.Char(
			string = 'Nombres',
			#default = '', 
			#required=True, 
			)

	x_caregiver_dni = fields.Char(
			string = "DNI", 	
			#required=True, 
			)

	x_caregiver_relation = fields.Selection(
			selection = pat_vars._FAMILY_RELATION, 		
			string = 'Parentesco',
			default = 'none', 
			#required=True, 
			)



	x_country_residence= fields.Many2one(
			'res.country', 
			string = 'País de residencia', 
			default = '', 
			#required=True, 
			)

	x_education_level= fields.Selection(
			selection = pat_vars._education_level_type,
			string = 'Grado de instrucción',
			#default = 'university', 
			#required=True, 
			)



	# Control docs 

	x_control_dni_copy = fields.Boolean(
			string = 'Copia de DNI', 
			default = False 
			)

	x_control_informed_consent = fields.Boolean(
			string = 'Consentimiento informado', 
			default = False 
			)

	x_control_visia_record = fields.Boolean(
			string = 'Registro VISIA pre-procedimiento', 
			default = False 
			)

	x_control_photo_record = fields.Boolean(
			string = 'Registro fotográfico pre-procedimiento', 
			default = False 
			)

	x_control_treatment_signed_patient = fields.Boolean(
			string = 'Copia de información de tratamiento Láser firmada por el paciente', 
			default = False 
			)

	x_control_postlaser_instructions_signed = fields.Boolean(
			string = 'Copia de indicaciones post-Láser firmado por el paciente', 
			default = False 
			)

	x_control_treatment_signed_doctor = fields.Boolean(
			string = 'Informe de tratamiento Láser firmado por el doctor', 
			default = False 
			)

	x_control_clinical_analsis = fields.Boolean(
			string = 'Análisis clínicos', 
			default = False 
			)

	x_control_control_pictures = fields.Boolean(
			string = 'Fotos de controles', 
			default = False 
			)

	x_control_control_pictures_visia = fields.Boolean(
			string = 'Fotos de controles con VISIA', 
			default = False 
			)

	x_control_physician = fields.Many2one(
			'oeh.medical.physician',
			string="Médico responsable del control", 
			#required=True, 
			#index=True
			)







# ----------------------------------------------------------- On Changes ------------------------------------------------------



	# Last Name 
	@api.onchange('x_last_name', 'x_first_name')
	def _onchange_x_last_name(self):
		if self.x_last_name and self.x_first_name:
			self.name = pat_funcs.strip_accents(self.x_last_name.upper() + ' ' + self.x_first_name)




	@api.onchange('x_last_name')
	def _onchange_x_last_name_test(self):
		
		#print 'Test name'

		if self.x_last_name:
			ret = pat_funcs.test_name(self, self.x_last_name)
			
			#print ret 
			#print 
			
			return ret




















# ----------------------------------------------------------- Computes ------------------------------------------------------

	# Treatment count  
	x_treatment_count = fields.Integer(
			string = "Número de tratammientos",
			default = 0, 

			compute='_compute_x_treatment_count',
		)

	
	@api.multi
	#@api.depends('x_allergies')

	def _compute_x_treatment_count(self):

		for record in self:
			count = 0 

			for tr in record.treatment_ids:   
				count = count + 1  

			record.x_treatment_count = count  





	x_nr_cosmetologies = fields.Integer(

			'Nr Cosmiatrías', 

			default=0, 

			compute='_compute_x_nr_cosmetologies',
		)

	
	@api.multi
	#@api.depends('x_allergies')

	def _compute_x_nr_cosmetologies(self):

		for record in self:
			
			count = 0 

			for tr in record.cosmetology_ids:   
				count = count + 1  

			record.x_nr_cosmetologies = count  















# ----------------------------------------------------------- Buttons Update ------------------------------------------------------


	# Button - Update 
	# -------------------
	@api.multi
	def x_update(self):  

		#print 
		#print 'Update'

		self.x_date_created = self.x_date_created








# ----------------------------------------------------------- Buttons Treatment ------------------------------------------------------


	# Button - Treatment 
	# -------------------
	@api.multi
	def open_treatment_current(self):  


		treatment_id = self.env['openhealth.treatment'].search([
																		
																		('patient','=', self.id),
																
																],
																#order='start_date desc',
																order='write_date desc',
																limit=1,).id


		#print 
		#print 'Open Treatment'
		patient_id = self.id 
		#print patient_id

		return {

			# Mandatory 
			'type': 'ir.actions.act_window',
			'name': 'Open Treatment Current',



			# Window action 
			'res_model': 'openhealth.treatment',
			'res_id': treatment_id,


			# Views 
			"views": [[False, "form"]],
			'view_mode': 'form',
			'target': 'current',

			

			'flags': {
					'form': {'action_buttons': True, }
					#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
			},	

			'context':   {
				'search_default_patient': patient_id,
				'default_patient': patient_id,
			}
		}

	# open_treatment_current 








# ----------------------------------------------------------- Buttons Cosmetology ------------------------------------------------------


	# Button - Cosmetology 
	# -------------------
	@api.multi
	def open_cosmetology_current(self):  


		cosmetology_id = self.env['openhealth.cosmetology'].search([
																		('patient','=', self.id),
																],
																order='start_date desc',
																limit=1,).id




		#print 
		#print 'Open Cosmetology'
		patient_id = self.id 
		#print patient_id

		return {

			# Mandatory 
			'type': 'ir.actions.act_window',
			'name': 'Open cosmetology Current',


			# Window action 
			'res_model': 'openhealth.cosmetology',
			'res_id': cosmetology_id,


			# Views 
			"views": [[False, "form"]],
			'view_mode': 'form',
			'target': 'current',



			'flags': {
					'form': {'action_buttons': True, }
					#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
			},	



			'context':   {
				'search_default_patient': patient_id,
				'default_patient': patient_id,
			}
		}

	# open_cosmetology_current 






# ----------------------------------------------------------- Actions ------------------------------------------------------

	# Removem
	#@api.multi
	#def remove_myself(self):  	
	#	self.unlink()








# ----------------------------------------------------------- CRUD ------------------------------------------------------

# Create 
	@api.model
	def create(self,vals):

		print 'jx'
		print 'CRUD - Patient - Create'
		print 
		#print vals
	


		# Put your logic here 
		res = super(Patient, self).create(vals)
		# Put your logic here 




		# My logic 
		# Create a Treatment - When Patient is created - DEPRECATED !
		#name = vals['name']
		#patient_id = self.env['oeh.medical.patient'].search([('name', '=', name),]).id 
		#treatment = self.env['openhealth.treatment'].create({'patient': patient_id,})





		# Update Partner 
		#print self.street  
		#if self.street != False:
		#if True:
		#	print 'Update Partner !'
		#	self.partner_id.street = self.street



		return res
	# CRUD - Create 




# Write 
	@api.multi
	def write(self,vals):

		print 'jx'
		print 'CRUD - Patient - Write'
		print 
		#print vals
		#print 
		#print 

		#if vals['x_doctor'] != False: 
		#	print vals['x_doctor']
		#if vals['user_id'] != False: 
		#	print vals['user_id']




		#Write your logic here
		res = super(Patient, self).write(vals)
		#Write your logic here




		# Lang 
		#self.lang = 'es_ES'






		# Validations
		#self.email = self.email.lower()
		#self.street = self.street.title()






		# Update Partner 
		#if self.street != False:

		#	print 'Update Partner !'

		#	self.partner_id.street = self.street

		#	self.partner_id.street2 = self.street2

		#	self.partner_id.street2_sel = self.street2_sel

		#	self.partner_id.zip = self.zip

		#	self.partner_id.city = self.city.title()

		#	self.partner_id.state_id = self.state_id

		#	self.partner_id.country_id = self.country_id

		#	self.partner_id.x_dni = self.x_dni

		#	self.partner_id.email = self.email

		#	self.partner_id.phone = self.phone

		#	self.partner_id.mobile = self.mobile

		#	self.partner_id.lang = 'es_ES'




		#if self.x_ruc != False:

		#	self.partner_id.x_ruc = self.x_ruc

		#	self.partner_id.x_firm = self.x_firm



		return res

	# CRUD - Write 

