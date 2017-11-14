# -*- coding: utf-8 -*-
#
#
# 		*** OPEN HEALTH - Purchase   
# 
# Created: 				30 Oct 2017
# Last updated: 	 	14 Nov 2017

from openerp import models, fields, api




class PurchaseOrder(models.Model):
	
	_inherit = 'purchase.order'
	_description = "Purchase Order"




# New

	@api.multi
	def remove_myself(self):  

		self.state = 'cancel'
		self.unlink()



