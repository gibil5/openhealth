# -*- coding: utf-8 -*-
#
# 	Evaluation 
# 
# Created: 				26 Aug 2016
# Last updated: 	 	20 Sep 2016

from openerp import models, fields, api
from datetime import datetime



EVALUATION_TYPE = [
	#('Pre-arraganged Appointment', 'Primera consulta'),
	('Pre-arraganged Appointment', 'Consulta'),
	('Ambulatory', 'Procedimiento'),
	('Periodic Control', 'Control'),
	]





#------------------------------------------------------------------------
class Evaluation(models.Model):
	_inherit = 'oeh.medical.evaluation'
	#_name =	'openhealth.evaluation5'



	name = fields.Char(
			)




	#name = fields.Char(
			#compute='_compute_name', 
	#		default=7,
			#default=jx_type,
			#default = get_jx_type()  
	#		)
	#@api.multi
	#@api.depends('start_date')
	#def _compute_name(self):
	#	for record in self:
			#record.name = record.patient.name
	#		record.name = '77'





	treatment_id = fields.Many2one('openextension.treatment',
			ondelete='cascade', 

			#compute='_compute_treatment_id', 
			#default = 'x', 

			#string="Treatment", 
			#string="Tratamiento", 

			#required=True, 
			#index=True, 
			)

	#@api.depends('patient')

	#def _compute_treatment_id(self):
	#	for record in self:
	#		record.treatment_id= record.patient.name 




	patient = fields.Many2one(
			'oeh.medical.patient',
			string = "Paciente", 	
			required=True, 
			)

	doctor = fields.Many2one(
			'oeh.medical.physician',
			string = "Médico", 	
			required=True, 
			)



	evaluation_start_date = fields.Date(
			#string = "Fecha de Evaluación", 	
			string = "Fecha", 	
			default = fields.Date.today, 
			#readonly = True, 
			required=True, 
			)



	evaluation_type = fields.Selection(
			selection = EVALUATION_TYPE, 
			#string = 'Tipo de evaluación',
			string = 'Tipo',

			#default = 'Pre-arraganged Appointment', 
			#default = 'Ambulatory', 
			#default = 'Periodic Control', 

			required=True, 
			)

	chief_complaint = fields.Char(
			string = 'Motivo de consulta', 
			default = '', 
			#required=True, 
			)









#class Control(models.Model):
#	_name = 'openhealth.control'

#	_inherit = 'oeh.medical.evaluation'


#	treatment_id = fields.Many2one('openextension.treatment',
#			ondelete='cascade', 
#			)

#	evaluation_type = fields.Selection(
#			selection = EVALUATION_TYPE, 
#			string = 'Tipo de evaluación',

			#default = 'Pre-arraganged Appointment', 
			#default = 'Ambulatory', 
#			default = 'Periodic Control', 

#			required=True, 
#			)
