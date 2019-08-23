# -*- coding: utf-8 -*-
"""
		Patient

 		Created: 		26 Aug 2016
		Last up: 		28 Apr 2019
"""
from __future__ import print_function
from openerp import models, fields, api
from . import pat_vars
from . import pat_funcs
from . import chk_patient
from openerp.addons.openhealth.models.libs import count_funcs

from openerp import _
from openerp.exceptions import Warning as UserError

class Patient(models.Model):
	"""
	Patient Class. 
	Inherits OeHealth Patient Class.

	This is a very dangerous thing to do. Should NEVER be done:

	# Container
	#container_id = fields.Many2one(
	#	'openhealth.container',
	#	ondelete='cascade',		# Very Dangerous. When Container is removed, Patient is removed.
	#)
	"""
	_inherit = 'oeh.medical.patient'

	_order = 'x_id_code desc'

	_description = 'Patient'


# ----------------------------------------------------------- First Level - Buttons ---------------------------------------------

# ----------------------------------------------------------- Open Treatment - Button ----------------------
	@api.multi
	def open_treatment(self):
		"""
		Open Treatment Button
		"""

		# Validate
		self.validate()


		# Search
		treatment = self.env['openhealth.treatment'].search([
																('patient', '=', self.id),
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



# ----------------------------------------------------------- Generate Estado de Cuenta - Button ----------------------
	# Generate
	@api.multi
	def generate_order_report(self):
		"""
		Estado de Cuenta.
		"""

		# Validate
		self.validate()


		# Clean
		self.remove_order_report()

		# Create
		self.order_report_nex = self.create_order_report()
		res_id = self.order_report_nex.id

		# Update
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



# ----------------------------------------------------------- Print Patient HC - Button ------------------
	# Print Patient
	@api.multi
	def print_patient_hc(self):
		"""
		Print Patient HC - Button
		"""

		# Validate
		self.validate()


		name = 'openhealth.report_patient_view'
		return self.env['report'].get_action(self, name)


# ----------------------------------------------------------- Deactivate Patient - Button --------------------------
	# Deactivate
	@api.multi
	def deactivate_patient(self):
		"""
		Deactivate Patient - Button
		"""
		self.active = False
		self.partner_id.active = False

# ----------------------------------------------------------- Activate Patient - Button ----------------------------
	# Activate Patient
	@api.multi
	def activate_patient(self):
		"""
		Activate Patient - Button
		"""
		self.active = True
		self.partner_id.active = True



# ----------------------------------------------------------- Validate - Button -----------
	@api.multi
	def validate(self):
		"""
		Just a wrapper
		"""
		print()
		print('Wrapper')





# ----------------------------------------------------------- Second Level - Implementation ---------------------------------------------

# ----------------------------------------------------------- Estado de Cuenta --------------------

	# Relational
	order_report_nex = fields.Many2one(
			'openhealth.order.report.nex',
			string="Estado de cuenta",
		)


	# Remove
	@api.multi
	def remove_order_report(self):
		"""
		high level support for doing this and that.
		"""
		print()
		print('Remove Order Report')
		#self.order_report_nex = False
		self.order_report_nex.unlink()		# This !
	# remove_order_report


	# Create
	@api.multi
	def create_order_report(self):
		"""
		high level support for doing this and that.
		"""
		print()
		print('Create Order Report')
		name = 'EC - ' + self.partner_id.name
		order_report_id = self.env['openhealth.order.report.nex'].create({
																			'name': name,
																			'patient': self.id,
																			'partner_id': self.partner_id.id,
																		}).id
		#print name 			# Warning - Generates Error in Prod. Because of Latin chars (ie Ñ).
		return order_report_id
	# create_order_report







# ----------------------------------------------------------- Constraints - Sql -------------------
	# Uniqueness constraints for:
	# 	Name, Id Code (Nr de Historia), Id Doc (Documento de Identidad)
	_sql_constraints = [
							('name_unique', 'Check(1=1)', 'SQL Warning: name must be unique !'),
							('x_id_code_unique', 'Check(1=1)', 'SQL Warning: x_id_code must be unique !'),
							('x_id_doc_unique', 'Check(1=1)', 'SQL Warning: x_id_doc must be unique !'),
						]



# ----------------------------------------------------------- Constraints Python - Important ------

	# Id doc - Documento Identidad
	@api.constrains('x_id_doc')
	def check_x_id_doc(self):
		"""
		high level support for doing this and that.
		"""
		chk_patient.check_x_id_doc(self)



	# Ruc
	@api.constrains('x_ruc')
	def check_x_ruc(self):
		"""
		Check Ruc
		"""
		chk_patient.check_x_ruc(self)

	# Check Name
	@api.constrains('name')
	def check_name(self):
		"""
		Check Name
		"""
		chk_patient.check_name(self)

	# Check - Hr History
	@api.constrains('x_id_code')
	def _check_x_id_code(self):
		"""
		Check Id Code
		"""
		chk_patient.check_x_id_code(self)




# ----------------------------------------------------------- Id Doc ------------------------------
	# Id Document
	x_id_doc = fields.Char(
			'Nr. Doc.',
			#required=True,
		)

	# Id Document Type
	x_id_doc_type = fields.Selection(

			#selection=pat_vars._id_doc_type_list,
			selection=pat_vars.get_id_doc_type_list(),

			string='Tipo de documento',
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
			#record.x_id_doc_type_code = pat_vars._dic_id_doc_code[record.x_id_doc_type]
			record.x_id_doc_type_code = pat_vars.get_dic_id_doc_code(record.x_id_doc_type)




# ----------------------------------------------------------- Mode Admin --------------------------
	# Mode Admin
	x_admin_mode = fields.Boolean(
			'Modo Admin',
		)


# ----------------------------------------------------------- Test - Fields -----------------------
	x_test_case = fields.Char(
			'Test Case',
		)

	x_test = fields.Boolean(
			'Test',
		)






# ----------------------------------------------------------- QC ----------------------------------
	# Data complete
	x_data_complete = fields.Boolean(
			string="Data Complete",

			compute='_compute_x_data_complete',
	)

	@api.multi
	def _compute_x_data_complete(self):
		for record in self:
			#if record.x_legacy or record.x_treatment_count > 0:
			#	record.x_data_complete = True
			#else:
			#	record.x_data_complete = False

			record.x_data_complete = (record.x_legacy or record.x_treatment_count > 0)



	# Legacy
	x_legacy = fields.Boolean(
			string="Legacy",

			compute='_compute_x_legacy',
	)

	@api.multi
	def _compute_x_legacy(self):
		for record in self:
			if record.x_counter < 13963:
				record.x_legacy = True



	# Counter
	x_counter = fields.Integer(
			string="Counter",

			compute='_compute_x_counter',
	)

	@api.multi
	def _compute_x_counter(self):
		for record in self:
			if record.x_id_code != False:
				record.x_counter = str(record.x_id_code)




# ----------------------------------------------------------- HC Number ---------------------------
	# Default - HC Number
	@api.model
	def _get_default_id_code(self):

		name_ctr = 'emr'

 		counter = self.env['openhealth.counter'].search([
																('name', '=', name_ctr),
														],
															#order='write_date desc',
															#limit=1,
														)

		# Manage Exception
		try:
			counter.ensure_one()

	 		# Init
	 		prefix = counter.prefix
	 		separator = counter.separator
	 		padding = counter.padding
	 		value = counter.value

			name = count_funcs.get_name(self, prefix, separator, padding, value)

			return name

		except:
			#print("An exception occurred")
			msg = "ERROR: Record Must be One."
			#class_name = type(counter).__name__
			#obj_name = counter.name
			#msg =  msg + '\n' + class_name + '\n' + obj_name
			msg =  msg 

			raise UserError(_(msg))




	# NC Number
	x_id_code = fields.Char(
			'Nr Historia Médica',

			#default=_get_default_id_code,
		)



# ----------------------------------------------------------- Primitives - Redefined --------------

	# Allergies
	x_allergies = fields.Many2one(
			'openhealth.allergy',
			string="Alergias",
			required=False,
		)

	# Stree2 Char - If Province
	street2_char = fields.Char(
			string="Distrito Prov.",
			required=False,
		)



# ----------------------------------------------------------- Legacy ------------------------------

	# Date created
	x_date_created = fields.Date(
			string="Fecha de Apertura",
			default=fields.Date.today,
			#readonly = True,
			required=False,
		)

	x_date_record = fields.Datetime(
			string='Fecha Registro',
		)

	x_district = fields.Char(
			string='Distrito L',
		)







# ----------------------------------------------------------- Personal - Hard wired to Partner ----


# ----------------------------------------------------------- Personal - 2 ------------------------
	# Nationality
	x_nationality = fields.Selection(
			[
				('peruvian', 'Peruano'),
				('other', 'Otro'),
			],
			'Nacionalidad',
			default="peruvian",
			required=True,
		)


	# First Impression
	x_first_impression = fields.Selection(
			[
				('positive', 'Positivo'),
				('normal', 'Normal'),
				('insecure', 'Inseguro'),
				('asking', 'Preguntón'),
				('barterint', 'Regateador'),
				('agressive', 'Agresivo'),
				('psychiatric', 'Psiquiátrico'),
				('lawyer', 'Abogado'),
				#('other', 'Otro'),
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
															('patient_name', '=', record.name),
														],
														#order='appointment_date desc',
														limit=1,)

			if x_card.name != False:
				record.x_vip = True



	# Vip Card
	x_card = fields.Many2one(
			'openhealth.card',
			string="Tarjeta VIP",

			compute='_compute_x_card',
		)

	#@api.multi
	@api.depends('name')
	def _compute_x_card(self):
		for record in self:
			x_card = record.env['openhealth.card'].search([
															('patient_name', '=', record.name),
														],
														#order='appointment_date desc',
														limit=1,)
			record.x_card = x_card




# ----------------------------------------------------------- Autofill ----------------------------

	# Open Treatment
	@api.multi
	def autofill(self):
		"""
		high level support for doing this and that.
		"""

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
 		if allergy_id != False:
			self.x_allergies = allergy_id

		self.x_id_doc_type = 'dni'
		self.x_id_doc = '09817195'



# ----------------------------------------------------------- Autofill ----------------------------

	# Autofill
	x_autofill = fields.Boolean(
			string="Autofill",
			default=False,
		)



# ----------------------------------------------------------- Relational --------------------------

	# Treatments
	treatment_ids = fields.One2many(
			'openhealth.treatment',
			'patient',
			string="Tratamientos"
		)


# ----------------------------------------------------------- Re-definitions ----------------------

	# Age
	age = fields.Char(
			string="Edad",
		)

	# Sex
	sex = fields.Selection(

			#selection=pat_vars._sex_type_list,
			selection=pat_vars.get_sex_type_list(),

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
			string='Ocupación',
			placeholder='',
			#required=True,
		)



# ----------------------------------------------------------- Fields ------------------------------

	# First
	x_first_name = fields.Char(
		string="Nombres",
		required=True,
		default='',
	)


	# Last
	x_last_name = fields.Char(
		string="Apellidos",
		required=True,
		default='',
	)


	# Active
	x_active = fields.Boolean(
			string="Activa",
			default=True,
			#readonly = True,
			required=True,
			)

	x_first_contact = fields.Selection(

			#selection=pat_vars._first_contact_list,
			selection=pat_vars.get_first_contact_list(),

			string='¿ Cómo se enteró ?',
			#required=True,
		)

	x_country_residence = fields.Many2one(
			'res.country',
			string='País de residencia',
			default='',
		)

	x_education_level = fields.Selection(

			#selection=pat_vars._education_level_type,
			selection=pat_vars.get_education_level_type(),

			string='Grado de instrucción',
		)


	# Caregiver
	x_caregiver_last_name = fields.Char(
			string='Apellidos',
		)

	x_caregiver_first_name = fields.Char(
			string='Nombres',
		)

	x_caregiver_dni = fields.Char(
			string="DNI",
		)

	x_caregiver_relation = fields.Selection(

			#selection=pat_vars._FAMILY_RELATION,
			selection=pat_vars.get_FAMILY_RELATION(),

			string='Parentesco',
			default='none',
		)

	phone_3 = fields.Char(
		string="Teléfono",
		required=False,
		)



	# Control docs
	x_control_dni_copy = fields.Boolean(
			string='Copia de DNI',
			default=False
			)

	x_control_informed_consent = fields.Boolean(
			string='Consentimiento informado',
			default=False
			)

	x_control_visia_record = fields.Boolean(
			string='Registro VISIA pre-procedimiento',
			default=False
			)

	x_control_photo_record = fields.Boolean(
			string='Registro fotográfico pre-procedimiento',
			default=False
			)

	x_control_treatment_signed_patient = fields.Boolean(
			string='Copia de información de tratamiento Láser firmada por el paciente',
			default=False
			)

	x_control_postlaser_instructions_signed = fields.Boolean(
			string='Copia de indicaciones post-Láser firmado por el paciente',
			default=False
			)

	x_control_treatment_signed_doctor = fields.Boolean(
			string='Informe de tratamiento Láser firmado por el doctor',
			default=False
			)

	x_control_clinical_analsis = fields.Boolean(
			string='Análisis clínicos',
			default=False
			)

	x_control_control_pictures = fields.Boolean(
			string='Fotos de controles',
			default=False
			)

	x_control_control_pictures_visia = fields.Boolean(
			string='Fotos de controles con VISIA',
			default=False
			)

	x_control_physician = fields.Many2one(
			'oeh.medical.physician',
			string="Médico responsable del control",
			)

	x_date_consent = fields.Date(
			string="Fecha de consentimiento informado",
			default=fields.Date.today,
		)


# ----------------------------------------------------------- Treatment Count ---------------------

	# Treatment count
	x_treatment_count = fields.Integer(
			string="Nr TRATAMIENTOS",
			default=0,

			compute='_compute_x_treatment_count',
		)

	@api.multi
	def _compute_x_treatment_count(self):
		for record in self:
			count = 0
			#for tr in record.treatment_ids:
			for _ in record.treatment_ids:
				count = count + 1
			record.x_treatment_count = count








# ----------------------------------------------------------- On Changes --------------------------

	# Ternary If
	#isApple = True if fruit == 'Apple' else False

	# Autofill
	@api.onchange('x_autofill')
	def _onchange_x_autofill(self):
		#self.autofill() if self.x_autofill == True else 'don'
		if self.x_autofill:
			self.autofill()


	# Street2 ?
	@api.onchange('street2_char')
	def _onchange_street2_char(self):
		self.street2 = self.street2_char

	# Zip  Street2
	@api.onchange('street2_sel')
	def _onchange_street2_sel(self):

		#self.street2 = pat_vars.zip_dic_inv[self.street2_sel]
		self.street2 = pat_vars.get_zip_dic_inv(self.street2_sel)
		
		self.zip = self.street2_sel

	# Street
	@api.onchange('street')
	def _onchange_street(self):
		self.street = self.street.strip().title() if self.street != False else ''



# ----------------------------------------------------------- On Changes - Name -------------------

	# Only format last and first. Do not assign Name.
	# This is done in CRUD.


	# Must have two or more last names
	@api.onchange('x_last_name')
	def _onchange_x_last_name_test(self):
		#return lib.test_for_one_last_name(self, self.x_last_name) if self.x_last_name else 'don'
		return pat_funcs.test_for_one_last_name(self, self.x_last_name) if self.x_last_name else 'don'


	# Name
	@api.onchange('x_last_name', 'x_first_name')
	def _onchange_x_last_name(self):
		#print 'On Change'
		#print 'Last First Names'

		#self.name = lib.strip_accents(self.x_last_name.upper() + ' ' + \
																# self.x_first_name.upper()) if self.x_last_name and self.x_first_name else 'don'

		if self.x_last_name:
			#self.x_last_name = lib.remove_whitespaces(self.x_last_name.upper())
			self.x_last_name = pat_funcs.remove_whitespaces(self.x_last_name.upper())

		if self.x_first_name:
			#self.x_first_name = lib.remove_whitespaces(self.x_first_name.upper())
			self.x_first_name = pat_funcs.remove_whitespaces(self.x_first_name.upper())





# ----------------------------------------------------------- Test - Computes----------------------

	# Computes
	def test_computes(self):
		"""
		high level support for doing this and that.
		"""
		print()
		print('Patient - Computes')
		# Partner
		print()
		print('Computes - Partner')
		print(self.partner_id.city_char)
		print(self.partner_id.x_address)
		print(self.partner_id.x_vip)
		# Patient
		print()
		print('Computes')
		print(self.name)
		print(self.x_treatment_count)
		print(self.x_vip)
		print(self.x_card)
		print(self.x_legacy)
		print(self.x_counter)


	# Actions
	def test_actions(self):
		"""
		high level support for doing this and that.
		"""
		#print
		#print 'Patient - Actions'
		self.deactivate_patient()
		self.activate_patient()
		self.open_treatment()
		self.generate_order_report()
		if self.x_test:
			self.autofill()


	# Actions
	def test_services(self):
		"""
		high level support for doing this and that.
		"""
		#print
		#print 'Patient - Services'
		for treatment in self.treatment_ids:
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



# ----------------------------------------------------------- Test --------------------------------
	# Test - Integration
	@api.multi
	def test(self):
		"""
		high level support for doing this and that.
		"""
		print()
		print('Patient - Test')

		# Test Unit
		self.test_computes()
		self.test_actions()
		self.test_services()

		# Test Cycle - Dep ?
		#self.test_cycle()
	# test




# ----------------------------------------------------------- Const - Print -----------------------
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



# ----------------------------------------------------------- CRUD --------------------------------
	# Create
	@api.model
	def create(self, vals):
		#print
		#print 'CRUD - Patient - Create'

		if 'name' in vals and 'x_first_name' in vals and 'x_last_name' in vals:

			name = vals['name']
			#print name

			#if name == False:
			if not name:

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
		#if res.x_date_record == False:
		if not res.x_date_record:
			res.x_date_record = res.create_date


		return res
	# CRUD - Create
