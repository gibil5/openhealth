# -*- coding: utf-8 -*-
#
# 	ItemCounter
# 
#

from openerp import models, fields, api

class ItemCounter(models.Model):
	
	#_inherit='sale.closing'

	#_name = 'openhealth.product.counter'
	_name = 'openhealth.item.counter'
	



# ----------------------------------------------------------- Deprecated ? ------------------------------------------------------
	# Report Sale 
	#report_sale_a_id = fields.Many2one(
	#	'openhealth.report.sale', 
	#	string='Report Reference', 		
	#	ondelete='cascade', 
	#)

	#report_sale_b_id = fields.Many2one(
	#	'openhealth.report.sale', 
	#	string='Report Reference', 		
	#	ondelete='cascade', 
	#)

	#report_sale_c_id = fields.Many2one(
	#	'openhealth.report.sale', 
	#	string='Report Reference', 		
	#	ondelete='cascade', 
	#)





	categ = fields.Selection(

			[	
				('a', 		'A'),
				('b', 		'B'),
				('c', 		'C'),
			], 

		)



# ----------------------------------------------------------- Relational ------------------------------------------------------




	# Report Sale Product 
	report_sale_product_id = fields.Many2one(

		'openhealth.report.sale.product', 
		
		string='Report Reference', 		
		ondelete='cascade', 
	)









# ----------------------------------------------------------- Actions ------------------------------------------------------
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






# ----------------------------------------------------------- Vars ------------------------------------------------------
	name = fields.Char()


	qty = fields.Integer(
			string="Cantidad", 
		)


	total = fields.Float(
			string="Total", 
		)




