# -*- coding: utf-8 -*-
"""
	Item Counter

	Created: 	2018
	Last up:	10 Dec 2019
"""
from openerp import models, fields, api

class ItemCounter(models.Model):
	"""
	Used by:
		Report Sale Product
	"""

	_name = 'openhealth.item.counter'
	

# ----------------------------------------------------------- Relational ------------------------------------------------------

	# Report Sale Product 
	report_sale_product_id = fields.Many2one(
		'openhealth.report.sale.product', 
		string='Report Reference', 		
		ondelete='cascade', 
	)



# ----------------------------------------------------------- Vars ------------------------------------------------------
	name = fields.Char(
		)

	qty = fields.Integer(
			string="Cantidad", 
		)

	total = fields.Float(
			string="Total", 
		)


