# -*- coding: utf-8 -*-
"""
	Order - Controller

	Created: 			 6 dec 2020
	Last up: 			 5 apr 2021
"""
from __future__ import print_function
from openerp import models, fields, api

from .commons import pl_creates, action_funcs

class OrderBl(models.Model):
	"""
    Order controller.
    Directs flow between Order and other models (Treatment).
	"""
	_inherit = 'sale.order'


# ---------------------------------------------------- Used by Treatment - Create Proc -------
	def create_procedure_man(self, treatment):
		"""
		Create Procedure Man - In prog
		Used by: Treatment
		"""
		# Update Order
		self.x_procedure_created = True
		# Loop
		for line in self.order_line:
			print(line.product_id)
			if line.product_id.is_procedure():
				product_product = line.product_id
				# Create Procedure
				pl_creates.create_procedure(treatment, product_product)

	def proc_is_not_created_and_state_is_sale(self):
		"""
		Used by: Treatment
		"""
		print()
		print('order - proc_is_not_created_and_state_is_sale')
		return not self.x_procedure_created and self.state == 'sale'


# ----------------------------------------------------------- Test - Pay myself --------------
	def pay_myself(self):
		"""
		Pay Myself
		Used by: Treatment Test
		"""
		print()
		print('Order - Pay myself')
		if self.state == 'draft':
			self.create_payment_method()
			self.x_payment_method.saledoc = 'ticket_receipt'
			self.x_payment_method.state = 'done'
			self.state = 'sent'
			self.validate_and_confirm()


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
		Open myself
		Used by Payment Method comeback
		"""
		print('open_myself')
		res_model = self._name
		res_id = self.id
		return action_funcs.open_myself(res_model, res_id)

