# -*- coding: utf-8 -*-
#
# 	*** OPEN HEALTH
# 
# Created: 				26 Aug 2016
# Last updated: 	 	17 Sep 2016

from openerp import models, fields, api
from datetime import datetime




class Evaluation(models.Model):
	
	_inherit = 'oeh.medical.evaluation'


	treatment_id = fields.Many2one('openextension.treatment',
			ondelete='cascade', 
			#string="Treatment", 
			string="Tratamiento", 
			)


	patient = fields.Many2one(
			'oeh.medical.patient',
			string="Paciente", 
			#string="Patient", 
			#domain = [
			#			('name', '=', 'Javier Revilla'),
			#		],
			#default = lambda self: self.env['oeh.medical.patient'].search([('name','=','Javier Revilla')]), 
			#index=True
			required=True, 
			)


	doctor = fields.Many2one(
			'oeh.medical.physician',
			string="Médico", 
			#string="Physician", 

			#default = lambda self: self.env['oeh.medical.physician'].search([('name','=','Fernando Chavarri')]), 
			required=True, 
			)


	evaluation_start_date = fields.Date(
			string = "Fecha de Evaluación", 	
			default = fields.Date.today, 
			#readonly = True, 
			required=True, 
			)

	EVALUATION_TYPE = [
			('Pre-arraganged Appointment', 'Primera consulta'),
			('Ambulatory', 'Procedimiento'),
			('Periodic Control', 'Control'),
			]

	evaluation_type = fields.Selection(
			selection = EVALUATION_TYPE, 
			string = 'Tipo de evaluación',
			default = 'Ambulatory', 
			required=True, 
			)


	#chief_complaint = fields.Char(
	#		string = 'Motivo de consulta', 
	#		default = '', 
	#		required=True, 
	#		)


