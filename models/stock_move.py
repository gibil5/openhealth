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

