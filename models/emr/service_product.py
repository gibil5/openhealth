# -*- coding: utf-8 -*-
#
# 	Service Product 
# 

from openerp import models, fields, api

class ServiceProduct(models.Model):

	_inherit = 'openhealth.service'

	_name = 'openhealth.service.product'

	

	# Service 
	service = fields.Many2one(

			'product.template',

			domain = [
						('type', '=', 'product'),
					],


			string="Servicio",

			required=True, 
		)


