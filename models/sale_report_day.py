# -*- coding: utf-8 -*-
#
#
# 		*** Sale Report Day  
# 
#

from openerp import models, fields, api



class SaleReportDay(models.Model):
	
	_inherit = 'sale.report'

	_name = 'sale.report.day'

	_description = 'Sale Report Day'

	#_order = 'write_date desc'


