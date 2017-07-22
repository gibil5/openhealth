# -*- coding: utf-8 -*-
#
# 	Sale Report 
# 
#

from openerp import models, fields, api
from . import treatment_vars



class sale_report(models.Model):
	

	_inherit='sale.report'
	#_name = 'openhealth.report'

	


	note = fields.Char(
			#string="Nota",		
			string="Note",		
			
			readonly=True
		)



	#comment = fields.Selection(
	#	[
	#	('product', 'Product'),
	#	('service', 'Service'),
	#	], 
	#	string='Comment', 
	#	default='product', 
	#	readonly=True
	#)


	# Family 
	#x_family = fields.Selection(
	#		#string = "Tipo", 	
	#		string = "Familia", 	
			#default='product',
	#		selection = treatment_vars._family_list, 
			#required=True, 
	#	)


	#x_cancel_reason = fields.Char(
			#string='Motivo de anulación', 
	#		string='Tipo', 
	#	)



