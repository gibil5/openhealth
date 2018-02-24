# -*- coding: utf-8 -*-
#
#
# 		*** OPEN HEALTH - Legacy 
# 

# Created: 				24 Feb 2018
# Last updated: 	 	id


from openerp import models, fields, api
from datetime import datetime



class Legacy(models.Model):

	#_inherit = 'oeh.medical.patient'

	#_order = 'write_date desc'

	_description = 'Legacy'



	_name = 'openhealth.legacy'







# ----------------------------------------------------------- Primitives ------------------------------------------------------



	vspace = fields.Char(
			' ', 
			readonly=True
		)

