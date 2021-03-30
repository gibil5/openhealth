# -*- coding: utf-8 -*-
"""
	Pl Creates - Openhealth
	- Used by 
		Order

	Created: 			27 Jul 2020
	Last up: 			29 mar 2021

	This a key dependency.
	
	Encapsulates creation on database

	Create Order
		- create_order_con
		- create_order

	Create Procedure 
		- create_procedure
"""
from __future__ import print_function
from . import tre_funcs

# ----------------------------------------------------------- Create Shopping Cart -----------------
def create_shopping_cart(treatment, env, service, treatment_id):
	"""
	Used by Treatment - create_order_pro
	"""
	print()
	print('pl_creates - create_shopping_cart')

	# init 
	service_name = service.service.name
	price = service.price_applied
	qty = service.qty

	# Search product
	print()
	print('Search product ')
	product_id = env.search([	('name', '=', service_name),
								('sale_ok', '=', True),
								('pl_price_list', '=', '2019')]).id
	#print(product)

	# Create cart
	#if product.name:
	cart_line = treatment.shopping_cart_ids.create({	'product': 		product_id,
														'price': 		price,
														'qty': 			qty,
														'treatment': 	treatment_id})
# create_shopping_cart


# ----------------------------------------------------------- Create Order Target -----------------
def create_order_con(self, target, price_list):
	"""
	Used by Treatment - create_order_con
	Create order - consultation
	"""
	print()
	print('OH - pl_create_order_con')
	print(self)
	print(target)
	print(price_list)

	# Search Partner
	print()
	print('Search partner')
	partner = self.env['res.partner'].search([
												('name', '=', self.patient.name),
											],
											limit=1,)
	print(partner)

	# Search
	print()
	print('Search pricelist')
	pricelist = self.env['product.pricelist'].search([
											#('active', 'in', [True]),
											],
											#order='x_serial_nr asc',
											limit=1,
										)
	print(pricelist)


	# Create Order
	print()
	print('Create order')
	print(partner.id)
	print(self.patient.id)
	print(self.patient.x_id_doc)
	print(self.patient.x_id_doc_type)
	print(self.physician.id)
	order = self.env['sale.order'].create({
											'patient': self.patient.id,
											'x_id_doc': self.patient.x_id_doc,
											'x_id_doc_type': self.patient.x_id_doc_type,
											'x_doctor': self.physician.id,
											'state':'draft',
											'partner_id': partner.id,
											'x_family': 'consultation',
											'treatment': self.id,

											'pricelist_id': pricelist.id,
										})
	print(order)

	# Init
	_dic_con = {
					'medical':		'CONSULTA MEDICA',
					'gynecology':	'CONSULTA GINECOLOGICA',
					'premium':		'CONSULTA MEDICA DR. CHAVARRI',
	}
	name = _dic_con[target]

	# Search
	print()
	print('Search product')
	product = self.env['product.product'].search([
														('name', 'in', [name]),
														('pl_price_list', 'in', [price_list]),
													],
														#order='date_begin asc',
														#limit=1,
												)
	print(product)
	print(product.name)

	# Create Order Line
	print()
	print('Create order line')
	ol = order.order_line.create({
									'name': 			product.name,
									'product_id': 		product.id,
									'order_id': 		order.id,
								})
	return order
# create_order_con

# ----------------------------------------------------------- Create Order Target -----------------
def create_order(self):
	"""
	Used by Treatment - create_order_pro
	Create Order - By Line
	"""
	print()
	print('OH - pl_create_order')

	# Search Partner
	print()
	print('Search partner')
	partner = self.env['res.partner'].search([
													('name', '=', self.patient.name),
												],
												#order='appointment_date desc',
												limit=1,)

	# Search Pl
	print()
	print('Search pricelist')
	pricelist = self.env['product.pricelist'].search([
											#('active', 'in', [True]),
											],
											#order='x_serial_nr asc',
											limit=1,
										)
	print(pricelist)

	# Create Order
	order = self.env['sale.order'].create({
													'state':'draft',
													'x_doctor': self.physician.id,

													#'partner_id': self.partner_id.id,
													'partner_id': partner.id,
													#'x_ruc': self.partner_id.x_ruc,
													#'x_dni': self.partner_id.x_dni,

													'patient': self.patient.id,
													'x_id_doc': self.patient.x_id_doc,
													'x_id_doc_type': self.patient.x_id_doc_type,
													'x_family': 'procedure',

													'treatment': self.id,

													'pricelist_id': pricelist.id,
												})
	#print(order)



	# Create Order Lines
	for cart_line in self.shopping_cart_ids:

		product = cart_line.product

		#print(product)
		#print(product.name)

		# Create Order Line
		ol = order.order_line.create({
										'name': 		product.name,
										'product_id': 	product.id,
										'price_unit': 	cart_line.price,
										'product_uom_qty': cart_line.qty,
										'order_id': 	order.id,
									})
	return order
#create_order

#------------------------------------------------ Create Procedure Go --------------------------------
def create_procedure(self, product):
	"""
	Used by: Treatment - create_procedure_auto
	Create Procedure - Core
	Input is a Product Product !!!
	"""
	print()
	print('OH - create_procedure_go')

# Init
	# Product Template
	product_template = product.get_product_template()
	#print(product_template)


	# Patient
	patient_id = self.patient.id


	# Doctor
	#doctor = pl_user.get_actual_doctor(self)
	doctor = tre_funcs.get_actual_doctor(self)

	doctor_id = doctor.id
	if doctor_id == False:
		doctor_id = self.physician.id

	# Chief Complaint
	chief_complaint = self.chief_complaint

	# Treatment
	treatment_id = self.id

# Create Procedure
	procedure = self.procedure_ids.create({
											'patient':patient_id,
											'doctor':doctor_id,
											'product':product_template.id,
											'chief_complaint':chief_complaint,
											'treatment':treatment_id,
										})
	print(procedure)
	print(procedure.name)

# create_procedure_go
