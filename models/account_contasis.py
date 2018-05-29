# -*- coding: utf-8 -*-
#
# 	Account Contasis
# 
# Created: 				18 April 2018
#

from openerp import models, fields, api
import datetime
import resap_funcs
import acc_funcs


class AccountContasis(models.Model):

	#_inherit='sale.closing'

	_name = 'openhealth.account.contasis'

	#_order = 'create_date desc'
	#_order = 'date_begin asc'
	_order = 'date_begin asc,name asc'




# ----------------------------------------------------------- Inheritable ------------------------------------------------------



# ----------------------------------------------------------- Relational ------------------------------------------------------


	# Account Lines 
	account_line = fields.One2many(
			'openhealth.account.line', 
			'account_id', 
		)

	# Payment Lines 
	payment_line = fields.One2many(
			'openhealth.payment_method_line',
			'account_id', 			
		)






# ----------------------------------------------------------- Primitives ------------------------------------------------------
	
	# Name 
	name = fields.Char(
			string="Nombre", 		
			required=True, 
		)


	# Type 
	x_type = fields.Selection(

			selection=[	
						('order', 		'Ventas'),
						('patient', 	'Pacientes'),
			], 

			string="Tipo",
			
			#required=True, 
			required=False, 
		)






	# Dates
	date = fields.Date(
			string="Fecha", 
			default = fields.Date.today, 
			#readonly=True,
			required=True, 
		)


	date_begin = fields.Date(
			string="Fecha Inicio", 
			default = fields.Date.today, 
			#readonly=True,
			required=True, 
		)


	date_end = fields.Date(
			string="Fecha Fin", 
			default = fields.Date.today, 
			#readonly=True,
			required=True, 
		)




	vspace = fields.Char(
			' ', 
			readonly=True
		)




	# Totals
	total_amount = fields.Float(
			#'Total Monto',
			'Total',
			readonly=True, 
		)



	# Totals Count
	total_count = fields.Integer(
			#'Total Ventas',
			#'Nr',
			'Nr Pacientes',
			readonly=True, 
		)








# ----------------------------------------------------------- Actions ------------------------------------------------------

	# Update Orders
	@api.multi
	def update_orders(self):  

		print
		print 'Update Orders'



		# Clear 
		self.account_line.unlink()
		self.payment_line.unlink()



		# Orders 
		orders,count = resap_funcs.get_orders_filter(self, self.date_begin, self.date_end)

		amount_sum = 0 
		count = 0 



		# Loop 
		for order in orders: 
			
			# Stats 
			amount_sum = amount_sum + order.amount_untaxed 
			count = count + 1
		
		
			# Vars Order 
			serial_nr = order.x_serial_nr


			date = order.date_order
			#print date 


			patient = order.patient.id 
			x_type = order.x_type


			state = order.state



			# Document and Document type 
			if x_type in ['invoice', 'ticket_invoice']: 	# Ruc 
				document = order.patient.x_ruc
				document_type = '6'
			else: 
				if order.patient.x_dni != False: 			# Dni
					document = order.patient.x_dni
					document_type = '1'
				else: 
					document = order.patient.x_id_doc
					document_type = acc_funcs._doc_type[order.patient.x_id_doc_type]




			# Account Lines 
			for line in order.order_line:

				amount = line.price_subtotal
				amount_net, amount_tax = acc_funcs.get_net_tax(self, amount)
				
				
				product = line.product_id.id
				qty = line.product_uom_qty


				acc_line = self.account_line.create({
														'name': order.name, 
														'patient': patient, 
														
														'product': product, 
														'qty': qty, 

														'state': state, 

														'serial_nr': serial_nr, 
														'x_type': x_type, 
														'document': document, 					# Id Doc
														'document_type': document_type, 		# Id Doc Type 
														
														'date': date,
														'date_time': date,

														'amount': amount,
														'amount_net': amount_net,
														'amount_tax': amount_tax,


														'account_id': self.id, 
					})

				acc_line.update_fields()





			# Payment Lines 
			for line in order.x_payment_method.pm_line_ids:

				#amount = line.price_subtotal
				#amount_net, amount_tax = acc_funcs.get_net_tax(self, amount)


				pay_line = self.payment_line.create({
														#'patient': patient, 
														#'serial_nr': serial_nr, 
														#'x_type': x_type, 
														#'document': document, 					# Id Doc
														#'document_type': document_type, 		# Id Doc Type 
														#'date': date,
														#'date_time': date,
														#'amount': amount,
														#'amount_net': amount_net,
														#'amount_tax': amount_tax,

														'patient': patient, 
														'serial_nr': serial_nr, 
														'x_type': x_type, 
														'date_time': date,

														'name': line.name, 
														'subtotal': line.subtotal, 
														'method': line.method, 
																												
														'account_id': self.id, 
					})









		# Stats 
		self.total_amount = amount_sum
		self.total_count = count

	# update_orders
