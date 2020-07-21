# -*- coding: utf-8 -*-
"""
 	Service Product - Legacy 2018
 
 	Created: 			2016
 	Last up: 	 		24 April 2019

	24 Apr 2019:		Cleanup after 2019 PL. Must disappear:
						- Onchanges. 
"""
from openerp import models, fields, api

class ServiceProduct(models.Model):
	"""
	Service Product
	"""
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
