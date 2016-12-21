# -*- coding: utf-8 -*-
#
# 	*** OPEN HEALTH
# 
# Created: 				26 Aug 2016
# Last updated: 	 	17 Sep 2016

from openerp import models, fields, api
from datetime import datetime

import jxvars

import jrfuncs

import pat_vars



class Patient(models.Model):
	#_name = 'openhealth.patient'	#The best solution ? So that impact is minimal ?

	_inherit = 'oeh.medical.patient'





	# Name

	#name = fields.Char(
	#	string = "Nombre completo", 	
		#compute='_compute_name',		
	#)

	#name = fields.Char(
	#	string='Name', 
	#	select=True,
	#	)
	
	#@api.depends('a_first_name', 'a_last_name')
	#@api.multi

	#def _compute_name(self):
	#	for record in self:
	#		if record.a_first_name and record.a_last_name:
	#			record.name = record.a_last_name.upper() + ' ' + record.a_first_name

	#name_clone = fields.Char(
	#	string = "Nombre completo", 	
	#	compute='_compute_name_clone',		
	#)

	#def _compute_name_clone(self):
	#	for record in self:
	#		if record.name:
	#			record.name_clone = record.name



	@api.onchange('a_last_name', 'a_first_name')
	def _onchange_a_last_name(self):
		if self.a_last_name and self.a_first_name:

			#self.name = self.a_last_name.upper() + ' ' + self.a_first_name

			self.name = jrfuncs.strip_accents(self.a_last_name.upper() + ' ' + self.a_first_name)










	# Full name
	a_full_name = fields.Char(
		string = "Nombre completo",

		compute='_compute_full_name',
	)
	

	@api.depends('a_first_name', 'a_last_name')
	#@api.multi

	def _compute_full_name(self):
		
		for record in self:
			
			#record.name = record.first_name.upper() + ' ' + record.last_name.upper()
			if record.a_first_name and record.a_last_name:
				
				#record.a_full_name = record.a_first_name.upper() + '  ' + record.a_last_name.upper()

				#full = record.a_first_name.lower() + '_' + record.a_last_name.lower()
				full = record.a_last_name.lower() + '_' + record.a_first_name.lower()
				
				full = full.replace (" ", "_")
				full = jrfuncs.strip_accents(full)

				record.a_full_name = full






	
	# Autofill

	x_autofill = fields.Boolean(
		string="Autofill",
		default=False, 
	)

	@api.onchange('x_autofill')
	
	def _onchange_x_autofill(self):

		if self.x_autofill == True:

			#self.name = 'Michi Felina'
			#self.a_first_name = 'Tigroide'
			


			#self.a_last_name = 'Revilla Rondón'
			#self.a_first_name = 'Fredy'
			#self.a_last_name = 'Fuchs Vibors'
			#self.a_first_name = 'Hans'



			#self.name = self.a_last_name + ' ' + self.a_first_name



			self.sex = 'Male'


			self.dob = '1965-05-26'
			self.a_dni = '09817194'

			self.email = 'tigroide55@gmail.com'
			self.phone_1 = '4760118'

			self.a_allergies = 'Ninguna'

			self.a_first_contact = 'recommendation'

			self.street = 'Av. San Borja Norte 610'
			self.street2_sel = 41
			#self.street2 = 'San Borja'
			#self.zip = 41
			#self.city = 'Lima'
			#self.country_id = 175








# ----------------------------------------------------------- Relational ------------------------------------------------------

	#a_treatment_ids = fields.One2many(
	treatment_ids = fields.One2many(
			'openextension.treatment', 
			'patient', 
			
			string="Tratamientos"
			)




	appointment_ids = fields.One2many(
			'oeh.medical.appointment', 
			'patient', 
			
			string = "Citas", 
			)




	#partner_ids = fields.One2many(
	#		'res.partner', 
	#		'patient', 
			
	#		string = "Partners", 
	#		)













# ----------------------------------------------------------- On change ------------------------------------------------------

	# On Change
	#@api.onchange('name')
	#def _onchange_name(self):
	#	ret = jrfuncs.test_name(self, self.name)
	#	return ret

















	#@api.depends('a_first_name', 'a_last_name')
	#@api.multi

	#def _compute_name(self):
	#	for record in self:
	#		if record.a_first_name and record.a_last_name:
	#			#record.a_full_name = record.a_first_name.upper() + '  ' + record.a_last_name.upper()
	#			record.name = record.a_first_name + ' ' + record.a_last_name



	# On Change
	#@api.onchange('a_first_name')
	#def _onchange_first_name(self):
	#	if self.a_first_name and self.a_last_name:
	#		self.name = self.a_first_name + ' ' + self.a_last_name
			#self.name = self.a_first_name.upper() + ' ' + self.a_last_name.upper()


	#@api.onchange('a_last_name')
	#def _onchange_last_name(self):
	#	if self.a_first_name and self.a_last_name:
	#		self.name = self.a_first_name + ' ' + self.a_last_name
			#self.name = self.a_first_name.upper() + ' ' + self.a_last_name.upper()






			
			#print 'jx'




	a_first_name = fields.Char(
		string = "Nombres", 	
		#required=False, 
		required=True, 
		default='',		
	)






	a_last_name = fields.Char(
		string = "Apellidos", 	
		#required=False, 
		required=True, 
		default='',	
	)







	# NEW 

	# Date created 
	a_date_created = fields.Date(
			string = "Fecha de apertura",

			default = fields.Date.today, 
			
			#readonly = True, 
			required=True, 
			#default='z',
			
			)


	a_date_consent = fields.Date(
			string = "Fecha de consentimiento informado", 	
			default = fields.Date.today, 
			#readonly = True, 
			#required=True, 
			#default='z',			
			)




	# Active 
	a_active = fields.Boolean(
			string = "Activa", 	
			default = True, 
			#readonly = True, 
			required=True, 
			)





	# REQUIRED


	age = fields.Char(
			string = "Edad", 		
			)

	
	sex = fields.Selection(
			string="Sexo",

			required=True, 
			#required=False, 
		)


	dob = fields.Date(
			string="Fecha nacimiento",

			required=True, 
			#required=False, 
		)


	a_dni = fields.Char(
			string = "DNI", 	
	
			required=True, 
			#required=False, 
			)

	a_allergies = fields.Char(
			string = "Alergias", 	
			
			required=True, 
			#required=False, 
			)


	a_first_contact = fields.Selection(
			selection = pat_vars._first_contact_list, 
			#string = '¿ Primer contacto con la clínica ?',
			string = '¿ Cómo se enteró ?',
			#default = 'none', 
			
			required=True, 
			#required=False, 
			)

	street = fields.Char(
			string = "Dirección", 	
			
			required=True, 
			#required=False, 
		)


	street2 = fields.Char(
			string = "Distrito", 	
			
			required=True, 
			#required=False, 
		)

	zip = fields.Integer(
			string = 'Código',  
			#compute='_compute_zip', 

			required=True, 			
			#required=False, 			
			)

	email = fields.Char(
			string = 'email',  
			placeholder = '',

			required=True, 
			#required=False, 
			)



	#@api.multi
	#def get_country_id(self):		
	#	print
	#	print 'get country id'
	#	country = self.env['res.country'].search([('name', 'like', 'Peru')])
	#	print country
	#	country_id = country.id
	#	print country_id
	#	print 
	#	return country_id



	country_id = fields.Many2one(
			'res.country', 
			string = 'País', 

			#default = 'Peru', 
			default = 175,

			#required=False, 
			required=True, 
			)




	city = fields.Selection(
			#selection = _city_list, 
			selection = pat_vars._city_list, 
			string = 'Departamento',  
			#default = ('lima','Lima'), 
			default = 'lima', 

			required=True, 
			#required=False, 
		)

	phone_1 = fields.Char(
		string="Teléfono 1",

		required=True, 
		#required=False, 
		)










	# On Change
	@api.onchange('a_dni')
	def _onchange_a_dni(self):

		ret = jrfuncs.test_for_digits(self, self.a_dni)

		if ret != 0: 
			return ret


		ret = jrfuncs.test_for_length(self, self.a_dni, 8)

		if ret != 0: 
			return ret





	# Phone 1


	@api.onchange('phone_1')

	def _onchange_phone_1(self):

		ret = jrfuncs.test_for_digits(self, self.phone_1)

		if ret != 0: 
			return ret





	# Phone 2

	phone_2 = fields.Char(
		string="Teléfono 2",
		required=False, 
		)


	@api.onchange('phone_2')

	def _onchange_phone_2(self):

		ret = jrfuncs.test_for_digits(self, self.phone_2)

		if ret != 0: 
			return ret





	# Phone 3 - Caregiver 

	phone_3 = fields.Char(
		string="Teléfono",
		required=False, 
		)

	@api.onchange('phone_3')

	def _onchange_phone_3(self):

		ret = jrfuncs.test_for_digits(self, self.phone_3)

		if ret != 0: 
			return ret

















	

	# Caregiver
	a_caregiver_last_name = fields.Char(
			string = 'Apellidos',
			#default = '', 
			#required=True, 
			)

	a_caregiver_first_name = fields.Char(
			string = 'Nombres',
			#default = '', 
			#required=True, 
			)

	a_caregiver_dni = fields.Char(
			string = "DNI", 	
			#required=True, 
			)
			

	FAMILY_RELATION = [
			
			('none', 'Ninguno'),

			('Father', 'Padre'),
			('Mother', 'Madre'),
			('Brother', 'Hermano'),
			('Grand Father', 'Abuelo'),
			('Friend', 'Amigo'),
			('Husband', 'Esposo'),
			('Other', 'Otro'),
			#('Sister', 'Hermana'),
			#('Wife', 'Esposa'),
			#('Grand Mother', 'Abuela'),
			#('Aunt', 'Tía'),
			#('Uncle', 'Tío'),
			#('Nephew', 'Sobrino'),
			#('Niece', 'Sobrina'),
			#('Cousin', 'Primo'),
			#('Relative', 'Pariente'),
			]

	a_caregiver_relation = fields.Selection(
			selection = FAMILY_RELATION, 
			string = 'Parentesco',
			default = 'none', 
			#default = 'Father', 
			#required=True, 
			)




	#a_country_residence = fields.Selection(
	#		selection = 'res.country', 
	#		string = 'País de residencia',
	#		default = 'Perú', 
	#		required=True, 
	#		)

	a_country_residence= fields.Many2one(
			'res.country', 
			string = 'País de residencia', 
			default = '', 
			#required=True, 
			)





	_education_level_type = [
			('first', 'Primaria'),
			('second', 'Secundaria'),
			('technical', 'Instituto'),
			('university', 'Universidad'),
			('masterphd', 'Posgrado'),
			]

	a_education_level= fields.Selection(
			selection = _education_level_type,
			string = 'Grado de instrucción',
			#default = 'university', 
			#required=True, 
			)





	# Control docs 
	a_control_dni_copy = fields.Boolean(
			string = 'Copia de DNI', 
			default = False 
			)

	a_control_informed_consent = fields.Boolean(
			string = 'Consentimiento informado', 
			default = False 
			)




	a_control_visia_record = fields.Boolean(
			string = 'Registro VISIA pre-procedimiento', 
			default = False 
			)

	a_control_photo_record = fields.Boolean(
			string = 'Registro fotográfico pre-procedimiento', 
			default = False 
			)




	a_control_treatment_signed_patient = fields.Boolean(
			string = 'Copia de información de tratamiento Láser firmada por el paciente', 
			default = False 
			)

	a_control_postlaser_instructions_signed = fields.Boolean(
			string = 'Copia de indicaciones post-Láser firmado por el paciente', 
			default = False 
			)



	a_control_treatment_signed_doctor = fields.Boolean(
			string = 'Informe de tratamiento Láser firmado por el doctor', 
			default = False 
			)

	a_control_clinical_analsis = fields.Boolean(
			string = 'Análisis clínicos', 
			default = False 
			)

	a_control_control_pictures = fields.Boolean(
			string = 'Fotos de controles', 
			default = False 
			)

	a_control_control_pictures_visia = fields.Boolean(
			string = 'Fotos de controles con VISIA', 
			default = False 
			)





	#jx 
	#_physician_list = [
	#		('chavarri_fernando','Fernando Chavarri'),
	#		('canales_paul','Paul Canales'),
	#		('desiree','Desiree'),
	#		('gonzales_leonardo','Leonardo Gonzáles'),
	#		('vasquez_javier','Javier Vásquez'),
	#		]

	#a_physician = fields.Selection(
	#		selection = _physician_list, 
	#		string = 'Doctor',  
			#default = '', 
			#required=True, 
	#		)

	# Physician 
	a_control_physician = fields.Many2one(
			'oeh.medical.physician',
			string="Médico responsable del control", 
			#required=True, 
			#index=True
			)
			#string="Physician", 
	        #default='Fernando Chavarri',






	# EXISTENT



	#jx 
	street2_sel = fields.Selection(

			selection = pat_vars._street2_list, 

			string = "Distrito", 	
			#required=True, 
		)



	@api.onchange('street2_sel')

	def _onchange_street2_sel(self):
		self.street2 = pat_vars.zip_dic_inv[self.street2_sel]
		self.zip = self.street2_sel




	street2_char = fields.Char(
			string = "Distrito", 	
			#required=True, 
		)

	@api.onchange('street2_char')

	def _onchange_street2_char(self):

		self.street2 = self.street2_char














	#@api.multi
	@api.depends('street2','city')

	def _compute_zip(self):
		for record in self:

			#if (record.street2 in jxvars.zip_dic) and (record.city == 'lima')  :
			if (record.street2 in pat_vars.zip_dic) and (record.city == 'lima')  :

				#record.zip=jxvars.zip_dic[record.street2]
				record.zip=pat_vars.zip_dic[record.street2]

			else:
				record.zip=0






	function = fields.Char(
			string = 'Ocupación',  
			placeholder = '',
			#required=True, 
			)


	#mobile = fields.Char(
	#		string = 'Celular',  
	#		placeholder = '',
			#required=True, 
	#		)

	#phone = fields.Char(
	#		string = 'Teléfono',  
	#		placeholder = '',
			#required=True, 
	#		)

            





    # Counts 
	# -----------
	#_vaccine_count = fields.Function(
	#_vaccine_count = fields.Integer(
	#		__vaccine_count, 
	#		string="Vaccines", 
	#		)


	# Vaccine count  
	#a_vaccine_count = fields.Integer(
	#		compute='_compute_a_vaccine_count',
	#		string = "Número de vacunas",
	#		default = 55, 
	#		)

	#@api.multi
	#def _compute_a_vaccine_count(self):
	#	for record in self:
			#record.a_vaccine_count = 5
	#		sub_total = 0 
	#		for tr in record.a_treatment_ids:   
	#			sub_total = sub_total + 1  
	#		record.a_vaccine_count = sub_total  



	# Treatment count  
	a_treatment_count = fields.Integer(
			compute='_compute_a_treatment_count',
			string = "Número de tratammientos",
			default = 0, 
			)

	@api.multi
	#@api.depends('a_allergies')
	#@api.depends('a_treatment_ids')
	def _compute_a_treatment_count(self):
		for record in self:
			#record.a_treatment_count = 5
			sub_total = 0 
			for tr in record.treatment_ids:   
				sub_total = sub_total + 1  
			record.a_treatment_count = sub_total  








	nr_treatments = fields.Integer(
			compute='_compute_nr_treatments',
			string = "Número de vacunas",
			default = 55, 
			)

	@api.multi
	#@api.depends('a_allergies')
	#@api.depends('a_treatment_ids')
	def _compute_nr_treatements(self):
		for record in self:
			record.nr_treatments = 5  
			#record.a_nr_treatments = 5  
			#sub_total = 0 
			#for tr in record.treatment_ids:   
			#	sub_total = sub_total + 1  
			#record.a_nr_treatments= sub_total  









	# Buttons
	# -----------------------------------------------------------------------------------------------------------------


	# Button - Treatment 
	# -------------------
	@api.multi
	def open_treatment_current(self):  

		print 
		print 'Open Treatment'

		patient_id = self.id 
		print patient_id


		return {

			# Mandatory 
			'type': 'ir.actions.act_window',
			'name': 'Open Treatment Current',

			# Window action 
			'res_model': 'openextension.treatment',

			# Views 
			"views": [[False, "form"]],
			'view_mode': 'form',
			'target': 'current',

			'context':   {
				'search_default_patient': patient_id,
				'default_patient': patient_id,
			}

		}








# ----------------------------------------------------------- CRUD ------------------------------------------------------

	@api.model
	def create(self,vals):

		print 
		print 'Patient - Create - Override'
		print 
		print vals
		print 
	

		#appointment_date = vals['appointment_date']
		#doctor = vals['doctor']
		#patient = vals['patient']


		#print "appointment date: ", appointment_date
		#print "doctor: ", doctor
		#print "patient: ", patient
		
		#print "treatment: ", treatment
		#print self.treatment





		# Return 
		res = super(Patient, self).create(vals)

		return res







