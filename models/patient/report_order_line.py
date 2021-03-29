# -*- coding: utf-8 -*-
"""
	Order Line Report

	Created: 			28 May 2018
	Last up: 	 		29 mar 2021
"""
from openerp import models, fields, api
from openerp.addons.openhealth.models.order import ord_vars
import openerp.addons.decimal_precision as dp

#from openerp.addons.openhealth.models.libs import lib
from openerp.addons.openhealth.models.commons.libs import lib

#class order_report_nex_line(models.Model):
class PatientOrderReport(models.Model):
	"""
	Used by:
		- Patient - Estado de Cuenta
		- Order - Report Sale Product
	"""
	_name = 'openhealth.report.order_line'

	#_inherit='openhealth.line'

	_description = "Openhealth Report Order Line"



# ----------------------------------------------------------- Inherited ------------------------------------------------------

	# Date Created 
	x_date_created = fields.Datetime(
			#string='Fecha', 
			string='Fecha y Hora', 
		)


	# Product Product 
	product_id = fields.Many2one(
			
			'product.product', 
			
			string='Producto', 
			domain=[('sale_ok', '=', True)], 
			change_default=True, 
			ondelete='restrict',
		)

	# Subtotal 
	price_subtotal = fields.Float(
			string='Subtotal', 
			readonly=True, 
			store=True, 

			compute='_compute_amount', 
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

	# Tax 
	price_tax = fields.Float(
			string='Tax', 
			#readonly=True, 
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

	# Unit Net 
	price_unit_net = fields.Float(
			string='Precio Unitario Neto', 
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





# ----------------------------------------------------------- Handles -----------------------------
	# Order Report Nex 
	order_report_nex_id = fields.Many2one(
			
			'openhealth.order.report.nex',
			
			string='Report Reference',

			ondelete='cascade', 
	)


# ----------------------------------------------------------- Report Sale Product -----------------
	# Report Sale Product 
	report_sale_product_id = fields.Many2one(

		'openhealth.report.sale.product', 
		
		string='Report Reference', 		

		ondelete='cascade', 
	)



# ----------------------------------------------------------- Primitives ------------------------------------------------------
	# State 
	state = fields.Selection(
			selection = ord_vars._state_list, 
			string='Estado',
		)
