# -*- coding: utf-8 -*-
#
# 	Control 	
# 

from openerp import models, fields, api
from datetime import datetime

import jxvars




class Control(models.Model):
	_name = 'openhealth.control'
	_inherit = 'oeh.medical.evaluation'


	name = fields.Char(
			string = 'Control #',
			)
			
	procedure = fields.Many2one('openhealth.procedure',
			ondelete='cascade', 
			)