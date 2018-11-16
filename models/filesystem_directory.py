# -*- coding: utf-8 -*-
"""
	Filesystem Directory

	Created: 			15 Nov 2018
	Last mod: 			15 Nov 2018
"""
from openerp import models, fields, api

class filesystem_directory(models.Model):
	"""
	high level support for doing this and that.
	"""
	_inherit = 'ir.filesystem.directory'



	x_flag = fields.Boolean(
			'Flag',
		)

