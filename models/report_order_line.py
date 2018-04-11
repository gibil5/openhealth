# -*- coding: utf-8 -*-
#
# 	Order Line Report
# 

from openerp import models, fields, api
import openerp.addons.decimal_precision as dp


class order_report_nex_line(models.Model):

	#_inherit='sale.order.line'


	#_name = 'openhealth.order.report.nex.line'
	_name = 'openhealth.report.order_line'


	#_description = "Openhealth Order Report Nex Line"
	_description = "Openhealth Report Order Line"







# ----------------------------------------------------------- Handles ------------------------------------------------------
	
	# Report Sale 
	report_sale_id = fields.Many2one(

		'openhealth.report.sale', 
		
		string='Report Reference', 		
		ondelete='cascade', 
	)






	# Report Sale Product 
	report_sale_product_id = fields.Many2one(

		'openhealth.report.sale.product', 
		
		string='Report Reference', 		
		ondelete='cascade', 
	)




	# Order Report Nex 
	order_report_nex_id = fields.Many2one(

		'openhealth.order.report.nex', 
		
		string='Report Reference', 		
		ondelete='cascade', 
	)









# ----------------------------------------------------------- Primitives ------------------------------------------------------

	name = fields.Text(
		string='Description', 
		required=True, 
		)



	# Date Created 
	x_date_created = fields.Datetime(
			string='Fecha', 
		)





	#partner_id = fields.Many2one(
	#	'res.partner', 
		
	#	string='Cliente', 
	#	required=True, 		
	#	)
	



	patient = fields.Many2one(
		'oeh.medical.patient',

		string='Paciente', 
		#required=True, 		
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





# ----------------------------------------------------------- Computes ------------------------------------------------------

	# Compute Amount 
	@api.depends('product_uom_qty', 'price_unit')
	def _compute_amount(self):
		for line in self:
			price = line.price_unit
			total = price * line.product_uom_qty
			line.update({
				'price_total': total,
				'price_subtotal': total,
			})





