# -*- coding: utf-8 -*-
#
# 	Service Excilite 
# 

from openerp import models, fields, api
from datetime import datetime

import exc





class ServiceExcilite(models.Model):
	#_name = 'openhealth.laserexcilite'
	_name = 'openhealth.service.excilite'

	_inherit = 'openhealth.service'
	
	
	
	
	# From Service
	zone = fields.Char(
			default='x',
			)
			
	pathology = fields.Char(
			default='x',
			)
					
	


	# First
	vitiligo = fields.Selection(
			selection = exc._vitiligo_list, 
			string="Vitiligo", 
			default='',	
			)

	psoriasis = fields.Selection(
			selection = exc._psoriasis_list, 
			string="Psoriasis", 
			default='',	
			)
			
	alopecias = fields.Selection(
			selection = exc._alopecias_list, 
			string="Alopecias", 
			default='',	
			)



