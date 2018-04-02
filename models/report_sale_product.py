# -*- coding: utf-8 -*-
#
# 	ReportSaleProduct 
# 
#

from openerp import models, fields, api

#import datetime

import clos_funcs



class ReportSaleProduct(models.Model):
	
	#_inherit='sale.closing'

	_name = 'openhealth.report.sale.product'
	




# ----------------------------------------------------------- Primitives ------------------------------------------------------
	
	# Dates
	date = fields.Date(
			string="Fecha", 
			default = fields.Date.today, 
			#readonly=True,
			required=True, 
		)








# ----------------------------------------------------------- Actions ------------------------------------------------------

	# Update 
	@api.multi
	def update_report(self):  

		print 'jx'
		print 'Update report'

# Total 
		x_type = 'all'
		orders,count = clos_funcs.get_orders(self, self.date, x_type)






		





# ----------------------------------------------------------- Primitives ------------------------------------------------------
	# Other 
	vspace = fields.Char(
			' ', 
			readonly=True
		)

