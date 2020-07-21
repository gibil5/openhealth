# -*- coding: utf-8 -*-
"""
	Order
		Created: 			26 Aug 2016
		Last mod: 			20 Jul 2020
"""
from __future__ import print_function
import datetime
from openerp import models, fields, api
from openerp import _
from openerp.exceptions import Warning as UserError
from openerp.addons.openhealth.models.libs import lib
from openerp.addons.openhealth.models.patient import pat_vars, chk_patient
from . import test_order
from . import chk_order
from . import exc_ord
from . import tick_funcs
from . import ord_vars
from . import ord_funcs
from . import raw_funcs
from . import qr

class sale_order(models.Model):
	"""
	Sale Class - Inherited from the medical Module OeHealth. Has the Business Logic of the Clinic.
	This is only a Data Model. Must NOT contain Business Rules.
	All BRs should be in Classes and Libraries.
	"""
	_inherit = 'sale.order'
	_description = 'Order'

# ----------------------------------------------------------- Fields -------------------------------
	# Transfer Free
	pl_transfer_free = fields.Boolean(
			'TRANSFERENCIA GRATUITA',

			default=False,
		)

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


# --------------------------------- Price List - Computes ----------------------
	# Price List
	pl_price_list = fields.Char(
			string="Pl - Price List",
			compute='_compute_pl_price_list',
		)

	@api.multi
	def _compute_pl_price_list(self):
		for record in self:
			price_list = ''
			for line in record.order_line:
				price_list =line.get_price_list()
			record.pl_price_list = price_list

	x_amount_flow = fields.Float(
			'Pl - Total F',
			compute='_compute_x_amount_flow',
		)

	@api.multi
	def _compute_x_amount_flow(self):
		for record in self:
			if record.x_block_flow:
				record.x_amount_flow = 0
			elif record.state in ['credit_note']  and  record.x_credit_note_amount not in [0, False]:
				record.x_amount_flow = - record.x_credit_note_amount
			else:
				record.x_amount_flow = record.amount_total

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


# ---------------------------------------------- Price List - Fields ------------------------------------------
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

	# Receptor
	pl_receptor = fields.Char(
			string='Receptor',
		)


# ----------------------------------------------------------- Configurator -------------------------
	def _get_default_configurator(self):
		print()
		print('Default Configurator')
		# Search
		configurator = self.env['openhealth.configurator.emr'].search([
												#('active', 'in', [True]),
												],
												#order='x_serial_nr asc',
												limit=1,
											)
		return configurator

	configurator = fields.Many2one(
			'openhealth.configurator.emr',
			string="Config",
			required=True,
			readonly=True,
			default=_get_default_configurator,
		)


# ---------------------------------- Partner - Not Dep -------------------------
	# On Change Partner
	@api.onchange('partner_id')
	def _onchange_partner_id(self):
		if self.partner_id.name != False:
			self.x_partner_dni = self.partner_id.x_dni

	# DNI - Used by Budget - Allows research of Patient by DNI - Important
	x_partner_dni = fields.Char(
			string='DNI',
			states={	'draft': 	[('readonly', False)],
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
	# _onchange_x_partner_dni

# ------------------------------- Used by - Print Ticket - Header and Footer ---
	def get_title(self):
		return self.x_title

	def get_serial_nr(self):
		return self.x_serial_nr

	def get_firm_address(self):
		return self.patient.x_firm_address

	def get_patient_address(self):
		return self.patient.x_address

	def get_note(self):
		if self.pl_transfer_free:
			note = 'TRANSFERENCIA A TITULO GRATUITO'
		else:
			if self.x_type in ['ticket_receipt']:
				note = 'Representación impresa de la BOLETA DE VENTA ELECTRONICA.'
			elif self.x_type in ['ticket_invoice']:
				note = 'Representación impresa de la FACTURA DE VENTA ELECTRONICA.'
			else:
				note = ''
		return note

# ----------------------------------------------------------- Ticket - Get Raw Line - Stub ----------------
	def get_raw_line(self, argument):
		"""
		Just a stub.
		"""
		line = raw_funcs.get_ticket_raw_line(self, argument)
		return line


# ----------------------------------------------------------- Ticket - Header - Getters ----------------

	# Company Address
	def get_company_name(self):
		company_name = self.configurator.company_name
		return company_name

	# Company Address
	def get_company_address(self):
		company_address = self.configurator.ticket_company_address
		return company_address

	# Company Address
	def get_company_phone(self):
		company_phone = self.configurator.company_phone
		return company_phone

	# Company Address
	def get_company_ruc(self):
		company_ruc = self.configurator.ticket_company_ruc
		return company_ruc



# ----------------------------------------------------------- Ticket - Footer - Getters ----------------

	# Description
	def get_description(self):
		description = self.configurator.ticket_description
		return description


	# Warning
	def get_warning(self):
		warning = self.configurator.ticket_warning
		return warning


	# Website
	def get_website(self):
		website = self.configurator.website
		return website


	# Email
	def get_email(self):
		email = self.configurator.email
		return email




# ----------------------------------------------------------- Print Ticket - Amounts -------------------------------

	def get_amount_total(self):
		"""
		Used by Print Ticket.
		Is zero if Transfer Free.
		"""
		#print()
		#print('Get Amount Total')

		if self.pl_transfer_free:
			total = 0

		else:
			total = tick_funcs.get_total(self)

		#return tick_funcs.get_total(self)
		return total




	def get_total_net(self):
		"""
		Used by Print Ticket.
		Is zero if Transfer Free.
		"""
		#print()
		#print('Get Total Net')

		if self.pl_transfer_free:
			self.x_total_net = 0

		else:
			self.x_total_net =  tick_funcs.get_net(self)

		return self.x_total_net



	def get_total_tax(self):
		"""
		Used by Print Ticket.
		Is zero if Transfer Free.
		"""
		#print()
		#print('Get Total Tax')

		if self.pl_transfer_free:
			self.x_total_tax = 0

		else:
			self.x_total_tax = tick_funcs.get_tax(self)

		return self.x_total_tax



	def get_total_in_words(self):
		"""
		Used by Print Ticket.
		"""
		#print()
		#print('Get Total Words')

		if self.pl_transfer_free:
			words = 'Cero'

		else:
			words = tick_funcs.get_words(self)

		#return tick_funcs.get_words(self)
		return words



	def get_total_cents(self):
		"""
		Used by Print Ticket.
		"""
		#print()
		#print('Get Total Cents')

		if self.pl_transfer_free:
			cents = '0.0'

		else:
			cents = tick_funcs.get_cents(self)

		#return tick_funcs.get_cents(self)
		return cents





# ----------------------------------------------------------- Natives  - Computes OK -------------------------

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


	# Partner Vip - OK
	x_partner_vip = fields.Boolean(
			'Vip',
			default=False,

			compute="_compute_partner_vip",
		)

	@api.multi
	def _compute_partner_vip(self):
		for record in self:
			count = self.env['openhealth.card'].search_count([
																('patient_name', '=', record.partner_id.name),
														])
			if count == 0:
				record.x_partner_vip = False
			else:
				record.x_partner_vip = True





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


# ----------------------------------------------------------- Natives  - Killed Computes -------------------------
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
	#def validate(self):
	def validate_and_confirm(self):
		"""
		Validate the order. Before Confirmation.
		"""
		print()
		print('Validate')


		# Handle Exceptions
		exc_ord.handle_exceptions(self)


		# If Everything is OK
		self.check_and_generate()



		# Make Serial Number
		#if self.x_serial_nr != '' and not self.x_admin_mode:
		#if self.state in ['validated']  and  self.x_serial_nr != '' and not self.x_admin_mode:

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


		# Payment method validation
		self.check_payment_method()


		# Doctor User Name
		if self.x_doctor.name != False:
			uid = self.x_doctor.x_user_name.id
			self.x_doctor_uid = uid



		# Date - Must be that of the Sale, not the Budget.
		self.date_order = datetime.datetime.now()



		# Date - Update Day and Month
		ord_funcs.update_day_and_month(self)


		# Update Descriptors (family and product)
		ord_funcs.update_descriptors(self)




		# Vip Card - Detect and Create
		ord_funcs.detect_vip_card_and_create(self)





		# Type
		if self.x_payment_method.saledoc != False:
			self.x_type = self.x_payment_method.saledoc


		# Create Procedure
		print('Create Procedure')

		if self.treatment.name != False:
			for line in self.order_line:

				# Init
				product = line.product_id

				# Conditional
				if product.is_procedure():
					self.treatment.create_procedure_auto(product)


				line.update_recos()


			# Update Order
			#self.x_procedure_created = True
			self.set_procedure_created(True)



		# Id Doc and Ruc
		# Invoice
		if self.x_type in ['ticket_invoice', 'invoice']:
			if self.x_ruc in [False, '']:
				msg = "Error: RUC Ausente."
				raise UserError(_(msg))

		# Receipt
		elif self.x_type in ['ticket_receipt', 'receipt']:
			if self.x_id_doc_type in [False, '']  or self.x_id_doc in [False, '']:
				msg = "Error: Documento de Identidad Ausente."
				raise UserError(_(msg))


		# Update Patient
		if self.patient.x_id_doc in [False, '']:
			self.patient.x_id_doc_type = self.x_id_doc_type
			self.patient.x_id_doc = self.x_id_doc


		# Change Electronic
		self.x_electronic = True


		# Title
		if self.x_type in ['ticket_receipt', 'receipt']:
			self.x_title = 'Boleta de Venta Electrónica'
		elif self.x_type in ['ticket_invoice', 'invoice']:
			self.x_title = 'Factura de Venta Electrónica'
		else:
			self.x_title = 'Venta Electrónica'



		# QR
		#if self.x_type in ['ticket_receipt', 'ticket_invoice']:
		#	self.make_qr()


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

		# Init vars
		ruc_company = self.configurator.company_ruc

		x_type = self.x_type

		serial_nr = self.x_serial_nr
		amount_total = self.amount_total
		total_tax = self.x_total_tax
		date = self.date_order
		receptor_id_doc_type = self.x_id_doc_type
		receptor_id_doc = self.x_id_doc
		receptor_ruc = self.x_ruc

		# Create Object
		qr_obj = qr.QR(date, ruc_company, receptor_id_doc_type, receptor_id_doc, receptor_ruc, x_type, serial_nr, amount_total, total_tax)

		# Get data
		img_str = qr_obj.get_img_str()
		name = qr_obj.get_name()

		# Print
		qr_obj.print_obj()

		# Update the Database
		self.write({
						'x_qr_img': img_str,
						'qr_product_name':name,
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
		high level support for doing this and that.
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
		high level support for doing this and that.
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
		high level support for doing this and that.
		"""
		#print
		#print 'CheckSum'
		self.check_payment_method()
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

	# Check payment method
	@api.multi
	def check_payment_method(self):
		"""
		high level support for doing this and that.
		"""
		#print
		#print 'Check Payment Method'
		pm_total = 0
		for pm in self.x_payment_method.pm_line_ids:
			pm_total = pm_total + pm.subtotal
		self.x_pm_total = pm_total



# ----------------------------------------------------------- Serial Nr ---------------------------

	# Serial Number
	x_serial_nr = fields.Char(
			'Número de serie',
		)

	# Counter Value
	x_counter_value = fields.Integer(
			string="Contador",
		)


# ----------------------------------------------------------- Constraints - Sql -------------------
	# Uniqueness constraints for:
	# Serial Number
	_sql_constraints = [
				#('x_serial_nr','unique(x_serial_nr)', 'SQL Warning: x_serial_nr must be unique !'),
				('x_serial_nr', 'Check(1=1)', 'SQL Warning: x_serial_nr must be unique !'),
			]

# ----------------------------------------------------------- Constraints - From Chk Patient ------

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

	# Check Serial Nr
	@api.constrains('x_serial_nr')
	def _check_x_serial_nr(self):
		chk_order.check_serial_nr(self)



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


# ----------------------------------------------------------- Correct -----------------------------
	# Correct payment method
	@api.multi
	def correct_pm(self):
		#print
		#print 'Correct Payment Method'


		if self.x_payment_method.name == False:
			self.x_payment_method = self.env['openhealth.payment_method'].create({
																					'order': 	self.id,
																					'partner':	self.partner_id.id,
																					'total':	self.amount_total,
																			})
		res_id = self.x_payment_method.id

		return {
			# Mandatory
			'type': 'ir.actions.act_window',
			'name': 'Open Payment Method Current',
			# Window action
			'res_id': res_id,
			'res_model': 'openhealth.payment_method',
			# Views
			"views": [[False, "form"]],
			'view_mode': 'form',
			'target': 'current',
			#'view_id': view_id,
			#"domain": [["patient", "=", self.patient.name]],
			#'auto_search': False,
			'flags': {
						'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
						#'form': {'action_buttons': True, }
						#'form': {'action_buttons': False, }
					},
			'context': {}
		}
	# correct_pm


# ----------------------------------------------------------- Pay ---------------------------------
	# DNI
	x_dni = fields.Char(
			string='DNI',
			readonly=True,
		)

	# RUC
	x_ruc = fields.Char(
			string='RUC',
			#readonly=True,
		)

# ----------------------------------------------------------- Locked - By State -------------------

	# States
	READONLY_STATES = {
		'draft': 		[('readonly', False)],
		'sent': 		[('readonly', False)],
		'sale': 		[('readonly', True)],
		'cancel': 		[('readonly', True)],
	}

	# Patient
	patient = fields.Many2one(
			'oeh.medical.patient',
			string='Paciente',
			#states=READONLY_STATES,
		)

	# Doctor
	x_doctor = fields.Many2one(
			'oeh.medical.physician',
			string="Médico",
			states=READONLY_STATES,
		)

	# Order Line
	order_line = fields.One2many(
			'sale.order.line',
			'order_id',
			string='Order Lines',
			#states=READONLY_STATES, 			# Done by the View
		)


# ----------------------------------------------------------- On Changes --------------------------

	# Patient
	@api.onchange('patient')
	def _onchange_patient(self):
		#print
		#print 'On Change Patient'

		if self.patient.name != False:

			# Init
			self.x_ruc = False
			self.partner_id = self.patient.partner_id.id

			# Id Doc
			if self.patient.x_id_doc != False:
				self.x_id_doc = self.patient.x_id_doc
				self.x_id_doc_type = self.patient.x_id_doc_type

			# Get x Dni
			elif self.patient.x_dni not in [False, '']:
				self.x_id_doc = self.patient.x_dni
				self.x_id_doc_type = 'dni'
				self.x_dni = self.patient.x_dni

			# Ruc
			if self.patient.x_ruc != False:
				self.x_ruc = self.patient.x_ruc



	# Doctor
	@api.onchange('x_doctor')
	def _onchange_x_doctor(self):
		if self.x_doctor.name != False:
			treatment = self.env['openhealth.treatment'].search([
																	('patient', '=', self.patient.name),
																	('physician', '=', self.x_doctor.name),
													],
														order='write_date desc',
														limit=1,
													)
			self.treatment = treatment


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

	# Pricelist
	pricelist_id = fields.Many2one(
			'product.pricelist',
			string='Pricelist',
			readonly=True,
			states={'draft': [('readonly', False)], 'sent': [('readonly', False)]},
			help="Pricelist for current sales order.",
			required=True,
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


# ----------------------------------------------------------- Primitives --------------------------

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

		# Init vars
		name = 'Pago'
		method = 'cash'
		balance = self.x_amount_total
		firm = self.patient.x_firm
		ruc = self.patient.x_ruc

		# Create
		self.x_payment_method = self.env['openhealth.payment_method'].create({
																				'order': self.id,
																				'method': method,
																				'subtotal': balance,
																				'total': self.x_amount_total,
																				'partner': self.partner_id.id,
																				'date_created': self.date_order,
																				'firm': firm,
																				'ruc': ruc,
																			})
		payment_method_id = self.x_payment_method.id

		# Create Lines
		name = '1'
		method = 'cash'
		subtotal = self.x_amount_total
		payment_method = self.x_payment_method.id

		self.x_payment_method.pm_line_ids.create({
																	'name': name,
																	'method': method,
																	'subtotal': subtotal,
																	'payment_method': payment_method,
										})

		return {
				'type': 'ir.actions.act_window',
				'name': ' New PM Current',
				'view_type': 'form',
				'view_mode': 'form',
				'target': 'current',
				'res_model': 'openhealth.payment_method',
				'res_id': payment_method_id,
				'flags': 	{
							#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
							#'form': {'action_buttons': False, }
							'form':{'action_buttons': False, 'options': {'mode': 'edit'}}
							},
				'context': {
							'default_order': self.id,
							'default_name': name,
							'default_method': method,
							'default_subtotal': balance,
							'default_total': self.x_amount_total,
							'default_partner': self.partner_id.id,
							'default_date_created': self.date_order,
							'default_firm': firm,
							'default_ruc': ruc,
							}
				}
	# create_payment_method


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
		# Quick access Button
		"""
		consultation_id = self.id
		return {
				'type': 'ir.actions.act_window',
				'name': ' Edit Order Current',
				'view_type': 'form',
				'view_mode': 'form',

				'res_model': self._name,
				'res_id': consultation_id,

				'target': 'current',
				'flags': {
						#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
						'form': {'action_buttons': True, }
						},
				'context': {}
		}


#----------------------------------------------------------- Qpen myself --------------------------
	@api.multi
	def open_myself(self):
		"""
		For Payment Method comeback
		"""
		order_id = self.id
		return {
			# Mandatory
			'type': 'ir.actions.act_window',
			'name': 'Open Order Current',
			# Window action
			'res_model': 'sale.order',
			'res_id': order_id,
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
			'context':   {

			}
		}
	# open_myself


# ----------------------------------------------------------- Remove and Reset ------------
	# Reset
	@api.multi
	def reset(self):
		"""
		high level support for doing this and that.
		"""
		self.x_payment_method.unlink()
		self.state = 'draft'


	# Remove - Protected for Sales
	@api.multi
	def remove_myself(self):
		"""
		high level support for doing this and that.
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


# ---------------------------------------------- Cancel -------------------------------------------
	# Cancel
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
