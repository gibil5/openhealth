# -*- coding: utf-8 -*-
#
# 	ProductCounter
# 
#

from openerp import models, fields, api



class ProductCounter(models.Model):
	
	#_inherit='sale.closing'

	_name = 'openhealth.product.counter'
	



	name = fields.Char()

	qty = fields.Integer(
			string="Cantidad", 
		)

	total = fields.Float(
			string="Total", 
		)




	# Report Sale Product 
	report_sale_product_id = fields.Many2one(

		'openhealth.report.sale.product', 
		
		string='Report Reference', 		
		ondelete='cascade', 
	)




	# Increase 
	@api.multi
	def increase_qty(self, qty):  

		#print
		#print 'Increase Qty'

		self.qty = self.qty + qty 




	# Increase 
	@api.multi
	def increase_total(self, total):  

		#print
		#print 'Increase Total'

		self.total = self.total + total 






