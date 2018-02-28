# -*- coding: utf-8 -*-
#
# 	Order Report
# 
#
from openerp import models, fields, api

class sale_order_report(models.Model):

	_inherit='sale.order'					# Very important 

	_description = "Openhealth Order Report"

	_name = 'openhealth.order.report'




# ----------------------------------------------------------- Actions ------------------------------------------------------






# ----------------------------------------------------------- Primitives ------------------------------------------------------

	# Total 
	amount_total_report = fields.Float(
			'Total S/.', 
			default='0', 

			compute='_compute_amount_total_report', 
		)

	@api.multi
	def _compute_amount_total_report(self):
		for record in self:		
			total = 0 
			for line in record.order_line_report: 
				total = total + line.price_subtotal 
			record.amount_total_report = total




	# Line 
	order_line_report = fields.One2many(

			'sale.order.line', 
			'order_report_id', 

			string='Order Lines Report', 
			states={'cancel': [('readonly', True)], 'done': [('readonly', True)]}, 
			copy=True, 
		)


