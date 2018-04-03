# -*- coding: utf-8 -*-
#
# 	ReportSaleProduct 
# 
#

from openerp import models, fields, api

#import datetime

import resap_funcs



class ReportSaleProduct(models.Model):
	
	#_inherit='sale.closing'

	_name = 'openhealth.report.sale.product'
	




# ----------------------------------------------------------- Primitives ------------------------------------------------------
	

	name = fields.Char()


	# Dates
	date = fields.Date(
			string="Fecha", 
			default = fields.Date.today, 
			#readonly=True,
			required=True, 
		)


	qty = fields.Integer()





# ----------------------------------------------------------- Actions ------------------------------------------------------

	# Update 
	@api.multi
	def update_report(self):  

		print 'jx'
		print 'Update report'



		# Orders 
		orders,count = resap_funcs.get_orders(self, self.date)




		# Categ 
		#categ_name = 'Cremas'
		#categ =  self.env['product.category'].search([
		#												('name', '=', categ_name),
		#										],
													#order='x_serial_nr asc',
		#											limit=1,
		#										)
		#categ_id = categ.id 




		# Order lines
		for order in orders: 
			for line in order.order_line: 
				if line.product_id.categ_id.name == 'Cremas': 
					print line.product_id.name 





		





# ----------------------------------------------------------- Primitives ------------------------------------------------------
	# Other 
	vspace = fields.Char(
			' ', 
			readonly=True
		)

