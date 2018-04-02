# -*- coding: utf-8 -*-
#
# 		Stock Picking    
# 
# Created: 				14 Nov 2017
# Last updated: 	 	14 Nov 2017
#
from openerp import models, fields, api


class StockPicking(models.Model):
	
	_inherit = 'stock.picking'
	_description = "Stock Picking"






	# ----------------------------------------------------------- Primitives ------------------------------------------------------

	x_type = fields.Selection(

			selection=[
						('test', 			'test'),
						('legacy', 			'legacy'),
					], 

			string="Tipo", 
		)	





	vspace = fields.Char(
			string=' ', 
			readonly=True, 
		)



	

	# ----------------------------------------------------------- On Changes ------------------------------------------------------

	#@api.onchange('min_date')
	#def _onchange_min_date(self):	
	#	usage = 'internal'
	#	return {
	#				'domain': {
	#								'location_dest_id': [
	#														('usage', '=', usage),
	#													], 
	#
	#								'location_id': 		[
	#														('usage', '=', usage),
	#													], 
	#
	#						},
	#		}






	# ----------------------------------------------------------- Actions ------------------------------------------------------

	#@api.multi
	#def remove_myself(self):  
	#	print 'jx'
	#	print 'Remove myself'
	#	self.unlink()





