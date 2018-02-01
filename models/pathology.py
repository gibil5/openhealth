# -*- coding: utf-8 -*-
#
# 	Pathology 
# 
# Created: 				26 Dec 2016
# Last updated: 	 	id.

from openerp import models, fields, api



class Pathology(models.Model):

	#_inherit = 'openhealth.base', 

	_name = 'openhealth.pathology'





# ----------------------------------------------------------- Primitives ------------------------------------------------------


	zone_ids = fields.One2many(

			#'openhealth.zone', 
			'openhealth.nexzone', 

			'pathology', 
		)












	# Name 
	name = fields.Char(
		)

	# Name short
	name_short = fields.Char(
		)







	body_local = fields.Boolean(
		)

	face_local = fields.Boolean(
		)

	face_all = fields.Boolean(
		)




	face_all_hands = fields.Boolean(
		)

	face_all_neck = fields.Boolean(
		)

	cheekbones = fields.Boolean(
		)



	hands = fields.Boolean(
		)

	neck = fields.Boolean(
		)

	neck_hands = fields.Boolean(
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



