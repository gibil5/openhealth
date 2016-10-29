# -*- coding: utf-8 -*-
#
# 	Service Medical treatment 
# 

from openerp import models, fields, api
from datetime import datetime
import jxvars


class ServiceMedical(models.Model):
	_name = 'openhealth.service.medical'
	_inherit = 'openhealth.service'
	
	
		
	# Service 
	service = fields.Many2one(
			'product.template',

			domain = [
						('type', '=', 'service'),
						#('x_treatment', '=', 'medical'),
						('x_treatment', '=', 'laser_co2'),

					],
	)
	
	
	#------------------------------------- Medical ----------------------------------------
	

