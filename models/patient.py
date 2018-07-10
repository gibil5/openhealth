# -*- coding: utf-8 -*-
#
#		Patient 
# 
# Created: 			26 Aug 2016
#
# Last up: 			 9 Jul 2018
#

from openerp import models, fields, api
from datetime import datetime
import pat_funcs
import pat_vars
import count_funcs

class Patient(models.Model):

	_inherit = 'oeh.medical.patient'

	#_order = 'write_date desc'
	#_order = 'create_date desc'
	_order = 'x_id_code desc'




# ----------------------------------------------------------- Tmp ------------------------------------------------------

	x_nr_quick_hands = fields.Integer()
	
	x_nr_quick_body_local = fields.Integer()
	
	x_nr_quick_face_local = fields.Integer()

	x_nr_quick_cheekbones = fields.Integer()
	
	x_nr_quick_face_all = fields.Integer()
	
	x_nr_quick_face_all_hands = fields.Integer()
	
	x_nr_quick_face_all_neck = fields.Integer()
	
	x_nr_quick_neck = fields.Integer()
	
	x_nr_quick_neck_hands = fields.Integer()

	x_service_quick_ids = fields.One2many(
			'openhealth.service.quick', 
			'patient', 
		)




# ----------------------------------------------------------- Active Treatment ------------------------------------------------------

	# Active Treatment 
	treatment_active = fields.Many2one(
			'openhealth.treatment', 
			'Tratamiento Activo', 


			#domain = [
			#			('patient', '=', name),	
			#		],
		)



	# Clear App
	@api.multi 
	def update_treatment_active(self):
		
		print
		print 'Sincronizar'


		return {
				'domain': {'treatment_active': [
													('patient', '=', self.name),
							]},
			}




# ----------------------------------------------------------- Clear Apps ------------------------------------------------------

	# Clear App
	@api.multi 
	def clear_appointments(self):
		
		print
		print 'Clear Appointments'

		print self.appointment_ids
		self.appointment_ids.unlink()





# ----------------------------------------------------------- Update Date Record  ------------------------------------------------------

	# Dates 
	@api.multi 
	def update_date_record(self):
		print
		print 'Update - Date Record'
		print self.create_date
		print self.x_date_record
		if self.x_date_record == False: 
			self.x_date_record = self.create_date
			print 'Updated !'
			print 

	# update_date_record


# ----------------------------------------------------------- Activate and Deactivate ------------------------------------------------------

	# Cancel
	@api.multi 
	def deactivate_patient(self):

		print
		print 'Cancel Patient'

		# Init 
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



		# Conter Decrease 
		name_ctr = 'emr'
 		counter = self.env['openhealth.counter'].search([
																('name', '=', name_ctr), 
														],
															#order='write_date desc',
															limit=1,
														)
 		counter.decrease()

 	# deactivate_patient




	# Activate Patient 
	@api.multi 
	def activate_patient(self):

		print
		print 'Activate Patient'

		# Init 
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


		# Conter Increase 
		name_ctr = 'emr'
 		counter = self.env['openhealth.counter'].search([
																('name', '=', name_ctr), 
														],
															#order='write_date desc',
															limit=1,
														)
 		counter.increase()

 	# activate_patient




# ----------------------------------------------------------- HC Number ------------------------------------------------------

	# Default - HC Number 
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


	# NC Number 
	x_id_code = fields.Char(
			'Nr Historia Médica',

			default=_get_default_id_code, 
		)






# ----------------------------------------------------------- Primitives - Redefined ------------------------------------------------------

	# Allergies 
	x_allergies = fields.Many2one(
			'openhealth.allergy', 
			string = "Alergias", 
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
			string='Distrito L', 
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



	# Remove 
	@api.multi 
	def remove_order_report(self):
		self.order_report_nex = False
	# remove_order_report



	# Create 
	@api.multi 
	def create_order_report(self):
		name = 'EC - ' + self.partner_id.name
		order_report_id = self.env['openhealth.order.report.nex'].create({
																			'name': name, 
																			'patient': self.id,	
																			'partner_id': self.partner_id.id,
																		}).id
		#print name 			# Warning - Generates Error in Prod. Because of Latin chars (ie Ñ). 
		return order_report_id
	# create_order_report



	# Generate 
	@api.multi 
	def generate_order_report(self):

		print 
		print 'Generate Order Report'

		# Clean 
		self.remove_order_report()
		
		# Create
		self.order_report_nex = self.create_order_report()
		res_id = self.order_report_nex.id

		# Update 
		self.order_report_nex.update_order_report()

		return {
				'type': 'ir.actions.act_window',
				'name': ' New Order Report', 
				'view_type': 'form',
				'view_mode': 'form',	
				'target': 'current',
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
	# generate_order_report






# ----------------------------------------------------------- Verify - DNI and RUC ------------------------------------------------------

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





# ----------------------------------------------------------- Personal - Now Hard wired to Partner ------------------------------------------------------


# ----------------------------------------------------------- New Personal ------------------------------------------------------

	# Id Document 
	x_id_doc = fields.Char(
			'Doc. identidad', 
		)


	# Id Document Type 
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


	# Nationality 
	x_nationality = fields.Selection(
			[	
				('peruvian', 	'Peruano'),
				('other', 		'Otro'),
			], 
			'Nacionalidad', 
			default="peruvian",
			required=True,  
		)

#Positivo
#Normal
#Inseguro
#Preguntón
#Regateador 
#Agresivo
#Psiquiátrico
#Abogado 


	# First Impression 
	#x_first_impression = fields.Char(
	x_first_impression = fields.Selection(

			[	
				('positive', 		'Positivo'),

				('normal', 			'Normal'),

				('insecure', 		'Inseguro'),

				('asking', 			'Preguntón'),


				('barterint', 		'Regateador'),

				('agressive', 		'Agresivo'),

				('psychiatric', 	'Psiquiátrico'),

				('lawyer', 			'Abogado'),

				#('other', 			'Otro'),
			], 

			string="Primera impresión", 
			
			default='normal', 
			
			#required=False, 
			required=True, 
		)


	# Vip 
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



	# Vip Card 
	x_card = fields.Many2one(
			'openhealth.card',
			string = "Tarjeta VIP", 	

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
			self.street2_sel = 41
			self.street = 'Av. San Borja Norte 610'			


			self.function = 'Ingeniero'
			self.x_education_level = 'university'

			self.x_first_impression = 'normal'


			#self.x_last_name = 'Revilla Rondon'
			#self.x_first_name = 'Toby'
			#self.x_last_name = 'Fuchs Vibors'
			#self.x_first_name = 'Hans'
			#self.name = self.x_last_name + ' ' + self.x_first_name
			#self.street2 = 'San Borja'
			#self.zip = 41
			#self.city = 'Lima'
			#self.country_id = 175

	# _onchange_x_autofill


# ----------------------------------------------------------- Relational ------------------------------------------------------

	# Treatments 
	treatment_ids = fields.One2many(
			'openhealth.treatment', 		
			'patient', 
			string="Tratamientos"
		)


	# Appointments 
	appointment_ids = fields.One2many(
			'oeh.medical.appointment', 
			'patient', 			
			string = "Citas", 
		)




# ----------------------------------------------------------- Re-definitions ------------------------------------------------------

	# Age
	age = fields.Char(
			string = "Edad", 		
		)

	# Sex 
	sex = fields.Selection(
			selection = pat_vars._sex_type_list, 
			string="Sexo",
			required=False, 
		)


	# Date of Birth  
	dob = fields.Date(
			string="Fecha nacimiento",
			required=False, 
			default="2000-01-01"
		)

	# Function
	function = fields.Char(
			string = 'Ocupación',  
			placeholder = '',
			#required=True, 
		)




	# ----------------------------------------------------------- Deprecated ------------------------------------------------------

	# Dictionary - For Reports 
	#_dic = {
	#			'Male':		'Masculino', 
	#			'Female':	'Femenino', 
	#			'none':		'Ninguno', 
	#			'':			'', 
	#		}



	# ----------------------------------------------------------- New fields ------------------------------------------------------

	# First 
	x_first_name = fields.Char(
		string = "Nombres", 	
		required=True, 
		default='',		
	)


	# Last 
	x_last_name = fields.Char(
		string = "Apellidos", 	
		required=True, 
		default='',	
	)


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





	x_active = fields.Boolean(
			string = "Activa", 	
			default = True, 
			#readonly = True, 
			required=True, 
			)

	x_first_contact = fields.Selection(

			selection = pat_vars._first_contact_list, 
		
			string = '¿ Cómo se enteró ?',
			required=True, 
		)

	x_country_residence= fields.Many2one(
			'res.country', 
			string = 'País de residencia', 
			default = '', 
		)

	x_education_level= fields.Selection(
			selection = pat_vars._education_level_type,
			string = 'Grado de instrucción',
		)



	# Caregiver
	x_caregiver_last_name = fields.Char(
			string = 'Apellidos',
		)

	x_caregiver_first_name = fields.Char(
			string = 'Nombres',
		)

	x_caregiver_dni = fields.Char(
			string = "DNI", 	
		)

	x_caregiver_relation = fields.Selection(
			selection = pat_vars._FAMILY_RELATION, 		
			string = 'Parentesco',
			default = 'none', 
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

	x_date_consent = fields.Date(
			string = "Fecha de consentimiento informado", 	
			default = fields.Date.today, 
			#readonly = True, 
			#required=True, 
		)






	# ----------------------------------------------------------- On Changes ------------------------------------------------------

	# Last Name 
	@api.onchange('x_last_name', 'x_first_name')
	def _onchange_x_last_name(self):
		if self.x_last_name and self.x_first_name:
			self.name = pat_funcs.strip_accents(self.x_last_name.upper() + ' ' + self.x_first_name)

	@api.onchange('x_last_name')
	def _onchange_x_last_name_test(self):
		if self.x_last_name:
			ret = pat_funcs.test_name(self, self.x_last_name)			
			return ret






	# ----------------------------------------------------------- Treatment Count ------------------------------------------------------

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





	# ----------------------------------------------------------- Open Treatment ------------------------------------------------------

	# Open Treatment 
	@api.multi
	def open_treatment(self):  

		#print
		#print 'Open Treatment'

		# Init  
		#patient_id = self.id 


		# Search 
		treatment = self.env['openhealth.treatment'].search(	[		
																	('patient','=', self.id),
																	#('patient','=', patient_id),
																],
																order='write_date desc',
																limit=1,
															)
		#treatment_id = treatment.id


		return {
					# Mandatory 
					'type': 'ir.actions.act_window',
					'name': 'Open Treatment Current',
					# Window action 
					'res_model': 'openhealth.treatment',

					#'res_id': treatment_id,
					'res_id': treatment.id,
					
					# Views 
					"views": [[False, "form"]],
					'view_mode': 'form',
					'target': 'current',
					'flags': {
							'form': {'action_buttons': True, }
							#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
					},	
					'context':   {
									#'search_default_patient': patient_id,
									#'default_patient': patient_id,
									'search_default_patient': self.id,
									'default_patient': self.id,
					}
			}
	# open_treatment




	# ----------------------------------------------------------- CRUD ------------------------------------------------------

	# Create 
	@api.model
	def create(self,vals):

		print 
		print 'CRUD - Patient - Create'
		print 
	
		# Put your logic here 
		res = super(Patient, self).create(vals)
		# Put your logic here 


		# Serial Number. Increase must be AFTER creation 
		name_ctr = 'emr'
	 	counter = self.env['openhealth.counter'].search([
																	('name', '=', name_ctr), 
															],
																#order='write_date desc',
																limit=1,
															)
		counter.increase()		# Here !!!
		#print self.x_id_code


		# Date record 
		if res.x_date_record == False: 
			res.x_date_record = res.create_date

		return res
	# CRUD - Create 



	# Write 
	@api.multi
	def write(self,vals):

		#Write your logic here
		res = super(Patient, self).write(vals)
		#Write your logic here

		return res

	# CRUD - Write 

