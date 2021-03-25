# -*- coding: utf-8 -*-
"""
	Texto

	TXT Line - For Electronic Container

	Created: 		14 Oct 2016
	Last up: 		13 Dec 2019
"""
from openerp import models, fields, api
from openerp.exceptions import ValidationError
#from openerp.exceptions import Warning

class Texto(models.Model):
	"""
	TXT Lines
	"""
	_name = 'openhealth.texto'

	_order = 'name asc'

	_description = 'TXT Lines for the Electronic Container'








# ----------------------------------------------------------- Fields ------------------------------

	name = fields.Char()

	content = fields.Char()


# ----------------------------------------------------------- Handles -----------------------------

	# Electronic Container
	container_id = fields.Many2one(
			'openhealth.container',
			ondelete='cascade',
		)





