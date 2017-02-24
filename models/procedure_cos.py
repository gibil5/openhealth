# -*- coding: utf-8 -*-
#
# 	*** Procedure Cos
#

# Created: 				 1 Nov 2016
# Last updated: 	 	 7 Dec 2016 



from openerp import models, fields, api
from datetime import datetime

import jxvars
import cosvars

import time_funcs
import jrfuncs
import procedure_funcs



class ProcedureCos(models.Model):
	
	_name = 'openhealth.procedure.cos'
	
	#_inherit = 'oeh.medical.evaluation'
	_inherit = 'openhealth.procedure'



	cosmetology = fields.Many2one(
			'openhealth.cosmetology',
			string="Cosmiatría", 
			ondelete='cascade', 
			)



	chief_complaint = fields.Selection(			# Necessary 
			string = 'Motivo de consulta', 

			selection = cosvars._chief_complaint_list, 

			#required=True, 
			required=False, 
			)


