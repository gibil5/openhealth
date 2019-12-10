# -*- coding: utf-8 -*-
"""
	Service Ipl 

 	Created: 			2016
 	Last up: 	 		24 April 2019

	24 Apr 2019:	Cleanup after 2019 PL. Must disappear:
					- Onchanges. 
"""
from datetime import datetime
from openerp import models, fields, api
from . import ipl

#from . import prodvars
from openerp.addons.openhealth.models.product import prodvars

class ServiceIpl(models.Model):
	
	_name = 'openhealth.service.ipl'
	
	_inherit = 'openhealth.service'
	

# ----------------------------------------------------------- Natives ------------------------------
	service = fields.Many2one(
			'product.template',
			domain = [
						('type', '=', 'service'),
						('x_treatment', '=', 'laser_ipl'),
					],
	)

# ---------------------------------------------- Default --------------------------------------------------------
	# Laser 
	laser = fields.Selection(
			selection = prodvars._laser_type_list, 
			string="Láser",
			default='laser_ipl',
			index=True,
		)
