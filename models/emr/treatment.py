# -*- coding: utf-8 -*-
"""
		Treatment
		Created: 			26 Aug 2016
		Last up: 	 		02 Aug 2020

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
from . import pl_user
from . import time_funcs
from . import test_treatment
from . import reco_funcs

from . import action_funcs

from . import counter_objects

class Treatment(models.Model):
	"""
	Treatment class
	"""
	_name = 'openhealth.treatment'
	_order = 'write_date desc'
	_description = 'Treatment'

# ----------------------------------------------------------- PL ---------------------------
	# Shopping cart
	shopping_cart_ids = fields.One2many(
			'price_list.cart_line',
			'treatment',
			string="Shopping Cart"
		)

# ----------------------------------------------------------- Fields - Services ------------------------
	# co2
	service_co2_ids = fields.One2many(
			'openhealth.service_co2',
			'treatment',
			string="Servicios Co2"
	)

	# excilite
	service_excilite_ids = fields.One2many(
			'openhealth.service_excilite',
			'treatment',
			string="Servicios excilite"
	)

  	# cosmetology
	service_cosmetology_ids = fields.One2many(
			'openhealth.service_cosmetology',
			'treatment',
			string="Servicios cosmetology"
	)

  	# echography
	service_echography_ids = fields.One2many(
			'openhealth.service_echography',
			'treatment',
			string="Servicios Ecografia"
	)

	# ipl
	service_ipl_ids = fields.One2many(
	    'openhealth.service_ipl',
	    'treatment',
	    string="Servicios ipl"
	    )

	# ndyag
	service_ndyag_ids = fields.One2many(
	    'openhealth.service_ndyag',
	    'treatment',
	    string="Servicios ndyag"
	    )

	# quick
	service_quick_ids = fields.One2many(
	    'openhealth.service_quick',
	    'treatment',
	    string="Servicios quick"
	    )

	# product
	service_product_ids = fields.One2many(
	    'openhealth.service_product',
	    'treatment',
	    string="Servicios product"
	    )

	# gynecology
	service_gynecology_ids = fields.One2many(
	    'openhealth.service_gynecology',
	    'treatment',
	    string="Servicios Ginecologia"
	    )

	# promotion
	service_promotion_ids = fields.One2many(
	    'openhealth.service_promotion',
	    'treatment',
	    string="Servicios Promocion"
	    )

# ----------------------------------------------------------- Primitive ---------------------------
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

# ----------------------------------------------------------- Process --------------------------
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
			string='Motivo de consulta',
			selection=eval_vars._chief_complaint_list,
			required=False,
			readonly=False,
		)

	start_date = fields.Date(
			string="Fecha inicio",
			default=fields.Date.today,
			readonly=True,
			states=READONLY_STATES,
		)

# ----------------------------------------------------------- Number ofs --------------------------
	# Budgets - Consultations 			# DEP ?
	nr_budgets_cons = fields.Integer(
			string="Presupuestos Consultas",
			compute="_compute_nr_budgets_cons",
	)
	@api.multi
	def _compute_nr_budgets_cons(self):
		for record in self:
			obj = counter_objects.CounterObjects(self.env['sale.order'], 'draft', 'CONSULTA', record.id,)
			record.nr_budgets_cons = obj.count()


	# Invoices - Consultations
	nr_invoices_cons = fields.Integer(
			string="Facturas Consultas",
			compute="_compute_nr_invoices_cons",
	)
	@api.multi
	def _compute_nr_invoices_cons(self):
		for record in self:
			obj = counter_objects.CounterObjects(self.env['sale.order'], 'sale', 'CONSULTA', record.id,)
			record.nr_invoices_cons = obj.count()


	# Budgets - Proc
	nr_budgets_pro = fields.Integer(
			string="Presupuestos - Pro",
			compute="_compute_nr_budgets_pro",
	)
	@api.multi
	def _compute_nr_budgets_pro(self):
		for record in self:
			obj = counter_objects.CounterObjects(self.env['sale.order'], 'draft', 'procedure', record.id, 'x_family')
			record.nr_budgets_pro = obj.count()

	# Invoices - Proc
	nr_invoices_pro = fields.Integer(
			string="Facturas",
			compute="_compute_nr_invoices_pro",
	)
	@api.multi
	def _compute_nr_invoices_pro(self):
		for record in self:
			obj = counter_objects.CounterObjects(self.env['sale.order'], 'sale', 'procedure', record.id, 'x_family')
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
			ctr = 0
			for c in record.consultation_ids:
				ctr = ctr + 1
			record.nr_consultations = ctr


	# Procedures
	nr_procedures = fields.Integer(
			string="Procedimientos",
			compute="_compute_nr_procedures",
	)
	@api.multi
	def _compute_nr_procedures(self):
		for record in self:
			record.nr_procedures = self.env['openhealth.procedure'].search_count([
																					('treatment', '=', record.id),
																	])
	# Sessions
	nr_sessions = fields.Integer(
			string="Sesiones",
			compute="_compute_nr_sessions",
	)
	@api.multi
	def _compute_nr_sessions(self):
		for record in self:
			record.nr_sessions = self.env['openhealth.session.med'].search_count([
																					('treatment', '=', record.id),
																				])
	# Controls
	nr_controls = fields.Integer(
			string="Controles",
			compute="_compute_nr_controls",
	)
	@api.multi
	def _compute_nr_controls(self):
		for record in self:
			record.nr_controls = 0
			record.nr_controls = self.env['openhealth.control'].search_count([
																				('treatment', '=', record.id),
																				])

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
			[
				('all', 'All'),
				('product', 'Product'),
				('laser', 'Laser'),
				('cosmetology', 'Cosmetology'),
				('medical', 'Medical'),
				('new', 'New'),
				('credit_note', 'Nota de Credito'),
				('block_flow', 'Flujo bloqueado'),
			],
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


# ----------------------------------------------------------- Card ------------
	# Sex - Used by header
	patient_sex = fields.Char(
			string="Sexo",
			compute='_compute_patient_sex',
		)
	@api.multi
	def _compute_patient_sex(self):
		for record in self:
			if record.patient.sex != False:
				record.patient_sex = record.patient.sex[0]

	# Age - id
	patient_age = fields.Char(
			string="Edad",
			compute='_compute_patient_age',
		)
	@api.multi
	def _compute_patient_age(self):
		for record in self:
			if record.patient.age != False:
				record.patient_age = record.patient.age.split()[0]

	# City - id
	patient_city = fields.Char(
			string="Lugar de procedencia",
			compute='_compute_patient_city',
		)
	@api.multi
	def _compute_patient_city(self):
		for record in self:
			if record.patient.city_char != False:
				city = record.patient.city_char
				record.patient_city = city.title()

	# Vip - id
	vip = fields.Boolean(
		string="VIP",
		compute='_compute_vip',
	)
	@api.multi
	def _compute_vip(self):
		for record in self:
			card = record.env['openhealth.card'].search([
															('patient_name', '=', record.patient.name),
														],
														limit=1,)
			if card.name != False:
				record.vip = True

# ----------------------------------------------------------- Price list  --------------------------------

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

	# Reset
	@api.multi
	def reset_procs(self):
		"""
		Reset Procedures
		"""
		self.add_procedures = False

	# Toggle
	@api.multi
	def toggle_add_procedures(self):
		"""
		Toggle add procedures
		"""
		self.add_procedures = not self.add_procedures

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
			domain=[
						#('x_family', 'in', ['procedure', 'cosmetology']),
						('pl_family', 'in', ['LASER CO2']),
					],
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
		for record in self:
			obj = treatment_state.TreatmentState(record)
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

			#record.nr_services = 0

			#co2 = self.env['openhealth.service.co2'].search_count([('treatment', '=', record.id),])
			#quick =	self.env['openhealth.service.quick'].search_count([('treatment', '=', record.id),])
			#exc = self.env['openhealth.service.excilite'].search_count([('treatment', '=', record.id),])
			#ipl = self.env['openhealth.service.ipl'].search_count([('treatment', '=', record.id),])
			#ndyag = self.env['openhealth.service.ndyag'].search_count([('treatment', '=', record.id),])
			#medical = self.env['openhealth.service.medical'].search_count([('treatment', '=', record.id),])
			#vip = self.env['openhealth.service.vip'].search_count([('treatment', '=', record.id),])
			#product = self.env['openhealth.service.product'].search_count([('treatment', '=', record.id),])
			#record.nr_services = quick + co2 + exc + ipl + ndyag + medical + vip + product

			co2 = self.env['openhealth.service_co2'].search_count([('treatment', '=', record.id),])
			record.nr_services = co2


	# Co2
	nr_services_co2 = fields.Integer(
			string="Servicios",

			compute="_compute_nr_services_co2",
	)
	@api.multi
	def _compute_nr_services_co2(self):
		for record in self:
			#services = self.env['price_list.service_co2'].search_count([('treatment', '=', record.id),])
			services = self.env['openhealth.service_co2'].search_count([('treatment', '=', record.id),])
			record.nr_services_co2 = services


# ----------------------------------------------------------- Create Buttons  ----------
	@api.multi
	def create_order_con(self):
		"""
		Create Order Consultation Standard - Medical
		One mode
		"""
		print()
		#print('PL - treatment - create_order_con')
		print('OH - create_order_con')

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
	def create_consultation(self):
		"""
		Create consultation - Button
		"""
		print()
		print('OH - create_consultation')

		# Init vars
		patient_id = self.patient.id
		treatment_id = self.id
		chief_complaint = self.chief_complaint

		# Doctor
		doctor = pl_user.get_actual_doctor(self)
		doctor_id = doctor.id
		if not doctor_id:
			doctor_id = self.physician.id

		# Date
		GMT = time_funcs.Zone(0, False, 'GMT')
		evaluation_start_date = datetime.datetime.now(GMT).strftime("%Y-%m-%d %H:%M:%S")

		# Search
		consultation = self.env['openhealth.consultation'].search([
																		('treatment', '=', self.id),
																],
																#order='appointment_date desc',
																limit=1,)

		# If Consultation not exist
		if not consultation.name:
			# Create
			consultation = self.env['openhealth.consultation'].create({
																		'patient': patient_id,
																		'treatment': treatment_id,
																		'evaluation_start_date': evaluation_start_date,
																		'chief_complaint': chief_complaint,
																		'doctor': doctor_id,
													})

		return {
				# Mandatory
				'type': 'ir.actions.act_window',
				'name': 'Open Consultation Current',
				# Window action
				'res_model': 'openhealth.consultation',
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
	# create_consultation

# ----------------------------------------------------------- Create Service ---------------------------
	@api.multi
	def create_service(self):
		"""
		Create Service
		Opens a new form. For Reco choice.
		"""
		print()
		print('OH - create_service')

		# Init
		res_id = self.id
		res_model = 'openhealth.treatment'
		view_id = self.env.ref('openhealth.treatment_2_form_view').id

		# Open
		return {
			# Mandatory
			'type': 'ir.actions.act_window',
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
	# create_service

# -----------------------------------------------------------  Create Order Procedure - 2019 -------------
	@api.multi
	def create_order_pro(self):
		"""
		Create Order Procedure - 2019
		From Recommendations
		"""
		print('treatment - create_order_pro')

		# Clear cart
		self.shopping_cart_ids.unlink()

		# Init
		#price_list = '2019'

		service_list = [
							self.service_product_ids,
							self.service_co2_ids,
							self.service_excilite_ids,
							self.service_ipl_ids,
							self.service_ndyag_ids,
							self.service_quick_ids,
							#self.service_medical_ids,
							self.service_cosmetology_ids,
							self.service_gynecology_ids,
							self.service_echography_ids,
							self.service_promotion_ids,
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

	# create_order_pro

# ----------------------------------------------------------- Create Procedure  -------------------
	# Create Procedure
	#@api.multi
	#def create_procedure(self, product):
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
	#jx
	@api.multi
	def create_procedure_man(self):
		"""
		Create Procedure Manual
		"""
		print()
		print('treatment - create_procedure_man')
		print("order_pro_ids: {}".format(self.order_pro_ids))
		# Loop
		for order in self.order_pro_ids:
			print("order: {}".format(order))
			if order.proc_is_not_created_and_state_is_sale() or self.override:
				order.create_procedure_man(self)
	# create_procedure_man

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
		ret = reco_funcs.create_service(treatment_id, family, subfamily, physician_id)

		return ret


# ----------------------------------------------------------- Open Myself -------------------------
	# Open Myself
	@api.multi
	def open_myself(self):
		"""
		Used by
		"""
		#treatment_id = self.id
		return action_funcs.open_myself('openhealth.treatment', self.id)

	# open_myself

#----------------------------------------------------------- Quick Button - Used by Patient ---------
	@api.multi
	def open_line_current(self):
		"""
		# Quick access Button
		"""
		return {
				'type': 'ir.actions.act_window',
				'name': ' Edit Order Current',
				'view_type': 'form',
				'view_mode': 'form',
				'res_model': self._name,
				'res_id': self.id,
				'target': 'current',
				'flags': {
						#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
						'form': {'action_buttons': True, }
						},
				'context': {}
		}

# ----------------------------------------------------------- Test All Cycle - Step by Step --------------------------
	@api.multi
	def test_create_budget_consultation(self):
		"""
		Test
		"""
		print()
		print('Test Create Budget Consultation')
		test_treatment.test_create_budget_consultation(self)

	@api.multi
	def test_create_sale_consultation(self):
		"""
		Test
		"""
		print()
		print('Test Create Sale Consultation')
		test_treatment.test_create_sale_consultation(self)

	@api.multi
	def test_create_consultation(self):
		"""
		Test
		"""
		print()
		print('Test Create Consultation')
		test_treatment.test_create_consultation(self)

	@api.multi
	def test_create_recommendations(self):
		"""
		Test
		"""
		print()
		print('Test Create Recommendations')
		test_treatment.test_create_recommendations(self)

	@api.multi
	def test_create_budget_procedure(self):
		"""
		Test
		"""
		print()
		print('Test Create Budget procedure')
		test_treatment.test_create_budget_procedure(self)

	@api.multi
	def test_create_sale_procedure(self):
		"""
		Test
		"""
		print()
		print('Test Create Sale procedure')
		test_treatment.test_create_sale_procedure(self)


	#jx
	@api.multi
	def test_create_procedure(self):
		"""
		Create Procedure - Button
		"""
		print()
		print('Test Create procedure manual')

		#if True:
		if False:
			test_funcs.disablePrint()
			self.test_reset()
			self.test_create_budget_consultation()
			self.test_create_sale_consultation()
			self.test_create_consultation()
			self.test_create_recommendations()
			self.test_create_budget_procedure()
			self.test_create_sale_procedure()
			test_funcs.enablePrint()

		#test_treatment.test_create_procedure(self)
		self.create_procedure_man()



	@api.multi
	def test_create_sessions(self):
		"""
		Test
		"""
		print()
		print('Test Create sessions')
		test_treatment.test_create_sessions(self)

	@api.multi
	def test_create_controls(self):
		"""
		Test
		"""
		print()
		print('Test Create controls')
		test_treatment.test_create_controls(self)


# ----------------------------------------------------------- Test Integration --------------------
	@api.multi
	def test_integration(self):
		"""
		Integration Test
		"""
		print()
		print('OH - treatment.py - test_integration')
		if self.patient.x_test:
			# Reset
			#test_treatment.reset_treatment(self)
			# Test Integration
			test_treatment.test_integration_treatment(self)
		print()
		print()
		print('SUCCESS !')

# ----------------------------------------------------------- Test Reset --------------------------
	@api.multi
	def test_reset(self):
		"""
		Reset Test
		"""
		print()
		print('OH - Test Reset Button')
		if self.patient.x_test:
			test_treatment.test_reset_treatment(self)
		print()
		print()
		print('SUCCESS !')

