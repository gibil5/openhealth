# -*- coding: utf-8 -*-
#
# 		*** Order Admin 
# 
# 		Created: 			21 Nov 2019
# 		Last updated: 	 	21 Nov 2019
#
from openerp import models, fields, api

class OrderAdmin(models.Model):
	
	_name = 'openhealth.order.admin'

	_description = 'Pricelist Order Admin'



	name = fields.Char(
			default='Corrector de Ventas',
			required=True,
		)


	order = fields.Many2one(
			'sale.order',
			string='Venta',
		)



	counter = fields.Integer(
			string='Contador',
		)

	fix_counter = fields.Boolean(
			string='Corregir Nr de Serie',
			default=False,
		)


	serial_number = fields.Char(
			string='Nr de Serie',
		)






