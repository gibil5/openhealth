# -*- coding: utf-8 -*-
"""
	ReportSaleProduct

	Only Data model. No functions.

 	Created: 			    Nov 2016
	Last up: 	 		 10 Dec 2019
"""

from __future__ import print_function
from openerp import models, fields, api

#from openerp.addons.openhealth.models.management import mgt_funcs

class ReportSaleProduct(models.Model):
	"""
	Uses:
		Product Item Counter
	Used by:
		Caja
	As: 
		Venta de Productos por Fecha
	"""
	
	_name = 'openhealth.report.sale.product'
	


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




# ----------------------------------------------------------- Primitives ------------------------------------------------------

	# Title 
	title = fields.Char(
			string="Nombre",
		)




	# Name 
	name = fields.Date(
			string="Fecha", 
			default = fields.Date.today, 
			#readonly=True,
			required=True, 
		)




	# Dates
	date_begin = fields.Date(
			string="Fecha Inicio", 
		)

	date_end = fields.Date(
			string="Fecha Final", 
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

