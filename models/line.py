# -*- coding: utf-8 -*-
#
# 		Line
# 		Inherited by: management_order_line, marketing_order_line, order_report_nex_line, electronic_line 
# 		
# 		Created: 				26 May 2018
# 		Last updated: 			14 Sep 2018
#
from openerp import models, fields, api
import openerp.addons.decimal_precision as dp
import lib 

class Line(models.Model):	
	_name = 'openhealth.line'
	_order = 'x_date_created asc'



# ----------------------------------------------------------- Fields ------------------------------------------------------

	# Date Created 
	x_date_created = fields.Datetime(
			string='Fecha', 
		)


	# Name 
	name = fields.Char(
			string="Nombre", 		
			#required=True, 
		)



# ----------------------------------------------------------- Core ------------------------------------------------------

	# Product Product 
	product_id = fields.Many2one(
			
			'product.product', 
			
			string='Producto', 
			domain=[('sale_ok', '=', True)], 
			change_default=True, 
			ondelete='restrict', 			
			#required=True, 
		)


	# Qty
	product_uom_qty = fields.Float(
			string='Cantidad', 
			digits=dp.get_precision('Product Unit of Measure'), 
			default=1.0,
			required=True, 
		)


	# Unit 
	price_unit = fields.Float(
			'Precio Unit.', 
			digits=dp.get_precision('Product Price'), 
			default=0.0, 
			required=True, 
		)




# ----------------------------------------------------------- Prices - Computes ------------------------------------------------------

	# Unit Net 
	price_unit_net = fields.Float(
			string='Precio Unitario Neto', 
			#readonly=True, 
			store=True, 

			compute='_compute_amount', 
		)
	
	# Unit Tax
	#price_unit_tax = fields.Float(
	#		string='Precio Unitario Tax', 
			#readonly=True, 
	#		store=True, 

	#		compute='_compute_amount', 
	#	)




	
	# Subtotal 
	price_subtotal = fields.Float(
			string='Subtotal', 
			readonly=True, 
			store=True, 

			compute='_compute_amount', 
		)
	

	# Net 
	price_net = fields.Float(
			string='Neto', 
			#readonly=True, 
			store=True, 

			compute='_compute_amount', 
		)

	# Tax 
	price_tax = fields.Float(
			string='Tax', 
			#readonly=True, 
			store=True, 

			compute='_compute_amount', 
		)



	# Total 
	price_total = fields.Float(
			string='Total', 
			readonly=True, 
			store=True, 

			compute='_compute_amount', 
		)


	# Compute - Total and Subtotal 
	@api.depends('product_uom_qty', 'price_unit')
	def _compute_amount(self):
		for line in self:

			price_unit = line.price_unit
			unit_net, unit_tax = lib.get_net_tax(price_unit)
			

			total = price_unit * line.product_uom_qty
			net, tax = lib.get_net_tax(total)
			

			line.update({
				'price_total': total,
				'price_subtotal': total,

				'price_net': net,
				'price_tax': tax,

				'price_unit_net': unit_net,
				#'price_unit_tax': unit_tax,
			})


