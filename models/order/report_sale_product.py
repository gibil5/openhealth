# -*- coding: utf-8 -*-
"""
	ReportSaleProduct

	Only Data model. No functions.

 	Created: 			    Nov 2016
	Last up: 	 		 10 Dec 2019
"""

from __future__ import print_function
from openerp import models, fields, api

class ReportSaleProduct(models.Model):
	"""
	Uses:
		Product Item Counter
		Report Order Lines
	Used by:
		Caja
	As: 
		Venta de Productos por Fecha
	"""
	
	_name = 'openhealth.report.sale.product'
	
	_inherit='openhealth.django.interface'



# ----------------------------------------------------------- Relational ------------------------------------------------------	
	# Item Counter
	item_counter_ids = fields.One2many(
			'openhealth.item.counter', 
			'report_sale_product_id', 
		)


	# Order Lines - For detail
	order_line_ids = fields.One2many(
			'openhealth.report.order_line', 
			'report_sale_product_id', 
		)




# ----------------------------------------------------------- Redefined ------------------------------------------------------
	# Name 
	name = fields.Date(
			string="Fecha", 
			default = fields.Date.today, 
			#readonly=True,
			required=True, 
		)


# ----------------------------------------------------------- Primitives ------------------------------------------------------

	# Title 
	title = fields.Char(
			string="Nombre",
		)



	several_dates = fields.Boolean(
			'Varias Fechas',
			default=False,
		)


	# Totals
	total_qty = fields.Integer(
			string="Cantidad", 
		)

	total = fields.Float(
			string="Total", 
		)

	vspace = fields.Char(
			' ', 
			readonly=True
		)

