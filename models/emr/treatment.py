# -*- coding: utf-8 -*-
"""
 		*** Treatment

 		Created: 			26 Aug 2016
 		Last up: 	 		21 Jan 2019
"""
from __future__ import print_function
import datetime
from openerp import models, fields, api
from . import time_funcs
from . import treatment_vars
from openerp.addons.openhealth.models.libs import creates as cre
from openerp.addons.openhealth.models.libs import lib, user
from . import test_foo
from . import test_treatment

class Treatment(models.Model):

	_inherit = 'openhealth.process'

	_name = 'openhealth.treatment'

	_order = 'write_date desc'

	_description = 'Treatment'



# ----------------------------------------------------------- Dep !!! ------------------------
	# Appointments
	#appointment_ids = fields.One2many(
	#		'oeh.medical.appointment',
	#		'treatment',
	#		string="Citas",
	#	)

	# Reservations
	#reservation_ids = fields.One2many(
	#		'oeh.medical.appointment',
	#		'treatment',
	#		string="Reserva de sala",
	#		domain=[
						#('x_machine', '!=', 'false'),
	#				],
	#		)


	# Appointments
	#nr_appointments = fields.Integer(
	#		string="Citas",
	#		compute="_compute_nr_appointments",
	#)
	#@api.multi
	#def _compute_nr_appointments(self):
	#	for record in self:
	#		record.nr_appointments = self.env['oeh.medical.appointment'].search_count([
	#																					('treatment', '=', record.id),
	#																					#('x_target', '=', 'doctor'),
	#																])




# ----------------------------------------------------------- All Services - Dep ? ------------------------
	# Product
	@api.multi
	def create_service_product(self):
		#ret = reco_funcs.create_service_product(self)
		return 0

	# Co2
	@api.multi
	def create_service_co2(self):
		#ret = reco_funcs.create_service_co2(self)
		return 0

	# Quick
	@api.multi
	def create_service_quick(self):
		#ret = reco_funcs.create_service_quick(self)
		return 0

	# Excilite
	@api.multi
	def create_service_excilite(self):
		#ret = reco_funcs.create_service_excilite(self)
		return 0

	# Ipl
	@api.multi
	def create_service_ipl(self):
		#ret = reco_funcs.create_service_ipl(self)
		return 0

	# Ndyag
	@api.multi
	def create_service_ndyag(self):
		#ret = reco_funcs.create_service_ndyag(self)
		return 0

	# Medical
	@api.multi
	def create_service_medical(self):
		#ret = reco_funcs.create_service_medical(self)
		return 0

	# Cosmetology
	@api.multi
	def create_service_cosmetology(self):
		#ret = reco_funcs.create_service_cosmetology(self)
		return 0




# ----------------------------------------------------------- Test --------------------------------

	x_test_scenario = fields.Selection(
			[
				('co2', 'Co2'),
				('exc', 'Exc'),
				('quick', 'Quick'),
				('ipl', 'Ipl'),
				('ndyag', 'Ndyag'),

				('all', 'All'),
			],
			string="Scenarios",
		)

	x_test = fields.Boolean(
			'Test',
		)

	# Electronic
	electronic_order = fields.One2many(
			'openhealth.electronic.order',
			'treatment_id',
		)


# ----------------------------------------------------------- Optimization ------------------------
	delta_1 = fields.Float(
			'Delta 1',
		)

	delta_2 = fields.Float(
			'Delta 2',
		)


# ----------------------------------------------------------- Test Flags --------------------------

	# Clear All
	@api.multi
	def clear_all(self):
		test_treatment.clear_all(self)

	# Set All
	@api.multi
	def set_all(self):
		test_treatment.set_all(self)




# ----------------------------------------------------------- Vip  --------------------------------

	# Vip
	vip = fields.Boolean(
		string="VIP",
		#default=False,

		compute='_compute_vip',
	)
	@api.multi
	def _compute_vip(self):
		for record in self:
			card = record.env['openhealth.card'].search([
															('patient_name', '=', record.patient.name),
														],
														#order='appointment_date desc',
														limit=1,)
			if card.name != False:
				record.vip = True




	# Pricelist
	pricelist_id = fields.Many2one(
			'product.pricelist',
			string='Pricelist',
			readonly=True,
			#states={'draft': [('readonly', False)], 'sent': [('readonly', False)]},
			#help="Pricelist for current sales order.",

			compute='_compute_pricelist_id',
	)
	@api.multi
	def _compute_pricelist_id(self):
		for record in self:

			record.pricelist_id = record.patient.property_product_pricelist



# ----------------------------------------------------------- Create Procedure  -------------------
	# Create Procedure
	@api.multi
	def create_procedure(self, date_app, subtype, product_id):
		#print
		#print 'Create Procedure'
		ret = cre.create_procedure_go(self, date_app, subtype, product_id)
	# create_procedure



# ----------------------------------------------------------- Create Controls  --------------------
	# Create Controls
	@api.multi
	def create_controls(self):
		#print
		#print 'Create Controls'
		control_date = self.start_date
		patient_id = self.patient.id
		doctor_id = self.physician.id
		treatment_id = self.id
		chief_complaint = self.chief_complaint

		# Create Control
		control = self.control_ids.create({
											'evaluation_start_date':control_date,
											'first_date':control_date,
											'patient':patient_id,
											'doctor':doctor_id,
											'chief_complaint':chief_complaint,
											'treatment': treatment_id,

											#'appointment': appointment_id,
											#'product':product_id,
											#'procedure':procedure_id,
									})
	# create_controls



# ----------------------------------------------------------- Testing Booleans --------------------

	# Create Flags

	# Sessions
	ses_create = fields.Boolean(
			string="Ses",
			default=False,
		)

	# Controls
	con_create = fields.Boolean(
			string="Con",
			default=False,
		)



	# Laser
	co2_create = fields.Boolean(
			string="Co2",
			default=False,
		)

	exc_create = fields.Boolean(
			string="Exc",
			default=False,
		)

	ipl_create = fields.Boolean(
			string="Ipl",
			default=False,
		)

	ndy_create = fields.Boolean(
			string="Ndyag",
			default=False,
		)

	qui_create = fields.Boolean(
			string="Quick",
			default=False,
		)

	# Medical
	med_create = fields.Boolean(
			string="Med",
			default=False,
		)

	# Cosmeto
	cos_create = fields.Boolean(
			string="Cos",
			default=False,
		)

	# Vip
	vip_create = fields.Boolean(
			string="Vip",
			default=False,
		)

	# Product
	product_create = fields.Boolean(
			string="Product",
			default=False,
		)




# ----------------------------------------------------------- Reload ------------------------------

	# Reload
	@api.multi
	def reload(self):
		#print
		#print 'Reload'
		return {
				'type': 'ir.actions.client',
				'tag': 'reload',
		}








# ----------------------------------------------------------- Create Procedure Manual  ------------
	@api.multi
	def create_procedure_man(self):
		#print
		#print 'Create Procedure - Manual'


		# Loop - Create Procedures
		ret = 0
		for order in self.order_pro_ids:

			if order.state == 'sale':

				# Update
				order.x_procedure_created = True

				# Loop
				for line in order.order_line:


					# Init
					date_app = order.date_order
					product_id = line.product_id

					# Search
					product_template = self.env['product.template'].search([
																				('x_name_short', '=', product_id.x_name_short),
												])

					subtype = product_template.x_treatment

					ret = cre.create_procedure_go(self, date_app, subtype, product_id.id)








# ----------------------------------------------------------- Manual ------------------------------

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



# ----------------------------------------------------------- Alta --------------------------------

	# Closed
	treatment_closed = fields.Boolean(
			string="De Alta",
			default=False,
		)



# ----------------------------------------------------------- Canonical ---------------------------

	# Name
	name = fields.Char(
			string="Tratamiento #",

			compute='_compute_name',
		)
	@api.multi
	#@api.depends('start_date')
	def _compute_name(self):
		for record in self:
			record.name = 'TR0000' + str(record.id)


	# Space
	vspace = fields.Char(
			' ',
			readonly=True
		)


	# Active
	active = fields.Boolean(
			default=True,
		)




# ----------------------------------------------------------- Macro -------------------------------

	# Sex
	patient_sex = fields.Char(
			string="Sexo",

			compute='_compute_patient_sex',
		)

	@api.multi
	def _compute_patient_sex(self):
		#print
		#print 'Compute Patient Sex'
		for record in self:
			#print 'record'
			if record.patient.sex != False:
				record.patient_sex = record.patient.sex[0]


	# Age
	patient_age = fields.Char(
			string="Edad",

			compute='_compute_patient_age',
		)

	@api.multi
	def _compute_patient_age(self):
		#print
		#print 'Compute Patient Age'
		for record in self:
			#print 'record'
			if record.patient.age != False:
				record.patient_age = record.patient.age.split()[0]


	# City
	patient_city = fields.Char(
			string="Lugar de procedencia",

			compute='_compute_patient_city',
		)

	@api.multi
	def _compute_patient_city(self):
		#print
		#print 'Compute Patient City'
		for record in self:
			#print 'record'
			if record.patient.city_char != False:
				city = record.patient.city_char
				record.patient_city = city.title()





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
						#('x_family', '=', 'procedure'),
						('x_family', 'in', ['procedure', 'cosmetology']),
					],
		)





# ----------------------------------------------------------- Services ----------------------------

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
	#@api.depends('consultation_ids')
	def _compute_state(self):
		for record in self:

			# Init
			state = 'empty'


			if record.treatment_closed:
				state = 'done'

			elif record.nr_controls > 0:
				state = 'controls'

			elif record.nr_sessions > 0:
				state = 'sessions'

			elif record.nr_procedures > 0:
				state = 'procedure'

			elif record.nr_invoices_pro > 0:
				state = 'invoice_procedure'

			elif record.nr_budgets_pro > 0:
				state = 'budget_procedure'

			elif record.nr_services > 0:
				state = 'service'

			elif record.consultation_progress == 100:
				state = 'consultation'

			elif record.nr_invoices_cons > 0:
				state = 'invoice_consultation'

			elif record.nr_budgets_cons > 0:
				state = 'budget_consultation'

			#elif record.nr_appointments > 0:
			#	state = 'appointment'


			# Assign
			record.state = state

	# _compute_state





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
																	('x_family', '=', 'consultation'),
																	('state', '=', 'draft'),
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
																			('x_family', '=', 'consultation'),
																			('state', '=', 'sale'),
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
																	#order='appointment_date desc', limit=1)











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
			services = self.env['openhealth.service.co2'].search_count([('treatment', '=', record.id),])
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







# ----------------------------------------------------------- Creates - Manual, Process and Testing -----------



# ----------------------------------------------------------- Create Order - Fields ---------------------------

	# Partner
	partner_id = fields.Many2one(
			'res.partner',
			string="Cliente",

			compute='_compute_partner_id',
		)

	#@api.multi
	@api.depends('patient')
	def _compute_partner_id(self):
		for record in self:
			partner = record.env['res.partner'].search([
															('name', 'like', record.patient.name),

														],
														#order='appointment_date desc',
														limit=1,)

			record.partner_id = partner
	# _compute_partner_id






# ----------------------------------------------------------- Create Order Consultation  ----------
	@api.multi
	def create_order_con_tst(self):

		# Init
		target = 'consultation'

		# Create
		order = cre.create_order(self, target)

		return order



# ----------------------------------------------------------- Create Order Consultation  ----------
	@api.multi
	def create_order_con(self):

		# Init
		target = 'consultation'

		# Create
		order = cre.create_order(self, target)

		# Open
		return {
				# Created
				'res_id': order.id,
				# Mandatory
				'type': 'ir.actions.act_window',
				'name': 'Open Order Current',
				# Window action
				'res_model': 'sale.order',
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
				'context': {}
			}
	# create_order_con







# -----------------------------------------------------------  Create Order Pro  ------------------
	@api.multi
	def create_order_pro(self):

		target = 'procedure'

		order = cre.create_order(self, target)

		return {
				# Created
				'res_id': order.id,
				# Mandatory
				'type': 'ir.actions.act_window',
				'name': 'Open Order Current',
				# Window action
				'res_model': 'sale.order',
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
				'context': {}
			}
	# create_order_pro




# ----------------------------------------------------- Create Consultation -----------------------
	# Create Consultation
	@api.multi
	def create_consultation(self):

		# Init vars
		patient_id = self.patient.id
		treatment_id = self.id
		chief_complaint = self.chief_complaint


		# Doctor
		doctor = user.get_actual_doctor(self)
		doctor_id = doctor.id

		if doctor_id == False:
			doctor_id = self.physician.id


		# Date
		GMT = time_funcs.Zone(0, False, 'GMT')
		#evaluation_start_date = datetime.now(GMT).strftime("%Y-%m-%d %H:%M:%S")
		evaluation_start_date = datetime.datetime.now(GMT).strftime("%Y-%m-%d %H:%M:%S")



		# Apointment
		#if False:
		#	appointment = self.env['oeh.medical.appointment'].search([
		#																('patient', '=', self.patient.name),
		#																('doctor', '=', self.physician.name),
		#																('x_type', '=', 'consultation'),
		#														],
		#														order='appointment_date desc', limit=1)
		#	appointment_id = appointment.id
		
		#appointment_id = False





		# Search
		consultation = self.env['openhealth.consultation'].search([
																		('treatment', '=', self.id),
																],
																#order='appointment_date desc',
																limit=1,)
		# Create if it does not exist
		if consultation.name == False:

			# Change App state
			#if False:
			#	if appointment.name != False:
			#		appointment.state = 'Scheduled'


			# Consultation
			consultation = self.env['openhealth.consultation'].create({
																		'patient': patient_id,
																		'treatment': treatment_id,
																		'evaluation_start_date': evaluation_start_date,
																		'chief_complaint': chief_complaint,
																		#'appointment': appointment_id,
																		'doctor': doctor_id,
													})
			consultation_id = consultation.id


			# Update
			#if False:
			#	rec_set = self.env['oeh.medical.appointment'].browse([
			#															appointment_id
			#														])
			#	ret = rec_set.write({
			#							'consultation': consultation_id,
			#						})



		consultation_id = consultation.id

		# Update Patient
		#consultation.update_patient()

		return {

			# Mandatory
			'type': 'ir.actions.act_window',
			'name': 'Open Consultation Current',
			# Window action
			'res_model': 'openhealth.consultation',
			'res_id': consultation_id,
			# Views
			"views": [[False, "form"]],
			'view_mode': 'form',
			'target': 'current',
			#'view_id': view_id,
			#'view_id': 'oeh_medical_evaluation_view',
			#'view_id': 'oehealth.oeh_medical_evaluation_view',
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
							#'default_appointment': appointment_id,
			}
		}
	# create_consultation_man





# ----------------------------------------------------------- Create Service (Recommendation) -----

	# Create Service
	@api.multi
	def create_service(self):
		#print
		#print 'Create Service'

		# Init
		res_id = self.id
		res_model = 'openhealth.treatment'
		view_id = self.env.ref('openhealth.treatment_2_form_view').id
		#print view_id

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
					#'form': {'action_buttons': True, }
					'form': {'action_buttons': False, }
					},
			'context': {
						#'default_treatment': treatment_id,
					}
		}
	# create_service


# ----------------------------------------------------------- Update ------------------------------
	# Flag
	flag = fields.Boolean(
			'Flag',
		)

	# Update
	@api.multi
	def update(self):
		#print
		#print 'Update'
		self.flag = not self.flag
	# update


# ----------------------------------------------------------- Test Libs --------------------
	@api.multi
	def test_libs(self):
		"""
		Test Libraries
		"""

		print()
		print('Test Libs')


		# Product (Generated Names)
		lib = test_foo.LibGen()
		lib.test()
		print(lib)


		# Export TXT
		#self.electronic_order.unlink()
		#for order in self.order_ids:
		#	electronic_order = cre.create_order_electronic(self, order)
		#	lib = test_foo.LibExp(electronic_order)
		#	lib.test()
		#	print(lib)


		# Check Patient
		lib = test_foo.LibChkPatient(self.patient)
		lib.test()
		print(lib)


		# Products
		lib = test_foo.Products(self)
		lib.test()
		print(lib)


		# Reports
		lib = test_foo.Reports(self)
		lib.test()
		print(lib)


		# Patients
		lib = test_foo.Patients(self)
		lib.test()
		print(lib)


		# Payments
		lib = test_foo.Payments(self)
		lib.test()
		print(lib)

	# test_libs

# ----------------------------------------------------------- Test - Computes ---------------------
	def test_computes(self):
		print()
		print('Treatment - Computes')
		#t0 = timer()
		print(self.name)
		print(self.state)
		print(self.progress)
		print(self.vip)
		print(self.pricelist_id)
		print(self.patient_sex)
		print(self.patient_age)
		print(self.patient_city)
		print(self.x_vip_inprog)
		print(self.consultation_progress)
		#print(self.nr_appointments)
		print(self.nr_consultations)
		print(self.nr_budgets_cons)
		print(self.nr_invoices_cons)
		print(self.nr_services)
		print(self.nr_services_co2)
		print(self.nr_services_excilite)
		print(self.nr_services_ipl)
		print(self.nr_services_ndyag)
		print(self.nr_services_quick)
		print(self.nr_services_medical)
		print(self.nr_services_cosmetology)
		print(self.nr_services_vip)
		print(self.nr_services_product)
		print(self.nr_controls)
		print(self.nr_sessions)
		print(self.nr_procedures)
		#t1 = timer()
		#self.delta_1 = t1 - t0
		#print self.delta_1
	# test_computes



# ----------------------------------------------------------- Test Create Recos --------------------------------
	# Test
	def test_create_recos(self):
		#print
		#print 'Treatment - Test'
		ret = self.create_service_product()
		ret = self.create_service_co2()
		ret = self.create_service_excilite()
		ret = self.create_service_ipl()
		ret = self.create_service_ndyag()
		ret = self.create_service_quick()
		ret = self.create_service_medical()
		ret = self.create_service_cosmetology()
	# test_create_recos



# ----------------------------------------------------------- Test Integration --------------------
	@api.multi
	def test_integration(self):
		"""
		Integration Test of the Treatment Class.
		"""
		print()
		print('Test Integration')
		if self.patient.x_test:

			# Reset
			test_treatment.reset_treatment(self)

			# Test Integration
			test_treatment.test_integration_treatment(self)


# ----------------------------------------------------------- Test Reset --------------------------
	@api.multi
	def test_reset(self):
		print()
		print('Test Case - Reset')
		if self.patient.x_test:
			test_treatment.reset_treatment(self)


# ----------------------------------------------------------- Test --------------------------------
	# Test
	@api.multi
	def test(self):
		print()
		print('Treatment - Test')		
		if self.patient.x_test:
			self.test_reset()
			self.test_integration()
			self.test_create_recos()
			self.test_computes()
			#self.test_libs()
