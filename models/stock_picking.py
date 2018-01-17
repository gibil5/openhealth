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

		print 'jx'
		print 'Remove myself'

		#self.pack_operation_exist = False

		#self.picking_type_id = False

		#self.state = 'draft'






		#for po in self.pack_operation_pack_ids:
		#	po.state = 'draft'
		
		#for po in self.pack_operation_product_ids:
		#	po.state = 'draft'
		
		#for po in self.pack_operation_ids:
		#	po.state = 'draft'

		#self.pack_operation_pack_ids.unlink()
		#self.pack_operation_product_ids.unlink()
		#self.pack_operation_ids.unlink()



		self.unlink()





