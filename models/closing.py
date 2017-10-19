# -*- coding: utf-8 -*-
#
#
# 	Closing 
# 
# Created: 				18 Oct 2017
# Last updated: 	 	18 Oct 2017
#



from openerp import models, fields, api
import datetime


class Closing(models.Model):
	
	#_inherit='sale.closing'
	_name = 'openhealth.closing'
	




	# Name 
	name = fields.Char(
			string="Cierre de Caja #", 

			#compute='_compute_name', 
		)


	vspace = fields.Char(
			' ', 
			readonly=True
		)



	#date = fields.Datetime(
	date = fields.Date(
			
			string="Fecha", 

			default = fields.Date.today, 
			
			#readonly=True,

			
			#required=False, 
			required=True, 

			#compute='_compute_x_appointment_date', 
		)




	total = fields.Float(
			'Total',

			default = 0, 

			compute='_compute_total', 
		)


	@api.multi
	#@api.depends('x_appointment')

	def _compute_total(self):
		for record in self:

			print 'jx'
			print 'compute total'


			date = record.date + ' '
			print 'date: ', date 


			orders = record.env['sale.order'].search([

														('state', '=', 'sale'),
														
														#('date_order', '=', '2017-10-18'),
														#('date_order', 'like', '2017-10-18'),
														#('date_order', 'like', '2017-10-18 '),
														('date_order', 'like', date),

#'2017-10-18 21:23:18'

														#('x_name_short','=', target),
														#('x_origin','=', False),
												])

			print 'orders: ', orders


			amount_untaxed = 0 
			count = 0 


			for order in orders: 
				amount_untaxed = amount_untaxed + order.amount_untaxed 
				count = count + 1


			print 'amount_untaxed: ', amount_untaxed
			print 'count: ', count

			#record.total = 5.5 
			record.total = amount_untaxed

			print 



	# orders 
	#order_ids = fields.One2many(
	#		'sale.order',			 
	#		'closing', 
	#		string="Ventas",
	#		domain = [
	#					('state', '=', 'sale'),
	#					('date_order', '=', '2017-10-18'),
	#				],
	#	)





