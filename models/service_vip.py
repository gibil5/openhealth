# -*- coding: utf-8 -*-
#
# 	Service vip 
# 

from openerp import models, fields, api

class Servicevip(models.Model):

	_inherit = 'openhealth.service'

	_name = 'openhealth.service.vip'

	

	# Service 
	service = fields.Many2one(
			'product.template',


			domain = [
						#('type', '=', 'service'),
						#('type', '=', 'product'),
						#('default_code', '=', '57'),

						#('default_code', '=', '495'),
						('type', '=', 'product'),
					],


			string="Servicio",
			required=True, 
		)


