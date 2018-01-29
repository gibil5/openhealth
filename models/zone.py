# -*- coding: utf-8 -*-
#
# 	Zone 
# 
# Created: 				26 Jan 2018
# Last updated: 	 	id.

from openerp import models, fields, api



class Zone(models.Model):

	_name = 'openhealth.zone'

	_order = 'name_short asc'




	name = fields.Char(
			string="Nombre", 
		)

	name_short = fields.Char(
			#string="Nombre corto", 
		)


	treatment = fields.Selection(

			selection=[
							('laser_quick',		'Quick'), 
							('laser_co2',		'Co2'), 
							('laser_excilite',	'Excilite'), 
							('laser_ipl',		'ipl'), 
							('laser_ndyag',		'ndyag'), 
				],
		)