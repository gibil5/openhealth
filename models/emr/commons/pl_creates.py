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




# ----------------------------------------------- Create order consultation ----
#def create_order_con(self, target, price_list):
def create_order_con(self, partner_id, pricelist_id, product):
	"""
	Used by Treatment - create_order_con
	Create order - consultation
	"""
	print()
	print('OH - pl_create_order_con')
	print(partner_id)
	print(pricelist_id)
	print(product)

	# Create Order
	print()
	print('Create order')
	#print(self.patient.id)
	#print(self.patient.x_id_doc)
	#print(self.patient.x_id_doc_type)
	#print(self.physician.id)

	order = self.env['sale.order'].create({
											'partner_id': partner_id,
											'pricelist_id': pricelist_id,

											'patient': self.patient.id,
											'x_id_doc': self.patient.x_id_doc,
											'x_id_doc_type': self.patient.x_id_doc_type,
											'x_doctor': self.physician.id,
											'state':'draft',
											'x_family': 'consultation',

											'treatment': self.id,
										})
	print(order)


	# Create Order Line
	print()
	print('Create order line')
	ol = order.order_line.create({
									'product_id': 		product.id,
									'name': 			product.name,
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
	print(partner.name)


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
													'partner_id': partner.id,
													'patient': self.patient.id,
													'x_id_doc': self.patient.x_id_doc,
													'x_id_doc_type': self.patient.x_id_doc_type,
													'x_family': 'procedure',
													'pricelist_id': pricelist.id,
													
													'treatment': self.id,
												})
	#print(order)



	# Create Order Lines
	for cart_line in self.shopping_cart_ids:

		product = cart_line.product

		#print(product)
		#print(product.name)

		# Check if product complete 
		print()
		print('Check product_product complete')
		print(product)
		print(product.name)
		print(product.pl_price_list)
		print(product.pl_treatment)
		print(product.pl_family)

		#print(product.pl_subfamily)
		#print(product.pl_zone)
		#print(product.pl_pathology)
		#print(product.pl_sessions)
		#print(product.pl_level)
		#print(product.pl_time)
		#print(product.pl_zone)
		
		print()

		# Create Order Line
		ol = order.order_line.create({
										'product_id': 	product.id,

										'name': 		product.name,
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
