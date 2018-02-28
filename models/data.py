# -*- coding: utf-8 -*-
#
#
# 		*** OPEN HEALTH - Data 
# 

# Created: 				24 Feb 2018
# Last updated: 	 	id


from openerp import models, fields, api



class Data(models.Model):

	#_inherit = 'oeh.medical.patient'

	#_order = 'write_date desc'

	_description = 'Data'



	_name = 'openhealth.data'







# ----------------------------------------------------------- Primitives ------------------------------------------------------



	vspace = fields.Char(
			' ', 
			readonly=True
		)

