# -*- coding: utf-8 -*-
#
# 	allergy 
# 
# Created: 				4 Feb 2018
# Last updated: 	 	id.

from openerp import models, fields, api



class Allergy(models.Model):

	_name = 'openhealth.allergy'

	#_order = 'name_short asc'
	_order = 'name asc'




	name = fields.Char(
			string="Nombre", 
			required=True, 
		)


	name_short = fields.Char(
			#string="Nombre corto", 
		)

