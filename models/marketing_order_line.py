# -*- coding: utf-8 -*-
#
#
# 	Marketing Order Line 
# 

from openerp import models, fields, api
import openerp.addons.decimal_precision as dp


class marketing_order_line(models.Model):

	#_inherit='sale.order.line'

	_name = 'openhealth.marketing.order.line'

	_description = "Openhealth Marketing Order Line"





# ----------------------------------------------------------- Inheritable ------------------------------------------------------

	patient = fields.Many2one(
		'oeh.medical.patient',

		string='Paciente', 
		#required=True, 		
		)



	doctor = fields.Many2one(
			'oeh.medical.physician',
			string = "Médico", 	
		)



	product_id = fields.Many2one(
			'product.product', 
			
			string='Producto', 
			domain=[('sale_ok', '=', True)], 
			change_default=True, 
			ondelete='restrict', 
			required=True, 
		)




	# Date Created 
	x_date_created = fields.Datetime(
			string='Fecha', 
		)





# ----------------------------------------------------------- Handles ------------------------------------------------------
	
	# Patient Line  
	patient_line_sale_id = fields.Many2one(			
			'openhealth.patient.line',
			ondelete='cascade', 			
		)




	# Patient Line  Proc
	patient_line_id_proc = fields.Many2one(
			'openhealth.patient.line',
			ondelete='cascade', 			
		)



	# Patient Line  
	patient_line_id = fields.Many2one(			
			'openhealth.patient.line',
			ondelete='cascade', 			
		)



	# Patient Line Vip 
	patient_line_id_vip = fields.Many2one(
			'openhealth.patient.line',
			ondelete='cascade', 			
		)






# ----------------------------------------------------------- Primitives ------------------------------------------------------

	name = fields.Text(
		string='Description', 
		required=True, 
		)



	# State 
	#state = fields.Selection(
	#		selection = ord_vars._state_list, 
	#		string='Estado',	
			#readonly=False,
			#default='draft',
	#	)
















	

	


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





