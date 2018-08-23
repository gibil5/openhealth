# -*- coding: utf-8 -*-
#
# 	Service consultation 
# 

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


