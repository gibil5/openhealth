# -*- coding: utf-8 -*-
"""
		*** Physician
 
		Created: 		 6 Mar 2017
		Last up:		24 Aug 2019
"""
from openerp import models, fields, api


# ----------------------------------------------------------- Physician ------------------------------------------------------

class Physician(models.Model):

	_inherit = 'oeh.medical.physician'	
	
	#_order = 'name'
	#_order = 'idx asc'



# ----------------------------------------------------------- Fields ------------------------------------------------------

	#idx = fields.Integer(
	idx = fields.Char(
			#default=-1, 
		)

	x_therapist = fields.Boolean(
			string='Terapeuta', 
			default=False,
		)	
	
	x_user_name = fields.Many2one(		
			'res.users',
			string = "Nombre de usuario", 	
		)

	consultancy_type = fields.Selection(			
			string='Tipo', 
		)

	vspace = fields.Char(
			' ', 
			readonly=True
		)
