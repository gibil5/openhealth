# -*- coding: utf-8 -*-
#
# 	Order Line
# 
#

from openerp import models, fields, api



class sale_order_line(models.Model):


	#_name = 'openhealth.order_line'

	_inherit='sale.order.line'






	product_uom_qty = fields.Float(
		string='Quantity', 

		#required=True, 

		#digits=dp.get_precision('Product Unit of Measure'), 		
		#digits=(16, 1), 
		digits=(16, 0), 

		required=False,
		default=1.0
	)




	product_uom = fields.Many2one(
		'product.uom', 
		string='Unit of Measure', 
		#required=True
		required = False,
	)

#product_uom_qty = fields.Float(string='Quantity', digits=dp.get_precision('Product Unit of Measure'), required=True, default=1.0)
#product_uom = fields.Many2one('product.uom', string='Unit of Measure', required=True)


	customer_lead = fields.Float(
		'Delivery Lead Time', 

		#required=True, 
		required=False, 

		default=0.0,
		help="Number of days between the order confirmation and the shipping of the products to the customer", oldname="delay")



	order_id = fields.Many2one('sale.order', string='Order Reference', 
		
		#required=True, 
		required=False, 
		
		ondelete='cascade', index=True, copy=False)




	x_price_vip = fields.Float(
			string="Precio Vip",

			required=False, 
		)



