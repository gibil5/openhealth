# -*- coding: utf-8 -*-
"""
	order_procedure.py
	OrderProcedure Class

	Created: 			31 Jul 2020
	Last up: 	 		31 Jul 2020
"""
from . import pl_creates

class OrderProcedure(object):
	"""
	Used by Treatment.
	"""

	def __init__(self, service_list):
		print('OrderProcedure - init')
		self.service_list = service_list


    def create_order(env, shopping_cart_ids)

		# Create Cart
		for service_ids in service_list:

			for service in service_ids:

				if (service.service.name not in [False]) 	and 	(service.service.pl_price_list in [price_list]):

					# Product
					print()
					print('Product search')
					#product = self.env['product.product'].search([
					product = env.search([
																	('name', '=', service.service.name),
																	('sale_ok', '=', True),
																	('pl_price_list', '=', '2019'),
													])
					#print(product)

					# Create Cart
					print()
					print('Create cart')
					if product.name not in [False]:
						#cart_line = self.shopping_cart_ids.create({
						cart_line = shopping_cart_ids.create({
																			'product': 		product.id,
																			'price': 		service.price_applied,
																			#'qty': 			service.qty,
																			'qty': 			1,
																			'treatment': 	self.id,
																})

		# Create Order
		print()
		print('Create order')
		order = pl_creates.pl_create_order(self)
		#print(order)
