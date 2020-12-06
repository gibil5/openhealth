# -*- coding: utf-8 -*-
"""
	*** Patient

	Created: 			26 aug 2016
	Last up: 			 5 dec 2020

	- Is this a singleton (1180 lines) ?
	- Reduce third party dependencies (oehealth).
	- Eliminate crossed dependencies.

	Data flow:
	- One2many (two way)
		Sales
		Treatments
		Consultations
		Procedures
		Controls
	
	- Many2one (one way)
		Configurator 
		Vip card
		User
		Country
		Physician
		Origin (marketing)
		Estado de cuenta
		Allergies
"""
from __future__ import print_function
from openerp import models, fields, api

from . import pat_vars
from . import pat_funcs
from . import chk_patient
from . import count_funcs

class Patient(models.Model):
	"""
	Patient Class
	- Oehealth free.

	- No black boxes (not depending on oehealth).
	- Object oriented.
	- Using pure functions in external libs.
	- Unit testing, through validation buttons (checks presence and validity).
	- Compatible with python3.
	- Using quality checking (pylint).
	"""
	#_inherit = 'oeh.medical.patient'
	_name = 'oeh.medical.patient'
	_inherits = {'res.partner': 'partner_id'}
	_description = 'Patient class'
	_order = 'x_id_code desc'

# ------------------------------------------------------------- Relational -----

# ------------------------------------------------------------- One2many -----
	# Treatments
	treatment_ids = fields.One2many(
			'openhealth.treatment',
			'patient',
			string="Tratamientos",
		)

	# Sales
	sale_ids = fields.One2many(
			'openhealth.patient.sale',
			'patient_id',
			string="Ventas",
		)

	# controls
	control_ids = fields.One2many(
			'openhealth.patient.control',
			'patient_id',
			string="Controles",
		)

	# procedures
	procedure_ids = fields.One2many(
			'openhealth.patient.procedure',
			'patient_id',
			string="Procedimientos",
		)

	# consultations
	consultation_ids = fields.One2many(
			'openhealth.patient.consultation',
			'patient_id',
			string="Consultas",
		)

# ------------------------------------------------------------- Many2one -----
	# User
	user_id = fields.Many2one(
		'res.users',
		string='Creado por',
		track_visibility='onchange',
		default=lambda self: self.env.user,
	)

	# Country
	x_country_residence = fields.Many2one(
			'res.country',
			string='País de residencia',
			default='',
		)

	# Physician
	x_control_physician = fields.Many2one(
			'oeh.medical.physician',
			string="Médico responsable del control",
			)

	# Marketing
	origin = fields.Many2one(
			'openhealth.patient.origin',
			string='Primer Contacto',
		)

	# Estado de cuenta
	order_report_nex = fields.Many2one(
			'openhealth.order.report.nex',
			string="Estado de cuenta",
		)

	# Allergies
	x_allergies = fields.Many2one(
			'openhealth.allergy',
			string="Alergias",
			required=False,
		)

	# Configurator
	def _get_default_configurator(self):
		return self.env['openhealth.configurator.emr'].search([],limit=1,)

	configurator = fields.Many2one(
			'openhealth.configurator.emr',
			string="Configuracion",
			default=_get_default_configurator,
		)

	# Vip Card
	x_card = fields.Many2one(
			'openhealth.card',
			string="Tarjeta VIP",
			compute='_compute_x_card',
		)
	@api.depends('name')
	def _compute_x_card(self):
		for record in self:
			record.x_card = record.env['openhealth.card'].search([('patient_name', '=', record.name),],limit=1,)

# --------------------------------------------------------------------- Oehealth ---
	SEX = [
		('Male', 'Male'),
		('Female', 'Female'),
	]

	name = fields.Char()

	identification_code = fields.Char('Patient ID', size=256, help='Patient Identifier provided by the Health Center', readonly=True)

	dob = fields.Date('Date of Birth')

	#age = fields.function(_patient_age, method=True, type='char', size=32, string='Patient Age',help="It shows the age of the patient in years(y), months(m) and days(d).\nIf the patient has died, the age shown is the age at time of death, the age corresponding to the date on the death certificate. It will show also \"deceased\" on the field")
	age = fields.Char()

	sex = fields.Selection(SEX, 'Sex', select=True)

# -------------------------------------------------------------- Primitives ----
	# First
	x_first_name = fields.Char(
		#string="Nombres",
		string="Nombres (obligatorio)",
		required=True,
		default='',
	)

	# Last
	x_last_name = fields.Char(
		#string="Apellidos",
		string="Apellidos (obligatorio)",
		required=True,
		default='',
	)

# --------------------------------------------------------------------- Ruc ----
	x_ruc_available = fields.Boolean(
			'RUC',
			default=False,
		)

	x_firm_address = fields.Char(
			'Direccion de la Empresa',  		# For the Patient
		)

# -------------------------------------------------------------- Caregiver -----
	# Caregiver
	x_caregiver = fields.Boolean(
			'Acompañante',
			default=False,
		)

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
			selection=pat_vars.get_FAMILY_RELATION(),
			string='Parentesco',
			default='none',
		)

# ------------------------------------------------------------------ Fields ----
	# Active
	x_active = fields.Boolean(
			string="Activa",
			default=True,
			required=True,
			)

	x_education_level = fields.Selection(
			selection=pat_vars.get_education_level_type(),
			string='Grado de instrucción',
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


	x_date_consent = fields.Date(
			string="Fecha de consentimiento informado",
			default=fields.Date.today,
		)

# ----------------------------------------------- State --------------------------------
	# Alta
	discharged = fields.Boolean(
			'Alta',
			default=False,
		)

	# State
	state = fields.Selection(
			[
				('empty', 'Inicio'),
				('treatment', 'Tratamiento'),
				('done', 'Alta'),
			],
			string="Estado",
			compute='_compute_state',
	)
	@api.multi
	def _compute_state(self):
		for record in self:
			if record.x_treatment_count > 0:
				record.state = 'treatment'
			else:
				record.state = 'empty'

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
			for _ in record.treatment_ids:
				count = count + 1
			record.x_treatment_count = count

	# Data complete
	x_data_complete = fields.Boolean(
			string="Data Complete",

			compute='_compute_x_data_complete',
	)
	@api.multi
	def _compute_x_data_complete(self):
		for record in self:
			record.x_data_complete = (record.x_legacy or record.x_treatment_count > 0)

# ------------------------------------------------------------- Marketing ------
	# Vip
	x_vip = fields.Boolean(
		string="VIP",
		default=False,
		compute='_compute_x_vip',
	)
	@api.depends('x_card')
	def _compute_x_vip(self):
		"""
		The patient is Vip if there is a Vip card, with his name
		"""
		for record in self:
			record.x_vip = False
			#x_card = record.env['openhealth.card'].search([
			#												('patient_name', '=', record.name),
			#											],
														#order='appointment_date desc',
			#											limit=1,)
			#if x_card.name != False:
			#	record.x_vip = True


# ------------------------------------------------------------- Marketing ------
	x_first_contact = fields.Selection(
			selection=pat_vars._first_contact_list,
			string='¿ Cómo se enteró ?',
		)

# ----------------------------------------------- Nrs --------------------------
	# Nr Sales
	nr_sales = fields.Integer(
			string="Nr Ventas",
			#compute="_compute_nr_sales",
	)
	#@api.multi
	#def _compute_nr_sales(self):
	#	for record in self:
	#		record.nr_sales = self.env['sale.order'].search_count([
	#																('state', '=', 'sale'),
	#																('patient', '=', record.name),
	#															])

	# Nr Consultations
	nr_consultations = fields.Integer(
			string="Nr Consultas",
			#compute="_compute_nr_consultations",
	)
	#@api.multi
	#def _compute_nr_consultations(self):
	#	for record in self:
	#		record.nr_consultations = self.env['openhealth.consultation'].search_count([
	#																					('patient', '=', record.name),
	#																])

	# Nr Procedures
	nr_procedures = fields.Integer(
			string="Nr Procs",
			#compute="_compute_nr_procedures",
	)
	#@api.multi
	#def _compute_nr_procedures(self):
	#	for record in self:
	#		record.nr_procedures = self.env['openhealth.procedure'].search_count([
	#																				('patient', '=', record.name),
	#																])

# ---------------------------------------------------------- Get Name Code -----
	def get_name_code(self):
		"""
		Get name code - used by
		"""
		words = self.name.upper().split()
		code = words[0] + '_' + words[1]
		code = code.replace('.', '')
		return code


# ----------------------------------------------------------- HC Number ---------------------------
	# Default - HC Number
	@api.model
	def _get_default_id_code(self):
		print()
		print('Get Default Id Code')

		name_ctr = 'emr'

		counter = self.env['openhealth.counter'].search([
																('name', '=', name_ctr),
														],
															#order='write_date desc',
															#limit=1,
														)

		if counter.name not in [False]:

			# Init
			prefix = counter.prefix
			separator = counter.separator
			padding = counter.padding
			value = counter.value
			#name = count_funcs.get_name(self, prefix, separator, padding, value)
			name = count_funcs.get_name(prefix, separator, padding, value)
			return name

	# NC Number
	x_id_code = fields.Char(
			'Nr Historia Médica',

			default=_get_default_id_code,
		)



# ----------------------------------------------------------- First Level - Buttons ---------------------------------------------

# ----------------------------------------------------------- Open Treatment - Button ----------------------
	@api.multi
	def create_budget(self):
		"""
		Create Budget Button
		"""
		return {
					# Mandatory
					'type': 'ir.actions.act_window',
					'name': 'Open Budget Current',
					# Model
					'res_model': 'sale.order',
					#'res_id': treatment.id,
					# Views
					"views": [[False, "form"]],
					'view_mode': 'form',
					#'target': 'current',
					'target': 'new',
					'flags': {
							#'form': {'action_buttons': True, }
							'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
					},
					'context':   {
									'default_patient': self.id,
					}
			}
	# create_budget

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

		counter = self.env['openhealth.counter'].search([
															('name', '=', 'emr'),
														],
														#order='appointment_date desc',
														limit=1,)
		if counter.name != False:
			#counter.synchro()
			counter.decrease()

# ----------------------------------------------------------- Activate Patient - Button ----------------------------
	# Activate Patient
	@api.multi
	def activate_patient(self):
		"""
		Activate Patient - Button
		"""
		self.active = True
		self.partner_id.active = True


# ----------------------------------------------------------- Second Level - Implementation ---------------------------------------------

# ----------------------------------------------------------- Estado de Cuenta --------------------


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

# ------------------------------------------------------- Constraints - Sql ----
	# Uniqueness constraints for:
	# 	Name, Id Code (Nr de Historia), Id Doc (Documento de Identidad)
	_sql_constraints = [
							('name_unique', 'Check(1=1)', 'SQL Warning: name must be unique !'),
							('x_id_code_unique', 'Check(1=1)', 'SQL Warning: x_id_code must be unique !'),
							('x_id_doc_unique', 'Check(1=1)', 'SQL Warning: x_id_doc must be unique !'),
						]

# ------------------------------------------ Constraints Python - Important ----
	# Id doc - Documento Identidad
	@api.constrains('x_id_doc')
	def check_x_id_doc(self):
		"""
		Check id doc
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
		)

	# Id Document Type
	x_id_doc_type = fields.Selection(
			selection=pat_vars.get_id_doc_type_list(),
			string='Tipo de documento',
		)

	# Id Document Type
	x_id_doc_type_code = fields.Char(
			string='Tipo de documento Cod',

			compute='_compute_x_id_doc_type_code',
		)
	@api.multi
	def _compute_x_id_doc_type_code(self):
		for record in self:
			record.x_id_doc_type_code = pat_vars.get_dic_id_doc_code(record.x_id_doc_type)

# ----------------------------------------------------------- Mode Admin --------------------------
	# Mode Admin
	x_admin_mode = fields.Boolean(
			'Modo Admin',
		)

# ----------------------------------------------------------- QC ---------------
	# test
	x_test = fields.Boolean(
			'Test',
		)

	# Legacy
	x_legacy = fields.Boolean(
			string="Legacy",

			compute='_compute_x_legacy',
	)
	@api.multi
	def _compute_x_legacy(self):
		for record in self:
			#if (record.x_counter < 13963) and (record.configurator.name in ['Lima']):
			#	record.x_legacy = True
			#else:
			#	record.x_legacy = False
			record.x_legacy = bool((record.x_counter < 13963) and (record.configurator.name in ['Lima']))

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

# ----------------------------------------------------------------- Legacy -----
	# Date created
	x_date_created = fields.Date(
			string="Fecha de Apertura",
			default=fields.Date.today,
			required=False,
		)

	x_date_record = fields.Datetime(
			string='Fecha Registro',
		)

	x_district = fields.Char(
			string='Distrito L',
		)

# ----------------------------------------------------------- Primitives - Redefined --------------

	# Stree2 Char - If Province
	street2_char = fields.Char(
			string="Distrito Prov.",
			required=False,
		)

# ---------------------------------------- Personal - Hard wired to Partner ----

# ----------------------------------------------------------- Personal - 2 -----
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
			],
			string="Primera impresión",
			default='normal',
			required=True,
		)

# ----------------------------------------------------------- Autofill ---------
	@api.multi
	def autofill(self):
		"""
		Autofill
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
		self.function = 'Ingeniero'
		self.x_education_level = 'university'
		self.x_first_impression = 'normal'
		self.sex = 'Male'
		self.x_id_doc_type = 'dni'
		self.x_id_doc = '09817194'
		self.x_first_contact = 'website'
		self.street2_sel = 41
		self.street = 'Av. San Borja Norte 610'

# ----------------------------------------------------------------- Autofill ---
	# Autofill
	x_autofill = fields.Boolean(
			string="Autofill",
			default=False,
		)

# ----------------------------------------------------------- Re-definitions ---
	# Age
	age = fields.Char(
			string="Edad",
		)

	# Sex
	sex = fields.Selection(
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
	function = fields.Selection(
			selection=pat_vars._function_list,
			string='Ocupación',
			placeholder='',
		)

# -------------------------------------------------------------- On Changes ----
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
		self.street2 = pat_vars.get_zip_dic_inv(self.street2_sel)
		self.zip = self.street2_sel

	# Street
	@api.onchange('street')
	def _onchange_street(self):
		self.street = self.street.strip().title() if self.street != False else ''

# -------------------------------------------------------- On Changes - Name ---
	# Only format last and first. Do not assign Name. This is done in CRUD.

	# Must have two or more last names
	@api.onchange('x_last_name')
	def _onchange_x_last_name_test(self):
		return pat_funcs.test_for_one_last_name(self, self.x_last_name) if self.x_last_name else 'don'

	# Name
	@api.onchange('x_last_name', 'x_first_name')
	def _onchange_x_last_name(self):
		if self.x_last_name:
			self.x_last_name = pat_funcs.remove_whitespaces(self.x_last_name.upper())
		if self.x_first_name:
			self.x_first_name = pat_funcs.remove_whitespaces(self.x_first_name.upper())

# ----------------------------------------------------------- Const - Print ----
	# Dic - For report generation
	_dic = {
				False: 	'',
				# Sex
				'Male': 	'Masculino',
				'Female': 	'Femenino',
				# Education
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

# -------------------------------------------------------------------- CRUD ----
	# Create
	@api.model
	def create(self, vals):
		# Init
		if 'name' in vals and 'x_first_name' in vals and 'x_last_name' in vals:
			name = vals['name']
			if not name:
				last_name = vals['x_last_name']
				first_name = vals['x_first_name']
				name = last_name.upper() + ' ' + first_name.upper()
				vals['name'] = name

		# Put your logic before
		res = super(Patient, self).create(vals)
		# Put your logic after

		# Serial Number. Increase must be AFTER creation
		name_ctr = 'emr'
		counter = self.env['openhealth.counter'].search([
															('name', '=', name_ctr),
														],
														#order='write_date desc',
														limit=1,
														)
		counter.increase()		# Here !!!

		# Date record - dep ?
		#if not res.x_date_record:
		#	res.x_date_record = res.create_date

		return res
	# CRUD - Create


# ------------------------------------------------------- Update Name ------
	@api.multi
	def update_name(self):
		"""
		Update Name
		"""
		print()
		print('Update name')

		last_name = self.x_last_name

		first_name = self.x_first_name

		self.name = last_name.upper() + ' ' + first_name.upper()


# ------------------------------------------------------- Update Age ------
	@api.multi
	def update_age(self):
		"""
		Update age
		"""
		print()
		print('Update age')
		self.age = pat_funcs.compute_age_from_dates(self.dob)

# ------------------------------------------------------- Update Controls ------
	@api.multi
	def update_controls(self, model):
		"""
		Update Controls
		"""
		print()
		print('Update Controls')
		# Clean
		self.control_ids.unlink()

		# Search
		objs = self.env[model].search([
										('patient', 'in', [self.name]),
									])
		# Create
		for obj in objs:
			self.control_ids.create({
												'date': 		obj.evaluation_start_date,
												'patient': 		obj.patient.id,
												'doctor': 		obj.doctor.id,
												'state': 		obj.state,
												'product': 		obj.product.name,
												'family': 		obj.laser,
												'patient_id':	self.id,
												'res_id': 		obj.id,
												'res_model': 	obj._name,
							})

# ----------------------------------------------------------- Update Sales -----
	@api.multi
	def update_sales(self, model):
		"""
		Update Sales
		"""
		print()
		print('Update Sales')

		# Clean
		self.sale_ids.unlink()

		# Search
		orders = self.env[model].search([
											('patient', 'in', [self.name]),
											('state', 'in', ['sale']),
										])

		# Create
		for order in orders:
			self.sale_ids.create({
										'patient': 	order.patient.id,
										'doctor': 	order.x_doctor.id,
										'date': 	order.date_order,
										'state': 	order.state,
										'product': 	order.pl_product,
										'family': 	order.pl_family,
										'nr_lines': order.nr_lines,
										'amount': 	order.amount_total,
										'patient_id': self.id,
										'res_id': 	order.id,
										'res_model': order._name,
										})

# ---------------------------------------------------- Update Consultations ----
	@api.multi
	def update_consultations(self, model):
		"""
		Update Consultations
		"""
		print()
		print('Update Consultations')

		# Clean
		self.consultation_ids.unlink()

		# Search
		objs = self.env[model].search([
										('patient', 'in', [self.name]),
									])

		# Create
		for obj in objs:
			 self.consultation_ids.create({
												'patient': 		obj.patient.id,
												'doctor': 		obj.doctor.id,
												'date': 		obj.evaluation_start_date,
												'state': 		obj.state,
												'patient_id': self.id,
												'res_id': 		obj.id,
												'res_model': 	obj._name,
							})

# ------------------------------------------------------ Update Procedures -----
	@api.multi
	def update_procedures(self, model):
		"""
		Update Procedures
		"""
		print()
		print('Update Procedures')

		# Clean
		self.procedure_ids.unlink()

		# Search
		objs = self.env[model].search([
										('patient', 'in', [self.name]),
									])

		# Create
		for obj in objs:
			self.procedure_ids.create({
													'patient': 		obj.patient.id,
													'doctor': 		obj.doctor.id,
													'date': 		obj.evaluation_start_date,
													'state': 		obj.state,
													'product': 		obj.product.name,
													'family': 		obj.pl_laser,
													'patient_id': self.id,
													'res_id': 		obj.id,
													'res_model': 	obj._name,
												})

# -------------------------------------------------------------- Update Nr -----
	@api.multi
	def update_nr_ofs(self):
		"""
		Update Nr ofs
		"""
		print()
		print('Update Nr Ofs')

		# Nr Sales
		self.nr_sales = self.env['sale.order'].search_count([
																('state', '=', 'sale'),
																('patient', '=', self.name),
															])

		# Nr Consultations
		self.nr_consultations = self.env['openhealth.consultation'].search_count([
																					('patient', '=', self.name),
																				])

		# Nr Procs
		self.nr_procedures = self.env['openhealth.procedure'].search_count([
																				('patient', '=', self.name),
																			])

# --------------------------------------------------------------- Update -------
	@api.multi
	def update_nex(self):
		"""
		Update all macros.
		"""
		print()
		print('Update - nex')
		self.update_name()
		self.update_age()
		self.update_controls('openhealth.control')
		self.update_sales('sale.order')
		self.update_consultations('openhealth.consultation')
		self.update_procedures('openhealth.procedure')
		self.update_nr_ofs()

# -------------------------------------------------------------- Update all ----
	@api.multi
	def update_all(self):
		"""
		Update all patients.
		"""
		print()
		print('Update All')

		# Init
		model = 'oeh.medical.patient'

		# Search
		#patients = self.env[model].search([], order='x_date_record desc', limit=self.configurator.patient_limit)
		patients = self.env[model].search([], order='x_date_record desc')

		# Count
		count = 0
		for patient in patients:
			patient.update_nex()
			count = count + 1
		#print(count)

# -------------------------------------------------------- Validate - Button ---
	@api.multi
	def validate(self):
		"""
		Validates presence and validity.
		"""
		print()
		print('Validate')
