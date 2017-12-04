from openerp import models, fields, api




class StockMove(models.Model):
	
	_inherit = 'stock.move'

	_description = "Stock Move"

	_order = 'create_date desc'

