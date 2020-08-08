# -*- coding: utf-8 -*-
"""
		Order - Openhealth
		Created: 			26 Aug 2016
		Last mod: 			08 Aug 2020

		This tangled object must be split in several objs, with clear roles.
		That must be be:
			- Anthropomorphic.
			- With clear roles.
			- Loosely coupled.
			- ...

		Data should be injected into the loosely couple objs.

		Objects:
			- QR
			- Serial Number
			- TicketCompany
			- TicketCustomer
			- TicketSale
			- DocId

		From PgAdmin
		-------------
		SELECT * FROM public.sale_order;
		DELETE FROM public.sale_order WHERE partner_id = 391;
"""
from __future__ import print_function
import datetime

from openerp import models, fields, api
#from openerp.exceptions import Warning as UserError
from openerp.addons.openhealth.models.patient import pat_vars, chk_patient
from openerp.addons.openhealth.models.emr import pl_creates, action_funcs

from . import test_order
#from . import chk_order
from . import ord_vars
from . import raw_funcs
from . import qr
from . import ticket_line
from . import fix_treatment
from . import ord_funcs
from . import tick_funcs

from . import check_order

class SaleOrder(models.Model):
	"""
	Sale Class - Inherited from the medical Module OeHealth.
	"""
	_inherit = 'sale.order'
	_description = 'Order'

# ----------------------------------------------------------- Relational -------------------------------
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

# ----------------------------------------- Constraints - From Patient ----------
	# Check Ruc
	@api.constrains('x_ruc')
	def _check_x_ruc(self):
		if self.x_type in ['ticket_invoice', 'invoice']:
			chk_patient.check_x_ruc(self)

	# Check Id doc - Use Chk Patient
	@api.constrains('x_id_doc')
	def _check_x_id_doc(self):
		if self.x_type in ['ticket_receipt', 'receipt']:
			chk_patient.check_x_id_doc(self)



# ---------------------------------------------- Price List - Fields ------------------------------------------


# ------------------------------------------- Natives  - Computes OK -----------

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

# ----------------------------------------------------------- Natives -------------------------
	# Net
	x_total_net = fields.Float(
			"Neto",
		)

	# Tax
	x_total_tax = fields.Float(
			"Impuesto",
		)

# ----------------------------------------------------------- Validate Button ----------------------------

	@api.multi
	def validate_and_confirm(self):
		"""
		Validate and confirm the order.
		"""
		print()
		print('Validate and confirm')

		# Handle Exceptions
		#exc_ord.handle_exceptions(self)

		# Payment method validation
		#self.check_payment_method()
		self.x_pm_total = raw_funcs.check_payment_method(self.x_payment_method.pm_line_ids)

		# If Everything is OK
		self.check_and_generate()

		# Make Serial Number
		self.make_serial_number()

		# Make QR
		if self.x_type in ['ticket_receipt', 'ticket_invoice']:
			self.make_qr()

		# State
		self.state = 'sale'

	# validate

# ----------------------------------------------------------- Check and Generate ----------------------------
	def check_and_generate(self):
		"""
		Check if everything is OK
		And Generate several variables.
		"""
		print()
		print('Check and Generate')

		# Doctor User Name
		self.x_doctor_uid = raw_funcs.get_doctor_uid(self.x_doctor)


		# Date - Must be that of the Sale, not the Budget.
		self.date_order = datetime.datetime.now()

		# Date - Update Day and Month
		ord_funcs.update_day_and_month(self)

		# Update Descriptors (family and product)
		ord_funcs.update_descriptors(self)

		# Vip Card - Detect and Create
		ord_funcs.detect_vip_card_and_create(self)

		# Type
		if self.x_payment_method.saledoc:
			self.x_type = self.x_payment_method.saledoc


		# Create Procedure
		raw_funcs.create_procedure(self.treatment, self.order_line)


		# Id Doc and Ruc
		raw_funcs.check_docs(self.x_type, self.x_ruc, self.x_id_doc, self.x_id_doc_type)

		# Update Patient
		if self.patient.x_id_doc in [False, '']:
			self.patient.x_id_doc_type = self.x_id_doc_type
			self.patient.x_id_doc = self.x_id_doc

		# Change Electronic
		self.x_electronic = True

		# Title
		self.x_title = raw_funcs.get_title(self.x_type)

		# Change State
		self.state = 'validated'

	# check_and_generate


# ----------------------------------------------------------- Make SN - BUtton ----------------------
	# Make Serial Number
	@api.multi
	def make_serial_number(self):
		"""
		Make Serial Number
		This is an example of how you can encapsulte Business Rules.
		In the Libraries.
		"""
		print()
		print('Make Serial Number')
		# Get Next Counter
		self.x_counter_value = ord_funcs.get_next_counter_value(self, self.x_type, self.state)
		# Make Serial Number
		self.x_serial_nr = ord_funcs.get_serial_nr(self.x_type, self.x_counter_value, self.state)

# ----------------------------------------------------------- Make QR - BUtton ----------------------
	# Make QR
	@api.multi
	def make_qr(self):
		"""
		Make QR Image for Electronic Billing
		This is an example of how you can apply the Three Layered Model. To encapsulte Business Rules.
		"""
		print()
		print('Make QR')

		# Create loosely coupled object
		h = self.get_hash_for_qr()
		qr_obj = qr.QR(h)

		# Get data
		name = qr_obj.get_name()
		img_str = qr_obj.get_img_str()

		# Print
		qr_obj.print_obj()

		# Update the Database
		self.write({
						'qr_product_name':name,
						'x_qr_img': img_str,
				})
	# make_qr

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

	x_credit_note_owner = fields.Many2one(
			'sale.order',
			'Documento que modifica',
		)

	x_credit_note = fields.Many2one(
			'sale.order',
			'Nota de Crédito',
		)

# ---------------------------------------------- Credit Note - Block Flow -------------------------
	# Block Flow
	@api.multi
	def block_flow(self):
		"""
		Used by Credit Notes
		"""
		print()
		print('Block Flow')
		if self.state in ['credit_note']:
			self.x_block_flow = True
			self.x_credit_note_owner.x_block_flow = True
		elif self.state in ['sale']:
			self.x_block_flow = True

	# Unblock Flow
	@api.multi
	def unblock_flow(self):
		"""
		Used by Credit Notes
		"""
		print()
		print('Unblock Flow')
		if self.state in ['credit_note']:
			self.x_block_flow = False
			self.x_credit_note_owner.x_block_flow = False

# ---------------------------------------------- Credit Note - Update -----------------------------
	# Update CN
	@api.multi
	def update_credit_note(self):
		"""
		Update Credit note
		"""
		print()
		print('Update CN')
		print(self.x_credit_note_type)

		if self.state in ['credit_note']:
			self.x_credit_note_owner_amount = self.x_credit_note_owner.amount_total
			self.order_line.unlink()
			name = self.x_credit_note_type
			# Search
			product = self.env['product.product'].search([
															('x_name_short', 'in', [name]),
															],
															#order='date_begin asc',
															limit=1,
														)
			print(product)
			product_id = product.id
			print(product_id)
			line = self.order_line.create({
											'product_id': product_id,
											'price_unit': self.x_credit_note_amount,
											'product_uom_qty': 1,
											'order_id': self.id,
										})
	# update_credit_note

# ---------------------------------------------- Credit Note - Create -----------------------------
	# Create CN
	@api.multi
	def create_credit_note(self):
		"""
		Create Credit note
		"""
		print()
		print('Create CN')

		# Init
		state = 'credit_note'

# New - Ord Funcs
		# Get counter
		counter_value = ord_funcs.get_next_counter_value(self, self.x_type, state)

		# Get serial nr
		serial_nr = ord_funcs.get_serial_nr(self.x_type, counter_value, state)

		# Duplicate with different fields
		credit_note = self.copy(default={
											'x_serial_nr': serial_nr,
											'x_counter_value': counter_value,
											'x_credit_note_owner': self.id,
											'x_title': 'Nota de Crédito Electrónica',
											'x_payment_method': False,
											'state': state,
											'amount_total': self.amount_total,
											'amount_untaxed': self.amount_untaxed,
								})
		print(credit_note)

		# Update Self
		self.write({
							'x_credit_note': credit_note.id,
					})
	# create_credit_note

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

	# Date Date
	x_date_order_date = fields.Date(
		'Fecha',
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

# ----------------------------------------------------------- Legacy ------------------------------
	# Legacy
	x_legacy = fields.Boolean(
			'Legacy',
			default=False,
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

# ----------------------------------------------------------- Checksum ----------------------------
	# Checksum
	x_checksum = fields.Float(
			'Checksum',
			readonly=True,
			default=5,
		)

	# Checksum Func
	@api.multi
	def checksum(self):
		"""
		Checksum
		"""		
		#obj = check_order.CheckOrder()
		
		#self.check_payment_method()
		self.x_pm_total = raw_funcs.check_payment_method(self.x_payment_method.pm_line_ids)

		delta = int(self.amount_total) - int(self.x_pm_total)
		if delta != 0:
			self.x_checksum = 1
		else:
			self.x_checksum = 0


	# Pm Total
	x_pm_total = fields.Float(
			'Total MP',
			readonly=True,
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
			selection=pat_vars._id_doc_type_list,
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

# ----------------------------------------------------- Admin --------------------------
	@api.multi
	def correct_serial_number(self):
		"""
		Correct Serial Number - Admin only
		"""
		print()
		print('correct_serial_number')
		self.x_serial_nr = ord_funcs.get_serial_nr(self.x_type, self.x_counter_value, self.state)

# ----------------------------------------------------- Fixers --------------------------
	@api.multi
	def fix_treatment(self):
		"""
		Fix Treatment
		"""
		print()
		print('Fix Treatment')
		fixer = fix_treatment.FixTreatment(self.env['openhealth.treatment'], self.patient.id, self.x_doctor.id)
		fixer.fix()

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
	# States
	READONLY_STATES = {
		'draft': 		[('readonly', False)],
		'sent': 		[('readonly', False)],
		'sale': 		[('readonly', True)],
		'cancel': 		[('readonly', True)],
	}

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

	# Order Line
	order_line = fields.One2many(
			'sale.order.line',
			'order_id',
			string='Order Lines',
			#states=READONLY_STATES, 			# Done by the View
		)

	# Receptor
	pl_receptor = fields.Char(
			string='Receptor',
		)

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


# ---------------------------------- Partner - Not Dep -------------------------
	# Partner
	@api.onchange('partner_id')
	def _onchange_partner_id(self):
		print('_onchange_partner_id')
		print(self.pricelist_id)
		if self.partner_id.name != False:
			self.x_partner_dni = self.partner_id.x_dni
		print(self.pricelist_id)

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

	# On Change Partner Dni
	@api.onchange('x_partner_dni')
	def _onchange_x_partner_dni(self):
		self.patient = ord_funcs.search_patient_by_id_document(self)

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

# ---------------------------------------------- Create Payment Method - Button Pagar ----------------------------
	@api.multi
	def create_payment_method(self):
		"""
		Button Pagar
		"""
		# Update Descriptors
		ord_funcs.update_descriptors(self)
		env = self.env['openhealth.payment_method']
		self.x_payment_method, ret = raw_funcs.create_pm(env, self.id, self.date_order, self.x_amount_total, self.partner_id.id, self.patient.x_firm, self.patient.x_ruc)
		return ret

# ----------------------------------------------------------- Print -------------------------------
	@api.multi
	def print_ticket_electronic(self):
		"""
		Check and Print Ticket Electronic
		"""
		print('')
		print('Print Electronic')

		# Check Patient for Ticket
		ord_funcs.check_ticket(self, self.x_type, self.state)

		# Print
		name = 'openhealth.report_ticket_receipt_electronic'
		action = self.env['report'].get_action(self, name)
		return action

#----------------------------------------------------------- Quick Button - For Treatment ---------
	@api.multi
	def open_line_current(self):
		"""
		Used by Treatment
		"""
		print('open_line_current')
		res_model = self._name
		res_id = self.id
		return action_funcs.open_line_current(res_model, res_id)

#----------------------------------------------------------- Qpen myself --------------------------
	@api.multi
	def open_myself(self):
		"""
		Open myself - Used by Payment Method comeback
		"""
		print('open_myself')
		res_model = self._name
		res_id = self.id
		return action_funcs.open_myself(res_model, res_id)


# ----------------------------------------------------------- Remove and Reset ------------
	# Reset
	@api.multi
	def reset(self):
		"""
		Reset order
		"""
		self.x_payment_method.unlink()
		self.state = 'draft'


	# Remove - Protected for Sales
	@api.multi
	def remove_myself(self):
		"""
		Remove myself
		"""
		if self.state in ['credit_note']:
			#raise UserError("Advertencia: La Nota de Crédito va a ser eliminada del sistema !")
			self.reset()
			self.unlink()
		else:
			#raise UserError("Advertencia: La Venta va a ser convertida en Presupuesto !")
			self.reset()


	# Remove Force
	@api.multi
	def remove_myself_force(self):
		"""
		high level support for doing this and that.
		"""
		self.reset()
		self.unlink()


# ---------------------------------------------- Cancel and Activate -------------------------------------------
	x_cancel = fields.Boolean(
			string='',
			default=False
		)

	@api.multi
	def cancel_order(self):
		"""
		Cancel Order
		"""
		self.x_cancel = True
		self.state = 'cancel'

	@api.multi
	def activate_order(self):
		"""
		Activate Order
		"""
		self.x_cancel = False
		self.state = 'sale'

# ----------------------------------------------------------- Test --------------------------------
	def pay_myself(self):
		"""
		Pay Myself
		Used by Treatment Test
		"""
		print()
		print('Order - Pay myself')
		test_order.pay_myself(self)

# ----------------------------------------------------------- QR - tools --------------------------------
	def get_hash_for_qr(self):
		"""
		QR Tool
		"""
		# Init vars
		#ruc_company = self.configurator.company_ruc
		ruc_company = '12345678901'
		x_type = self.x_type
		serial_nr = self.x_serial_nr
		amount_total = self.amount_total
		total_tax = self.x_total_tax
		date = self.date_order
		receptor_id_doc_type = self.x_id_doc_type
		receptor_id_doc = self.x_id_doc
		receptor_ruc = self.x_ruc

		h = {}
		h['ruc_company'] = str(ruc_company)
		h['x_type'] = str(x_type)
		h['serial_nr'] = str(serial_nr)
		h['amount_total'] = str(amount_total)
		h['total_tax'] = str(total_tax)
		h['date'] = str(date)
		h['receptor_id_doc_type'] = str(receptor_id_doc_type)
		h['receptor_id_doc'] = str(receptor_id_doc)
		h['receptor_ruc'] = str(receptor_ruc)

		return h

# ----------------------------------------------------------- Test QR --------------------------------
	@api.multi
	def test_qr(self):
		"""
		Test QR
		"""
		print()
		print('order - test_qr')

		# Create loosely coupled object
		h = self.get_hash_for_qr()
		qr_obj = qr.QR(h)

		# Get data
		print(qr_obj.get_name())
		print(qr_obj.get_img_str())
		#qr_obj.print_obj()


# ----------------------------------------------------------- Ticket - tools --------------------------------
	def get_company(self, tag):
		"""
		Used by Ticket
		"""
		options = {
			'name' : self.configurator.company_name,
			'ruc' : self.configurator.ticket_company_ruc,
			'address' : self.configurator.ticket_company_address,
			'phone' : self.configurator.company_phone,
			'note' : self.configurator.ticket_note,
			'description' : self.configurator.ticket_company_address,
			'warning' : self.configurator.ticket_warning,
			'website' : self.configurator.company_website,
			'email' : self.configurator.company_email,
		}
		return options[tag]


	def get_ticket(self, item):
		"""
		Used by Ticket
		"""
		if item == 'title':
			ret = self.x_title
		elif item == 'serial_nr':
			ret = self.x_serial_nr
		return ret

# ----------------------------------------------------------- Ticket - Get Raw Line - Stub ----------------
	def get_ticket_line(self, tag):
		"""
		Uses the Ticket class.
		"""
		print()
		print('get_ticket_line')
		#line = raw_funcs.get_ticket_raw_line(self, tag)
		print(tag)

		if tag in ['Cliente']:
			value = self.patient.name
		elif tag in ['DNI']:
			value = self.x_id_doc
		elif tag in ['Direccion']:
			value = self.patient.x_address
		elif tag in ['Fecha']:
			value = raw_funcs.get_date_corrected(self.date_order)
		elif tag in ['Ticket']:
			value = self.x_serial_nr

		obj = ticket_line.TicketLine(tag, value)

		line = obj.get_line()

		return line

# ----------------------------------------------------------- Ticket - Get Raw Line - Stub ----------------
	def get_items_header(self, tag):
		"""
		Uses the Ticket class.
		"""
		print()
		print('get_items_header')
		if tag in ['items_header']:
			tag = 'items'
			value = 'header'
		obj = ticket_line.TicketLine(tag, value)
		line = obj.get_line_items()
		return line

# ----------------------------------------------------------- Ticket - Get Raw Line - Aux ----------------
	#def get_total_net(self):
	#def get_total_tax(self):

	def get_amount_total(self):
		"""
		Used by Print Ticket.
		Is zero if Transfer Free.
		"""
		if self.pl_transfer_free:
			total = 0
		else:
			total = tick_funcs.get_total(self)
		return total

	def get_total_in_words(self):
		"""
		Used by Print Ticket.
		"""
		if self.pl_transfer_free:
			words = 'Cero'
		else:
			words = tick_funcs.get_words(self)
		return words

	def get_total_cents(self):
		"""
		Used by Print Ticket.
		"""
		if self.pl_transfer_free:
			cents = '0.0'
		else:
			cents = tick_funcs.get_cents(self)
		return cents

# ----------------------------------------------------------- Ticket - Get Raw Line - Stub ----------------
	def get_raw_line(self, argument):
		"""
		Uses the Ticket class.
		"""
		print()
		print('get_raw_line')
		print(argument)

		# Default
		tag = 'TOTAL S/.'
		value = str(self.get_amount_total())

		# Totals
		if argument in ['totals_net']:
			tag = 'OP. GRAVADAS S/.'
			#value = str(self.get_total_net())
			value = str(raw_funcs.get_total_net(self.amount_total, self.pl_transfer_free))

		elif argument in ['totals_free']:
			tag = 'OP. GRATUITAS S/.'
			value = '0'

		elif argument in ['totals_exonerated']:
			tag = 'OP. EXONERADAS S/.'
			value = '0'

		elif argument in ['totals_unaffected']:
			tag = 'OP. INAFECTAS S/.'
			value = '0'

		elif argument in ['totals_tax']:
			tag = 'I.G.V. 18% S/.'
			#value = str(self.get_total_tax())
			value = str(raw_funcs.get_total_tax(self.amount_total, self.pl_transfer_free))

		#elif argument in ['totals_total']:
		#	tag = 'TOTAL S/.'
		#	value = str(self.get_amount_total())

		obj = ticket_line.TicketLine(tag, value)
		line = obj.get_line()
		return line

# ----------------------------------------------------------- Ticket - Get Raw Line - Stub ----------------
	def get_words_line(self, argument):
		"""
		Uses the Ticket class.
		"""
		print()
		print('get_words_line')
		print(argument)

		# Words
		if argument in ['words_header']:
			tag = 'Son:'
			value = ''
		elif argument in ['words_soles']:
			tag = ''
			value = str(self.get_total_in_words())
		elif argument in ['words_cents']:
			tag = ''
			value = str(self.get_total_cents())
		elif argument in ['words_footer']:
			tag = ''
			value = 'Soles'

		obj = ticket_line.TicketLine(tag, value)
		line = obj.get_line()
		return line

# ----------------------------------------------------------- Test Ticket --------------------------------
	@api.multi
	def test_ticket(self):
		"""
		Test Ticket
		"""
		print('')
		print('Test Ticket')
		name = 'openhealth.report_ticket_receipt_electronic'
		action = self.env['report'].get_action(self, name)
		return action

# ----------------------------------------------------------- Test Validation --------------------------------
	@api.multi
	def test_validation(self):
		"""
		Test Validation
		"""
		print('')
		print('Test Validation')
		self.validate_and_confirm()

# ----------------------------------------------------------- Test Payment method --------------------------------
	@api.multi
	def test_pm(self):
		"""
		Test Payment method
		"""
		print('')
		print('test_pm')
		self.create_payment_method()


# ----------------------------------------------------------- Test Payment method --------------------------------
	@api.multi
	def test_serial_number(self):
		"""
		Test Serial Number
		"""
		print('')
		print('test_serial_number')
		self.make_serial_number()

# ----------------------------------------------------- Test --------------------------
	@api.multi
	def test(self):
		"""
		Unit Testing - All
		"""
		print()
		print('Test Order')
		#tester = TestOrder(self)
		#tester.test_raw_receipt(self)
		#tester.test_raw_invoice(self)
		#tester.test_raw_credit_note(self)
		#tester.test_serial_number(self)
		#action0 = self.test_raw_receipt()
		#return action0
		#action1 = self.test_raw_invoice()
		#return action1
		#action2 = self.test_raw_credit_note()
		#return action2
		#self.test_serial_number()
		#return action0, action1, action2


# ---------------------------------------------------- Used by Treatment - Create Proc -------
	def create_procedure_man(self, treatment):
		"""
		Create Procedure Man - In prog
		Used by: Treatment
		"""
		# Update Order
		self.set_procedure_created()
		# Loop
		for line in self.order_line:
			print(line.product_id)
			if line.product_id.is_procedure():
				product_product = line.product_id
				# Create Procedure
				#pl_creates.create_procedure_go(treatment, product_product)
				pl_creates.create_procedure(treatment, product_product)

	def set_procedure_created(self, value=True):
		"""
		Set Procedure Created
		Used by: Treatment and Order
		"""
		print()
		print('order - set_procedure_created')
		self.x_procedure_created = value

	def proc_is_not_created_and_state_is_sale(self):
		"""
		Used by: Treatment
		"""
		print()
		print('order - proc_is_not_created_and_state_is_sale')
		return not self.x_procedure_created and self.state == 'sale'
