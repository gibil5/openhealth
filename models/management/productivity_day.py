# -*- coding: utf-8 -*-
"""
	Productivity Day
	Simplified version of Day Line

	Just an empty shell

	Created: 			 8 Dec 2019
	Last up: 			 8 Dec 2019
"""

from openerp import models, fields, api


class ProductivityDay(models.Model):
	"""
	Productivity Day
	All names must be extremely descriptive
	"""

	_name = 'productivity.day'

	#_order = 'date asc'

	#_inherit = 'openhealth.management.line'
