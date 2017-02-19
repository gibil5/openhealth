# -*- coding: utf-8 -*-
#
# 	*** Product
# 
# Created: 			    Nov 2016
# Last updated: 	 19 Feb 2017

from openerp import models, fields, api
from datetime import datetime

import prodvars



class Product(models.Model):
	#_name = 'openhealth.service'
	_inherit = 'product.template'



	uom = fields.Many2one(
			'product.uom',
			required=False, 
		)





	# Only Products 

	x_brand = fields.Char(
			string="Marca", 
		)





	# Canonical 

	x_family = fields.Selection(
			selection=prodvars._family_list,
		)	

	x_treatment = fields.Selection(
			selection=prodvars._treatment_list,
		)	
	
	x_zone = fields.Selection(
			selection=prodvars._zone_list,
		)	
	
	x_pathology = fields.Selection(
			selection=prodvars._pathology_list,
		)

	x_sessions = fields.Char(
			default="",
		)

	x_time = fields.Char(
		)

	x_name_short = fields.Char(
		)







	# Before 
	x_date_updated = fields.Date(
			)

	x_date_created = fields.Date(
			)

	x_price_vip = fields.Float(
			#string = 'Precio VIP - nex',
		)



