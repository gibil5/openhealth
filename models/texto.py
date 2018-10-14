# -*- coding: utf-8 -*-
#
#		Text 
# 
# 		Created: 		26 Aug 2016
# 		Last up: 		26 Sep 2018
#
from openerp import models, fields, api

class Texto(models.Model):
	
	#_inherit = 'oeh.medical.patient'
	
	#_order = 'x_id_code desc'

	_name = 'openhealth.texto'




	name = fields.Char()


	content = fields.Char()


	container_id = fields.Many2one(
		'openhealth.container', 		
		ondelete='cascade', 
	)
