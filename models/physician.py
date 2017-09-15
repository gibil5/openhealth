# -*- coding: utf-8 -*-
#
#
# 		*** OPEN HEALTH - Physician
# 
# Created: 				6 Mar 2017
# Last updated: 	 	Id.



from openerp import models, fields, api




class Physician(models.Model):
	

	_inherit = 'oeh.medical.physician'	
	
	#_name = 'openhealth.physician'
	



	#name = fields.Char(
	#		string="Terapeuta #", 
			#compute='_compute_name', 
	#	)


	vspace = fields.Char(
			' ', 
			readonly=True
		)
	



	x_therapist = fields.Boolean(
			string='Terapeuta', 
			default=False,
		)	


	_phy_list = [

		('therapist','therapist'), 
		('doctor','doctor'), 

		#('',''), 

	]



	x_type = fields.Selection(
			string='Tipo', 

			selection = _phy_list, 

			#default='therapist',
		)



