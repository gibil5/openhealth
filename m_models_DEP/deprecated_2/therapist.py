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
	
	#_inherit = 'oeh.medical.physician'	
	
	_name = 'openhealth.therapist'
	



	name = fields.Char(
			string="Terapeuta #", 
			#compute='_compute_name', 
		)