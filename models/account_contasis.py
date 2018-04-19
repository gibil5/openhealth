# -*- coding: utf-8 -*-
#
# 	Account Contasis
# 
# Created: 				18 April 2018
#
#

from openerp import models, fields, api

import datetime

import resap_funcs



class AccountContasis(models.Model):
	
	#_inherit='sale.closing'

	_name = 'openhealth.account.contasis'
	
	_order = 'create_date desc'





# ----------------------------------------------------------- Relational ------------------------------------------------------

	# Lines 
	account_line = fields.One2many(
			'openhealth.account.line', 
			'account_id', 
		)






# ----------------------------------------------------------- Primitives ------------------------------------------------------
	
	# Name 
	name = fields.Char(
		)

	vspace = fields.Char(
			' ', 
			readonly=True
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
			#required=True, 
		)

	date_end = fields.Date(
			string="Fecha Fin", 
			default = fields.Date.today, 
			#readonly=True,
			#required=True, 
		)





	# Totals
	total_amount = fields.Float(
			'Total',
			#default = 0, 
		)

	# Totals
	total_count = fields.Integer(
			'Total',
			#default = 0, 
		)











# ----------------------------------------------------------- Actions ------------------------------------------------------

	# Update 
	@api.multi
	def update_totals(self):  

		print 'jx'
		print 'Update totals'





		# Totals 
		orders,count = resap_funcs.get_orders_filter(self, self.date_begin, self.date_end)

		amount_sum = 0 
		count = 0 

		for order in orders: 
			
			amount_sum = amount_sum + order.amount_untaxed 
			count = count + 1
		
			serial_nr = order.x_serial_nr
			date = order.date_order
			patient = order.patient.id  
			amount = order.amount_untaxed


			self.account_line.create({

										'serial_nr': serial_nr, 

										'date': date,

										'patient': patient, 

										'amount': amount,

										'account_id': self.id, 
				})




		self.total_amount = amount_sum
		self.total_count = count




		






