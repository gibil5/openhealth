# -*- coding: utf-8 -*-
#
# 	*** Image  Full	
# 
# Created: 				 22 Jun 2017
# Last updated: 	 	 22 Jun 2017

from openerp import models, fields, api



class ImageFull(models.Model):
	
	_name = 'openhealth.image_full'

	#_inherit = 'base_multi_image.image'



	name = fields.Char(
		'Nombre', 
		required=True, 
	)


	file = fields.Binary(
		'Image',
		#filters='*.png,*.jpg,*.gif'
		required=True, 
	)



	image = fields.Many2one(
			'base_multi_image.image',
			string="Image",
			#ondelete='cascade', 
		)



