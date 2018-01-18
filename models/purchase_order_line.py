# -*- coding: utf-8 -*-
#
#
# 		*** OPEN HEALTH - Purchase Order line  
# 
# Created: 				13 Dec 2017
# Last updated: 	 	13 Dec 2017

from openerp import models, fields, api

import openerp.addons.decimal_precision as dp

from datetime import datetime
from openerp.tools import DEFAULT_SERVER_DATETIME_FORMAT
from openerp import api, fields, models, _, SUPERUSER_ID



class PurchaseOrderLine(models.Model):
	
	_inherit = 'purchase.order.line'
	
	_description = "Purchase Order Line"






	price_unit = fields.Float(
			string='Unit Price', 
			required=True, 
			digits=dp.get_precision('Product Price')
		)



	#@api.onchange('price_subtotal')
	#def _onchange_price_subtotal(self):
	#	self.price_unit = 55


	@api.onchange('product_id')
	def onchange_product_id(self):
		result = {}
		if not self.product_id:
			return result

		# Reset date, price and quantity since _onchange_quantity will provide default values
		self.date_planned = datetime.today().strftime(DEFAULT_SERVER_DATETIME_FORMAT)
		

		#self.price_unit = self.product_qty = 0.0
		#self.price_unit = 55.5
		self.price_unit = self.product_id.standard_price
		

		self.product_uom = self.product_id.uom_po_id or self.product_id.uom_id
		result['domain'] = {'product_uom': [('category_id', '=', self.product_id.uom_id.category_id.id)]}

		product_lang = self.product_id.with_context({
			'lang': self.partner_id.lang,
			'partner_id': self.partner_id.id,
		})
		self.name = product_lang.display_name
		if product_lang.description_purchase:
			self.name += '\n' + product_lang.description_purchase

		fpos = self.order_id.fiscal_position_id
		if self.env.uid == SUPERUSER_ID:
			company_id = self.env.user.company_id.id
			self.taxes_id = fpos.map_tax(self.product_id.supplier_taxes_id.filtered(lambda r: r.company_id.id == company_id))
		else:
			self.taxes_id = fpos.map_tax(self.product_id.supplier_taxes_id)

		self._suggest_quantity()
		self._onchange_quantity()

		return result







	product_qty = fields.Float(
			string='Quantity', 

			#digits=dp.get_precision('Product Unit of Measure'), 
			digits=(16, 0), 
			
			required=True,
		)
	
	
	#date_planned = fields.Datetime(
	date_planned = fields.Date(
			string='Scheduled Date', 
			required=True, 
			index=True
		)





	#x_default_code = fields.Char(
	#		string='Código', 
	#	)








