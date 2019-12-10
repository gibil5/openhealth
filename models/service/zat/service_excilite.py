# -*- coding: utf-8 -*-
"""
	Service Excilite 

 	Created: 			2016
 	Last up: 	 		24 April 2019

	24 Apr 2019:	Cleanup after 2019 PL. Must disappear:
					- Onchanges. 
"""
from openerp import models, fields, api
from datetime import datetime

#from . import vars_exc

from openerp.addons.openhealth.models.product import prodvars

class ServiceExcilite(models.Model):

	_name = 'openhealth.service.excilite'

	_inherit = 'openhealth.service'


# ----------------------------------------------------------- Natives ------------------------------
	service = fields.Many2one(
			'product.template',
			domain = [
						('type', '=', 'service'),
						('x_treatment', '=', 'laser_excilite'),
					],
	)

# ---------------------------------------------- Default --------------------------------------------------------
	# Laser 
	laser = fields.Selection(
			selection = prodvars._laser_type_list, 
			string="Láser",
			default='laser_excilite',
			index=True,
		)
