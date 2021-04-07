# -*- coding: utf-8 -*-
"""
	Order - Data model

	Created: 			26 Aug 2016
 	Last up: 	 			29 mar 2021

	Design:
		- This is a Data model. There should be NO Business logic.
		- This is not a singleton (1190 lines).
		- Reduce third party dependencies (oehealth).
		- Eliminate crossed dependencies.
		- All common services should be in the libs module.
		- Use publish/subscribe communication pattern.

	Follow the LOD (Law of Demeter - Tell dont aks).
		- Coupling is bad. Cohesion is good.

	Objects must be be:
		- Anthropomorphic, with clear roles and loosely coupled.

	Data should be injected into the loosely couple objs.

	Remember SOLID:
		- Single responsiblity.
		- Open/closed.
		- Liskov susbstitution.
		- Interface seggregation.
		- Dependency inversion.

	From PgAdmin
	-------------
	SELECT * FROM public.sale_order;
	DELETE FROM public.sale_order WHERE partner_id = 391;
"""
from __future__ import print_function
import datetime
from openerp import models, fields, api

from commons import pl_creates, action_funcs
from . import ord_vars
from . import raw_funcs
from . import qr
from . import fix_treatment
from . import ord_funcs

#from libs import pl_creates, eval_vars, tre_funcs, action_funcs
#from openerp.addons.openhealth.models.libs import pl_creates, action_funcs
#from openerp.addons.openhealth.models.commons.libs import pl_creates, action_funcs
#from . import test_order

class SaleOrder(models.Model):
	"""
	Sale Class
	- Inherits from the Base module Sale.
	- Oehealth free.
	"""
	_inherit = 'sale.order'
	_description = 'Order'

# ----------------------------------------------------------- Constants ---------------------------
	# States
	READONLY_STATES = {
		'draft': 		[('readonly', False)],
		'sent': 		[('readonly', False)],
		'sale': 		[('readonly', True)],
		'cancel': 		[('readonly', True)],
	}

# ----------------------------------------------------------- Relations ---------------------------

# --------------------------------------------------------------- One2many -----
	# Order Line
	order_line = fields.One2many(
			'sale.order.line',
			'order_id',
			string='Order Lines',
			#states=READONLY_STATES, 			# Done by the View
		)


# --------------------------------------------------------------- Many2one -----
	# Patient
	ticket = fields.Many2one(
			'openhealth.ticket',
			#string="Ticket",
			required=True,
			default=lambda self: raw_funcs.get_ticket(self.env['openhealth.ticket']),
		)

	# Patient
	patient_id = fields.Many2one(
			'oeh.medical.patient',
			string="Paciente",
			required=False,
		)

	# Treatment
	treatment = fields.Many2one(
			'openhealth.treatment',
			string="Tratamiento",
			readonly=False,
			#states=READONLY_STATES,
		)

	# Partner - already Created by OeHealth
	partner_id = fields.Many2one(
			'res.partner',
			string="Cliente",
			required=False,
			readonly=False,
		)

	# Pricelist
	pricelist_id = fields.Many2one(
			'product.pricelist',
			string='Pricelist',
			readonly=False,
			#default=_get_default_pricelist_id,
			#default=lambda self: self._get_default_pricelist(),
			default=lambda self: raw_funcs.get_pricelist(self.env['product.pricelist']),
			required=True,
		)

	# Configurator
	configurator = fields.Many2one(
			'openhealth.configurator.emr',
			string="Config",
			required=True,
			default=lambda self: raw_funcs.get_configurator(self.env['openhealth.configurator.emr']),
		)

	# Doctor
	x_doctor = fields.Many2one(
			'oeh.medical.physician',
			string="Médico",
			states=READONLY_STATES,
		)

	# Patient
	patient = fields.Many2one(
			'oeh.medical.patient',
			string='Paciente',
			#states=READONLY_STATES,
		)

	# Credit note
	x_credit_note = fields.Many2one(
			'sale.order',
			'Nota de Crédito',
		)

	x_credit_note_owner = fields.Many2one(
			'sale.order',
			'Documento que modifica',
		)

	# Payment Method
	x_payment_method = fields.Many2one(
			'openhealth.payment_method',
			string="Pago",
			states=READONLY_STATES,
		)

	x_doctor_uid = fields.Many2one(
			'res.users',
			string="Médico Uid",
			readonly=True,
		)


# ------------------------------------------- Computes (callbacks) -------------------------

	# Amount flow
	x_amount_flow = fields.Float(
			'Pl - Total F',
		
			compute='_compute_x_amount_flow',
		)
	@api.multi
	def _compute_x_amount_flow(self):
		for record in self:
			record.x_amount_flow = raw_funcs.get_amount_flow(record.x_block_flow, record.state, record.x_credit_note_amount, record.amount_total)


	# Descriptor - Family
	pl_family = fields.Char(
			string="Pl - Familia",

			compute='_compute_pl_family',
		)
	@api.multi
	def _compute_pl_family(self):
		for record in self:
			families = ''
			for line in record.order_line:
				families = families + line.get_family() + ', '
			record.pl_family = families[0:-2]

	# Descriptor - Product
	pl_product = fields.Char(
			string="Pl - Producto",
		
			compute='_compute_pl_product',
		)
	@api.multi
	def _compute_pl_product(self):
		for record in self:
			products = ''
			for line in record.order_line:
				products = products + line.get_product() + ', '
			record.pl_product = products


	# Type Code - OK
	x_type_code = fields.Char(
			string='Tipo Codigo',

			compute='_compute_x_type_code',
		)
	@api.multi
	def _compute_x_type_code(self):
		for record in self:
			if record.x_type in ['ticket_receipt', 'ticket_invoice', 'receipt', 'invoice', 'advertisement', 'sale_note']:
				record.x_type_code = ord_vars._dic_type_code[record.x_type]

	# Nr lines - OK
	nr_lines = fields.Integer(
			default=0,
			string='Nr líneas',
			required=False,

			compute='_compute_nr_lines',
		)

	@api.multi
	#@api.depends('order_line')
	def _compute_nr_lines(self):
		for record in self:
			ctr = 0
			for _ in record.order_line:
				ctr = ctr + 1
			record.nr_lines = ctr

	# Amount total - OK
	x_amount_total = fields.Float(
			string="x Total",

			compute="_compute_x_amount_total",
		)
	@api.multi
	def _compute_x_amount_total(self):
		for record in self:
			sub = 0.0
			for line in record.order_line:
				sub = sub + line.price_subtotal
			record.x_amount_total = sub

	# Amount Flow - Verify !
	x_amount_flow = fields.Float(
			'Total F',

			compute='_compute_x_amount_flow',
		)
	@api.multi
	def _compute_x_amount_flow(self):
		for record in self:
			if record.x_block_flow:
				record.x_amount_flow = 0
			elif record.x_credit_note_amount not in [0, False]:
				record.x_amount_flow = - record.x_credit_note_amount
			else:
				record.x_amount_flow = record.amount_total


# ----------------------------------------------------------- On Changes --------------------------
	# Patient
	@api.onchange('patient')
	def _onchange_patient(self):
		print('_onchange_patient')
		if self.patient.name:
			self.partner_id, self.x_dni, self.x_ruc, self.x_id_doc, self.x_id_doc_type = raw_funcs.get_patient_ids(self.patient)
			self.pricelist_id = raw_funcs.get_pricelist(self.env['product.pricelist'])

	# Doctor
	@api.onchange('x_doctor')
	def _onchange_x_doctor(self):
		if self.patient.name:
			self.treatment = raw_funcs.get_treatment(self.env['openhealth.treatment'], self.patient.name, self.x_doctor.name)


	# Partner
	@api.onchange('partner_id')
	def _onchange_partner_id(self):
		print('_onchange_partner_id')
		print(self.pricelist_id)
		if self.partner_id.name != False:
			self.x_partner_dni = self.partner_id.x_dni
		print(self.pricelist_id)

	# On Change Partner Dni
	@api.onchange('x_partner_dni')
	def _onchange_x_partner_dni(self):
		self.patient = ord_funcs.search_patient_by_id_document(self)


# ----------------------------------------------------------- Legacy ------------------------------
	# Legacy
	x_legacy = fields.Boolean(
			'Legacy',
			default=False,
		)

# ----------------------------------------------------------- Fields -------------------------------
	# Transfer Free
	pl_transfer_free = fields.Boolean(
			'TRANSFERENCIA GRATUITA',
			default=False,
		)

# ----------------------------------------------------------- Descriptors ------
	# Family
	x_family = fields.Selection(
			string="Familia",
			selection=[
							('product', 'Producto'),
							('consultation', 'Consulta'),
							('procedure', 'Procedimiento'),
							('cosmetology', 'Cosmiatría'),
			],
		)

	# Product
	x_product = fields.Char(
			string="Producto",
		)


# ---------------------------------------------- Price List - Fields ------------------------

# ----------------------------------------------------------- Natives -------------------------
	# Net
	x_total_net = fields.Float(
			"Neto",
		)

	# Tax
	x_total_tax = fields.Float(
			"Impuesto",
		)

# ----------------------------------------------------------- Credit Note -------------------------

	x_block_flow = fields.Boolean(
			'Flujo Bloqueado',
			#readonly=True,
		)

	x_credit_note_type = fields.Selection(
			selection=ord_vars._credit_note_type_list,
			string='Motivo',
		)

	x_credit_note_amount = fields.Float(
			#'Monto Devolución',
			'La Devolución es por S/',
			default=0,
		)

	x_credit_note_owner_amount = fields.Float(
			'Importe',
			default=0,
		)

# ----------------------------------------------------------- Dates -------------------------------
	# Date
	date_order = fields.Datetime(
		states={
				'draft': [('readonly', False)],
				'sent': [('readonly', False)],
				'sale': [('readonly', True)],
				},
		index=True,
	)

	# Month
	x_month_order = fields.Selection(
			selection=ord_vars._month_order_list,
			string='Mes',
		)

	# Day
	x_day_order = fields.Selection(
			selection=ord_vars._day_order_list,
			string='Dia',
		)


# ----------------------------------------------------------- Payment ----------------------------
	x_pm_cash = fields.Float(
			'Cash',
		)

	x_pm_visa_credit = fields.Float(
			'Visa Credit',
		)

	x_pm_visa_debit = fields.Float(
			'Visa Debit',
		)

	x_pm_master_credit = fields.Float(
			'Master Credit',
		)

	x_pm_master_debit = fields.Float(
			'Master Debit',
		)

	x_pm_american = fields.Float(
			'American',
		)

	x_pm_diners = fields.Float(
			'Diners',
		)


# ----------------------------------------------------------- Serial Nr ---------------------------
	# Serial Number
	x_serial_nr = fields.Char(
			'Número de serie',
		)

	# Counter Value
	x_counter_value = fields.Integer(
			string="Contador",
		)

# ---------------------------------------------- Electronic ------------------------------------
	x_title = fields.Char(
			'Titulo',
			default='Venta Electrónica',
		)

	x_electronic = fields.Boolean(
			'Electronic',
			default=False,
		)

	x_qr_img = fields.Binary(
			'Código QR',
		)

	x_qr_data = fields.Char(
			'Data QR'
		)

# ----------------------------------------------------------- Mode Admin --------------------------
	x_admin_mode = fields.Boolean(
			'Modo Admin',
			help='Activa el Modo Administrador.',
		)

# ----------------------------------------------------------- Id Doc ------------------------------
	# Id Document
	x_id_doc = fields.Char(
			'Nr. Doc.',
			required=False,
		)

	# Id Document Type
	x_id_doc_type = fields.Selection(
			#selection=pat_vars._id_doc_type_list,
			selection=ord_vars._id_doc_type_list,
			string='Tipo de documento',
			required=False,
		)

	# Type
	x_type = fields.Selection(
			[
				('receipt', 'Boleta'),
				('invoice', 'Factura'),
				('advertisement', 'Canje Publicidad'),
				('sale_note', 'Canje NV'),
				('ticket_receipt', 'Boleta Electronica'),
				('ticket_invoice', 'Factura Electronica'),
			],
			string='Tipo',
			required=False,
			states={
					'draft': [('readonly', True)],
					'sent': [('readonly', True)],
					'sale': [('readonly', True)],
				},
		)


# ----------------------------------------------------------- Pay ---------------------------------
	# DNI
	x_dni = fields.Char(
			string='DNI',
			readonly=True,
		)

	# RUC
	x_ruc = fields.Char(
			string='RUC',
		)

# ----------------------------------------------------------- Locked - By State -------------------
	# Receptor
	pl_receptor = fields.Char(
			string='Receptor',
		)


	# DNI - Used by Budget - Allows research of Patient by DNI - Important
	x_partner_dni = fields.Char(
			string='DNI',
			states={'draft': 	[('readonly', False)],
						'sent': 	[('readonly', True)],
						'sale': 	[('readonly', True)],
						'cancel': 	[('readonly', True)],
						'done': 	[('readonly', True)],
					},
		)


# ----------------------------------------------------------- Primitives --------------------------

	# Delta
	x_delta = fields.Integer(
			'Delta',
		)

	# State
	state = fields.Selection(
			selection=ord_vars._state_list,
			string='Estado',
			readonly=False,
			default='draft',
			index=True,
		)


	# Blank line
	vspace = fields.Char(
			' ',
			readonly=True
		)

	# Proc Created - For Doctor budget creation
	x_procedure_created = fields.Boolean(
			'Procedimiento Creado',
			default=False,
		)

# ---------------------------------------------- Cancel and Activate -------------------------------------------
	x_cancel = fields.Boolean(
			string='',
			default=False
		)

