# -*- coding: utf-8 -*-
#
# 	Service vip 
# 

from openerp import models, fields, api

#from datetime import datetime
#from . import service_vip_vars
#from . import serv_funcs
#from . import prodvars




class Servicevip(models.Model):

	_inherit = 'openhealth.service'

	_name = 'openhealth.service.vip'

	

	# Service 
	service = fields.Many2one(
			'product.template',


			domain = [
						#('type', '=', 'service'),
						#('type', '=', 'product'),
						
						('default_code', '=', '57'),

					],


			string="Servicio",
			required=True, 
		)


