# -*- coding: utf-8 -*-
#
#
# 		*** OPEN HEALTH - Purchase Rfq  
# 
# Created: 				30 Oct 2017
# Last updated: 	 	30 Oct 2017

from openerp import models, fields, api




class PurchaseOrderLineRfq(models.Model):
	
	_inherit = 'purchase.order.line'

	_name = 'purchase.order.line.rfq'



	order_id = fields.Many2one(


		#'purchase.order', 
		'purchase.order.rfq', 


		string='Order Reference', 
		index=True, 
		required=True, 
		ondelete='cascade'
	)


