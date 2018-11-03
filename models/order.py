# -*- coding: utf-8 -*-
#
# 	Order
#
# 	Created: 			26 Aug 2016
# 	Last mod: 			25 Sep 2018
#
from openerp import models, fields, api
import datetime
from num2words import num2words
import math
from openerp import tools
from openerp import _
from openerp.exceptions import Warning
import ord_vars
import creates
import pat_vars
import user
import chk_patient
import chk_order
import lib
import lib_con

import qrcode
import base64
import cStringIO

class sale_order(models.Model):

	_inherit = 'sale.order'




# ----------------------------------------------------------- Constraints - Sql -------------------
	# Uniqueness constraints for:
	# Serial Number
	_sql_constraints = [
				#('x_serial_nr','unique(x_serial_nr)', 'SQL Warning: x_serial_nr must be unique !'),
				]


	# Serial Number 
	x_serial_nr = fields.Char(
			'Número de serie',
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



	# Make QR
	@api.multi
	def make_qr(self):
		print
		print 'Make QR'

		#if self.x_id_doc_type != False: 
		#	id_doc_type = self.x_id_doc_type
		#else: 
		#	id_doc_type = ''


		#if self.x_ruc in ['', False]:
		#	ruc = ''
		#else:
		#	ruc = self.x_ruc

		#self.x_qr_data = self.x_my_company.name + se + self.x_my_company.x_ruc + \
		#		se + \
		#		self.date_order + \
		#		se + \
		#		self.x_serial_nr + \
		#		se + \
		#		self.x_type_code + \
		#		se + \
		#		self.patient.name + \
		#		se + \
		#		id_doc_type + \
		#		se + \
		#		self.x_id_doc + \
		#		se + \
		#		"ruc" + se + ruc + \
		#		se + \
		#		str(self.amount_total)



		# Init 

		_dic_type_code = {
							'ticket_receipt': '03',
							'ticket_invoice': '01',
							'credit_note': '07',
							#'debit_note': '08',
		}

		_dic_type_doc = {
							'dni': 		'1',
							'ruc': 		'6',
							'other': 	'0',
							'ptp': 		'0',
							'foreign_card': '4',
							'passport': 	'7',
		}


		ruc_company = self.x_my_company.x_ruc
		
		type_code = _dic_type_code[self.x_type]

		series = self.x_serial_nr.split('-')[0]

		number = self.x_serial_nr.split('-')[1]

		igv = str(self.x_total_tax)

		total = str(self.amount_total)


		#date_format = "%Y/%m/%d"
		date_format = "%Y-%m-%d %H:%M:%S"

		#date = self.date_order.strftime("%Y-%m-%d %H:%M:%S")
		#date = self.date_order.strftime("%Y/%m/%d")

		#date = datetime.datetime.strptime(self.date_order, date_format).strftime("%Y-%m-%d %H:%M:%S")
		#date = datetime.datetime.strptime(self.date_order, date_format).strftime("%Y-%m-%d")
		#date = datetime.datetime.strptime(self.date_order, date_format).strftime("%d/%m/%Y")
		date = (datetime.datetime.strptime(self.date_order, date_format) - datetime.timedelta(hours=5)).strftime("%d/%m/%Y")


		if self.x_type in ['ticket_receipt', 'credit_note']:
			type_doc = _dic_type_doc[self.x_id_doc_type]
			doc = self.x_id_doc 
		elif self.x_type in ['ticket_invoice']:
			type_doc = '6'
			doc = self.x_ruc




		# Create
		se = '|'
		self.x_qr_data = ruc_company + se + type_code + se + series + se + number + se + igv + se + total + se + date + se + type_doc + se + doc 




		qr = qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=20,border=4,)

		#name = self.default_code+'_Product.png'
		#name = self.x_serial_nr + '_Product.png'
		name = self.x_qr_data + '.png'


		#qr.add_data(self.default_code) #you can put here any attribute SKU in my case
		#qr.add_data(self.x_serial_nr) #you can put here any attribute SKU in my case
		qr.add_data(self.x_qr_data) #you can put here any attribute SKU in my case


		qr.make(fit=True)

		img = qr.make_image()

		buffer = cStringIO.StringIO()

		img.save(buffer, format="PNG")

		img_str = base64.b64encode(buffer.getvalue())


		#self.write({'qr_product': img_str,'qr_product_name':name})
		self.write({'x_qr_img': img_str,'qr_product_name':name})





# ---------------------------------------------- Fix -------------------------------------------
	# Fix
	@api.multi
	def fix_serial_nr(self):
		print
		print 'Fix - Serial Nr'

		print self.x_serial_nr

		x_serial_nr = self.x_serial_nr.replace("B", "0")


		# Update
		ret = self.write({
							'x_serial_nr': x_serial_nr,
						})


		print self.x_serial_nr


# ---------------------------------------------- Duplicate -------------------------------------------
	# Duplicate
	@api.multi
	def create_credit_note(self):
		print
		print 'Create CN'

		serial_nr = 'FC1-000001'
		state = 'credit_note'

		# Dup
		#order = self.copy()
		order = self.copy(default={
									#'order_id':self.order_id.id,
									'x_serial_nr':	serial_nr,
									'x_credit_note_owner': self.id,

									'amount_total': self.amount_total,
									'amount_untaxed': self.amount_untaxed,
									'state': state,
								})
		print order


		# Update
		ret = self.write({
							'x_credit_note': order.id,
						})




# ---------------------------------------------- Cancel -------------------------------------------

	# Cancel Order
	@api.multi
	def cancel_order(self):
		print
		print 'Cancel Order'

		self.x_cancel = True
		self.state = 'cancel'

		#patient_id = self.patient.id
		#doctor_id = self.x_doctor.id
		#treatment_id = self.treatment.id
		#x_type = self.x_type
		#short_name = 'other'
		#qty = 1
		#order = creates.create_order_fast(self, patient_id, doctor_id, treatment_id, short_name, qty, x_type)
		#print order


		# Update
		#serial_nr = 'FC1-000001'

		#ret = order.write({
		#					'amount_total': self.amount_total,
		#					'amount_untaxed': self.amount_untaxed,
		#					'state': 'credit_note',
		#					'x_credit_note_owner': self.id,		
		#					'x_serial_nr': serial_nr,
		#				})

		# Create CN
		self.create_credit_note()








# ----------------------------------------------------------- Credit Note -------------------------

	x_credit_note_owner = fields.Many2one(
			'sale.order',
			'Propietario NC',
		)

	x_credit_note = fields.Many2one(
			'sale.order',
			'Nota de Crédito',
		)



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









# ----------------------------------------------------------- Constraints - Python ----------------

	# Check Serial Number
	#@api.constrains('x_serial_nr')
	#def _check_x_serial_nr(self):
	#	print
		#print 'Check Serial Nr'
		#chk_order._check_x_serial_nr(self)



	# Check Id doc - Documento Identidad 
	#@api.constrains('x_id_doc')
	#def _check_x_id_doc(self):
	#	print
		#print 'Check Id Doc'
		#chk_patient.check_x_id_doc(self)



	# Check Ruc
	@api.constrains('x_ruc')
	def _check_x_ruc(self):
		#print
		#print 'Check Ruc'
		chk_order.check_x_ruc(self)





# ----------------------------------------------------------- Counter -----------------------------

	# Counter Value
	x_counter_value = fields.Integer(
			string="Contador",
		)

	# Prefix
	x_prefix = fields.Char(
			'Prefix',
			default='001',
		)

	# Separator
	x_separator = fields.Char(
			'Separator',
			default='-',
		)

	# Padding
	x_padding = fields.Integer(
			'Padding',
			default=10,
		)



# ----------------------------------------------------------- Id Doc ------------------------------

	# Id Document
	x_id_doc = fields.Char(
			'Nr. Doc.',
			required=False,
		)


	# Id Document Type 
	x_id_doc_type = fields.Selection(
			selection = pat_vars._id_doc_type_list,
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
				('receipt', 			'Boleta'),
				('invoice', 			'Factura'),
				('advertisement', 		'Canje Publicidad'),
				('sale_note', 			'Canje NV'),
				('ticket_receipt', 		'Ticket Boleta'),
				('ticket_invoice', 		'Ticket Factura'),
			],
			string='Tipo',
			required=False,
			states={
					'draft': [('readonly', True)],
					'sent': [('readonly', True)],
					'sale': [('readonly', True)],
				}, 
		)








# ----------------------------------------------------------- Mode Admin --------------------------
	# Mode Admin
	x_admin_mode = fields.Boolean(
			'Modo Admin',
		)



# ----------------------------------------------------------- Correct -----------------------------
	# Correct payment method
	@api.multi
	def correct_pm(self):
		print
		print 'Correct Payment Method'

		#order_id = self.id

		if self.x_payment_method.name == False:
			
			#print 'Create'
			self.x_payment_method = self.env['openhealth.payment_method'].create({
																					'order': 	self.id,
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




# ----------------------------------------------------------- Legacy ------------------------------
	# Legacy
	x_legacy = fields.Boolean(
			'Legacy',
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
			string = "Médico",
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
			string = "Familia", 	
			selection = [
							('product','Producto'), 
							('consultation','Consulta'), 
							('procedure','Procedimiento'), 
							('cosmetology','Cosmiatría'), 
			], 

			#required=False, 
			#states=READONLY_STATES, 
			#readonly=True, 
		)


	# Product
	x_product = fields.Char(		
			string="Producto",	

			#required=False, 			
			#states=READONLY_STATES, 
			#readonly=True, 
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
		print 
		print 'On Change Patient'

		if self.patient.name != False: 

			# Init 
			self.x_ruc = False
			self.partner_id = self.patient.partner_id.id 


			print self.patient.x_id_doc
			print self.patient.x_id_doc_type
			#print self.patient.x_dni + '.'


			# Id Doc 
			if self.patient.x_id_doc != False: 
				
				print 'Mark 1'
				
				self.x_id_doc = self.patient.x_id_doc
				self.x_id_doc_type = self.patient.x_id_doc_type

			# Get x Dni 
			#elif self.patient.x_dni != '': 
			elif self.patient.x_dni not in [False, '']: 
				
				print 'Mark 2'
				
				self.x_id_doc = self.patient.x_dni
				self.x_id_doc_type = 'dni'
				self.x_dni = self.patient.x_dni


				# Update Patient - Dep 
				#self.x_msg = '1'
				#self.patient.x_id_doc = self.patient.x_dni
				#self.patient.x_id_doc_type = 'dni'


			# Ruc 				
			if self.patient.x_ruc != False: 
				print 'Mark 3'
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








# ----------------------------------------------------------- Check - Pm Total --------------------

	# Pm Total 
	x_pm_total = fields.Float(
			'Total MP', 
			readonly=True, 
		)


	# Checksum 
	x_checksum = fields.Float(
			'Checksum', 
			readonly=True, 
			default = -1, 
		)


	# Check payment method 
	@api.multi 
	def check_payment_method(self):

		#print 
		#print 'Check Payment Method'

		pm_total = 0 
		for pm in self.x_payment_method.pm_line_ids: 
			pm_total = pm_total + pm.subtotal
		self.x_pm_total = pm_total

		#if self.x_pm_total != self.amount_total:
		#	msg = 'Error: Verificar la Forma de Pago.'
		#	raise Warning(_(msg))




	# Check Sum 
	@api.multi 
	def check_sum(self):

		#print 
		#print 'Check Sum'

		self.x_checksum = self.amount_total - self.x_pm_total 




# ----------------------------------------------------------- Check - Content ---------------------

	# Personal identifiers: Dni, Ruc 
	# Check for length and digits 

	# Check Content 
	@api.multi 
	def check_content(self):
		print 
		print 'Check Content'

		#self.x_dni = self.partner_id.x_dni
		#self.x_ruc = self.partner_id.x_ruc

		#print self.patient.name 				# Generates an Error ! With Ñ
		#print 'Dni: ', self.x_dni
		#print 'Ruc: ', self.x_ruc 


		_length = {
					'dni': 8,
					'passport': 12,
					'foreign_card': 12,
					'ptp': 12,					# Verify !
		}


		# Dni - Generalize, to accept other docs (passport, foreign card, ptp)
		if self.x_type in ['ticket_receipt', 'receipt']: 

			print 'Receipt'

			# Test 


			# Nr of characters
			if self.x_id_doc_type not in ['other']: 
				length = _length[self.x_id_doc_type]
				ret = lib.test_for_length(self, self.x_id_doc, length)
				if ret != 0:
					msg = "Error: Documento debe tener " + str(length) + " caracteres."
					raise Warning(_(msg))



			# Must be Number - Only for DNIs 
			if self.x_id_doc_type in ['dni']: 
				ret = lib.test_for_digits(self, self.x_id_doc)
				if ret != 0:
					#msg = "Error: DNI debe ser un Número."
					msg = "Error: Documento debe ser un Número."
					raise Warning(_(msg))
	


			# Update 
			self.partner_id.x_dni = self.x_dni



		# Ruc
		elif self.x_type in ['ticket_invoice', 'invoice']: 

			print 'Invoice'
			print self.x_ruc
			

			# Test 
			length = 11
			ret = lib.test_for_length(self, self.x_ruc, length)
			if ret != 0:
				msg = "Error: RUC debe tener " + str(length) + " caracteres."
				raise Warning(_(msg))

			ret = lib.test_for_digits(self, self.x_ruc)
			if ret != 0:
				msg = "Error: RUC debe ser un Número."
				raise Warning(_(msg))

			# Update 
			self.partner_id.x_ruc = self.x_ruc




# ----------------------------------------------------------- Validate ----------------------------

	# Action confirm 
	@api.multi 
	def validate(self):
		#print
		#print 'Validate'


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
				if line.product_id.x_family in ['laser', 'medical', 'cosmetology']:

					# Create 
					creates.create_procedure_wapp(self, line.product_id.x_treatment, line.product_id.id)
				
				line.update_recos()

			# Update 
			self.x_procedure_created = True
			self.treatment.update_appointments()



		# Check Content - DEP 
		#self.check_content()




		# Update Patient 
		if self.patient.x_id_doc in [False, '']: 
			self.patient.x_id_doc_type = self.x_id_doc_type
			self.patient.x_id_doc = self.x_id_doc




		# Change State 
		self.state = 'validated'



		# Change Electronic 
		self.x_electronic = True

		# Title
		if self.x_type in ['ticket_receipt', 'receipt']:
			self.x_title = 'Boleta de Venta Electrónica'
		elif self.x_type in ['ticket_invoice', 'invoice']:
			self.x_title = 'Factura de Venta Electrónica'
		else:
			self.x_title = 'Venta Electrónica'


	# validate



# ----------------------------------------------------------- Action Confirm ----------------------

	# Action confirm 
	@api.multi 
	def action_confirm_nex(self):
		print 
		print 'Action confirm - Nex'

		
		#Write your logic here - Begin

		# Generate Serial Number		
		if self.x_serial_nr != '' and self.x_admin_mode == False: 



			# Prefix 
			prefix = ord_vars._dic_prefix[self.x_type]


			# Counter 
			self.x_counter_value = user.get_counter_value(self)
			

			# Padding 
			padding = ord_vars._dic_padding[self.x_type]




			# Serial Nr 
			self.x_serial_nr = prefix + self.x_separator + str(self.x_counter_value).zfill(padding)


		#Write your logic here - End 


		# The actual procedure 
		res = super(sale_order, self).action_confirm()


		#Write your logic here


		# QR
		if self.x_type in ['ticket_receipt']:
			self.make_qr()



	# action_confirm_nex





# ----------------------------------------------------------- Create Card -------------------------

	# Create Card Vip 
	@api.multi 
	def detect_create_card(self):


		# Detect if Card in Sale 
		sale_card = False 

		for line in self.order_line:
			if line.product_id.x_name_short == 'vip_card':
				sale_card = True




		# If Card in Sale  
		if sale_card:


			# Search Card in the Db
			card = self.env['openhealth.card'].search([ ('patient_name', '=', self.partner_id.name), ], order='date_created desc', limit=1)
			


			# If it does not exist - Create 
			if card.name == False: 
				card = self.env['openhealth.card'].create({
																'patient_name': self.partner_id.name,
															})




			# Update Partner - Vip Price List 
			pl = self.env['product.pricelist'].search([
																('name','=', 'VIP'),
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
	#date_order = fields.Datetime(string='Order Date', required=True, readonly=True, index=True, states={'draft': [('readonly', False)], 'sent': [('readonly', False)]}, copy=False, default=fields.Datetime.now)
	date_order = fields.Datetime(
		states={	
					'draft': [('readonly', False)], 
					'sent': [('readonly', False)], 
					'sale': [('readonly', True)], 

					#'editable': [('readonly', False)], 
				}, 
		
		index=True, 
	)


	# State 
	#state = fields.Selection([
	#	('draft', 'Quotation'),
	#	('sent', 'Quotation Sent'),
	#	('sale', 'Sale Order'),
	#	('done', 'Done'),
	#	('cancel', 'Cancelled'),
	#	], string='Status', readonly=True, copy=False, index=True, track_visibility='onchange', default='draft')
	state = fields.Selection(
			selection = ord_vars._state_list, 
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

			states={	
					'draft': [('readonly', False)], 
					'sent': [('readonly', False)], 
					'sale': [('readonly', True)], 
					
					#'editable': [('readonly', False)], 
				}, 
		)





	x_doctor_uid = fields.Many2one(
			'res.users',
			string = "Médico Uid", 	
			readonly = True,
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
			for l in record.order_line:
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
																('patient_name','=', record.partner_id.name),
														]) 
			if count == 0:
				record.x_partner_vip = False 
			else:	
				record.x_partner_vip = True 




# ----------------------------------------------------------- Primitives --------------------------






	# Cosmetology 
	cosmetology = fields.Many2one(
			'openhealth.cosmetology',
			ondelete='cascade', 			
			string="Cosmiatría", 
		)



	# For User Interface 
	vspace = fields.Char(
			' ', 
			readonly=True
		)





# ----------------------------------------------------- Product Selector --------------------------

	@api.multi
	def open_product_selector_product(self):  
		return self.open_product_selector('product')


	@api.multi
	def open_product_selector_service(self):
		return self.open_product_selector('service')


	# Buttons  - Agregar Producto Servicio
	@api.multi
	def open_product_selector(self, x_type):  

		# Init Vars 
		#context = self._context.copy()		
		order_id = self.id
		res_id = False

		# Search Model 
		res = self.env['openhealth.product.selector'].search([],
																#order='write_date desc',
																limit=1,
															)
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
								'form': {'action_buttons': False, 'options': {'mode': 'edit'}  }
							},
				'context': {
								'default_order_id': order_id ,
								'default_x_type': x_type ,
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
			string = "Mi compañía", 	
			domain = [
						('company_type', '=', 'company'),
					],
			compute="_compute_x_my_company",
		)


	@api.multi
	#@api.depends('partner_id')

	def _compute_x_my_company(self):

		for record in self:
				com = self.env['res.partner'].search([
															#('name', '=', 'Clinica Chavarri'),
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
			
			date_field2 = date_field1 + datetime.timedelta(hours=-5,minutes=0)
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
			string = "Cliente", 	
			ondelete='cascade', 			
			#required=True, 
			required=False, 

			states={	
					'draft': [('readonly', False)], 
					'sent': [('readonly', True)], 
					'sale': [('readonly', True)], 
					
					#'editable': [('readonly', False)], 
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













	# Activate
	@api.multi
	def activate_order(self):
		self.x_cancel = False
		self.state = 'sale'


	# Cancel 
	x_cancel = fields.Boolean(
			string='',
			default = False
		)




# ---------------------------------------------- Create Payment Method - Amount Total -------------

	# Amount total 
	x_amount_total = fields.Float(
			string = "x Total",

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



# ---------------------------------------------- Create Payment Method --------------------------------------------------------
	@api.multi 
	def create_payment_method(self):

		# Update Descriptors
		self.update_descriptors()

		# Init vars 
		name = 'Pago'
		method = 'cash'
		#balance = self.x_amount_total - self.pm_total
		balance = self.x_amount_total

		# For Receipts and Invoices  
		firm = self.partner_id.x_firm
		dni = self.partner_id.x_dni
		ruc = self.partner_id.x_ruc



		# Id Doc - Dep 
		#if self.patient.x_id_doc not in [False, '']: 
		#	id_doc = self.patient.x_id_doc
		#	id_doc_type = self.patient.x_id_doc_type
		#else: 
		#	id_doc = self.x_id_doc
		#	id_doc_type = self.x_id_doc_type



		# Create 
		self.x_payment_method = self.env['openhealth.payment_method'].create({
																				#'name': name,
																				'order': self.id,
																				'method': method,
																				'subtotal': balance,
																				'total': self.x_amount_total,
																				'partner': self.partner_id.id, 
																				'date_created': self.date_order,
																				'firm': firm,
																				'ruc': ruc,

																				# Deprecated 
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

		ret = self.x_payment_method.pm_line_ids.create({
																	'name': name,
																	'method': method ,
																	'subtotal': subtotal,
																	'payment_method': payment_method, 
										})
		



		#self.state = 'sent'		# Now, this is done by payment method. 



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
							'form': {'action_buttons': False, 'options': {'mode': 'edit'}  }
							},
				'context': {
				
							'default_order': self.id,
							'default_name': name,
							'default_method': method,
							'default_subtotal': balance,
							'default_total': self.x_amount_total,
							'default_partner': self.partner_id.id,
							'default_date_created': self.date_order,
							'default_dni': dni,
							'default_firm': firm,
							'default_ruc': ruc,

							#'default_saledoc': 'receipt', 
							#'default_pm_total': self.pm_total,
							}
				}
	# create_payment_method






# ----------------------------------------------------------- Update Descriptors ------------------------------------------------------

	# For batch 
	@api.multi 
	def update_descriptors_all(self):

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

		out = False

		for line in self.order_line:

			if not out: 

				# Consultations
				if line.product_id.categ_id.name in ['Consulta','Consultas']:
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

		name = 'openhealth.report_ticket_receipt_electronic'
		
		return self.env['report'].get_action(self, name)



	# Print Ticket - Deprecated !
	@api.multi
	def print_ticket(self):
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

		if self.x_family == 'consultation': 
			for app in self.treatment.appointment_ids: 
				if app.x_type == 'consultation': 
					#app.state = 'invoiced'
					app.state = 'Scheduled'

		if self.x_family == 'procedure': 
			for app in self.treatment.appointment_ids: 
				if app.x_type == 'procedure': 
					#app.state = 'invoiced'
					app.state = 'Scheduled'



#----------------------------------------------------------- Quick Button - For Treatment ---------

	# For Treatments Quick access
	@api.multi
	def open_line_current(self):  
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






	#----------------------------------------------------------- Qpen myself ------------------------------------------------------------

	# For Payment Method comeback 
	@api.multi 
	def open_myself(self):

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




# ----------------------------------------------------------- Update Order ------------------------------------------------------

	# Update colors (state)
	#@api.multi 
	#def update_order_nex(self):
		#print 
		#print 'Update Order Nex'
		#print 



# ----------------------------------------------------------- Remove - For Treatment   ------------------------------------------------------
	@api.multi
	def remove_myself(self):  
		self.test_reset()
		self.unlink()



# ----------------------------------------------------------- Reset ------------------------------------------------------
	
	# Test - Reset 
	@api.multi 
	def test_reset(self):
		#print 
		#print 'Order - Reset'
		self.x_payment_method.unlink()
		self.x_dni = ''
		self.x_ruc = ''
		self.state = 'draft'			# This works. 



# ----------------------------------------------------------- Pay ------------------------------------------------------
	# Test  
	@api.multi 
	def pay_myself(self, date_order=False):

		#print 
		#print 'Pay myself'

		if self.state == 'draft': 
			self.create_payment_method()
			
			#self.x_payment_method.saledoc = 'advertisement'
			self.x_payment_method.saledoc = 'ticket_receipt'

			self.x_payment_method.state = 'done'
			self.state = 'sent'
			self.validate()
			self.action_confirm_nex()

			# Update  
			if date_order != False: 
				ret = self.write({
									'date_order': date_order,
								})




# ----------------------------------------------------------- Generates ---------------------------
	# Generate Date Order
	def generate_date_order(self, date_order, delta_hou=0, delta_min=0, delta_sec=0):
		#print
		#print 'Generate Date Order'		
		date_order = lib.correct_date_delta(date_order, delta_hou, delta_min, delta_sec)
		self.date_order = date_order

	# generate_date_order


	# Generate Serial Nr
	def generate_serial_nr(self):
		#print 
		#print 'Generate Serial Nr'

		# Init 
		delta = 0 
		_dic_pad = {
						'ticket_receipt': 10,
						'ticket_invoice': 10,
						'receipt': 			6,
						'invoice':			6,
		}
		pad = _dic_pad[self.x_type]

		# Generate
		self.x_serial_nr = lib_con.generate_serial_nr(self.x_counter_value, delta, pad)

	# generate_date_order





# ----------------------------------------------------------- Test ------------------------------------------------------

	# Computes
	def test_computes(self):
		print 
		print 'Order - Computes'

		print 'x_partner_vip\t', 		self.x_partner_vip
		print 'nr_lines\t', 				self.nr_lines
		print 'x_amount_total\t', 		self.x_amount_total
		
		print 'x_total_in_words\t', 	self.x_total_in_words
		print 'x_total_cents\t', 		self.x_total_cents
		print 'x_total_net\t', 			self.x_total_net
		print 'x_total_tax\t', 			self.x_total_tax		
		print 'x_my_company\t', 	 	self.x_my_company
		print 'x_date_order_corr\t', 	self.x_date_order_corr




	# Actions
	def test_actions(self):
		print
		print 'Order - Actions'
		self.state_force()
		self.state_force()
		self.open_product_selector_product()
		self.open_product_selector_service()
		self.cancel_order()
		self.activate_order()
		self.open_line_current()



# ----------------------------------------------------------- Test - Init -------------------------
	# Test - Init
	@api.multi
	def test_init(self, patient_id, partner_id, doctor_id, treatment_id, pl_id):

		print
		print 'Order - Test Init'

		#self.test_reset()


		# Create Order
		order = self.env['sale.order'].create({
													'partner_id': 	partner_id,
													'patient': 		patient_id,
													'state':		'draft',
													'x_doctor': 	doctor_id,
													'pricelist_id': pl_id,
													'treatment': 	treatment_id,
												})

		# Create Order Lines


		# Tuples - Short Name + Manual price
		tup_arr = [
							('con_med',	0),  					# Consultation
							('con_med',	100),  					# Consultation
							('con_med',	200),  					# Consultation
							('con_gyn', 200),  					# Consultation

							('acneclean',	-1),  						# Product
							('vip_card',	-1),  						# Product 

							('quick_neck_hands_rejuvenation_1',	-1), 	# Quick
							('co2_nec_rn1_one',		-1), 				# Co2
							('exc_bel_alo_15m_one',	-1),				# Exc
							('ipl_bel_dep_15m_six',	-1), 			# Ipl
							('ndy_bol_ema_15m_six',	-1),				# Ndyag
							
							('bot_1zo_rfa_one',		-1), 			# Medical
							('car_bod_rfa_30m_six',	-1), 			# Cosmeto
					]



		# Init
		#price_manual = 0
		#price_applied = 0
		price_applied = -1
		reco_id= False


		# Create
		for tup in tup_arr:

			name_short = 	tup[0]
			price_manual = 	tup[1]

			# Prints
			#print tup
			#print name_short
			#print price_manual

			# Create
			ret = creates.create_order_lines_micro(order, name_short, price_manual, price_applied, reco_id)

		return [order]

	# test_init




# ----------------------------------------------------------- Test Unit ------------------------------------------------------
	# Test - Unit
	def test_unit(self):
		print
		print 'Order - Test Unit'

		# Computes
		#self.test_computes()

		# Actions - Remaining
		#self.test_actions()


		# Init
		total = 0
		#total_vip = 0


		for line in self.order_line:

			# Standard
			#total = 	line.product_id.list_price * line.product_uom_qty 		+ total
			
			price_std = line.product_id.list_price
			price_vip = line.product_id.x_price_vip
			price_manual = line.x_price_manual
			
			qty = line.product_uom_qty

			compact = line.x_description




			# Prints
			print 'product_id: ', line.product_id.name
			print 'price_std: ', price_std
			print 'price_vip: ',  price_vip
			print 'price_manual: ', price_manual
			#print price_applied
			print 'qty: ', qty
			print 'compact: ', compact


			# Assert
			#assert compact != 'x'  					# Assert 


			# Price

			# Manual
			if price_manual != -1: 
				price = price_manual
			
			# Public
			elif self.pricelist_id.name in ['Public Pricelist']:
				price = price_std

			# Vip
			else: 
				if line.product_id.type in ['service'] and price_vip != 0: 		# Is a service and has a Vip price
					price = price_vip
				else:
					price = price_std											# Is a service and does not have a Vip price


			# Total
			total = price * qty + total
			print 'price: ', price
			print 'total: ', total



		# Asserts
		print
		print 'Asserts'
		print self.pricelist_id.name
		print 'total: ', total
		print 'self.amount_total: ', self.amount_total

		assert self.amount_total == total    				# Assert


	# test_unit




# ----------------------------------------------------------- Test Integration ------------------------------------------------------
	# Test - Integration 
	# Test the whole Sale Cycle. 
	# With UI buttons included. Activate the different creation and write procedures. 
	def test_integration(self, test_case=False):
		print 
		print 'Order - Test Integration'
		print test_case



# Cycle - Begin
		
		# Create and Init - PM 
		self.create_payment_method()
		# Type 
		self.x_payment_method.saledoc = ord_vars._dic_tc_type[test_case]


		print self.x_payment_method.name
		self.x_payment_method.go_back()
		print self.x_payment_method.state
		
		# Order
		self.validate()					
		self.action_confirm_nex()
		self.print_ticket()


		# Cancel 
		if test_case in ['ticket_invoice_cancel', 'ticket_receipt_cancel']: 
			self.cancel_order()


# Cycle - End


	# test_integration



# ----------------------------------------------------------- Test ------------------------------------------------------
	# Test
	def test(self, test_case=False):
		print 
		print 'Order - Test'

		print test_case

		if self.patient.x_test: 

			if test_case != False: 
				x_type = test_case.split(',')[1].strip()
			
			else: 
				x_type = 'ticket_receipt'


			print test_case
			print x_type  


			# Test Integration 
			self.test_integration(x_type)


			# Test Unit 
			#self.test_unit()
	# test 
