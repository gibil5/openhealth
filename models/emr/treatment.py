# -*- coding: utf-8 -*-
"""
	Treatment
	Created: 			26 aug 2016
	Last up: 	 		25 oct 2020

	From PgAdmin
	-------------
	SELECT * FROM public.sale_order;
	DELETE FROM public.sale_order WHERE partner_id = 391;
"""
from __future__ import print_function
import datetime
from openerp import models, fields, api
from openerp.addons.openhealth.models.libs import eval_vars
from openerp.addons.price_list.models.lib import test_funcs

from . import treatment_vars
from . import treatment_state
from . import pl_creates

from . import test_treatment

from . import reco_funcs
from . import action_funcs
from . import counter_objects
from . import search_objects

from . import tre_funcs

# --------------------------------------------------------------- Constants ----
_model_treatment = "openhealth.treatment"
_model_sale = "sale.order"
_model_consultation = "openhealth.consultation"
_model_action = "ir.actions.act_window"
_model_service = "openhealth.service_all"

# ------------------------------------------------------------------- Class ----
class Treatment(models.Model):
	"""
	Treatment class
	"""
	_name = _model_treatment
	_order = 'write_date desc'
	_description = 'Treatment'

# ------------------------------------------------------------------------------
	# Shopping cart
	shopping_cart_ids = fields.One2many(
		'price_list.cart_line',
		'treatment',
		string="Shopping Cart"
	)

# ------------------------------------------------------------ Services --------
	# all
	service_all_ids = fields.One2many(
		'openhealth.service_all',
		'treatment',
		string="Servicios All"
	)


# ----------------------------------------------------------- Primitive ---------------------------

# ----------------------------------------------------------- Process ----------
	# States
	READONLY_STATES = {
		'empty': 		[('readonly', False)],
	}

	# Patient
	patient = fields.Many2one(
		'oeh.medical.patient',
		string="Paciente",
		index=True,
		ondelete='cascade',
		readonly=True,
		states=READONLY_STATES,
	)

	# Physician
	physician = fields.Many2one(
		'oeh.medical.physician',
		string="Médico",
		index=True,
		readonly=False,
		states=READONLY_STATES,
	)

	chief_complaint = fields.Selection(
		selection=eval_vars._chief_complaint_list,
		string='Motivo de consulta',
		required=False,
		readonly=False,
	)

	start_date = fields.Date(
		string="Fecha inicio",
		default=fields.Date.today,
		readonly=True,
		states=READONLY_STATES,
	)

# ----------------------------------------------------------- Card ------------
	# Name
	name = fields.Char(
		string="Tratamiento #",
		compute='_compute_name',
	)
	@api.multi
	def _compute_name(self):
		se = '-'
		for record in self:
			record.name = 'TR' + se + record.patient.get_name_code() + se + record.physician.get_name_code()


	# Sex - Used by header
	patient_sex = fields.Char(
		string="Sexo",
		compute='_compute_patient_sex',
		#compute=lambda self: self.patient.sex[0]
	)
	@api.multi
	def _compute_patient_sex(self):
		for record in self:
			record.patient_sex = record.patient.sex[0] if record.patient.sex else False


	# Age
	patient_age = fields.Char(
		string="Edad",
		compute='_compute_patient_age',
	)
	@api.multi
	def _compute_patient_age(self):
		for record in self:
			record.patient_age = record.patient.age.split()[0] if record.patient.age else False


	# City - id
	patient_city = fields.Char(
		string="Lugar de procedencia",
		compute='_compute_patient_city',
	)
	@api.multi
	def _compute_patient_city(self):
		for record in self:
			record.patient_city = record.patient.city_char.title() if record.patient.city_char else False


	# Vip - id
	vip = fields.Boolean(
		string="VIP",
		compute='_compute_vip',
	)
	@api.multi
	def _compute_vip(self):
		for record in self:
			card = search_objects.SearchObjects(record.env['openhealth.card'], 'patient_name', record.patient.name)
			record.vip = True if card.get_name() else False


# ----------------------------------------------------------- Number ofs -------
	# Budgets - Consultations
	nr_budgets_cons = fields.Integer(
		string="Presupuestos Consultas",
		compute="_compute_nr_budgets_cons",
	)
	@api.multi
	def _compute_nr_budgets_cons(self):
		for record in self:
			obj = counter_objects.CounterObjects(self.env[_model_sale], record.id, 'draft', 'CONSULTA')
			record.nr_budgets_cons = obj.count()


	# Invoices - Consultations
	nr_invoices_cons = fields.Integer(
		string="Facturas Consultas",
		compute="_compute_nr_invoices_cons",
	)
	@api.multi
	def _compute_nr_invoices_cons(self):
		for record in self:
			obj = counter_objects.CounterObjects(self.env[_model_sale], record.id, 'sale', 'CONSULTA')
			record.nr_invoices_cons = obj.count()


	# Budgets - Proc
	nr_budgets_pro = fields.Integer(
		string="Presupuestos - Pro",
		compute="_compute_nr_budgets_pro",
	)
	@api.multi
	def _compute_nr_budgets_pro(self):
		for record in self:
			obj = counter_objects.CounterObjects(self.env[_model_sale], record.id, 'draft', 'procedure', 'x_family')
			record.nr_budgets_pro = obj.count()

	# Invoices - Proc
	nr_invoices_pro = fields.Integer(
		string="Facturas",
		compute="_compute_nr_invoices_pro",
	)
	@api.multi
	def _compute_nr_invoices_pro(self):
		for record in self:
			obj = counter_objects.CounterObjects(self.env[_model_sale], record.id, 'sale', 'procedure',  'x_family')
			record.nr_invoices_pro = obj.count()


	# Consultations
	nr_consultations = fields.Integer(
		string="Nr Consultas",
		compute="_compute_nr_consultations",
	)
	#@api.multi
	@api.depends('consultation_ids')
	def _compute_nr_consultations(self):
		for record in self:
			model = _model_consultation
			obj = counter_objects.CounterObjects(self.env[model], record.id)
			record.nr_consultations = obj.count_fast()

	# Procedures
	nr_procedures = fields.Integer(
		string="Procedimientos",
		compute="_compute_nr_procedures",
	)
	@api.multi
	def _compute_nr_procedures(self):
		for record in self:
			model = 'openhealth.procedure'
			obj = counter_objects.CounterObjects(self.env[model], record.id)
			record.nr_procedures = obj.count_fast()

	# Sessions
	nr_sessions = fields.Integer(
		string="Sesiones",
		compute="_compute_nr_sessions",
	)
	@api.multi
	def _compute_nr_sessions(self):
		for record in self:
			model = 'openhealth.session.med'
			obj = counter_objects.CounterObjects(self.env[model], record.id)
			record.nr_sessions = obj.count_fast()

	# Controls
	nr_controls = fields.Integer(
		string="Controles",
		compute="_compute_nr_controls",
	)
	@api.multi
	def _compute_nr_controls(self):
		for record in self:
			model = 'openhealth.control'
			obj = counter_objects.CounterObjects(self.env[model], record.id)
			record.nr_controls = obj.count_fast()

# ----------------------------------------------------------- Test ----------------------------------------------------
	x_test = fields.Boolean(
		'Test',
		default=False,
	)

# ----------------------------------------------------------- Pricelist Fields - Dummy --------------------------------
	report_product = fields.Many2one(
		'openhealth.container.pricelist',
		string="PROD",
	)

# ----------------------------------------------------------- Pricelist Fields - Test --------------------------------
	x_test_scenario = fields.Selection(
		selection=treatment_vars._test_scenario_list,
		string="Test Scenarios",
	)

	test_pricelist_2019 = fields.Boolean(
		'PL 2019',
		default=True,
	)

	test_pricelist_2018 = fields.Boolean(
		'PL 2018',
		default=False,
	)


# ----------------------------------------------------------- Price list  ------
	# Pricelist
	pricelist_id = fields.Many2one(
		'product.pricelist',
		string='Pricelist',
		readonly=True,
		compute='_compute_pricelist_id',
	)
	@api.multi
	def _compute_pricelist_id(self):
		for record in self:
			record.pricelist_id = record.patient.property_product_pricelist

# ----------------------------------------------------------- Manual ------------------------------
	# Override config
	override = fields.Boolean(
		default=False,
	)

	# Manual
	add_procedures = fields.Boolean(
		string="Control Manual",
		default=False,
	)

# ----------------------------------------------------------- Canonical ---------------------------
	# Space
	vspace = fields.Char(
		' ',
		readonly=True
	)

	# Active
	active = fields.Boolean(
		default=True,
	)

	# Closed
	treatment_closed = fields.Boolean(
		string="De Alta",
		default=False,
	)

# ----------------------------------------------------------- Vip in prog -------------------------

	# Vip in progress
	x_vip_inprog = fields.Boolean(
		string="Vip en progreso",
		default=False,
		compute='_compute_vip_inprog',
	)

	@api.multi
	def _compute_vip_inprog(self):
		for record in self:
			record.x_vip_inprog = False
			#nr_vip = self.env['openhealth.service.product'].search_count([
			#																('treatment', '=', record.id),
			#																('service', 'in', ['tarjeta vip', 'Tarjeta Vip', 'Tarjeta VIP', 'TARJETA VIP']),
																			#('state','=', 'draft'),
			#	])
			#if nr_vip > 0:
			#	record.x_vip_inprog = True


# ----------------------------------------------------------- Relational --------------------------
	consultation_ids = fields.One2many(
		'openhealth.consultation',
		'treatment',
		string="Consultas",
	)

	procedure_ids = fields.One2many(
		'openhealth.procedure',
		'treatment',
		string="Procedimientos",
	)

	session_ids = fields.One2many(
		'openhealth.session.med',
		'treatment',
		string="Sesiones",
	)

	control_ids = fields.One2many(
		'openhealth.control',
		'treatment',
		string="Controles",
	)

	# Orders
	order_ids = fields.One2many(
		'sale.order',
		'treatment',
		string="Presupuestos",
	)

	# Orders Procedures
	order_pro_ids = fields.One2many(
		'sale.order',
		'treatment',
		string="Presupuestos",
		domain=[],
	)

# ----------------------------------------------------------- Consultation Progress ---------------
	# Consultation progress
	consultation_progress = fields.Float(
		default=0,
		compute="_compute_progress",
	)

	@api.multi
	#@api.depends('consultation_ids')
	def _compute_progress(self):
		for record in self:
			for con in record.consultation_ids:
				record.consultation_progress = con.progress

# ----------------------------------------------------------- State -------------------------------
	# State
	state = fields.Selection(
		selection=treatment_vars._state_list,
		string='Estado',
		default='empty',
		compute="_compute_state",
	)

	@api.multi
	def _compute_state(self):
		verbose = False
		for record in self:
			obj = treatment_state.TreatmentState(record, verbose)
			record.state = obj.get_state()


# ----------------------------------------------------------- Number ofs - Services - Dep ? ---------------
	# Number of Services
	nr_services = fields.Integer(
		string="Servicios",
		compute="_compute_nr_services",
	)
	@api.multi
	def _compute_nr_services(self):
		for record in self:
			record.nr_services = self.env[_model_service].search_count([('treatment', '=', record.id),])


# ----------------------------------------------------------- Create Buttons  ----------
	@api.multi
	def btn_create_order_con(self):
		"""
		Create Order Consultation Standard - Medical
		One mode
		"""
		print()
		print('btn_create_order_con')

		# Init
		price_list = '2019'
		target = 'medical'

		order = pl_creates.create_order_con(self, target, price_list)

		# Open Order
		return action_funcs.open_order(order)


# ----------------------------------------------------- Create Consultations ---------------------------------------------

# ----------------------------------------------------- Create Consultation -----------------------
	# Create Consultation
	@api.multi
	def btn_create_consultation(self):
		"""
		Create consultation - Button
		"""
		print()
		print('OH - btn_create_consultation')

		# Init vars
		patient_id = self.patient.id
		treatment_id = self.id
		chief_complaint = self.chief_complaint

		# Doctor
		doctor = tre_funcs.get_actual_doctor(self)
		doctor_id = doctor.id
		if not doctor_id:
			doctor_id = self.physician.id

		# Date
		GMT = tre_funcs.Zone(0, False, 'GMT')
		evaluation_start_date = datetime.datetime.now(GMT).strftime("%Y-%m-%d %H:%M:%S")

		# Search
		consultation = self.env[_model_consultation].search([
																		('treatment', '=', self.id),
																],
																#order='appointment_date desc',
																limit=1,)

		# If Consultation not exist
		if not consultation.name:
			# Create
			consultation = self.env[_model_consultation].create({
																		'patient': patient_id,
																		'treatment': treatment_id,
																		'evaluation_start_date': evaluation_start_date,
																		'chief_complaint': chief_complaint,
																		'doctor': doctor_id,
													})

		return {
				# Mandatory
				'type': _model_action,
				'name': 'Open Consultation Current',
				# Window action
				'res_model': _model_consultation,
				#'res_id': consultation_id,
				'res_id': consultation.id,
				# Views
				"views": [[False, "form"]],
				'view_mode': 'form',
				'target': 'current',
				#'view_id': view_id,
				#'view_id': 'oeh_medical_evaluation_view',
				#"domain": [["patient", "=", self.patient.name]],
				#'auto_search': False,
				'flags': {
							'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
							#'form': {'action_buttons': True, }
						},
				'context':   {
								'search_default_treatment': treatment_id,
								'default_patient': patient_id,
								'default_doctor': doctor_id,
								'default_treatment': treatment_id,
								'default_evaluation_start_date': evaluation_start_date,
								'default_chief_complaint': chief_complaint,
				}
			}
	# btn_create_consultation

# ----------------------------------------------------------- Create Service ---------------------------
	@api.multi
	def btn_create_reco(self):
		"""
		Create Service
		Opens a new form. For Reco choice.
		"""
		print()
		print('OH - btn_create_reco')

		# Init
		res_id = self.id
		res_model = _model_treatment
		view_id = self.env.ref('openhealth.treatment_2_form_view').id

		# Open
		return {
			# Mandatory
			'type': _model_action,
			'name': 'Open Treatment Current',
			# Window action
			'priority': 1,
			'res_id': res_id,
			'res_model': res_model,
			#'view_id': view_id,
			# Views
			#"views": [[False, "form"]],
			"views": [[view_id, "form"]],
			'view_mode': 'form',
			'target': 'current',
			#"domain": [["patient", "=", self.patient.name]],
			#'auto_search': False,
			'flags': {
						#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
						'form': {'action_buttons': False, }
					},
			'context': {
						#'default_treatment': treatment_id,
					}
		}
	# btn_create_reco

# -----------------------------------------------------------  Create Order Procedure - 2019 -------------
	@api.multi
	def btn_create_order_pro(self):
		"""
		Create Order Procedure - 2019
		From Recommendations
		"""
		print('treatment - btn_create_order_pro')

		# Clear cart
		self.shopping_cart_ids.unlink()

		# Init
		#price_list = '2019'

		service_list = [
							self.service_all_ids,
							#self.service_product_ids,
							#self.service_co2_ids,
							#self.service_excilite_ids,
							#self.service_ipl_ids,
							#self.service_ndyag_ids,
							#self.service_quick_ids,
							#self.service_medical_ids,
							#self.service_cosmetology_ids,
							#self.service_gynecology_ids,
							#self.service_echography_ids,
							#self.service_promotion_ids,
		]
		
		# Create Cart
		for service_ids in service_list:
			for service in service_ids:
				print()
				print('Create cart')
				pl_creates.create_shopping_cart(self, self.env['product.product'], service, self.id)


		# Create Order
		print()
		print('Create order')
		#order = pl_creates.pl_create_order(self)
		order = pl_creates.create_order(self)
		#print(order)

		# Open Order
		return action_funcs.open_order(order)

	# btn_create_order_pro

# ----------------------------------------------------------- Create Procedure  -------------------
	# Create Procedure
	def create_procedure_auto(self, product):
		"""
		Used by: Order
		Uses: Price List PL-Creates Library
		"""
		print()
		print('OH - create_procedure_auto')
		print(self)
		print(product)
		#pl_creates.create_procedure_go(self, product)
		pl_creates.create_procedure(self, product)
	# create_procedure

# ----------------------------------------------------------- Create Procedure Manual  ------------
	@api.multi
	def btn_create_procedure_man(self):
		"""
		Create Procedure Manual
		"""
		print()
		print('treatment - btn_create_procedure_man')
		print("order_pro_ids: {}".format(self.order_pro_ids))
		# Loop
		for order in self.order_pro_ids:
			print("order: {}".format(order))
			if order.proc_is_not_created_and_state_is_sale() or self.override:
				order.create_procedure_man(self)
	# btn_create_procedure_man

# ----------------------------------------------------------- Create Services  ------------
	# co2
	@api.multi
	def create_service_co2(self):
		"""
		Create Service Co2
		"""
		# Init
		family = 'laser'
		subfamily = 'co2'
		treatment_id = self.id
		physician_id = self.physician.id

		# Create
		#ret = reco_funcs.btn_create_reco(treatment_id, family, subfamily, physician_id)
		ret = self.create_service_for_me(treatment_id, family, subfamily, physician_id)

		return ret

# ---------------------------------------------- Create Service ----------------
	def create_service_for_me(self, treatment_id, family, subfamily, physician_id):
		"""
		Generic method for creating Services. 
		Compact. And easy to maintain. 
		"""
		print()
		print('Create Service Generic - ', subfamily)
		# init
		model_dic = {
						'all': 			_model_service,
						#'co2': 		_model_ser_co2,
						#'excilite': 	'openhealth.service_excilite',					
						#'ipl': 		'openhealth.service_ipl',
						#'ndyag': 		'openhealth.service_ndyag',
						#'quick': 		'openhealth.service_quick',
						#'cosmetology': 'openhealth.service_cosmetology',
						#'medical': 	'openhealth.service_medical',
						#'gynecology': 	'openhealth.service_gynecology',
						#'echography': 	'openhealth.service_echography',
						#'promotion': 	'openhealth.service_promotion',
						#'product': 	'openhealth.service_product',
			}
		model = model_dic[subfamily]

		# open 	
		return {
				'type': _model_action,
				'name': ' New Service Current', 
				'res_model':  	model,			
				#'res_id': consultation_id,
				"views": [[False, "form"]],
				#'view_type': 'form',
				'view_mode': 'form',	
				'target': 'current',
				'flags': 	{
								'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
								#'form': {'action_buttons': False, }
							},
				'context': {							
								'default_family': family,
								'default_physician': physician_id,
								#'default_pl_subfamily': subfamily,
								'default_treatment': treatment_id,
							}
				}
	# btn_create_reco

# ---------------------------------------------------- Test Integration --------
	@api.multi
	def test_integration(self):
		"""
		Integration Test
		"""
		print()
		print('OH - treatment.py - test_integration')
		value = self.env.context.get('key')
		print(value)
		if self.patient.x_test:
			if value == 'test_integration':
					#test_case = 'laser'
					#test_case = 'product'
					#test_case = 'medical'
					#test_case = 'cosmetology'
					#test_case = 'new'
					test_case = 'all'
					test_treatment.test_integration_treatment(self, test_case)

			elif value == 'test_reset':
				test_treatment.test_reset_treatment(self)
		print()
		print()
		print('SUCCESS !')

# -------------------------------------------------- Test Cycle ----------------
	@api.multi
	def test_cycle(self):
		"""
		Test Cycle
		"""
		print()
		print('test_cycle')
		value = self.env.context.get('key')
		print(value)
		test_treatment.test_create(self, value)


# ----------------------------------------------------------- Test Reports -----
	# Management
	report_management = fields.Many2one(
		'openhealth.management',
		string="MGT",
	)

	# Marketing
	report_marketing = fields.Many2one(
		'openhealth.marketing',
		string="MKT",
	)

	# Contasis
	report_contasis = fields.Many2one(
		'openhealth.account.contasis',
		string="ACC",
	)

	# Txt
	report_account = fields.Many2one(
		'openhealth.container',
		string="TXT",
	)

# ----------------------------------------------------- Test Report --------------------------
	@api.multi
	def test_report(self):
		"""
		Test Report
		"""
		print()
		print('test_report')
		value = self.env.context.get('key')
		print(value)

		if value == 'test_report_management':
			test_treatment.test_report_management(self)

		elif value == 'test_report_product':
			test_treatment.test_report_product(self)

		elif value == 'test_report_account':
			test_treatment.test_report_account(self)

		elif value == 'test_report_contasis':
			test_treatment.test_report_contasis(self)

		print()
		print('SUCCESS !')

# -------------------------------------------------------- Open Myself ---------
	# Open Myself
	@api.multi
	def open_myself(self):
		"""
		Used by - Procedure
		"""
		return action_funcs.open_myself(_model_treatment, self.id)
