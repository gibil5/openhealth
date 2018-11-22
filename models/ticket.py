# -*- coding: utf-8 -*-
"""
 	Order 

	Created: 				18 Jun 2018
	Last mod: 			Id
"""

from openerp import models, fields, api

class Ticket(models.Model):	
	#_inherit='sale.order'
	_name = 'openhealth.ticket'

	vspace = fields.Char(
			' ', 
			readonly=True
		)

