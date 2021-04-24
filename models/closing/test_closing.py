# -*- coding: utf-8 -*-
"""
		Test Closing

 		Created: 			30 Dec 2019
		Last up: 	 		30 Dec 2019
"""
from __future__ import print_function
from openerp import models, fields, api
#from openerp.addons.price_list.models.treatment import pl_creates  	# Use static method

# ----------------------------------------------------------- Pay ---------------------------------
def pay_myself(order, x_type, method):
	"""
	Pay Order
	"""
	print()
	print('Pay myself')

	if order.state == 'draft':


		order.create_payment_method()

		order.x_payment_method.saledoc = x_type


		# Here
		for line in order.x_payment_method.pm_line_ids:
			line.method = method



		order.x_payment_method.state = 'done'

		order.state = 'sent'

		order.validate_and_confirm()




# ----------------------------------------------------------- Create Order Consultation  ----------
@api.multi
def create_order_con(self, partner, patient, doctor, x_type, method):
	"""
	Create Order Consultation Standard - Medical
	"""
	print()
	print('TC - Create Order Con Med')


	# Init
	price_list = '2019'
	target = 'consultation'

	order = create_order(self, partner, patient, doctor, target, price_list)

	if order.state in ['draft']:
		pay_myself(order, x_type, method)

	return order



# ----------------------------------------------------------- Create Order Target -----------------

def create_order(self, partner, patient, doctor, target, price_list):
	"""
	Create Order - By Line
	"""
	print()
	print('TC - Create Order Con')
	print(target)


	price_list = '2019'


	# Create Order
	order = self.env['sale.order'].create({
													'state':		'draft',

													'partner_id': 	partner.id,
													'patient': 		patient.id,

													'x_doctor': 	doctor.id,

													'x_ruc': 		patient.x_ruc,
													'x_id_doc': 	patient.x_id_doc,
													'x_id_doc_type': patient.x_id_doc_type,
													'x_family': 	'consultation',

													#'treatment': self.id,
												})
	print(order)


	# Init
	_dic_con = {
					'consultation':		'CONSULTA MEDICA',
	}

	name = _dic_con[target]


	# Search
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
	ol = order.order_line.create({
									'name': 			product.name,
									'product_id': 		product.id,
									'order_id': 		order.id,
								})
	return order

	# pl_create_order_con

