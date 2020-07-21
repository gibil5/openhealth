# -*- coding: utf-8 -*-
"""
	Service Ndyag - Legacy 2018

 	Created: 			2016
 	Last up: 	 		24 April 2019

	24 Apr 2019:	Cleanup after 2019 PL. Must disappear:
					- Onchanges. 
"""

from openerp import models, fields, api
from datetime import datetime
from openerp.addons.openhealth.models.product import prodvars

class ServiceNdyag(models.Model):
	"""
	Service Ndyag
	"""
	_name = 'openhealth.service.ndyag'
	
	_inherit = 'openhealth.service'
	
	
# ----------------------------------------------------------- Natives ------------------------------
	service = fields.Many2one(
			'product.template',
			domain = [
						('type', '=', 'service'),
						('x_treatment', '=', 'laser_ndyag'),
					],
	)

# ---------------------------------------------- Default --------------------------------------------------------
	# Laser
	laser = fields.Selection(
			selection = prodvars._laser_type_list,
			string="Láser",
			default='laser_ndyag',
			index=True,
		)
