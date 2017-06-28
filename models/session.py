# -*- coding: utf-8 -*-
#
# 	*** Session 	
# 

# Created: 				 1 Nov 2016
# Last updated: 	 	 7 Dec 2016 



from openerp import models, fields, api
from datetime import datetime



from . import jxvars
from . import time_funcs




class Session(models.Model):
	_name = 'openhealth.session'

	#_inherit = 'oeh.medical.evaluation'
	_inherit = ['oeh.medical.evaluation', 'openhealth.base']





	# Autofill
	@api.onchange('x_autofill')
	
	def _onchange_x_autofill(self):

		if self.x_autofill == True:


			self.co2_power = 1.5

			self.co2_frequency = 10

			self.co2_energy = 150

			self.co2_mode_emission = 'fractional'

			self.co2_mode_exposure = 'one'

			self.co2_observations = 'Cicatriz plana hiperpigmentada en pómulo derecho. Pápulas en pómulos.'

			self.x_indications = 'Láser Co2 Fraccional.'






	# Evaluation Nr
	evaluation_nr = fields.Integer(
			string="Sesión #", 
			default=1, 
			)




	# Evaluation type 
	evaluation_type = fields.Selection(
			#selection = eval_vars.EVALUATION_TYPE, 
			#string = 'Tipo',
			
			default='session', 
			
			#required=True, 
			)




	# Treatment 
	treatment = fields.Many2one(
			'openhealth.treatment',
			
			ondelete='cascade', 
			)





	# Owner 
	owner_type = fields.Char(
			default = 'session',
		)

			
			


	# Appointments 

	appointment_ids = fields.One2many(


			'oeh.medical.appointment', 
			#'openhealth.appointment', 

		
			'session', 
			string = "Citas", 
			)






	name = fields.Char(
			string = 'Nombre',
			)

	evaluation_nr = fields.Integer(
			string="Sesión #", 
			default=1, 
			)





	# Relational 
	procedure = fields.Many2one(

			'openhealth.procedure',
			
			string="Procedimiento",
			
			readonly=True,
			
			ondelete='cascade', 
			)
			






	#------------------------------------------------------ Create Appointment ----------------------------------------------------------

	@api.multi
	def open_appointment(self):  

		#print 
		#print 'open appointment'

		owner_id = self.id 
		owner_type = self.owner_type

		patient_id = self.patient.id
		doctor_id = self.doctor.id

		#treatment_id = self.treatment.id 
		treatment_id = self.procedure.treatment.id 



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
							'default_session': owner_id,	

							'default_treatment': treatment_id,
							'default_patient': patient_id,
							'default_doctor': doctor_id,

							'default_x_type': owner_type,


							'default_appointment_date': appointment_date,
							}
				}







	#----------------------------------------------------------- Quick Button ------------------------------------------------------------

	@api.multi
	def open_line_current(self):  

		return {
				'type': 'ir.actions.act_window',
				'name': 'Edit Session Current', 
				'view_type': 'form',
				'view_mode': 'form',
				'res_model': self._name,
				'res_id': self.id,
				'target': 'current',

				'flags': {
						#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
						'form': {'action_buttons': True, }
						},
				
				'context': {}
		}





		