# -*- coding: utf-8 -*-
#
# 	*** OPEN HEALTH
# 
# Created: 				26 Aug 2016
# Last updated: 	 	17 Sep 2016

from openerp import models, fields, api
from datetime import datetime

import jxvars




class Patient(models.Model):
	#_name = 'openhealth.patient'
	#Te best solution. So that impact is minimal. 

	_inherit = 'oeh.medical.patient'



	# Names 
	#name = fields.Char(
	#	string = "Nombre completo", 	
	#	required=False, 
		#compute='_compute_name',
		#readonly=True, 
		#default='x',
	#)
	
	
	# Names
	a_full_name = fields.Char(
		string = "Nombre completo", 	
		#required=False, 
		compute='_compute_full_name',
		#readonly=True, 
		default='a',
	)
	
	@api.depends('a_first_name')
	#@api.multi

	def _compute_full_name(self):
		for record in self:
			#record.name = record.first_name.upper() + ' ' + record.last_name.upper()
			record.a_full_name = record.a_first_name.upper() + '  ' + record.a_last_name.upper()
			#record.name = record.name
	#		print 'jx'


	a_first_name = fields.Char(
		string = "Nombre", 	
		#quired=False, 
		#required=True, 
		default='b',		
	)


	a_last_name = fields.Char(
		string = "Apellido", 	
		#required=True, 
		#required=False, 
		default='c',	
	)



	# NEW 

	# Date created 
	a_date_created = fields.Date(
			string = "Fecha de apertura", 	
			#default = fields.Date.today, 
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




	a_dni = fields.Char(
			string = "DNI", 	
			required=True, 
			)


	def test_dni(self,cr,uid,ids,context=None):

		print context

		if context and (not context.isdigit()):
			return {
					'warning': {
						'title': "Error: DNI no es número",
						'message': context,
					}}

		if context and (len(str(context))!= 8):
			return {
					'warning': {
						'title': "Error: DNI no tiene 8 cifras",
						'message': context,
					}}
					
		return {}
		
		


	_first_contact_list = [
			('none','Ninguno'), 
			('recommendation','Recomendación'), 
			('tv','Tv'), 
			('radio','Radio'), 
			('internet','Internet'), 
			('website','Sitio web'), 
			('mail_campaign','Campaña de mail'), 
			]

	a_first_contact = fields.Selection(
			selection = _first_contact_list, 
			string = '¿ Primer contacto con la clínica ?',
			#default = 'none', 
			required=True, 
			)



	a_allergies = fields.Char(
			string = "Alergias", 	
			#required=True, 
			)


	a_treatment_ids = fields.One2many(
			#'openhealth.treatment', 
			'openextension.treatment', 
			#'patient_id', 
			'patient', 
			string="Tratamientos"
			)


	

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
	street = fields.Char(
			string = "Dirección", 	
			#required=True, 
		)

	street2 = fields.Char(
			string = "Distrito", 	
			#required=True, 
		)




	_city_list = [
			('lima','Lima'),
			('abancay','Abancay'),
			('arequipa','Arequipa'),
			('ayacucho','Ayacucho'),
			('cajamarca','Cajamarca'),
			('callao','Callao'),
			('cerro_de_pasco','Cerro de Pasco'), 
			('chachapoyas','Chachapoyas'),
			('chiclayo','Chiclayo'),
			('cuzco','Cuzco'),
			('huacho','Huacho'),
			('huancavelica','Huancavelica'),
			('huancayo','Huancayo'),
			#('huanuco','Huánuco'),
			('huanuco','Huanuco'),
			('huaraz','Huaraz'),
			('ica','Ica'),
			('iquitos','Iquitos'),
			('moquegua','Moquegua'),
			('moyobamba','Moyobamba'),
			('piura','Piura'),
			('pucallpa','Pucallpa'),
			('puerto_maldonado','Puerto Maldonado'), 
			('puno','Puno'),
			('tacna','Tacna'),
			('trujillo','Trujillo'),
			('tumbes','Tumbes'),
		]

	city = fields.Selection(
			selection = _city_list, 
			string = 'Departamento',  
			#default = ('lima','Lima'), 
			default = 'lima', 
			required=True, 
		)






	#a_district = fields.Selection(
	#zip = fields.Selection(
	zip = fields.Integer(
			#selection = zip_list, 
			#selection = jxvars.zip_list, 
			
			string = 'Código',  
			#default = ('lima','Lima'), 
			#default = 'Lima', 
			#placeholder="Código", 
			required=True, 
			
			compute='_compute_zip', 
			)

	#@api.multi
	@api.depends('street2','city')

	def _compute_zip(self):
		for record in self:
			#record.zip=zip_list[record.city]
			#record.zip=jxvars.zip_list[record.street2]
			if (record.street2 in jxvars.zip_dic) and (record.city == 'lima')  :
				record.zip=jxvars.zip_dic[record.street2]
			else:
				#record.zip=0
				record.zip=0






	function = fields.Char(
			string = 'Ocupación',  
			placeholder = '',
			#required=True, 
			)


	mobile = fields.Char(
			string = 'Celular',  
			placeholder = '',
			#required=True, 
			)

	phone = fields.Char(
			string = 'Teléfono',  
			placeholder = '',
			#required=True, 
			)

	email = fields.Char(
			string = 'email',  
			placeholder = '',
			#required=True, 
			)




	country_id = fields.Many2one(
			'res.country', 
			string = 'País', 
			#default = 'Perú', 
			#default = '51', 
			required=True, 
			)
            





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
			for tr in record.a_treatment_ids:   
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

		#patient_id = self.patient.id
		#doctor_id = self.physician.id
		patient_id = self.id 

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


