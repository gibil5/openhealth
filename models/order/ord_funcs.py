# -*- coding: utf-8 -*-
"""
	Order Funcs
	Encapsulate Order Business Rules
	Created: 			29 Aug 2019
	Last up: 	 		24 Jul 2020 
"""
from __future__ import print_function
from openerp.addons.openhealth.models.libs import lib
from openerp import _
from openerp.exceptions import Warning as OrderError
from . import ord_vars

# ----------------------------------------------------------- Ticket - Get Raw Line ----------------

# Raw Line
def check_ticket(self, family, state):
	"""
	Check Ticket
	Raise Errors 
	"""
	print()
	print('ord_funcs - Check Ticket')

	# Credit Note
	#if state in ['credit_note', ]:
	#	print()
	#	print('Check - Credit Note - ok')

	# Receipt
	if family in ['ticket_receipt', 'receipt']:
		print()
		print('Check - Receipt - ok')

	# Invoice
	elif family in ['ticket_invoice', 'invoice']:
		print('Check - Invoice')
		# Address
		address = self.get_firm_address()
		if address in [False, '']:
			msg = "Error: Factura - Empresa no tiene Direccion."
			raise OrderError(_(msg))
			#return OrderError(_(msg))
		# Ruc
		ruc = self.x_ruc

		if ruc in [False, '']:
			msg = "Error: Factura - Paciente no tiene RUC."
			raise OrderError(_(msg))
		# Firm
		firm = self.patient.x_firm
		if firm in [False, '']:
			msg = "Error: Factura - Paciente no tiene Razon social."
			raise OrderError(_(msg))
		print('ok')

	# Other
	else:
		print('This should not happen !')





#------------------------------------------------ Get Next Counter -------------------------------------

def get_next_counter_value(self, x_type, state):
	"""
	Get Next Counter value. Given type and state.
	If State in Validated or Sale.

	Used by:
		- Create Credit Note
		- Make Serial Number
	"""
	#print()
	#print('Get Next Counter Value')
	#print(x_type)
	#print(state)


	# Credit Note
	if state in ['credit_note']:

		order = self.env['sale.order'].search([
													('x_electronic', '=', True),
													('x_type', '=', x_type),
													('state', 'in', ['credit_note']),
												],
											
											#order='x_counter_value desc',		# Highly deprecated ! Unstable in Tacna
											order='date_order desc',
											
											limit=1,
										)

	# Sale, Cancel
	else:

		order = self.env['sale.order'].search([
													('x_electronic', '=', True),
													('x_type', '=', x_type),
													('state', 'in', ['sale', 'cancel']),
												],

											#order='x_counter_value desc',  	# Highly deprecated ! Unstable in Tacna
											order='date_order desc',

											limit=1,
										)

	return order.x_counter_value + 1






#------------------------------------------------ Get Serial Nr -----------------------------------
def get_serial_nr(x_type, counter_value, state):
	"""
	Get the Serial Nr, given the type, counter and state.
	"""
	#print()
	#print('Get Serial Nr')


	# Separator
	separator = '-'

	# Prefix
	if state in ['credit_note']:
		prefix = ord_vars.get_prefix_cn(x_type)
	else:
		prefix = ord_vars.get_prefix(x_type)

	# Padding
	padding = ord_vars.get_padding(x_type)

	# Serial Nr
	serial_nr = prefix  +  separator  +  str(counter_value).zfill(padding)

	return serial_nr





# ----------------------------------------------------------- Descriptors -------------------------
def update_descriptors(self):
	"""
	Update Descriptors
	Used by Order
	"""
	print()
	print('Update Descriptors')

	# Init
	out = False

	# Loop
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



# ----------------------------------------------------------- Month and Day -------------------------
#def update_day_month(self):
def update_day_and_month(self):
	"""
	Update Day and Month
	Used by Order
	"""
	print()
	print('Update Day And Month')

	date_format = "%d"
	self.x_day_order = lib.get_date_with_format(date_format, self.date_order)

	date_format = "%m"
	self.x_month_order = lib.get_date_with_format(date_format, self.date_order)






# ----------------------------------------------------------- Vip Card -------------------------
def detect_vip_card_and_create(self):
	"""
	Detects Vip Card in the Present Order
	If it exists, the Vip Card is created
	"""
	print()
	print('Detects Vip Card and Create')

	# Init
	sale_card = False


	# The Vip card is in the present order
	for line in self.order_line:


		#if line.product_id.x_name_short == 'vip_card':
		if line.product_id.is_vip_card():					# LOD compliant !!!


			print('Vip Card Detected')
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
			print('Vip Card Created')



		# Update Partner - Vip Price List
		pl = self.env['product.pricelist'].search([
														('name', '=', 'VIP'),
														],
														#order='appointment_date desc',
														limit=1,
												)

		self.partner_id.property_product_pricelist = pl

		print('Partner Updated')



# detect_create_card




# ----------------------------------------------------------- Getters -------------------------
def search_patient_by_id_document(self):
	print()
	print('Search Patient')

	# Protect against On change first time calls
	if self.x_partner_dni != False:

		# Search Patient - by ID IDOC
		patient = self.env['oeh.medical.patient'].search([
															('x_id_doc', '=', self.x_partner_dni),
											],
												order='write_date desc',
												limit=1,
											)

		# Search Patient - by DNI
		if patient.name == False:

			patient = self.env['oeh.medical.patient'].search([
																('x_dni', '=', self.x_partner_dni),
												],
													order='write_date desc',
													limit=1,
												)
		#print(patient.name)  	# Dep !

		# Update Patient
		#self.patient = patient.id

		return patient.id

	else:
		return False



