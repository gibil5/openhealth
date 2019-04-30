# -*- coding: utf-8 -*-
"""
	Order Line Report

	Created: 			28 May 2018
	Last updated: 	 		30 Apr 2019
"""
from openerp import models, fields, api
from . import ord_vars

class order_report_nex_line(models.Model):
	"""
	Used by Estado de Cuenta.
	By Report Sale Product
	"""
	_name = 'openhealth.report.order_line'

	_inherit='openhealth.line'

	_description = "Openhealth Report Order Line"


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
			#readonly=False,
			#default='draft',
		)
