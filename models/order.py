# -*- coding: utf-8 -*-
"""
	Order

	Created: 			26 Aug 2016
	Last mod: 			 5 Nov 2018
"""
from __future__ import print_function

import math
import datetime
try:
	from num2words import num2words
except (ImportError, IOError) as err:
	_logger.debug(err)
from openerp import models, fields, api
from openerp import _
from openerp.exceptions import Warning as UserError
from . import ord_vars
from . import creates
from . import pat_vars
from . import user
from . import lib_qr
from . import chk_patient
from . import test_order

class sale_order(models.Model):
	"""
	high level support for doing this and that.
	"""
	_inherit = 'sale.order'


# ----------------------------------------------------------- Dep ? -------------------------------



# ----------------------------------------------------------- Legacy ------------------------------
	# Legacy
	x_legacy = fields.Boolean(
			'Legacy',
			default=False,
		)


	# Update Legacy Jan
	@api.multi
	def update_legacy_jan(self):
		"""
		high level support for doing this and that.
		"""
		orders = self.env['sale.order'].search([
																('date_order', '>=', '2018-01-01'),
																('date_order', '<', '2018-02-01'),
													],
																order='date_order asc',
																#limit=1000,
												)
		for order in orders:
			order.update_legacy()



	# Update Legacy Fev
	@api.multi
	def update_legacy_fev(self):
		"""
		high level support for doing this and that.
		"""

		orders = self.env['sale.order'].search([
																('date_order', '>=', '2018-02-01'),
																('date_order', '<', '2018-03-01'),
													],
																order='date_order asc',
																#limit=1000,
												)
		for order in orders:
			order.update_legacy()



	# Update Legacy Mar
	@api.multi
	def update_legacy_mar(self):
		"""
		high level support for doing this and that.
		"""
		orders = self.env['sale.order'].search([
																('date_order', '>=', '2018-03-01'),
																('date_order', '<', '2018-03-06'),
													],
																order='date_order asc',
																#limit=1000,
												)
		for order in orders:
			order.update_legacy()
	# update_type_legacy_mar




	# Update Legacy
	@api.multi
	def update_legacy(self):
		"""
		high level support for doing this and that.
		"""
		self.x_legacy = True



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
			#chk_order.check_ruc(self)
			chk_patient.check_x_ruc(self)


	# Check Id doc - Use Chk Patient
	@api.constrains('x_id_doc')
	def _check_x_id_doc(self):
		if self.x_type in ['ticket_receipt', 'receipt']:
			chk_patient.check_x_id_doc(self)



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


	# Make QR
	@api.multi
	def make_qr(self):
		"""
		high level support for doing this and that.
		"""

		# Create Data
		self.x_qr_data = lib_qr.get_qr_data(self)

		# Create Img
		img_str, name = lib_qr.get_qr_img(self.x_qr_data)

		# Update
		self.write({
						'x_qr_img': img_str,
						'qr_product_name':name,
				})

	# make_qr



# ----------------------------------------------------------- Mode Admin --------------------------
	x_admin_mode = fields.Boolean(
			'Modo Admin',
		)


# ----------------------------------------------------------- Credit Note -------------------------


	x_credit_note_type = fields.Selection(
			selection=ord_vars._credit_note_type_list,
			string='Motivo',
		)

	x_credit_note_owner = fields.Many2one(
			'sale.order',
			'Documento que modifica',
		)

	x_credit_note = fields.Many2one(
			'sale.order',
			'Nota de Crédito',
		)


	def get_credit_note_type(self):
		"""
		Used by Print Ticket.
		"""
		_dic_cn = {
					'cancel': 					'Anulación de la operación.',
					'cancel_error_ruc': 		'Anulación por error en el RUC.',
					'correct_error_desc': 		'Corrección por error en la descripción.',
					'discount': 				'Descuento global.',
					'discount_item': 			'Descuento por item.',
					'return': 					'Devolución total.',
					'return_item': 				'Devolución por item.',
					'bonus': 					'Bonificación.',
					'value_drop': 				'Disminución en el valor.',
					'other': 					'Otros.',
		}
		return _dic_cn[self.x_credit_note_type]


# ----------------------------------------------------------- Electronic - Getters ----------------

	def get_patient_address(self):
		"""
		high level support for doing this and that.
		"""
		#print
		#print 'Get Patient Address'
		return self.partner_id.x_address


	def get_firm_address(self):
		"""
		high level support for doing this and that.
		"""
		#print
		#print 'Get Firm Address'
		#return self.partner_id.x_firm_address
		return self.partner_id.x_address


# ----------------------------------------------------------- Onchange - DNI ----------------------
	# Dni
	@api.onchange('x_partner_dni')
	def _onchange_x_partner_dni(self):
		#print
		#print 'On Change - DNI'

		if self.x_partner_dni != False:

			#print 'By Id Doc'

			# Search Patient - by ID IDOC
			patient = self.env['oeh.medical.patient'].search([
																('x_id_doc', '=', self.x_partner_dni),
												],
													order='write_date desc',
													limit=1,
												)
			#print patient.name



			if patient.name == False:

				#print 'By Dni'

				# Search Patient - by DNI
				patient = self.env['oeh.medical.patient'].search([
																	('x_dni', '=', self.x_partner_dni),
													],
														order='write_date desc',
														limit=1,
													)
				#print patient.name

			# Update
			self.patient = patient.id

	# _onchange_x_partner_dni




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


	# Type Code
	x_type_code = fields.Char(
			string='Tipo Codigo',

			compute='_compute_x_type_code',
		)

	@api.multi
	def _compute_x_type_code(self):
		for record in self:
			if record.x_type in ['ticket_receipt', 'ticket_invoice', 'receipt', 'invoice', 'advertisement', 'sale_note']:
				record.x_type_code = ord_vars._dic_type_code[record.x_type]



	# Type
	x_type = fields.Selection(
			[
				('receipt', 'Boleta'),
				('invoice', 'Factura'),
				('advertisement', 'Canje Publicidad'),
				('sale_note', 'Canje NV'),
				('ticket_receipt', 'Ticket Boleta'),
				('ticket_invoice', 'Ticket Factura'),
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
			'context': {
						#'default_order': order_id,
					}
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
			#default=lambda self: user._get_default_id(self, 'patient'),

			#states=READONLY_STATES,
		)

	# Doctor
	x_doctor = fields.Many2one(
			'oeh.medical.physician',
			string="Médico",
			#default=lambda self: user._get_default_id(self, 'doctor'),
			states=READONLY_STATES,
		)

	# Treatment
	treatment = fields.Many2one(
			'openhealth.treatment',
			ondelete='cascade',
			string="Tratamiento",
			states=READONLY_STATES,
		)

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


	# Order Line
	order_line = fields.One2many(
			'sale.order.line',
			'order_id',
			string='Order Lines',
			#states=READONLY_STATES, 			# By XML
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


			#print self.patient.x_id_doc
			#print self.patient.x_id_doc_type


			# Id Doc
			if self.patient.x_id_doc != False:
				self.x_id_doc = self.patient.x_id_doc
				self.x_id_doc_type = self.patient.x_id_doc_type


			# Get x Dni
			elif self.patient.x_dni not in [False, '']:
				self.x_id_doc = self.patient.x_dni
				self.x_id_doc_type = 'dni'
				self.x_dni = self.patient.x_dni

				# Update Patient - Dep
				#self.x_msg = '1'
				#self.patient.x_id_doc = self.patient.x_dni
				#self.patient.x_id_doc_type = 'dni'


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




	# Partner
	@api.onchange('partner_id')
	def _onchange_partner_id(self):
		if self.partner_id.name != False:
			self.x_partner_dni = self.partner_id.x_dni










# ----------------------------------------------------------- Validate ----------------------------

	# Action confirm
	@api.multi
	def validate(self):
		"""
		high level support for doing this and that.
		"""
		#print()
		#print('Validate')


		# Payment method validation
		self.check_payment_method()


		# Doctor User Name
		if self.x_doctor.name != False:
			uid = self.x_doctor.x_user_name.id
			self.x_doctor_uid = uid


		# Date - Must be that of the Sale, not the Budget.
		self.date_order = datetime.datetime.now()


		# Update Descriptors (family and product)
		self.update_descriptors()


		# Change Appointment State - To Invoiced
		self.update_appointment()


		# Vip Card - Detect and Create
		self.detect_create_card()


		# Type
		#print 'Type'
		if self.x_payment_method.saledoc != False:
			self.x_type = self.x_payment_method.saledoc
		#print self.x_type



		# Create Procedure with Appointment
		if self.treatment.name != False:

			for line in self.order_line:

				#print(line.product_id.name)

				if line.product_id.x_family in ['laser', 'medical', 'cosmetology']:

					# Create
					creates.create_procedure_wapp(self, line.product_id.x_treatment, line.product_id.id)

				line.update_recos()
			# Update
			self.x_procedure_created = True
			self.treatment.update_appointments()




		# Id Doc and Ruc
		#print self.x_type
		#print self.x_id_doc
		#print self.x_ruc

		# Invoice
		if self.x_type in ['ticket_invoice', 'invoice']:
			if self.x_ruc in [False, '']:
				msg = "Error: RUC Ausente."
				#raise Warning(_(msg))
				raise UserError(_(msg))

		# Receipt
		elif self.x_type in ['ticket_receipt', 'receipt']:
			if self.x_id_doc_type in [False, '']  or self.x_id_doc in [False, '']:
				msg = "Error: Documento de Identidad Ausente."
				#raise Warning(_(msg))
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



		# Change State
		self.state = 'validated'
	# validate



# ----------------------------------------------------------- Action Confirm ----------------------

	# Action confirm
	@api.multi
	def action_confirm_nex(self):
		"""
		high level support for doing this and that.
		"""
		#print
		#print 'Action confirm - Nex'


		#Write your logic here - Begin

		# Generate Serial Number
		#if self.x_serial_nr != '' and self.x_admin_mode == False:
		if self.x_serial_nr != '' and not self.x_admin_mode:


			# Prefix
			#prefix = ord_vars._dic_prefix[self.x_type]

			# Padding
			#padding = ord_vars._dic_padding[self.x_type]

			# Serial Nr
			#self.x_serial_nr = prefix + self.x_separator + str(self.x_counter_value).zfill(padding)



			# Counter
			#self.x_counter_value = user.get_counter_value(self)
			self.x_counter_value = user.get_counter_value(self, self.x_type, self.state)

			# Serial Nr
			#self.x_serial_nr = user.get_serial_nr(self.x_type, self.x_counter_value)
			self.x_serial_nr = user.get_serial_nr(self.x_type, self.x_counter_value, self.state)




		#Write your logic here - End


		# The actual procedure
		#res = super(sale_order, self).action_confirm()
		super(sale_order, self).action_confirm()


		#Write your logic here



		# QR
		if self.x_type in ['ticket_receipt', 'ticket_invoice']:
			self.make_qr()

	# action_confirm_nex




# ---------------------------------------------- Credit Note --------------------------------------
	# Duplicate
	@api.multi
	def create_credit_note(self):
		"""
		high level support for doing this and that.
		"""
		#print
		#print 'Create CN'


		# State
		state = 'credit_note'

		# Counter
		counter_value = user.get_counter_value(self, self.x_type, state)

		# Serial Nr
		serial_nr = user.get_serial_nr(self.x_type, counter_value, state)




		# Duplicate with different fields
		credit_note = self.copy(default={
											'x_serial_nr': serial_nr,
											'x_counter_value': counter_value,
											'x_credit_note_owner': self.id,
											'amount_total': self.amount_total,
											'amount_untaxed': self.amount_untaxed,
											'x_title': 'Nota de Crédito Electrónica',
											'state': state,

											'x_payment_method': False,
								})
		#print credit_note


		# Counter
		#credit_note.x_counter_value = user.get_counter_value(credit_note)
		#x_counter_value = user.get_counter_value(credit_note)
		#print x_counter_value


		# Update Self
		#ret = self.write({
		self.write({
							'x_credit_note': credit_note.id,
						})







# ----------------------------------------------------------- Create Card -------------------------

	# Create Card Vip
	@api.multi
	def detect_create_card(self):
		"""
		high level support for doing this and that.
		"""

		# Detect if Card in Sale
		sale_card = False

		for line in self.order_line:
			if line.product_id.x_name_short == 'vip_card':
				sale_card = True




		# If Card in Sale
		if sale_card:


			# Search Card in the Db
			card = self.env['openhealth.card'].search([('patient_name', '=', self.partner_id.name),], order='date_created desc', limit=1)



			# If it does not exist - Create
			if card.name == False:
				card = self.env['openhealth.card'].create({
																'patient_name': self.partner_id.name,
															})




			# Update Partner - Vip Price List
			pl = self.env['product.pricelist'].search([
															('name', '=', 'VIP'),
													],
															#order='appointment_date desc',
															limit=1,)
			self.partner_id.property_product_pricelist = pl



	# detect_create_card









# ----------------------------------------------------------- Vars --------------------------------

	# Delta
	x_delta = fields.Integer(
			'Delta',
		)



	# Date
	date_order = fields.Datetime(
		states={
					'draft': [('readonly', False)],
					'sent': [('readonly', False)],
					'sale': [('readonly', True)],
				},

		index=True,
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


	# Nr lines
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
			#for l in record.order_line:
			for _ in record.order_line:
				ctr = ctr + 1
			record.nr_lines = ctr



	# Partner Vip
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




# ----------------------------------------------------------- Primitives --------------------------

	# Blank line
	vspace = fields.Char(
			' ',
			readonly=True
		)


# ----------------------------------------------------- Product Selector --------------------------

	@api.multi
	def open_product_selector_product(self):
		"""
		high level support for doing this and that.
		"""
		return self.open_product_selector('product')


	@api.multi
	def open_product_selector_service(self):
		"""
		high level support for doing this and that.
		"""
		return self.open_product_selector('service')


	# Buttons  - Agregar Producto Servicio
	@api.multi
	def open_product_selector(self, x_type):
		"""
		high level support for doing this and that.
		"""

		# Init Vars
		#context = self._context.copy()
		order_id = self.id
		res_id = False

		# Search Model - Dep ?
		#res = self.env['openhealth.product.selector'].search([],
																#order='write_date desc',
		#														limit=1,
		#											)
		return {
				'type': 'ir.actions.act_window',
				'name': ' New Orderline Selector Current',
				'view_type': 'form',
				'view_mode': 'form',
				#'target': 'current',
				'target': 'new',

				'res_id': res_id,

				#'res_model': 'sale.order.line',
				'res_model': 'openhealth.product.selector',
				'flags': 	{
								#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
								#'form': {'action_buttons': False, }
								'form':{'action_buttons': False, 'options': {'mode': 'edit'}}
							},
				'context': {
								'default_order_id': order_id,
								'default_x_type': x_type,
					}}
	# open_product_selector






# ----------------------------------------------------------- Print Tickets -----------------------

	# Total in Words
	x_total_in_words = fields.Char(
			"",

			compute='_compute_x_total_in_words',
		)

	@api.multi
	#@api.depends('')
	def _compute_x_total_in_words(self):
		for record in self:
			words = num2words(record.amount_total, lang='es')
			if 'punto' in words:
				words = words.split('punto')[0]
			record.x_total_in_words = words.title()



	# Total in cents
	x_total_cents = fields.Integer(
			"Céntimos",

			compute='_compute_x_total_cents',
		)

	@api.multi
	#@api.depends('')
	def _compute_x_total_cents(self):
		for record in self:
			frac, whole = math.modf(record.amount_total)
			record.x_total_cents = frac * 100



	# Net
	x_total_net = fields.Float(
			"Neto",

			compute='_compute_x_total_net',
		)

	@api.multi
	#@api.depends('')
	def _compute_x_total_net(self):
		for record in self:
			x = record.amount_total / 1.18
			g = float("{0:.2f}".format(x))
			record.x_total_net = g



	# Tax
	x_total_tax = fields.Float(
			"Impuesto",

			compute='_compute_x_total_tax',
		)
	@api.multi
	#@api.depends('')
	def _compute_x_total_tax(self):
		for record in self:
			x = record.x_total_net * 0.18
			g = float("{0:.2f}".format(x))
			record.x_total_tax = g





	# My company
	x_my_company = fields.Many2one(
			'res.partner',
			string="Mi compañía",
			domain=[
						('company_type', '=', 'company'),
					],

			compute="_compute_x_my_company",
		)

	@api.multi
	def _compute_x_my_company(self):
		for record in self:
				com = self.env['res.partner'].search([
															('x_my_company', '=', True),
													],
													order='date desc',
													limit=1,
					)
				record.x_my_company = com



	# Date corrected
	x_date_order_corr = fields.Char(
			string='Order Date Corr',

			compute="_compute_date_order_corr",
		)

	@api.multi
	#@api.depends('partner_id')

	def _compute_date_order_corr(self):
		for record in self:

			DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
			date_field1 = datetime.datetime.strptime(record.date_order, DATETIME_FORMAT)

			date_field2 = date_field1 + datetime.timedelta(hours=-5, minutes=0)
			DATETIME_FORMAT_2 = "%d-%m-%Y %H:%M:%S"
			date_field2 = date_field2.strftime(DATETIME_FORMAT_2)
			record.x_date_order_corr = date_field2






# ----------------------------------------------------------- Primitives --------------------------

	# Proc Created - For Doctor budget creation
	x_procedure_created = fields.Boolean(
			'Procedimiento Creado',
			default=False,
		)



	# Partner
	partner_id = fields.Many2one(
			'res.partner',
			string="Cliente",
			ondelete='cascade',
			#required=True,
			required=False,

			states={
					'draft': [('readonly', False)],
					'sent': [('readonly', True)],
					'sale': [('readonly', True)],
				},
		)



	# DNI
	x_partner_dni = fields.Char(
			string='DNI',

			states={
						'draft': 	[('readonly', False)],
						'sent': 	[('readonly', True)],
						'sale': 	[('readonly', True)],
						'cancel': 	[('readonly', True)],
						'done': 	[('readonly', True)],
					},
		)





# ---------------------------------------------- Create Payment Method - Amount Total -------------

	# Amount total
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
			#if sub == 0.0:
			#	sub = float(record.x_ruc)
			record.x_amount_total = sub



# ---------------------------------------------- Create Payment Method ----------------------------
	@api.multi
	def create_payment_method(self):
		"""
		high level support for doing this and that.
		"""

		# Update Descriptors
		self.update_descriptors()

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

																				# Deprecated
																				#'name': name,
																				#'dni': dni,
																				#'id_doc_type': 	id_doc_type,
																				#'id_doc': 			id_doc,
																			})
		payment_method_id = self.x_payment_method.id


		# Create Lines
		name = '1'
		method = 'cash'
		subtotal = self.x_amount_total
		payment_method = self.x_payment_method.id

		#ret = self.x_payment_method.pm_line_ids.create({
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

							#'default_dni': dni,
							#'default_saledoc': 'receipt',
							#'default_pm_total': self.pm_total,
							}
				}
	# create_payment_method






# ----------------------------------------------------------- Update Descriptors ------------------

	# For batch
	@api.multi
	def update_descriptors_all(self):
		"""
		high level support for doing this and that.
		"""

		orders = self.env['sale.order'].search([
													('state', '=', 'sale'),
											],
												order='date_order desc',
												#limit=2000,
												limit=300,
											)
		#print orders

		for order in orders:
			order.update_descriptors()



	# Update Family and Product
	@api.multi
	def update_descriptors(self):
		"""
		high level support for doing this and that.
		"""

		out = False

		for line in self.order_line:

			if not out:

				# Consultations
				if line.product_id.categ_id.name in ['Consulta', 'Consultas']:
					self.x_family = 'consultation'
					self.x_product = line.product_id.x_name_ticket
					out = True

				# Procedures
				elif line.product_id.categ_id.name in ['Procedimiento', 'Quick Laser', 'Laser Co2', 'Laser Excilite', 'Laser M22', 'Medical']:
					self.x_family = 'procedure'
					self.x_product = line.product_id.x_name_ticket
					out = True

				# Cosmetology
				elif line.product_id.categ_id.name == 'Cosmeatria':
					self.x_family = 'cosmetology'
					self.x_product = line.product_id.x_name_ticket
					out = True


				# Products
				else:
					self.x_product = line.product_id.x_name_ticket
					if self.x_family != 'procedure':
						self.x_family = 'product'


		#print
		#print 'Update descriptors'
		#print self.x_family
		#print self.x_product

	#update_descriptors


# ----------------------------------------------------------- Print -------------------------------
	# Print Ticket - Electronic
	@api.multi
	def print_ticket_electronic(self):
		"""
		high level support for doing this and that.
		"""
		print('')
		print('Print Electronic')
		name = 'openhealth.report_ticket_receipt_electronic'
		action = self.env['report'].get_action(self, name)
		return action



	# Print Ticket - Deprecated !
	@api.multi
	def print_ticket(self):
		"""
		high level support for doing this and that.
		"""
		if self.x_type == 'ticket_receipt':
			name = 'openhealth.report_ticket_receipt_nex_view'
			return self.env['report'].get_action(self, name)
		elif self.x_type == 'ticket_invoice':
			name = 'openhealth.report_ticket_invoice_nex_view'
			return self.env['report'].get_action(self, name)



# ----------------------------------------------------------- Update Appointments -----------------

	# Update Appointment in Treatment
	@api.multi
	def update_appointment(self):
		"""
		high level support for doing this and that.
		"""
		if self.x_family == 'consultation':
			for app in self.treatment.appointment_ids:
				if app.x_type == 'consultation':
					app.state = 'Scheduled'
		if self.x_family == 'procedure':
			for app in self.treatment.appointment_ids:
				if app.x_type == 'procedure':
					app.state = 'Scheduled'



#----------------------------------------------------------- Quick Button - For Treatment ---------

	# For Treatments Quick access
	@api.multi
	def open_line_current(self):
		"""
		high level support for doing this and that.
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

	# For Payment Method comeback
	@api.multi
	def open_myself(self):
		"""
		high level support for doing this and that.
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
		#print
		#print 'Order - Reset'
		self.x_payment_method.unlink()
		self.state = 'draft'


	@api.multi
	def remove_myself(self):
		"""
		high level support for doing this and that.
		"""
		#self.test_reset()
		self.reset()
		self.unlink()



# ---------------------------------------------- Cancel -------------------------------------------

	# Cancel
	x_cancel = fields.Boolean(
			string='',
			default=False
		)


	# Cancel Order
	@api.multi
	def cancel_order(self):
		"""
		high level support for doing this and that.
		"""
		#print
		#print 'Cancel Order'
		self.x_cancel = True
		self.state = 'cancel'


	# Activate
	@api.multi
	def activate_order(self):
		"""
		high level support for doing this and that.
		"""
		self.x_cancel = False
		self.state = 'sale'



# ----------------------------------------------------------- Test --------------------------------

	# Test Case
	x_test_case = fields.Char()


	# Test
	@api.multi
	def test(self):
		"""
		high level support for doing this and that.
		"""
		#print
		#print 'Order - Test - Interface'
		test_order.test(self)



	def test_actions(self):
		"""
		high level support for doing this and that.
		"""
		print('')
		print('Test Actions')
		self.print_ticket_electronic()
		self.correct_pm()
		self.create_credit_note()
		self.cancel_order()
		self.activate_order()



	def test_computes(self):
		"""
		high level support for doing this and that.
		"""
		print('')
		print('Test Computes')

		print(self.x_type_code)
		print(self.nr_lines)
		print(self.x_partner_vip)
		print(self.x_total_in_words)
		print(self.x_total_cents)
		print(self.x_total_net)
		print(self.x_total_tax)
		print(self.x_my_company)
		print(self.x_date_order_corr)
		print(self.x_amount_total)
		#print(self.)



	# Pay myself
	def pay_myself(self):
		"""
		high level support for doing this and that.
		"""
		#print
		#print 'Order - Pay myself - Interface'
		test_order.pay_myself(self)
