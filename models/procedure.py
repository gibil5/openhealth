# -*- coding: utf-8 -*-
#
# 	Procedure 	
# 

from openerp import models, fields, api
from datetime import datetime





#------------------------------------------------------------------------
class Procedure(models.Model):
	_name = 'openhealth.procedure'
	_inherit = 'oeh.medical.evaluation'


	name = fields.Char(
			string = 'Procedimiento #',
			)


	#treatment_id = fields.Many2one('openextension.treatment',
	treatment = fields.Many2one('openextension.treatment',
			ondelete='cascade', 
			)



	EVALUATION_TYPE = [
			#('Pre-arraganged Appointment', 'Primera consulta'),
			('Pre-arraganged Appointment', 'Consulta'),
			('Ambulatory', 'Procedimiento'),
			('Periodic Control', 'Control'),
			]

	evaluation_type = fields.Selection(
			selection = EVALUATION_TYPE, 
			string = 'Tipo de evaluación',

			#default = 'Pre-arraganged Appointment', 
			default = 'Ambulatory', 
			#default = 'Periodic Control', 

			required=True, 
			)


	evaluation_start_date = fields.Date(
			string = "Fecha", 	
			default = fields.Date.today, 
			required=True, 
			)


	chief_complaint = fields.Char(
			string = 'Motivo de consulta', 
			default = '', 
			required=True, 
			)


	#-----------------------------------------------------------------------------
	# Aggregated 



