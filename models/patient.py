# -*- coding: utf-8 -*-
#
#		Patient 
# 
# Created: 				26 Aug 2016
#

from openerp import models, fields, api

from datetime import datetime
import pat_funcs
import pat_vars

import count_funcs


class Patient(models.Model):

	_inherit = 'oeh.medical.patient'

	#_order = 'write_date desc'
	_order = 'create_date desc'







# ----------------------------------------------------------- Deprecated ? ------------------------------------------------------

	#x_state = fields.Selection(		
	#	pat_vars._state_list, 
	#	string="Estado", 
		#default='draft', 
		#default='done', 
	#	default='active', 
	#)




# ----------------------------------------------------------- Active ------------------------------------------------------

	# Cancel
	@api.multi 
	def cancel_patient(self):

		print
		print 'Cancel Patient'


		self.active = False

		self.partner_id.active = False



		# Treatments
 		treatments = self.env['openhealth.treatment'].search([
																('patient', '=', self.name), 
														],
															#order='write_date desc',
															#limit=1,
														)
 		for treatment in treatments: 
 			treatment.active = False




		# Conter  
		name_ctr = 'emr'
 		
 		counter = self.env['openhealth.counter'].search([
																('name', '=', name_ctr), 
														],
															#order='write_date desc',
															limit=1,
														)
 		counter.decrease()






	# Activate Patient 
	@api.multi 
	def activate_patient(self):

		print
		print 'Activate Patient'


		self.active = True

		self.partner_id.active = True





		# Treatments
 		#treatments = self.env['openhealth.treatment'].search([
		#														('patient', '=', self.name), 
		#												],
															#order='write_date desc',
															#limit=1,
		#												)
 		#for treatment in treatments: 
 		#	treatment.active = True






		# Conter  
		name_ctr = 'emr'
 		
 		counter = self.env['openhealth.counter'].search([
																('name', '=', name_ctr), 
														],
															#order='write_date desc',
															limit=1,
														)
 		counter.increase()






# ----------------------------------------------------------- HC Number ------------------------------------------------------

	# Get Hc Number 
	@api.model
	def _get_default_id_code(self):

		name_ctr = 'emr'
 		
 		counter = self.env['openhealth.counter'].search([
																('name', '=', name_ctr), 
														],
															#order='write_date desc',
															limit=1,
														)

		name = count_funcs.get_name(self, counter.prefix, counter.separator, counter.padding, counter.value)

		return name




	# Id Code 
	x_id_code = fields.Char(
			'Nr Historia Médica',
			default=_get_default_id_code, 
		)






# ----------------------------------------------------------- Primitives ------------------------------------------------------


	# Allergies 
	x_allergies = fields.Many2one(
			'openhealth.allergy', 
			string = "Alergias", 

			#required=True, 
			required=False, 
		)


	
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







# ----------------------------------------------------------- Personal - Now Hard wired to Partner ------------------------------------------------------







# ----------------------------------------------------------- Legacy ------------------------------------------------------

	# Date created
	x_date_created = fields.Date(
			string = "Fecha de Apertura",
			default = fields.Date.today, 
			#readonly = True,
			required=False,
		)

	x_date_record = fields.Datetime(
			string='Fecha Registro', 
		)

	x_district = fields.Char(
			string='Distrito', 
		)

	# Correction comment 
	@api.multi 
	def correct_comment(self):
		print 'jx'
		print 'Correct Comment'
	 	comment = 'legacy, corr hd'
		self.comment = comment
	





# ----------------------------------------------------------- Estado de Cuenta ------------------------------------------------------

	# Estado de cuenta
	order_report_nex = fields.Many2one(			
			'openhealth.order.report.nex',		
			string="Estado de cuenta",		
		)




	# Generate 
	@api.multi 
	def generate_order_report(self):

		print 'jx'
		print 'Generate'



		# Clean 
		print 'Clean'
		self.remove_order_report()
		


		# Create
		print 'Create Or'
		self.order_report_nex = self.create_order_report()
		res_id = self.order_report_nex.id



		# Update 
		print 'Update'
		self.order_report_nex.update_order_report()




		return {
				'type': 'ir.actions.act_window',
				
				'name': ' New Order Report', 

				'view_type': 'form',

				'view_mode': 'form',	
				
				'target': 'current',

				#'res_model': 'openhealth.order.report',				
				'res_model': 'openhealth.order.report.nex',				
				
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
		self.order_report_nex = False





	# Create 
	@api.multi 
	def create_order_report(self):

		print
		print 'Create Order Report'


		name = 'EC - ' + self.partner_id.name


		print name, self.partner_id.id


		#order_report_id = self.env['openhealth.order.report'].create(
		
		order_report_id = self.env['openhealth.order.report.nex'].create(
																		{
																			'name': name, 
																			'partner_id': self.partner_id.id,											
																			
																			#'state':'sale',


																			#'subtotal':0,
																			#'pricelist_id': self.property_product_pricelist.id,	
																			#'patient': self.id,	
																			#'x_doctor': self.physician.id,	
																			#'treatment': self.id,
																			#'x_family': target, 
																			#'note': note, 
																		}
													).id


		

		return order_report_id











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












































# ----------------------------------------------------------- Personal ------------------------------------------------------


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
		)




	x_vip = fields.Boolean(
		string="VIP",
		default=False, 

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







	x_card = fields.Many2one(
			'openhealth.card',
			string = "Tarjeta VIP", 	
			#required=True, 

			compute='_compute_x_card', 
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


			# Personal 
			self.sex = 'Male'
			self.dob = '1965-05-26'

			self.x_dni = '09817195'
			
			self.email = 'jrevilla55@gmail.com'
			self.phone = '4760118'



			#self.x_allergies = 'Ninguna'
			name = 'Ninguna'
	 		allergy = self.env['openhealth.allergy'].search([
																('name', '=', name), 
															],
																#order='write_date desc',
																limit=1,
														) 		
			allergy_id = allergy.id
	 		if allergy_id != False: 
				self.x_allergies = allergy_id 


			
			self.x_first_contact = 'recommendation'
			self.comment = 'test'
			self.x_ruc = '09817194123'
			self.x_firm = 'Revilla y Asociados'
			self.mobile = '991960734'




			# Address 
			#self.city = 'arequipa'
			self.street2_sel = 41
			self.street = 'Av. San Borja Norte 610'			




			#self.x_last_name = 'Revilla Rondon'
			#self.x_first_name = 'Toby'
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









	# Date of Birth  
	dob = fields.Date(
			string="Fecha nacimiento",
			required=False, 
		)






	# Phone 3 - Caregiver 
	phone_3 = fields.Char(
		string="Teléfono",
		required=False, 
		)


	@api.onchange('phone_3')
	def _onchange_phone_3(self):
		ret = pat_funcs.test_for_digits(self, self.phone_3)
		if ret != 0: 
			return ret









	# Function
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

		print 
		print 'CRUD - Patient - Create'
		print 
		#print vals
	




		# Assign and Increase Counter 
		#if 'x_id_code' in vals: 

		#	name_ctr = 'emr'

	 	#	counter = self.env['openhealth.counter'].search([
		#															('name', '=', name_ctr), 
		#													],
																#order='write_date desc',
		#														limit=1,
		#													)


		#	name = count_funcs.get_name(self, counter.prefix, counter.separator, counter.padding, counter.value)

		#	vals['x_id_code'] = name 

		#	counter.increase()		# Here !!!


		#	print 'Gotcha !'
		#	print counter
		#	print name 
		#	print 'Increased'

		#else:
		#	print 'NOT Assigned nor Increased !'









		# Put your logic here 
		res = super(Patient, self).create(vals)
		# Put your logic here 





		# Increase - Must be after creation 
		name_ctr = 'emr'
	 	counter = self.env['openhealth.counter'].search([
																	('name', '=', name_ctr), 
															],
																#order='write_date desc',
																limit=1,
															)
		counter.increase()		# Here !!!
		print 'Increased'





		#print self.x_id_code



		return res
	# CRUD - Create 






# Write 
	@api.multi
	def write(self,vals):

		print 
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




		# Assign and Increase Counter 
		#if 'x_id_code' in vals: 
		#	print 'Assigned and Increased'
		#	print vals['x_id_code']
		#else:
		#	print 'NOT Assigned nor Increased !'




		#Write your logic here
		res = super(Patient, self).write(vals)
		#Write your logic here



		return res

	# CRUD - Write 

