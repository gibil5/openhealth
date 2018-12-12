# -*- coding: utf-8 -*-
#
# 	Order Line Report
# 

from openerp import models, fields, api



class sale_order_line_report(models.Model):

	_inherit='sale.order.line'

	_name = 'openhealth.order.line.report'




	order_id = fields.Many2one(

		#'sale.order', 
		'openhealth.order.report', 
		
		string='Order Reference', 		
		required=False, 
		ondelete='cascade', index=True, copy=False
	)



