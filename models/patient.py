# -*- coding: utf-8 -*-
#
# 	*** OPEN HEALTH
# 
# Created: 				26 Aug 2016
# Last updated: 	 	17 Sep 2016

from openerp import models, fields, api
from datetime import datetime





class Patient(models.Model):
	#_name = 'openhealth.patient'
	#Te best solution. So that impact is minimal. 

	_inherit = 'oeh.medical.patient'



	# NEW 

	# Date created 
	a_date_created = fields.Date(
			string = "Fecha de apertura", 	
			#default = fields.Date.today, 
			#readonly = True, 
			required=True, 
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
			#required=True, 
			)



	_first_contact_list = [
			('none','ninguno'), 
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
			#default = 'Padre', 
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
			required=True, 
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
			string = "", 	
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
			('huanuco','Huánuco'),
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
			string = '',  
			#default = ('lima','Lima'), 
			default = 'lima', 
			required=True, 
		)



	_lima_district_list = [

			('Lima','1'),
			('Ancón','2'),
			('Ate','3'),
			('Barranco','4'),
			('Breña','5'),
			('Carabayllo','6'),
			('Comas','7'),
			('Chaclacayo','8'),
			('Chorrillos','9'),
			('El Agustino','10'),
			('Jesús María','11'),
			('La Molina','12'),
			('La Victoria','13'),
			('Lince','14'),
			('Lurigancho','15'),
			('Lurín','16'),
			('Magdalena del Mar','17'),
			('Miraflores','18'),
			('Pachacamac','19'),
			('Pucusana','20'),
			('Pueblo Libre','21'),
			('Puente Piedra','22'),
			('Punta Negra','23'),
			('Punta Hermosa','24'),
			('Rímac','25'),
			('San Bartolo','26'),
			('San Isidro','27'),
			('Independencia','28'),
			('San Juan de Miraflores','29'),
			('San Luis','30'),
			('San Martín de Porres','31'),
			('San Miguel','32'),
			('Santiago de Surco','33'),
			('Surquillo','34'),
			('Villa María del Triunfo','35'),
			('San Juan de Lurigancho','36'),
			('Santa María del Mar','37'),
			('Santa Rosa','38'),
			('Los Olivos','39'),
			('Cieneguilla','40'),
			('San Borja','41'),
			('Villa El Salvador','42'),
			('Santa Anita','43'),
			]


	#a_district = fields.Selection(
	zip = fields.Selection(
			selection = _lima_district_list, 
			string = 'Distrito',  
			#default = ('lima','Lima'), 
			#default = 'Lima', 
			placeholder="Código", 
			required=True, 
			)



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


