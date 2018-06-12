# -*- coding: utf-8 -*-
#
#
# 	Marketing Order Line 
# 

from openerp import models, fields, api

#import openerp.addons.decimal_precision as dp


class marketing_order_line(models.Model):



	_inherit='openhealth.line'


	_name = 'openhealth.marketing.order.line'

	_description = "Openhealth Marketing Order Line"





# ----------------------------------------------------------- Inheritable ------------------------------------------------------

	#name = fields.Text(
	#	string='Description', 
	#	required=True, 
	#	)

	#patient = fields.Many2one(
	#	'oeh.medical.patient',
	#	string='Paciente', 
		#required=True, 		
	#	)


	# Doctor 
	doctor = fields.Many2one(
			'oeh.medical.physician',
			string = "Médico", 	
		)






	# Date Created 
	#x_date_created = fields.Datetime(
	#		string='Fecha', 
	#	)


	# Product 
	#product_id = fields.Many2one(
			
	#		'product.product', 
			
	#		string='Producto', 
	#		domain=[('sale_ok', '=', True)], 
	#		change_default=True, 
	#		ondelete='restrict', 
	#		required=True, 
	#	)


	# Qty
	#product_uom_qty = fields.Float(
	#	string='Cantidad', 
	#	digits=dp.get_precision('Product Unit of Measure'), 
	#	required=True, 
	#	default=1.0
	#	)



	# Prices 
	#price_unit = fields.Float(
	#	'Precio Unit.', 
	#	required=True, 
	#	digits=dp.get_precision('Product Price'), 
	#	default=0.0, 
	#	)
	
	#price_subtotal = fields.Monetary(
	#price_subtotal = fields.Float(
	#	compute='_compute_amount', 
	#	string='Subtotal', 
	#	readonly=True, 
	#	store=True, 
	#	)
		
	#price_total = fields.Monetary(
	#price_total = fields.Float(
	#	compute='_compute_amount', 
	#	string='Total', 
	#	readonly=True, 
	#	store=True
	#	)



	# Compute Amount 
	#@api.depends('product_uom_qty', 'price_unit')
	#def _compute_amount(self):
	#	for line in self:
	#		price = line.price_unit
	#		total = price * line.product_uom_qty
	#		line.update({
	#			'price_total': total,
	#			'price_subtotal': total,
	#		})








# ----------------------------------------------------------- Handles ------------------------------------------------------
	

	# Marketing Id
	marketing_id = fields.Many2one(			
			'openhealth.marketing',
			ondelete='cascade', 			
		)




	# Budget 
	patient_line_budget_id = fields.Many2one(			
			'openhealth.patient.line',
			ondelete='cascade', 			
		)



	# Sale 
	patient_line_sale_id = fields.Many2one(			
			'openhealth.patient.line',
			ondelete='cascade', 			
		)


	# Consu 
	patient_line_consu_id = fields.Many2one(			
			'openhealth.patient.line',
			ondelete='cascade', 			
		)


	# Product
	patient_line_product_id = fields.Many2one(			
			'openhealth.patient.line',
			ondelete='cascade', 			
		)



	# Proc
	patient_line_proc_id = fields.Many2one(
			'openhealth.patient.line',
			ondelete='cascade', 			
		)






	# Patient Line - Vip
	patient_line_id = fields.Many2one(			
			'openhealth.patient.line',
			ondelete='cascade', 			
		)



	# Patient Line - Vip with card 
	patient_line_id_vip = fields.Many2one(
			'openhealth.patient.line',
			ondelete='cascade', 			
		)






# ----------------------------------------------------------- Primitives ------------------------------------------------------


	# State 
	#state = fields.Selection(
	#		selection = ord_vars._state_list, 
	#		string='Estado',	
			#readonly=False,
			#default='draft',
	#	)











# ----------------------------------------------------------- Computes ------------------------------------------------------




