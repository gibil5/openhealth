# -*- coding: utf-8 -*-
#
#
# 		*** Sale Report Month  
# 
#

from openerp import models, fields, api



class SaleReportMonth(models.Model):
	
	_inherit = 'sale.report'

	_name = 'sale.report.month'

	_description = 'Sale Report Month'

	#_order = 'write_date desc'


