# -*- coding: utf-8 -*-
#
# 	Quotation 
# 

from openerp import models, fields, api
from datetime import datetime





#------------------------------------------------------------------------
class Order(models.Model):
	#_name = 'openhealth.order'
	
	
	#_inherit = 'oeh.medical.evaluation'
	#_inherit = 'oeh.medical.quotation'
	#_inherit = 'oeh.medical.order'
	
	
	_inherit = 'sale.order'
	#_inherit = 'account.invoice'
	
	


	name = fields.Char(
			string = 'Order #',
			#string = 'Procedimiento #',
			)
			
	consultation = fields.Many2one('openhealth.consultation',
			ondelete='cascade', 
			)