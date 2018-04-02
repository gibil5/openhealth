# -*- coding: utf-8 -*-

from openerp import models, fields, api

import stock_min_funcs  


class Inventory(models.Model):
	
	_inherit = 'openhealth.stock.min'

	_name = 'openhealth.stock.min.inventory'

	_description = "Stock Min Inventory"

	#_order = 'product_id,date desc'





# ----------------------------------------------------------- Actions ------------------------------------------------------

	# Update 
	@api.multi
	def update_lines(self):  

		print ''
		print 'Update Lines'


		lines = self.env['openhealth.stock.min.inventory.line'].search([

																		('state', '=', 'draft'),
																		#('categ', '=', 'topical'),
			
											],
												order='code asc',
												#limit=1,
											)

		print lines 



		for line in lines:
			print line 

			
			#line.state = 'done'

			line.inventory_id = self.id 


			#line.product_id = stock_min_funcs.get_product_id(self, line.code)
			#line.product_id = stock_min_funcs.get_product_id(self, line.code, line.description)

			line.product_id = stock_min_funcs.get_product_id(self, line.code, line.description, line.categ)






# ----------------------------------------------------------- Primitives ------------------------------------------------------
	name = fields.Char(
		)


	date = fields.Datetime(
			string="Fecha", 
		)


	author = fields.Many2one(
			'res.partner'
		)



	inventory_line = fields.One2many(

			'openhealth.stock.min.inventory.line', 
		
			'inventory_id', 

			#string='Order Lines', 

			#readonly=False, 

		)








