# -*- coding: utf-8 -*-
#
# 	Procedure 	
# 

from openerp import models, fields, api
from datetime import datetime

import jxvars

import time_funcs




class Procedure(models.Model):
	_name = 'openhealth.procedure'
	_inherit = 'oeh.medical.evaluation'



	name = fields.Char(
			#string = 'Procedimiento #',
			string = 'Proc #',
			)


	# Owner 
	owner_type = fields.Char(
			default = 'procedure',
		)






	# Redefinition 

	evaluation_type = fields.Selection(
			default = 'Ambulatory', 
			)



	# Relational 

	control_ids = fields.One2many(
			'openhealth.control', 
			'procedure', 
			string = "Controles", 
			)
			
	session_ids = fields.One2many(
			'openhealth.session', 
			'procedure', 
			string = "sessiones", 
			)

	treatment = fields.Many2one('openextension.treatment',
			ondelete='cascade', 
			)



	
	
	# Controls - Number

	nr_controls = fields.Integer(
			string="Controles",
			compute="_compute_nr_controls",
	)
	
	#@api.multi
	@api.depends('control_ids')

	def _compute_nr_controls(self):
		for record in self:
			ctr = 0 
			for c in record.control_ids:
				ctr = ctr + 1
			record.nr_controls = ctr		




	# Sessions - Number

	nr_sessions = fields.Integer(
			string="Sesiones",
			compute="_compute_nr_sessions",
	)
	
	#@api.multi
	@api.depends('session_ids')
	
	def _compute_nr_sessions(self):
		for record in self:
			ctr = 0 
			for c in record.session_ids:
				ctr = ctr + 1
			record.nr_sessions = ctr

	
	
	




	#------------------------------------ Buttons -----------------------------------------


	# Consultation - Quick Self Button  

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

				'context':   {}
		}





	# Open Control 

	@api.multi

	def open_control(self):  

		procedure_id = self.id 

		patient_id = self.patient.id
		doctor_id = self.doctor.id
		chief_complaint = self.chief_complaint
		
		evaluation_type = 'Periodic Control'
		product_id = self.product.id
		laser = self.laser
		

		# Date 		
		GMT = time_funcs.Zone(0,False,'GMT')
		print GMT
		evaluation_start_date = datetime.now(GMT).strftime("%Y-%m-%d %H:%M:%S")
		print evaluation_start_date 
		print 


		return {

			# Mandatory 
			'type': 'ir.actions.act_window',
			'name': 'Open control Current',


			# Optional 
			'res_model': 'openhealth.control',

			'view_mode': 'form',
			"views": [[False, "form"]],

			'target': 'current',

			'context':   {

				'default_patient': patient_id,
				'default_doctor': doctor_id,
				'default_chief_complaint': chief_complaint,

				'default_procedure': procedure_id,
				'default_evaluation_type':evaluation_type,
								
				'default_product': product_id,
				'default_laser': laser,
				
				'default_evaluation_start_date': evaluation_start_date,

			}
		}







	# Open Session  

	@api.multi
	def open_session(self):  
		print 
		print 'open session'

		procedure_id = self.id 

		patient_id = self.patient.id
		doctor_id = self.doctor.id
		chief_complaint = self.chief_complaint
		
		evaluation_type = 'Session'
		product_id = self.product.id
		laser = self.laser
		

		# Date 		
		GMT = time_funcs.Zone(0,False,'GMT')
		print GMT
		evaluation_start_date = datetime.now(GMT).strftime("%Y-%m-%d %H:%M:%S")
		print evaluation_start_date 
		print 

		return {

			# Mandatory 
			'type': 'ir.actions.act_window',
			'name': 'Open session Current',


			# Optional 
			'res_model': 'openhealth.session',

			'view_mode': 'form',
			"views": [[False, "form"]],

			'target': 'current',

			'context':   {

				'default_patient': patient_id,
				'default_doctor': doctor_id,
				'default_chief_complaint': chief_complaint,

				'default_procedure': procedure_id,
				'default_evaluation_type':evaluation_type,
								
				'default_product': product_id,
				'default_laser': laser,


				'default_evaluation_start_date': evaluation_start_date,
			}
		}





	# Open Appointment
	# -----------------
	@api.multi
	def open_appointment(self):  

		print 
		print 'open appointment'

		owner_id = self.id 
		owner_type = self.owner_type

		patient_id = self.patient.id
		doctor_id = self.doctor.id
		treatment_id = self.treatment.id 



		GMT = time_funcs.Zone(0,False,'GMT')
		appointment_date = datetime.now(GMT).strftime("%Y-%m-%d %H:%M:%S")
		#appointment_date = '2016-12-23'


		return {
				'type': 'ir.actions.act_window',

				'name': ' New Appointment', 
				
				'view_type': 'form',
				
				#'view_mode': 'form',			
				'view_mode': 'calendar',			
				
				'target': 'current',
				

				'res_model': 'oeh.medical.appointment',				
				
				'flags': 	{
							#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
							'form': {'action_buttons': True, }
							},


				'context': {
							'default_consultation': owner_id,					
							'default_treatment': treatment_id,
							'default_patient': patient_id,
							'default_doctor': doctor_id,

							'default_x_type': owner_type,


							'default_appointment_date': appointment_date,
							}
				}




