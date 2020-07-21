# -*- coding: utf-8 -*-
"""
	Service vip - Legacy 2018

"""

from openerp import models, fields, api

class Servicevip(models.Model):
	"""
	Service Vip
	"""
	_inherit = 'openhealth.service'

	_name = 'openhealth.service.vip'

	

	# Service 
	service = fields.Many2one(
			'product.template',
			domain = [
						('type', '=', 'product'),
					],
			string="Servicio",
			required=True, 
		)


