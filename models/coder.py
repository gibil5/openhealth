# -*- coding: utf-8 -*-
#
# 	Coder 
# 
# 	Created: 			16 Sep 2018
# 	Last updated: 		16 Sep 2018
#
from openerp import models, fields, api

class coder(models.Model):

	_name = 'openhealth.coder'

	#_inherit=''

	_order = 'name asc'

	_description = "Openhealth Coder"


# ----------------------------------------------------------- Fields ------------------------------------------------------

	name = fields.Char()

	code = fields.Char()

	x_type = fields.Selection(
								[
									('product', 'Product'),
									('service', 'Service'),
								],
		)


	product = fields.Many2one(
			'product.template', 
			'Product', 
		)
