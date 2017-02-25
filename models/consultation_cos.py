# -*- coding: utf-8 -*-
#
# 	*** Consultation Cos
# 

# Created: 				 1 Nov 2016
# Last updated: 	 	 7 Dec 2016 



from openerp import models, fields, api
from datetime import datetime,tzinfo,timedelta

import jxvars
import cosvars


import jrfuncs
import eval_vars
import time_funcs




class ConsultationCos(models.Model):

	#_inherit = 'oeh.medical.evaluation'
	_inherit = 'openhealth.consultation'

	_name = 'openhealth.consultation.cos'
	




	#cosmetology = fields.Many2one('openhealth.cosmetology',
	#		ondelete='cascade', 
	#		string="Cosmetología",
			#required=True, 
	#		)



	chief_complaint = fields.Selection(			# Necessary 
			string = 'Motivo de consulta', 

			selection = cosvars._chief_complaint_list, 

			#required=True, 
			required=False, 
			)






