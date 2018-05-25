# -*- coding: utf-8 -*-
#
#
# 	Marketing Recommendation Line 
# 

from openerp import models, fields, api

import prodvars


class marketing_recommendation_line(models.Model):

	#_inherit='sale.order.line'

	_name = 'openhealth.marketing.recom.line'

	_description = "Openhealth Marketing Recommendation Line"





# ----------------------------------------------------------- Inheritable ------------------------------------------------------

	# Product
	product_id = fields.Many2one(

			#'product.product', 
			'product.template', 
			
			string='Producto', 
			domain=[('sale_ok', '=', True)], 
			change_default=True, 
			ondelete='restrict', 
			required=True, 
		)


	doctor = fields.Many2one(
			'oeh.medical.physician',
			string = "Médico", 	
		)




	# Prices
	
	price = fields.Float(

			string='Precio Standard', 
		) 

	price_vip = fields.Float(
			
			string='Precio VIP', 
		) 

	price_manual = fields.Float(

			string="Precio Manual",
		)


	price_applied = fields.Float(

			string='Precio Aplicado', 
		) 





	# Date Created 
	x_date_created = fields.Datetime(
			string='Fecha', 
		)



	# Sub Family
	#x_treatment = fields.Selection(
	sub_family = fields.Selection(
			selection=prodvars._treatment_list,
			required=False, 
		)	





# ----------------------------------------------------------- Handles ------------------------------------------------------
	
	# Patient Line  Proc
	patient_line_id = fields.Many2one(
			
			'openhealth.patient.line',
			
			ondelete='cascade', 			
		)


