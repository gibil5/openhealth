# -*- coding: utf-8 -*-
#
# 	payment_method_line
# 
#

from openerp import models, fields, api

import ord_vars


class payment_method_line(models.Model):
	
	_name = 'openhealth.payment_method_line'



	name = fields.Char(
			#string="Medio de Pago", 
			string="Pago", 
			required=True, 
			readonly=True, 
		)


	vspace = fields.Char(
			' ', 
			readonly=True
			)




	method = fields.Selection(
			string="Medio", 
			selection = ord_vars._payment_method_list, 			
			required=True, 
		)




	subtotal = fields.Float(
			string = 'Sub-total', 
			required=True, 
		)



	#@api.onchange('subtotal')
	#def _onchange_subtotal(self):
	#	self.balance = self.total - (self.pm_total + self.subtotal)



	code = fields.Char(
			string="Codigo", 
			#required=True, 
		)


