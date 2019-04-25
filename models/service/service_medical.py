# -*- coding: utf-8 -*-
"""
	Service Medical treatment 

	Created: 			1 Nov 2016
	Last: 				29 Nov 2018
	24 Apr 2019:		Cleanup after 2019 PL. Must disappear:
						- Onchanges. 
"""
from datetime import datetime
from openerp import models, fields, api
from . import prodvars
from . import service_medical_vars

class ServiceMedical(models.Model):

	_name = 'openhealth.service.medical'
	
	_inherit = 'openhealth.service'
	

# ----------------------------------------------------------- Natives ------------------------------
	service = fields.Many2one(
			'product.template',
			domain = [
						('type', '=', 'service'),
						('x_family', '=', 'medical'),						
					],
	)
	
# ---------------------------------------------- Default --------------------------------------------------------
	laser = fields.Selection(
			selection = prodvars._laser_type_list, 
			string="Láser",
			default='medical',
			index=True,
		)
