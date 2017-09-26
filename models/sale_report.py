# -*- coding: utf-8 -*-
#
# 	Sale Report Pla
# 
#


from openerp import models, fields, api
from . import treatment_vars



class sale_report(models.Model):
	

	_inherit='sale.report'

	#_name = 'sale.report.pla'

	


	note = fields.Char(

			#string="Nota",		
			string="Note - jx",		
			
			readonly=True
		)



	price_subtotal = fields.Float(
		groups="openhealth.physicians,openhealth.managers,openhealth.directors"
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



