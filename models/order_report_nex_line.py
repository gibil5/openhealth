# -*- coding: utf-8 -*-
#
# 	Order Line Report
# 

from openerp import models, fields, api

import openerp.addons.decimal_precision as dp




class order_report_nex_line(models.Model):

	#_inherit='sale.order.line'

	_name = 'openhealth.order.report.nex.line'

	_description = "Openhealth Order Report Nex Line"






	# Report Sale Product 
	report_sale_product_id = fields.Many2one(

		'openhealth.report.sale.product', 
		
		string='Report Reference', 		
		ondelete='cascade', 
	)






	# Order Report Nex 
	order_report_nex_id = fields.Many2one(

		#'sale.order', 
		'openhealth.order.report.nex', 
		
		string='Order Reference', 		
		ondelete='cascade', 

		#required=False, 
		#index=True, 
		#copy=False
	)





	# Date Created 
	x_date_created = fields.Datetime(
			string='Fecha', 
		)






	name = fields.Text(
		string='Description', 
		required=True, 
		)
	

	product_id = fields.Many2one(
		'product.product', 
		
		string='Producto', 
		
		domain=[('sale_ok', '=', True)], 
		change_default=True, 
		ondelete='restrict', 
		required=True, 
		)
	

	price_unit = fields.Float(
		
		'Precio Unit.', 
		
		required=True, 
		digits=dp.get_precision('Product Price'), 
		default=0.0, 
		)
	

	product_uom_qty = fields.Float(

		string='Cantidad', 
		
		digits=dp.get_precision('Product Unit of Measure'), 
		required=True, 
		default=1.0
		)
	



	#price_subtotal = fields.Monetary(
	price_subtotal = fields.Float(
		compute='_compute_amount', 

		string='Subtotal', 
		
		readonly=True, 
		store=True, 
		)
		
		
	#price_total = fields.Monetary(
	price_total = fields.Float(
		compute='_compute_amount', 
		string='Total', 
		readonly=True, 
		store=True
		)





	#@api.depends('product_uom_qty', 'discount', 'price_unit', 'tax_id')
	@api.depends('product_uom_qty', 'price_unit')
	def _compute_amount(self):
		for line in self:
			price = line.price_unit
			total = price * line.product_uom_qty
			line.update({
				'price_total': total,
				'price_subtotal': total,
			})






	#@api.depends('product_uom_qty', 'discount', 'price_unit', 'tax_id')
	#def _compute_amount(self):
		"""
		Compute the amounts of the SO line.
		"""
	#   for line in self:
			
	#		price = line.price_unit * (1 - (line.discount or 0.0) / 100.0)
			
			#taxes = line.tax_id.compute_all(price, line.order_id.currency_id, line.product_uom_qty, product=line.product_id, partner=line.order_id.partner_id)
			
	#		line.update({
				#'price_tax': taxes['total_included'] - taxes['total_excluded'],
	#			'price_total': taxes['total_included'],
	#			'price_subtotal': taxes['total_excluded'],
	#		})




