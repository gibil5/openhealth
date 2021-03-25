# -*- coding: utf-8 -*-

"""

 	Electronic Line

 	Created: 			14 Sep 2018
 	Previous: 			14 Sep 2018
	Last: 				25 mar 2021
"""

from openerp import models, fields, api

class electronic_line(models.Model):
	_name = 'openhealth.electronic.line'
	_description = "Openhealth Electronic Line"

	_inherit='openhealth.line'

# ----------------------------------------------------------- Handle -----------
	# Electronic  
	electronic_order_id = fields.Many2one(
			'openhealth.electronic.order',
			ondelete='cascade',
		)
