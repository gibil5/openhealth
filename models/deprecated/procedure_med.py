from openerp import models, fields, api
from datetime import datetime



from . import medvars
from . import time_funcs
from . import jrfuncs
from . import procedure_funcs
from . import procedure_funcs_med






class Proceduremed(models.Model):
	
	_name = 'openhealth.procedure.med'
	
	_inherit = 'openhealth.procedure'





	session_ids = fields.One2many(
			#'openhealth.session', 
			'openhealth.session.med', 
			
			'procedure', 

			string = "sessiones", 
			)
