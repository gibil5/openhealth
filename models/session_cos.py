# -*- coding: utf-8 -*-
#
# 	*** Session Cos
#

# Created: 				 24 Feb 2017
# Last updated: 	 	 24 Feb 2017 



from openerp import models, fields, api
from datetime import datetime

import jxvars
import cosvars

import time_funcs
import jrfuncs
#import session_funcs



class SessionCos(models.Model):
	
	_name = 'openhealth.session.cos'
	
	#_inherit = 'oeh.medical.evaluation'
	_inherit = 'openhealth.session'




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





	procedure = fields.Many2one('openhealth.procedure.cos',
			string="Procedimiento Cos",
			readonly=True,
			ondelete='cascade', 
			)
			




