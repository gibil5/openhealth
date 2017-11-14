# -*- coding: utf-8 -*-
#
#
# 		*** OPEN HEALTH - Stock Picking    
# 
# Created: 				14 Nov 2017
# Last updated: 	 	14 Nov 2017

from openerp import models, fields, api




class StockPicking(models.Model):
	
	_inherit = 'stock.picking'
	_description = "Stock Picking"




# New

	@api.multi
	def remove_myself(self):  

		#self.pack_operation_exist = False

		self.pack_operation_ids.unlink()

		self.state = 'cancel'

		self.unlink()



