# -*- coding: utf-8 -*-
"""
 	Order

 	Created: 			12 Nov 2018
	Last mod: 			12 Nov 2018
"""
from openerp import models, fields, api


class sale_order_safe(models.Model):
	"""
	Safe Orders
	"""

	_inherit = 'sale.order'

	_name = 'safe.order'


