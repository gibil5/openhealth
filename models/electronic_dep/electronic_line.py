# -*- coding: utf-8 -*-
#
# 	Electronic Line 
# 
# 	Created: 			14 Sep 2018
# 	Last updated: 		14 Sep 2018
#
from openerp import models, fields, api

class electronic_line(models.Model):

	_name = 'openhealth.electronic.line'

	_inherit='openhealth.line'

	_description = "Openhealth Electronic Line"


# ----------------------------------------------------------- Handle ------------------------------

	# Electronic  
	electronic_order_id = fields.Many2one(
			'openhealth.electronic.order',
			ondelete='cascade',
		)
