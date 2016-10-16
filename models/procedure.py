# -*- coding: utf-8 -*-
#
# 	Procedure 	
# 

from openerp import models, fields, api
from datetime import datetime

import jxvars




class Procedure(models.Model):
	_name = 'openhealth.procedure'
	_inherit = 'oeh.medical.evaluation'


	name = fields.Char(
			string = 'Procedimiento #',
			)



	control_ids = fields.One2many(
			'openhealth.control', 
			'procedure', 
			string = "Controles", 
			)
			
			


	# Service 
	product = fields.Many2one(
			'product.template',

			#domain = [
			#			('type', '=', 'service'),
			#			('x_treatment', '=', _jx_laser_type),
			#		],

			string="Producto",
			required=True, 
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



	# Motivo de consulta
	chief_complaint = fields.Selection(
			string = 'Motivo de consulta', 
			selection = jxvars._pathology_list, 
			#default = '', 
			required=True, 
			)





	#------------------------------------- Aggregated ----------------------------------------


	#------------------------------------ Buttons -----------------------------------------

	# Consultation - Quick Self Button  
	# ---------------------------------

	@api.multi
	def open_line_current(self):  

		procedure_id = self.id 

		return {
				'type': 'ir.actions.act_window',
				'name': ' Edit Consultation Current', 
				'view_type': 'form',
				'view_mode': 'form',
				'res_model': self._name,
				'res_id': procedure_id,
				'target': 'current',
				'flags': {
						'form': {'action_buttons': True, }
						},

				'context':   {
				}
		}




	# Control 
	# ---------
	@api.multi
	def open_control(self):  

		patient_id = self.patient.id
		doctor_id = self.physician.id
		#chief_complaint = self.chief_complaint
		
		procedure_id = self.id 


		return {

			# Mandatory 
			'type': 'ir.actions.act_window',
			'name': 'Open control Current',

			'res_model': 'openhealth.control',

			'view_mode': 'form',
			"views": [[False, "form"]],

			'target': 'current',

			'context':   {
				#'search_default_treatment': treatment_id,

				#'default_patient': patient_id,
				#'default_doctor': doctor_id,
				#'default_treatment': treatment_id,
				#'default_chief_complaint': chief_complaint,
				
			}
		}

