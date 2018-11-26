# -*- coding: utf-8 -*-
"""
 	test_order.py

 	Test - Order

	Created: 			20 Nov 2018
	Last up: 	 		20 Nov 2018
"""



# ----------------------------------------------------------- Test --------------------------------
# Test
def test(self):
	"""
	high level support for doing this and that.
	"""
	#print
	#print 'Order - Test'
	if self.patient.x_test:
		self.x_test_case = 'ticket_receipt'
		test_integration(self)
# test




# ----------------------------------------------------------- Integration -------------------------
#def test_integration(self, test_case=False):
def test_integration(self):
	"""
	Test the whole Sale Cycle.
	With UI buttons included. Activate the different creation and write procedures.
	"""
	#print
	#print 'Order - Test Integration'


# Cycle - Begin

	# Create and Init - PM
	self.create_payment_method()


	# Type
	self.x_payment_method.saledoc = self.x_test_case


	#print self.x_payment_method.name
	self.x_payment_method.go_back()
	#print self.x_payment_method.state

	# Order
	self.validate()
	self.action_confirm_nex()
	self.print_ticket()


	# Cancel
	#if test_case in ['ticket_invoice_cancel', 'ticket_receipt_cancel']:
	#	self.cancel_order()

# Cycle - End

# test_integration



# ----------------------------------------------------------- Actions -----------------------------
# Actions
def test_actions(self):
	"""
	high level support for doing this and that.
	"""
	#print
	#print 'Order - Actions'
	self.state_force()
	self.state_force()
	self.open_product_selector_product()
	self.open_product_selector_service()
	self.cancel_order()
	self.activate_order()
	self.open_line_current()



# ----------------------------------------------------------- Unit --------------------------------
# Test - Unit
def test_unit(self):
	"""
	high level support for doing this and that.
	"""
	#print
	#print 'Order - Test Unit'

	# Computes
	#self.test_computes()

	# Actions - Remaining
	#self.test_actions()

	# Init
	total = 0

	for line in self.order_line:
		# Standard
		#total = 	line.product_id.list_price * line.product_uom_qty 		+ total
		price_std = line.product_id.list_price
		price_vip = line.product_id.x_price_vip
		price_manual = line.x_price_manual
		qty = line.product_uom_qty
		compact = line.x_description


		# Prints
		#print 'product_id: ', line.product_id.name
		#print 'price_std: ', price_std
		#print 'price_vip: ', price_vip
		#print 'price_manual: ', price_manual
		#print 'qty: ', qty
		#print 'compact: ', compact

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
			# Is a service and has a Vip price
			if line.product_id.type in ['service'] and price_vip != 0:
				price = price_vip
			# Is a service and does not have a Vip price
			else:
				price = price_std


		# Total
		total = price * qty + total
		#print 'price: ', price
		#print 'total: ', total


	# Asserts
	#print
	#print 'Asserts'
	#print self.pricelist_id.name
	#print 'total: ', total
	#print 'self.amount_total: ', self.amount_total
	#assert self.amount_total == total    				# Assert

# test_unit




# ----------------------------------------------------------- Pay ---------------------------------
def pay_myself(self):
	"""
	high level support for doing this and that.
	"""
	#print
	#print 'Pay myself'

	if self.state == 'draft':
		self.create_payment_method()
		self.x_payment_method.saledoc = 'ticket_receipt'
		self.x_payment_method.state = 'done'
		self.state = 'sent'
		self.validate()
		self.action_confirm_nex()

		# Update
		#if date_order != False:
		#	self.write({
		#					'date_order': date_order,
		#			})
