# -*- coding: utf-8 -*-
"""
	Order Business logic

	Created: 			 6 dec 2020
	Last up: 			 6 dec 2020
"""
from __future__ import print_function
from openerp import models, fields, api

from . import ord_funcs
from . import qr
from . import raw_funcs
import datetime

class OrderBusiness(models.Model):
	"""
    Order - Business logic.
    Contains the BL of the company.
	"""
	_inherit = 'sale.order'

# ------------------------------------------- Buttons - UI ----------------------------------------

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

# ---------------------------------------- Print -------------------------------
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

# --------------------------------------------------------- Cancel Button ------
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

# ---------------------------------------------- Credit Note - Create ----------
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

# ----------------------------------------------------- Test all ---------------
	@api.multi
	def test_all(self):
		"""
		Unit Testing - All
		"""
		print()
		print('test_all')
		value = self.env.context.get('key')
		print(value)

		if value == 'test_serial_number':
			print('test_serial_number')
			self.make_serial_number()

		elif value == 'test_qr':
			print('test_qr')
			# Create loosely coupled object
			h_qr = self.get_hash_for_qr()
			qr_obj = qr.QR(h_qr)
			# Get data
			print(qr_obj.get_name())
			print(qr_obj.get_img_str())

		elif value == 'test_ticket':
			print('test_ticket')
			name = 'openhealth.report_ticket_receipt_electronic'
			action = self.env['report'].get_action(self, name)
			return action

		elif value == 'test_validation':
			print('test_validation')
			self.validate_and_confirm()

		elif value == 'test_pm':
			print('test_pm')
			self.create_payment_method()


# --------------------------------------------------------- Validate Button ----

	@api.multi
	def validate_and_confirm(self):
		"""
		Button - Validate and confirm the order.
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


# ------------------------------------------- Services ----------------------------------------

# ------------------------------------------- Check and Generate ---------------
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

		h_qr = {}
		h_qr['ruc_company'] = str(ruc_company)
		h_qr['x_type'] = str(x_type)
		h_qr['serial_nr'] = str(serial_nr)
		h_qr['amount_total'] = str(amount_total)
		h_qr['total_tax'] = str(total_tax)
		h_qr['date'] = str(date)
		h_qr['receptor_id_doc_type'] = str(receptor_id_doc_type)
		h_qr['receptor_id_doc'] = str(receptor_id_doc)
		h_qr['receptor_ruc'] = str(receptor_ruc)

		return h_qr
