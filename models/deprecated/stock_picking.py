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





