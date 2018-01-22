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



	#location_dest_id = fields.Many2one(
	#		'stock.location', 
	#		required=True,
	#		string="Destination Location Zone",
	#		default=_default_location_destination, 
	#		readonly=True, 
	#		states={'draft': [('readonly', False)]}
	#	)



	#min_date = fields.function(
	#		get_min_max_date, 
	#		multi="min_max_date", 
	#		fnct_inv=_set_min_date,
	#		store={'stock.move': (_get_pickings_dates_priority, ['date_expected', 'picking_id'], 20)}, type='datetime', states={'done': [('readonly', True)], 'cancel': [('readonly', True)]}, string='Scheduled Date', select=1, help="Scheduled time for the first part of the shipment to be processed. Setting manually a value here would set it as expected date for all the stock moves.", 
	#		track_visibility='onchange'
	#	)




	#@api.onchange('min_date')
	#def _onchange_min_date(self):
	
	#	usage = 'internal'

	#	return {
	#				'domain': {'location_dest_id': [
	#													('usage', '=', usage),
	#							]},
	#		}






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





