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
import prodvars
import cosvars



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
	
	



	time_1 = fields.Selection(
			selection = prodvars._time_list, 
			string="Tiempo", 
			default='none',	
			)






	# Criosurgery
	cos_dia = fields.Selection(
			selection = cosvars._cos_dia_list, 
			default='none',	
			string="Punta de Diamante",
			)


	# Hialuronic
	cos_car = fields.Selection(
			selection = cosvars._cos_car_list, 
			default='none',	
			string="Carboxiterapia",
			)


	# Sclerotherapy
	cos_tri = fields.Selection(
			selection = cosvars._cos_tri_list, 
			default='none',	
			string="Láser Triactive",
			)






