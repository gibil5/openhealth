# -*- coding: utf-8 -*-
"""
	Filesystem File

	Created: 			15 Nov 2018
	Last mod: 			15 Nov 2018
"""
from openerp import models, fields, api

class filesystem_file(models.Model):
	"""
	high level support for doing this and that.
	"""
	_inherit = 'ir.filesystem.file'



	x_flag = fields.Boolean(
			'Flag',
		)

