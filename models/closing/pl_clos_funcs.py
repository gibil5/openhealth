# -*- coding: utf-8 -*-
"""
 		clos_funcs.py

 		Created: 			       2016
		Last up: 	 		 4 Sep 2018
"""
from __future__ import print_function
import datetime

#from openerp.addons.openhealth.models.order import clos_funcs
#from . import clos_funcs

from . import lib



# ----------------------------------------------------------- Set Form Total ----------------------------
def pl_set_form_totals(self):
	"""
	Get Form Totals - Formas de Pago
	"""
	print()
	print('2019 - Get Form Totals')


	# Get Orders
	x_type = 'all'

	#orders, count = clos_funcs.get_orders(self, self.date, x_type)


	state = 'credit_note'
	#orders, count = clos_funcs.get_orders_by_state(self, self.date, state)
	orders, count = lib.get_orders_by_state_all(self, self.date)  		# Only used by Closings
	#print(orders)
	#print(count)



	# Init
	cash_tot = 0
	ame_tot = 0
	din_tot = 0
	mac_tot = 0
	mad_tot = 0
	vic_tot = 0
	vid_tot = 0

	bbva_tot = 0
	scotiabank_tot = 0
	interbank_tot = 0
	bcp_tot = 0


	# Loop
	for order in orders:

		#print(order.state)


		if order.state == 'credit_note':
			payment_method = order.x_credit_note_owner.x_payment_method
			coeff = -1

		else:
			payment_method = order.x_payment_method
			coeff = 1


		#for pm_line in order.x_payment_method.pm_line_ids:
		for pm_line in payment_method.pm_line_ids:

			#print('mark')
			#print(pm_line.method)


			subtotal = pm_line.subtotal * coeff


			# Standard - Cash and Cards
			if pm_line.method == 'cash':
				#cash_tot = cash_tot + pm_line.subtotal
				cash_tot = cash_tot + subtotal

			elif pm_line.method == 'american_express':
				#ame_tot = ame_tot + pm_line.subtotal
				ame_tot = ame_tot + subtotal

			elif pm_line.method == 'diners':
				#din_tot = din_tot + pm_line.subtotal
				din_tot = din_tot + subtotal

			elif pm_line.method == 'credit_master':
				#mac_tot = mac_tot + pm_line.subtotal
				mac_tot = mac_tot + subtotal

			elif pm_line.method == 'debit_master':
				#mad_tot = mad_tot + pm_line.subtotal
				mad_tot = mad_tot + subtotal

			elif pm_line.method == 'credit_visa':
				#vic_tot = vic_tot + pm_line.subtotal
				vic_tot = vic_tot + subtotal

			elif pm_line.method == 'debit_visa':
				#vid_tot = vid_tot + pm_line.subtotal
				vid_tot = vid_tot + subtotal


			# New - Banks
			elif pm_line.method == 'bbva':
				#bbva_tot = bbva_tot + pm_line.subtotal
				bbva_tot = bbva_tot + subtotal

			elif pm_line.method == 'interbank':
				#interbank_tot = interbank_tot + pm_line.subtotal
				interbank_tot = interbank_tot + subtotal

			elif pm_line.method == 'scotiabank':
				#scotiabank_tot = scotiabank_tot + pm_line.subtotal
				scotiabank_tot = scotiabank_tot + subtotal

			elif pm_line.method == 'bcp':
				#bcp_tot = bcp_tot + pm_line.subtotal
				bcp_tot = bcp_tot + subtotal




	# Form
	self.cash_tot = cash_tot
	self.ame_tot = ame_tot
	self.din_tot = din_tot

	self.mac_tot = mac_tot
	self.mad_tot = mad_tot
	self.vic_tot = vic_tot

	self.vid_tot = vid_tot
	self.bbva_tot = bbva_tot
	self.interbank_tot = interbank_tot

	self.scotiabank_tot = scotiabank_tot
	self.bcp_tot = bcp_tot

	#return cash_tot, ame_tot, din_tot, 	mac_tot, mad_tot, vic_tot, 		vid_tot, bbva_tot, interbank_tot

# get_form_totals

