from openerp import models, fields, api
from datetime import datetime

import jxvars
import medvars

import time_funcs
import jrfuncs
import procedure_funcs
import procedure_funcs_med




class Proceduremed(models.Model):
	
	_name = 'openhealth.procedure.med'
	
	#_inherit = 'oeh.medical.evaluation'
	_inherit = 'openhealth.procedure'





	session_ids = fields.One2many(
			#'openhealth.session', 
			'openhealth.session.med', 
			
			'procedure', 

			string = "sessiones", 
			)
