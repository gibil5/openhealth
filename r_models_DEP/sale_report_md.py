# -*- coding: utf-8 -*-
#
#
# 		*** Sale Report Month  
# 
#

from openerp import models, fields, api


# jx Class 
class SaleReportMonth(models.Model):
	_inherit = 'sale.report'
	_name = 'sale.report.month'
	_description = 'Sale Report Month'
	#_order = 'write_date desc'



# jx Class 
class SaleReportDay(models.Model):
	_inherit = 'sale.report'
	_name = 'sale.report.day'
	_description = 'Sale Report Day'
	#_order = 'write_date desc'


