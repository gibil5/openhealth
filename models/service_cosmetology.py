# -*- coding: utf-8 -*-
#
#
# 		*** OPEN HEALTH - Service Cosmetology
# 
# Created: 				18 Feb 2017
# Last updated: 	 	20 Feb 2017



from openerp import models, fields, api
from datetime import datetime

#import service_cosmetology_vars



class ServiceCosmetology(models.Model):

	_name = 'openhealth.service.cosmetology'
	
	_inherit = 'openhealth.service'
	
	



	# Service 
	service = fields.Many2one(
			'product.template',

			domain = [
						#('type', '=', 'service'),
						#('x_treatment', '=', 'carboxytherapy'),
						('x_family', '=', 'cosmetology'),
					],
		)
	
	

