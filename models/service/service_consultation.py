# -*- coding: utf-8 -*-
"""
 	Service Consultation 
 
 	Created: 			2016
 	Last up: 	 		24 April 2019

	24 Apr 2019:		Cleanup after 2019 PL. Must disappear:
						- Onchanges. 
"""

from openerp import models, fields, api

class ServiceConsultation(models.Model):

	_inherit = 'openhealth.service'

	_name = 'openhealth.service.consultation'

	

	# Service 
	service = fields.Many2one(
			'product.template',
			domain = [
						#('type', '=', 'consultation'),
					],
			string="Servicio",
			required=True, 
		)
