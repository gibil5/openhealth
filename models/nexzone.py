# -*- coding: utf-8 -*-
#
# 	Nexzone 
# 
# Created: 				01 Feb 2018
# Last updated: 	 	id.

from openerp import models, fields, api



class Nexzone(models.Model):

	_name = 'openhealth.nexzone'

	#_order = 'name_short asc'




# ----------------------------------------------------------- Primitives ------------------------------------------------------

	pathology = fields.Many2one(
			'openhealth.pathology', 
		)






	name = fields.Char(
		)


	name_short = fields.Char(
		)




	treatment = fields.Selection(
			[
				('laser_quick','Quick Laser'), 

				('laser_co2','Laser Co2'), 
				('laser_excilite','Laser Excilite'), 
				('laser_ipl','Laser Ipl'), 
				('laser_ndyag','Laser Ndyag'), 
			], 
		)











	laser_quick = fields.Boolean(
		)

	laser_co2 = fields.Boolean(
		)

	laser_excilite = fields.Boolean(
		)

	laser_ipl = fields.Boolean(
		)

	laser_ndyag = fields.Boolean(
		)









	# Service 
	#service = fields.Many2one(			
	#		'openhealth.service',
	#	)
