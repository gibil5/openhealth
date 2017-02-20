# -*- coding: utf-8 -*-
#
#
# 		*** OPEN HEALTH - Therapist
# 
# Created: 				18 Feb 2017
# Last updated: 	 	Id.



from openerp import models, fields, api




class Therapist(models.Model):
	
	#_inherit = 'openhealth.process'	
	_name = 'openhealth.therapist'
	



	name = fields.Char(
			string="Terapeuta #", 
			#compute='_compute_name', 
		)