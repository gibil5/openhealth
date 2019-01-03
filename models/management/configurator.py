# -*- coding: utf-8 -*-
"""
	Configurator

	Created: 			28 Dic 2018
	Last updated: 		28 Dic 2018
"""
from __future__ import print_function
from openerp import models, fields, api

class Configurator(models.Model):
	"""
	high level support for doing this and that.
	"""
	_name = 'openhealth.configurator'



# ----------------------------------------------------------- Fields --------------------------

	name = fields.Char(
			#string="Nombre",
			required=True,
		)


	date_begin = fields.Date(
			string="Fecha Inicio",
			default=fields.Date.today,
		)


	date_end = fields.Date(
			string="Fecha Fin",
			default=fields.Date.today,
		)


	x_type = fields.Selection(
			[
				('fast', 'Fast'),
				('all', 'All'),
			],
			string="Type",
			required=True,
		)
