# -*- coding: utf-8 -*-

from openerp import models, fields, api



# Deprecated
# Purchase extension


class Quotation(models.Model):
	_name = 'openhealth.quotation'	
	_inherit = 'base_multi_image.owner'




	# Commons 
	vspace = fields.Char(
			' ', 
			readonly=True, 
			)

	name = fields.Char(
			'Nombre', 
			required=True, 
		)

	date = fields.Datetime(
			'Fecha',
			required=True, 
		)

	partner_id = fields.Many2one(
			'res.partner',	
		)

