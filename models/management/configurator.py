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


