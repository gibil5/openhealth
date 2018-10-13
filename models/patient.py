# -*- coding: utf-8 -*-
#
#		Patient 
# 
# 		Created: 		26 Aug 2016
# 		Last up: 		26 Sep 2018
#
from openerp import models, fields, api
from datetime import datetime
import lib
import user
import count_funcs
import pat_vars
import creates as cre

import chk_patient as chk
#import chk

import tst_pat




class Patient(models.Model):
	_inherit = 'oeh.medical.patient'
	_order = 'x_id_code desc'



# ----------------------------------------------------------- Test ------------------------------------------------------

	container_id = fields.Many2one(
		'openhealth.container', 		
		ondelete='cascade', 
	)



# ----------------------------------------------------------- Constraints - Sql ------------------------------------------------------
	# Uniqueness constraints for: 
	# 	Name
	# 	Id Code - Nr de Historia
	# 	Id Doc - Documento de Identidad 
	
	#_sql_constraints = [
	#						('name_unique','unique(name)', 'SQL Warning: name must be unique !'),
	#						('x_id_code_unique','unique(x_id_code)', 'SQL Warning: x_id_code must be unique !'),
	#						('x_id_doc_unique','unique(x_id_doc)', 'SQL Warning: x_id_doc must be unique !'),
	#					]     




# ----------------------------------------------------------- Constraints - Python - Abstract ------------------------------------------------------

	# Check Name  
	@api.constrains('name')
	def _check_name(self):
		#print
		#print 'Check Name'
		chk._check_name(self)



	# Check Id Code - Hr Historia  
	@api.constrains('x_id_code')
	def _check_x_id_code(self):
		#print
		#print 'Check Id Code'
		chk._check_x_id_code(self)



	# Check Ruc
	@api.constrains('x_ruc')
	def _check_x_ruc(self):
		#print
		#print 'Check Ruc'
		chk._check_x_ruc(self)




	# Check Phone 3
	@api.constrains('phone_3')
	def _check_phone_3(self):
		#print
		#print 'Check Phone 3'
		chk._check_phone_3(self)



	# Check Phone
	@api.constrains('phone')
	def _check_phone(self):
		#print
		#print 'Check Phone'
		chk._check_phone(self)




	# Check Mobile
	@api.constrains('mobile')
	def _check_mobile(self):
		#print
		#print 'Check Mobile'
		chk._check_mobile(self)




# ----------------------------------------------------------- Constraints - Python - Custom ------------------------------------------------------

	# Check Id doc - Documento Identidad 
	@api.constrains('x_id_doc')
	def _check_x_id_doc(self):

		chk.check_x_id_doc(self)






# ----------------------------------------------------------- Id Doc ------------------------------------------------------

	# Id Document 
	x_id_doc = fields.Char(
			#'Doc. identidad', 
			'Nr. Doc.', 

			#required=True,  
		)



	# Id Document Type 
	x_id_doc_type_code = fields.Char(
			string='Tipo de documento Cod', 

			compute='_compute_x_id_doc_type_code', 
		)

	@api.multi
	def _compute_x_id_doc_type_code(self):
		for record in self:			
	
			record.x_id_doc_type_code = pat_vars._dic_id_doc_code[record.x_id_doc_type]



	# Id Document Type 
	x_id_doc_type = fields.Selection(
			#[	
			#	('dni', 			'DNI'),
			#	('passport', 		'Pasaporte'),
			#	('foreigner_card', 	'Carnet de Extranjería'),
			#	('ptp', 			'PTP'),	
			#	('other', 			'Otro'),
			#], 
			selection = pat_vars._id_doc_type_list, 
			string='Tipo de documento', 
			#default="dni",

			#required=True,  
		)


	# Id Doc  
	#@api.onchange('x_id_doc')
	#def _onchange_x_id_doc(self):
		#self.autofill() if self.x_autofill == True else 'don'
		
		#if self.x_id_doc_type in ['dni']: 
		#	self.x_dni = self.x_id_doc





# ----------------------------------------------------------- QC ------------------------------------------------------

	# Data complete 
	x_data_complete = fields.Boolean(
			string="Data Complete", 

			compute='_compute_x_data_complete',
	)

	@api.multi
	#@api.depends('x_card')
	def _compute_x_data_complete(self):
		for record in self:	
			if record.x_legacy or record.x_treatment_count > 0: 
				record.x_data_complete = True
			else: 
				record.x_data_complete = False




	# Legacy 
	x_legacy = fields.Boolean(
			string="Legacy", 

			compute='_compute_x_legacy', 
	)

	@api.multi
	#@api.depends('x_card')
	def _compute_x_legacy(self):
		for record in self:
			#pass 
			if record.x_counter < 13963: 
				record.x_legacy = True



	# Counter 
	x_counter = fields.Integer(
			string="Counter", 
			#default=55, 

			compute='_compute_x_counter', 
	)

	@api.multi
	#@api.depends('x_card')
	def _compute_x_counter(self):
		for record in self:
			#pass 
			if record.x_id_code != False: 
				record.x_counter = str(record.x_id_code)




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
		#self.order_report_nex.update_order_report()
		self.order_report_nex.update()

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
				'context': {}
				}
	# generate_order_report





# ----------------------------------------------------------- Personal - Now Hard wired to Partner ------------------------------------------------------









# ----------------------------------------------------------- New Personal - 2 ------------------------------------------------------
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


	# First Impression 
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

	# Open Treatment 
	@api.multi
	def autofill(self):  

		# Personal 
		self.sex = 'Male'
		self.dob = '1965-05-26'
		self.email = 'jrevilla55@gmail.com'
		self.phone = '4760118'
		self.x_first_contact = 'recommendation'
		self.comment = 'test'
		self.x_ruc = '09817194123'
		self.x_firm = 'Revilla y Asociados'
		self.mobile = '991960734'
		self.street2_sel = 41
		self.street = 'Av. San Borja Norte 610'			
		self.function = 'Ingeniero'
		self.x_education_level = 'university'
		self.x_first_impression = 'normal'

 		allergy_id = self.env['openhealth.allergy'].search([
															('name', '=', 'Ninguna'), 
														],
															#order='write_date desc',
															limit=1,
													).id	
		#allergy_id = allergy.id
 		if allergy_id != False: 
			self.x_allergies = allergy_id 


		#self.x_dni = '09817195'
		self.x_id_doc_type = 'dni'
		self.x_id_doc = '09817195'



# ----------------------------------------------------------- Autofill ------------------------------------------------------
	
	# Autofill
	x_autofill = fields.Boolean(
			string="Autofill",
			default=False, 
		)



# ----------------------------------------------------------- Relational ------------------------------------------------------

	# Treatments 
	treatment_ids = fields.One2many(
			'openhealth.treatment', 		
			'patient', 
			string="Tratamientos"
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
				full = lib.strip_accents(full)
				record.x_full_name = full


	# Active 
	x_active = fields.Boolean(
			string = "Activa", 	
			default = True, 
			#readonly = True, 
			required=True, 
			)

	x_first_contact = fields.Selection(
			selection = pat_vars._first_contact_list, 
		
			string = '¿ Cómo se enteró ?',
			#required=True, 
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

	phone_3 = fields.Char(
		string="Teléfono",
		required=False, 
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
			)

	x_date_consent = fields.Date(
			string = "Fecha de consentimiento informado", 	
			default = fields.Date.today, 
		)


# ----------------------------------------------------------- Treatment Count ------------------------------------------------------

	# Treatment count  
	x_treatment_count = fields.Integer(
			string = "Nr TRATAMIENTOS",
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



# ----------------------------------------------------------- Deactivate ------------------------------------------------------
	# Deactivate
	@api.multi 
	def deactivate_patient(self):

		# Init 
		self.active = False
		self.partner_id.active = False

		# Treatments 		
 		#treatments = self.env['openhealth.treatment'].search([
		#														('patient', '=', self.name), 
		#												],
															#order='write_date desc',
															#limit=1,
		#												)

 		#for treatment in treatments: 
 		#	treatment.active = False


		# Conter Decrease - DEP ! 
 		#counter = self.env['openhealth.counter'].search([
		#														('name', '=', 'emr'), 
		#												],
															#order='write_date desc',
		#													limit=1,
		#												)
 		#counter.decrease()
 	
 	# deactivate_patient



# ----------------------------------------------------------- Activate ------------------------------------------------------
	# Activate Patient 
	@api.multi 
	def activate_patient(self):

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


		# Conter Increase - DEP ! 
 		#counter = self.env['openhealth.counter'].search([
		#														('name', '=', 'emr'), 
		#												],
															#order='write_date desc',
		#													limit=1,
		#												)
 		#counter.increase()
 	# activate_patient




# ----------------------------------------------------------- Open Treatment ------------------------------------------------------

	# Open Treatment 
	@api.multi
	def open_treatment(self):  

		#print
		#print 'Open Treatment'


		# Search 
		treatment = self.env['openhealth.treatment'].search([		
																('patient','=', self.id),
															],
															order='write_date desc',
															limit=1,
														)
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
									'search_default_patient': self.id,
									'default_patient': self.id,
					}
			}
	# open_treatment




# ----------------------------------------------------------- On Changes ------------------------------------------------------

	# Ternary If 
	#isApple = True if fruit == 'Apple' else False

	# Autofill 
	@api.onchange('x_autofill')
	def _onchange_x_autofill(self):
		self.autofill() if self.x_autofill == True else 'don'

	# Street2 ?
	@api.onchange('street2_char')
	def _onchange_street2_char(self):
		self.street2 = self.street2_char

	# Zip  Street2
	@api.onchange('street2_sel')
	def _onchange_street2_sel(self):
		self.street2 = pat_vars.zip_dic_inv[self.street2_sel]
		self.zip = self.street2_sel

	# Street 
	@api.onchange('street')
	def _onchange_street(self):
		self.street = self.street.strip().title() if self.street != False else ''



# ----------------------------------------------------------- On Changes - Name ------------------------------------------------------

	# Only format last and first. Do not assign Name. 
	# This is done in CRUD.


	# Must have two or more last names 
	@api.onchange('x_last_name')
	def _onchange_x_last_name_test(self):
		return lib.test_for_one_last_name(self, self.x_last_name) if self.x_last_name else 'don'

	
	# Name
	@api.onchange('x_last_name', 'x_first_name')
	def _onchange_x_last_name(self):
		print 'On Change'
		print 'Last First Names'

		#self.name = lib.strip_accents(self.x_last_name.upper() + ' ' + self.x_first_name.upper()) if self.x_last_name and self.x_first_name else 'don'

		if self.x_last_name: 
			self.x_last_name = lib.strip_accents(self.x_last_name.upper()) 

		if self.x_first_name: 
			self.x_first_name =  lib.strip_accents(self.x_first_name.upper()) 





# ----------------------------------------------------------- Test - Init ------------------------------------------------------
	
	# Test - Init  
	@api.multi 
	def test_init(self, patient_id=False, partner_id=False, doctor_id=False, treatment_id=False, pl_id=False):
		print 
		print 'Patient - Test Init'


		pat_array = tst_pat.test_init(self, patient_id, partner_id, doctor_id, treatment_id, pl_id)


		return pat_array



# ----------------------------------------------------------- Test - Computes------------------------------------------------------

	# Computes
	def test_computes(self):
		print 
		print 'Patient - Computes'

		# Partner 
		# Computes 
		print 
		print 'Computes - Partner'
		print self.partner_id.city_char
		print self.partner_id.x_address
		print self.partner_id.x_vip
		
		# Patient 
		print 
		print 'Computes'
		print self.name 
		print self.x_full_name
		print self.x_treatment_count
		print self.x_vip
		print self.x_card
		print self.x_legacy
		print self.x_counter


	# Actions
	def test_actions(self):
		print 
		print 'Patient - Actions'

		print 
		print 'Actions'
		self.deactivate_patient()
		self.activate_patient()
		self.open_treatment()
		self.generate_order_report()
		if self.x_test: 
			self.autofill()


	# Actions
	def test_services(self):
		print 
		print 'Patient - Services'

		for treatment in self.treatment_ids: 

			print 'Services'

			for service in treatment.service_co2_ids: 
				service.test()

			for service in treatment.service_excilite_ids: 
				service.test()

			for service in treatment.service_ipl_ids: 
				service.test()

			for service in treatment.service_ndyag_ids: 
				service.test()

			for service in treatment.service_product_ids: 
				service.test()

			for service in treatment.service_quick_ids: 
				service.test()


# ----------------------------------------------------------- Test - Cycle ------------------------------------------------------
	
	# Test - Cycle 
	# Test the whole Patient Cycle. 

	@api.multi 
	def test_cycle(self):
		print 
		print 'Patient - Test Cycle'

		# Unit Testing 
		#self.test_computes()
		#self.test_actions()
		#self.test_services()


		print self.name 

		print 
		print 'Treatments'
		for treatment in self.treatment_ids: 

			print treatment 
			
			order = treatment.create_order_con_tst()
			
			order.test(self.x_test_case)





# ----------------------------------------------------------- Test - Fields ------------------------------------------------------

	x_test = fields.Boolean(
			'Test', 
		)

	x_test_case = fields.Char(
			'Test Case', 
		)

# ----------------------------------------------------------- Test ------------------------------------------------------

	# Test - Integration 
	@api.multi 
	def test(self):
		print 'jx'
		print 'jx'
		print 'Patient - Test'

		# Test Cycle
		self.test_cycle()


	# test 




# ----------------------------------------------------------- Const - Print ------------------------------------------------------
	# Dic - For the HC Report 
	_dic = {
					False: 	'',	

					# Sex 
					'Male': 	'Masculino',	
					'Female': 	'Femenino',

					# Sex 
					'first': 		'Primaria',	
					'second': 		'Secundaria',
					'technical': 	'Técnica',
					'university': 	'Universidad',
					'masterphd': 	'Master / Doctorado',

					# Caregiver Relation 
					'none': 	'Ninguno',	
					'Father': 	'Padre',	
					'Mother': 	'Madre',	
					'Brother': 	'Hermano/a',	
					'Grand Father': 	'Abuelo/a',	
					'Friend': 	'Amigo/a',	
					'Husband': 	'Esposo/a',	
					'Other': 	'Otro',	
	}

# ----------------------------------------------------------- Print - Patient HC ------------------------------------------------------
	# Print Patient
	@api.multi
	def print_patient_hc(self):
		print 
		print 'Print Patient'
		
		name = 'openhealth.report_patient_view'

		return self.env['report'].get_action(self, name)



# ----------------------------------------------------------- Update - Id Docs ------------------------------------------------------

	# Update Id Docs 
	@api.multi
	def update_id_docs(self):
		print 
		print 'Update Id Docs'

		# Search 
 		#patients = self.env['oeh.medical.patient'].search([
		#														('x_legacy', '!=', True), 
		#												],
															#order='write_date desc',
		#													#limit=1,
		#												)

 		count_1 = self.env['oeh.medical.patient'].search_count([
																('x_legacy', '!=', True), 
														],
															#order='write_date desc',
															#limit=1,
														)
 		count_2 = self.env['oeh.medical.patient'].search_count([
																('x_legacy', '=', True), 
														],
															#order='write_date desc',
															#limit=1,
														)
 		print count_1 
 		print count_2





# ----------------------------------------------------------- CRUD ------------------------------------------------------

	# Create 
	@api.model
	def create(self,vals):
		#print 
		#print 'CRUD - Patient - Create'
		#print 
	

		#if 'name' in vals:
		if 'name' in vals 	and 	'x_first_name' in vals  	and  'x_last_name' in vals:

			name = vals['name']
			#print name 

			if name == False: 

				# Name 
				#print 'Name'
				last_name = vals['x_last_name']
				first_name = vals['x_first_name']

				#name = lib.strip_accents(last_name.upper() + ' ' + first_name.upper()) 
				name = last_name.upper() + ' ' + first_name.upper()
				
				vals['name'] = name 



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


		# Date record 
		if res.x_date_record == False: 
			res.x_date_record = res.create_date




		# Name 
		#res.name = lib.strip_accents(res.x_last_name.upper() + ' ' + res.x_first_name.upper()) 


		# Check 
		chk._check_name(res)
		

		return res
	# CRUD - Create 

