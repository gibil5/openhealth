# -*- coding: utf-8 -*-
#
# 	payment_method 
# 
#

from openerp import models, fields, api

import ord_vars


class PaymentMethod(models.Model):
	
	_name = 'openhealth.payment_method'

	#_inherit='openhealth.sale_document'



	name = fields.Char(
			#string="Medio de Pago", 
			string="Nombre", 

			#required=True, 
		)


	order = fields.Many2one(
			'sale.order',
			string="Presupuesto",
			ondelete='cascade', 
			required=True, 
		)



	subtotal = fields.Float(
			string = 'Sub-total', 
		)



	method = fields.Selection(
			string="Medio de Pago", 
			selection = ord_vars._payment_method_list, 			
		)




