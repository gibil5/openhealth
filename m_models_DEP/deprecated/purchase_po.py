# -*- coding: utf-8 -*-
#
#
# 		*** OPEN HEALTH - Purchase Rfq  
# 
# Created: 				30 Oct 2017
# Last updated: 	 	30 Oct 2017

from openerp import models, fields, api




class PurchaseOrderPo(models.Model):
	
	_inherit = 'purchase.order'

	_name = 'purchase.order.po'

