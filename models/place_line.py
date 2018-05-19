# -*- coding: utf-8 -*-
#
# 	Place
# 
# Created: 				18 May 2018
#

from openerp import models, fields, api


class PlaceLine(models.Model):
	
	_name = 'openhealth.place.line'

	#_order = 'idx asc'



# ----------------------------------------------------------- Relational ------------------------------------------------------

	account_id = fields.Many2one(
			'openhealth.account.contasis'
		)
