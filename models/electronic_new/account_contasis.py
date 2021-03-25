# -*- coding: utf-8 -*-
"""
 	Account Contasis

 	Created: 				18 Apr 2018
 	Last up: 				10 Dec 2018
"""
from openerp import models, fields, api
from . import acc_lib
from . import acc_vars

class AccountContasis(models.Model):
	"""
	high level support for doing this and that.
	"""
	_inherit = 'openhealth.account.contasis'

	_order = 'date_begin asc,name asc'



# ----------------------------------------------------------- Update ------------------------------

	# Update
	@api.multi
	def update(self):
		"""
		Update Account
		"""
		#print()
		#print('Pl - Account - Update')

		# Clean
		self.account_line.unlink()
		self.payment_line.unlink()

		# Sales and Cancelled
		#orders, count = acc_funcs.get_orders_filter(self, self.date_begin, self.date_end)
		orders, count = acc_lib.AccFuncs.get_orders_filter(self, self.date_begin, self.date_end)
		count = 0
		amount_sum = 0


		# Loop
		for order in orders:

			# Stats
			amount_sum = amount_sum + order.amount_untaxed
			count = count + 1


			# Init - From Order
			serial_nr = order.x_serial_nr
			date = order.date_order
			patient = order.patient.id
			x_type = order.x_type
			state = order.state


			# Document and Document type
			if x_type in ['invoice', 'ticket_invoice']: 		# Ruc
				document = order.patient.x_ruc
				document_type = '6'
				#print('mark 1')

			else:
				if order.patient.x_dni != False: 				# Dni
					document = order.patient.x_dni
					document_type = '1'
					#print('mark 2')

				else: 											# Other
					document = order.patient.x_id_doc
					document_type = acc_vars._doc_type[order.patient.x_id_doc_type]
					#print('mark 3')




			# Account Lines - Registro de Ventas and Contasis
			for line in order.order_line:

				# Init from Line
				amount = line.price_subtotal
				product = line.product_id.id
				qty = line.product_uom_qty

				# Net and Taxes
				#amount_net, amount_tax = acc_funcs.get_net_tax(self, amount)
				amount_net, amount_tax = acc_lib.AccFuncs.get_net_tax(amount)

				# Create
				acc_line = self.account_line.create({
														'name': order.name,
														'patient': patient,
														'product': product,
														'qty': qty,
														'state': state,
														'serial_nr': serial_nr,
														'date': date,
														'date_time': date,
														'amount': amount,
														'amount_net': amount_net,
														'amount_tax': amount_tax,
														'x_type': x_type,


														'document': document, 					# Id Doc  		-> Here !

														'document_type': document_type, 		# Id Doc Type


														'account_id': self.id,
					})

				acc_line.update_fields()




			# Payment Method Lines - Tarjetas
			for line in order.x_payment_method.pm_line_ids:

				# Create
				pay_line = self.payment_line.create({
														'patient': patient,
														'serial_nr': serial_nr,
														'x_type': x_type,
														'date_time': date,
														'name': line.name,
														'subtotal': line.subtotal,
														'method': line.method,
														'document': document, 					# Id Doc  		-> Here !
														'document_type': document_type,
														'state': state, 						# Very important !

														'account_id': self.id,
					})
				pay_line.update_fields()

		# Stats
		self.total_amount = amount_sum
		self.total_count = count
	# update



# ----------------------------------------------------------- Dep --------------------------------
	#test_target = fields.Boolean(
	#		string="Test Target",
	#	)
