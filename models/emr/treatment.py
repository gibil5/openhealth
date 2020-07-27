# -*- coding: utf-8 -*-
"""
		*** Treatment
		Created: 			26 Aug 2016
		Last up: 	 		26 Jul 2020
"""
from __future__ import print_function
from openerp import models, fields, api
from openerp.addons.openhealth.models.libs import eval_vars
from . import treatment_vars
from . import treatment_state

#from openerp.addons.openhealth.models.libs import lib, user, eval_vars
#from openerp.addons.openhealth.models.libs import creates as cre  	# Dep !
#from openerp.addons.price_list.models.treatment import pl_creates

class Treatment(models.Model):
	"""
	Treatment class
	"""
	_name = 'openhealth.treatment'
	_order = 'write_date desc'
	_description = 'Treatment'

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
			record.nr_budgets_cons = self.env['sale.order'].search_count([
																			('treatment', '=', record.id),
																			('state', '=', 'draft'),
																			('pl_family', 'like', 'CONSULTA'),
																	])
	# Invoices - Consultations
	nr_invoices_cons = fields.Integer(
			string="Facturas Consultas",
			compute="_compute_nr_invoices_cons",
	)
	@api.multi
	def _compute_nr_invoices_cons(self):
		for record in self:
			record.nr_invoices_cons = self.env['sale.order'].search_count([
																			('treatment', '=', record.id),
																			('state', '=', 'sale'),
																			('pl_family', '=', 'CONSULTA,'),
																	])
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


	# Budgets - Proc   					# DEP ?
	nr_budgets_pro = fields.Integer(
			string="Presupuestos - Pro",
			compute="_compute_nr_budgets_pro",
	)
	@api.multi
	def _compute_nr_budgets_pro(self):
		for record in self:
			record.nr_budgets_pro = self.env['sale.order'].search_count([
																		('treatment', '=', record.id),
																		('x_family', '=', 'procedure'),
																		('state', '=', 'draft'),
																	])
	# Invoices - Proc
	nr_invoices_pro = fields.Integer(
			string="Facturas",
			compute="_compute_nr_invoices_pro",
	)
	@api.multi
	def _compute_nr_invoices_pro(self):
		for record in self:
			record.nr_invoices_pro = self.env['sale.order'].search_count([
																			('treatment', '=', record.id),
																			('x_family', '=', 'procedure'),
																			('state', '=', 'sale'),
																	])
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


# ----------------------------------------------------------- Macro ------------
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
		self.add_procedures = False

	# Toggle
	@api.multi
	def toggle_add_procedures(self):
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
			nr_vip = self.env['openhealth.service.product'].search_count([
																			('treatment', '=', record.id),
																			('service', 'in', ['tarjeta vip', 'Tarjeta Vip', 'Tarjeta VIP', 'TARJETA VIP']),
																			#('state','=', 'draft'),
				])
			if nr_vip > 0:
				record.x_vip_inprog = True



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



# ----------------------------------------------------------- Services - Dep ? ----------------------------

	# Product
	service_product_ids = fields.One2many(
			'openhealth.service.product',
			'treatment',
			string="Servicios Producto"
		)

	# Vip
	service_vip_ids = fields.One2many(
			'openhealth.service.vip',
			'treatment',
			string="Servicios vip"
		)

	# Service
	service_ids = fields.One2many(
			'openhealth.service',
			'treatment',
			string="Servicios"
		)

	# Quick
	service_quick_ids = fields.One2many(
			'openhealth.service.quick',
			'treatment',
			string="Servicios quick"
			)

	# Co2
	service_co2_ids = fields.One2many(
			'openhealth.service.co2',
			'treatment',
			string="Servicios Co2"
			)

	# Excilite
	service_excilite_ids = fields.One2many(
			'openhealth.service.excilite',
			'treatment',
			string="Servicios Excilite"
			)

	# Ipl
	service_ipl_ids = fields.One2many(
			'openhealth.service.ipl',
			'treatment',
			string="Servicios ipl"
			)

	# Ndyag
	service_ndyag_ids = fields.One2many(
			'openhealth.service.ndyag',
			'treatment',
			string="Servicios ndyag"
			)

	# Medical
	service_medical_ids = fields.One2many(
			'openhealth.service.medical',
			'treatment',
			string="Servicios medical"
			)

	# Cosmetology
	service_cosmetology_ids = fields.One2many(
			'openhealth.service.cosmetology',
			'treatment',
			string="Servicios cosmeatria"
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


# ----------------------------------------------------------- Number ofs - Services ---------------
	# Number of Services
	nr_services = fields.Integer(
			string="Servicios",
			compute="_compute_nr_services",
	)
	@api.multi
	def _compute_nr_services(self):
		for record in self:
			quick =	self.env['openhealth.service.quick'].search_count([('treatment', '=', record.id),])
			co2 = self.env['openhealth.service.co2'].search_count([('treatment', '=', record.id),])
			exc = self.env['openhealth.service.excilite'].search_count([('treatment', '=', record.id),])
			ipl = self.env['openhealth.service.ipl'].search_count([('treatment', '=', record.id),])
			ndyag = self.env['openhealth.service.ndyag'].search_count([('treatment', '=', record.id),])
			medical = self.env['openhealth.service.medical'].search_count([('treatment', '=', record.id),])
			vip = self.env['openhealth.service.vip'].search_count([('treatment', '=', record.id),])
			product = self.env['openhealth.service.product'].search_count([('treatment', '=', record.id),])

			record.nr_services = quick + co2 + exc + ipl + ndyag + medical + vip + product



	# product
	nr_services_product = fields.Integer(
			string="Servicios Producto",

			compute="_compute_nr_services_product",
	)
	@api.multi
	def _compute_nr_services_product(self):
		for record in self:
			services = self.env['openhealth.service.product'].search_count([('treatment', '=', record.id),])
			record.nr_services_product = services



	# vip
	nr_services_vip = fields.Integer(
			string="Servicios vip",

			compute="_compute_nr_services_vip",
	)
	@api.multi
	def _compute_nr_services_vip(self):
		for record in self:
			services = self.env['openhealth.service.vip'].search_count([('treatment', '=', record.id),])
			record.nr_services_vip = services




	# Quick
	nr_services_quick = fields.Integer(
			string="Servicios Quick",

			compute="_compute_nr_services_quick",
	)
	@api.multi
	def _compute_nr_services_quick(self):
		for record in self:
			services = self.env['openhealth.service.quick'].search_count([('treatment', '=', record.id),])
			record.nr_services_quick = services



	# Co2
	nr_services_co2 = fields.Integer(
			string="Servicios",

			compute="_compute_nr_services_co2",
	)
	@api.multi
	def _compute_nr_services_co2(self):
		for record in self:
			services = self.env['price_list.service_co2'].search_count([('treatment', '=', record.id),])
			record.nr_services_co2 = services



	# excilite
	nr_services_excilite = fields.Integer(
			string="Servicios",

			compute="_compute_nr_services_excilite",
	)
	@api.multi
	def _compute_nr_services_excilite(self):
		for record in self:
			services = self.env['openhealth.service.excilite'].search_count([('treatment', '=', record.id),])
			record.nr_services_excilite = services


	# ipl
	nr_services_ipl = fields.Integer(
			string="Servicios",

			compute="_compute_nr_services_ipl",
	)
	@api.multi
	def _compute_nr_services_ipl(self):
		for record in self:
			services = self.env['openhealth.service.ipl'].search_count([('treatment', '=', record.id),])
			record.nr_services_ipl = services



	# ndyag
	nr_services_ndyag = fields.Integer(
			string="Servicios",

			compute="_compute_nr_services_ndyag",
	)
	@api.multi
	def _compute_nr_services_ndyag(self):
		for record in self:
			services = self.env['openhealth.service.ndyag'].search_count([('treatment', '=', record.id),])
			record.nr_services_ndyag = services



	# medical
	nr_services_medical = fields.Integer(
			string="Servicios",

			compute="_compute_nr_services_medical",
	)
	@api.multi
	def _compute_nr_services_medical(self):
		for record in self:
			services = self.env['openhealth.service.medical'].search_count([('treatment', '=', record.id),])
			record.nr_services_medical = services


	# Cosmetology
	nr_services_cosmetology = fields.Integer(
			string="Servicios",

			compute="_compute_nr_services_cosmetology",
	)
	@api.multi
	def _compute_nr_services_cosmetology(self):
		for record in self:
			services = self.env['openhealth.service.cosmetology'].search_count([('treatment', '=', record.id),])
			record.nr_services_cosmetology = services


# ----------------------------------------------------------- Open Myself -------------------------
	# Open Myself
	@api.multi
	def open_myself(self):
		treatment_id = self.id
		return {
			# Mandatory
			'type': 'ir.actions.act_window',
			'name': 'Open Consultation Current',
			# Window action
			'res_model': 'openhealth.treatment',
			'res_id': treatment_id,
			# Views
			"views": [[False, "form"]],
			'view_mode': 'form',
			'target': 'current',
			#'view_id': view_id,
			#"domain": [["patient", "=", self.patient.name]],
			#'auto_search': False,
			'flags': {
					'form': {'action_buttons': True, }
					#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
			},
			'context':   {}
		}
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
