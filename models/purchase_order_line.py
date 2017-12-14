# -*- coding: utf-8 -*-
#
#
# 		*** OPEN HEALTH - Purchase Order line  
# 
# Created: 				13 Dec 2017
# Last updated: 	 	13 Dec 2017

from openerp import models, fields, api




class PurchaseOrderLine(models.Model):
	
	_inherit = 'purchase.order.line'
	_description = "Purchase Order Line"




	product_qty = fields.Float(
			string='Quantity', 

			#digits=dp.get_precision('Product Unit of Measure'), 
			digits=(16, 0), 
			
			required=True,
		)
	
	
	#date_planned = fields.Datetime(
	date_planned = fields.Date(
			string='Scheduled Date', 
			required=True, 
			index=True
		)



	#x_default_code = fields.Char(
	#		string='Código', 
	#	)








