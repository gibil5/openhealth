# -*- coding: utf-8 -*-
#
# 	Evaluation 
# 
# Created: 				26 Aug 2016
# Last updated: 	 	20 Sep 2016

from openerp import models, fields, api
from datetime import datetime

import jxvars








#------------------------------------------------------------------------
class Evaluation(models.Model):
	#_name =	'openhealth.evaluation5'
	_inherit = 'oeh.medical.evaluation'



	name = fields.Char(
			)


	# Commons
	vspace = fields.Char(
			' ', 
			readonly=True
			)


	patient = fields.Many2one(
			'oeh.medical.patient',
			string = "Paciente - nex", 	
			required=True, 
	)

	doctor = fields.Many2one(
			'oeh.medical.physician',
			string = "Médico - nex", 	
			required=True, 
			)


	evaluation_start_date = fields.Date(
			string = "Fecha - nex", 	
			default = fields.Date.today, 
			required=True, 
			)



	chief_complaint = fields.Selection(
			string = 'Motivo de consulta - nex', 
			selection = jxvars._pathology_list, 
			required=True, 
			)





	EVALUATION_TYPE = [
		#('Pre-arraganged Appointment', 'Primera consulta'),
		('Pre-arraganged Appointment', 'Consulta'),
		('Ambulatory', 'Procedimiento'),
		('Periodic Control', 'Control'),
		]

	evaluation_type = fields.Selection(
			selection = EVALUATION_TYPE, 
			#string = 'Tipo de evaluación',
			string = 'Tipo',

			#default = 'Pre-arraganged Appointment', 
			#default = 'Ambulatory', 
			#default = 'Periodic Control', 

			required=True, 
			)





	treatment_id = fields.Many2one(
			'openextension.treatment',
			ondelete='cascade', 
			)

