# -*- coding: utf-8 -*-
#
#
# 		*** OPEN HEALTH - Stock Pack Operation    
# 
# Created: 				14 Nov 2017
# Last updated: 	 	14 Nov 2017

from openerp import models, fields, api




class StockPackOperation(models.Model):
	
	_inherit = 'stock.pack.operation'
	_description = "Stock Pack Operation"



# New
	@api.multi
	def remove_myself(self):  

		print 'jx'
		print 'Remove myself'

		self.unlink()

