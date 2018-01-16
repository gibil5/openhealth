# -*- coding: utf-8 -*-

from openerp import models, fields, api




class StockMove(models.Model):
	
	_inherit = 'stock.move'

	_description = "Stock Move"

	#_order = 'create_date desc'
	#_order = 'date desc'
	#_order = 'date_expected desc'

	#_name = "stock.move"
	#_description = "Stock Move"
	#_order = 'picking_id, sequence, id'



	kardex_id = fields.Many2one(
			'openhealth.kardex', 
		)
















	#'state': fields.selection([
	#								('draft', 'New'),
	#								('cancel', 'Cancelled'),
	#							   	('waiting', 'Waiting Another Move'),
	#							   	('confirmed', 'Waiting Availability'),
	#							   	('assigned', 'Available'),
	#							   	('done', 'Done'),
	#						], 
	#	'Status', readonly=True, select=True, copy=False,
	#	help= "* New: When the stock move is created and not yet confirmed.\n"\
	#				   "* Waiting Another Move: This state can be seen when a move is waiting for another one, for example in a chained flow.\n"\
	#				   "* Waiting Availability: This state is reached when the procurement resolution is not straight forward. It may need the scheduler to run, a component to me manufactured...\n"\
	#				   "* Available: When products are reserved, it is set to \'Available\'.\n"\
	#				   "* Done: When the shipment is processed, the state is \'Done\'."
	#	),
