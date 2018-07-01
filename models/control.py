# -*- coding: utf-8 -*-
#
# 	*** Control 	
# 
# Created: 				 1 Nov 2016
# Last updated: 	 	 20 Jun 2017

from openerp import models, fields, api

import datetime
from . import eval_vars
from . import time_funcs



class Control(models.Model):
	
	_name = 'openhealth.control'

	#_inherit = 'oeh.medical.evaluation'
	_inherit = ['oeh.medical.evaluation', 'base_multi_image.owner']




# ----------------------------------------------------------- Deprecated ------------------------------------------------------
	
	# Appointments 
	#appointment_ids = fields.One2many(
	#		'oeh.medical.appointment', 
	#		'control', 
	#		string = "Citas", 
	#	)




# ----------------------------------------------------------- Redef ------------------------------------------------------
	# Patient 
	patient = fields.Many2one(
			'oeh.medical.patient',
			string = "Paciente", 	
			ondelete='cascade', 

			#readonly=True, 
			readonly=False, 

			required=True, 
			#required=False, 
		)

	# Treatment 
	treatment = fields.Many2one(
			'openhealth.treatment',
			ondelete='cascade', 

			readonly=False, 

			required=True, 
			#required=False, 
		)



	# Control date 
	control_date = fields.Datetime(
			string = "Fecha Real", 	

			#required=True, 
		
			#compute='_compute_control_date', 
		)

	@api.multi
	#@api.depends('state')
	def _compute_control_date(self):
		for record in self:
			record.control_date = record.appointment.appointment_date




	# Appointment 
	appointment = fields.Many2one(
			'oeh.medical.appointment',			
			string='Cita #', 
			
			#required=False, 
			required=True, 
			
			#ondelete='cascade', 
		)


	# Appointemnt
	@api.onchange('appointment')
	def _onchange_appointment(self):

		print 
		print 'On Change - Appointment'

		self.control_date = self.appointment.appointment_date




# ----------------------------------------------------------- Dates ------------------------------------------------------


	# Default - First Date 
	#@api.model
	#def _get_first_date(self):
		#first_date = self.control_date
	#	first_date = self.appointment.appointment_date	
	#	return first_date



	# Control date 
	#first_date = fields.Datetime(
	first_date = fields.Date(
		
			string = "Fecha Inicial", 	
		
			#default=_get_first_date, 
			#compute='_compute_first_date', 
		)

	#@api.multi
	#@api.depends('state')
	#def _compute_first_date(self):
	#	for record in self:
	#		if record.first_date == False: 		
	#			record.first_date = record.control_date















# ----------------------------------------------------------- Re Definition ------------------------------------------------------


# ----------------------------------------------------------- Primitives ------------------------------------------------------

	# state 
	state = fields.Selection(

			selection = eval_vars._state_list, 
			
			compute='_compute_state', 
		)


	@api.multi
	#@api.depends('state')

	def _compute_state(self):
		for record in self:

			state = 'draft'

			if record.x_done: 
				state = 'done'

			record.state = state








	# Name 
	name = fields.Char(
			#string = 'Control #',
			string = 'Nombre',
		)

















	# Dates 
	#evaluation_start_date = fields.Date(	
	evaluation_start_date = fields.Datetime(
	
			string = "Fecha - jx", 	
	
			#required=True, 
			required=False, 
		
			compute='_compute_evaluation_start_date', 
		)

	@api.multi
	#@api.depends('state')

	def _compute_evaluation_start_date(self):
		for record in self:

			#record.evaluation_start_date = record.appointment.x_date
			record.evaluation_start_date = record.appointment.appointment_date












	# Done
	x_done = fields.Boolean(
			string="Realizado", 			
			default=False,

			#compute='_compute_x_done', 
		)


	#@api.multi
	#@api.depends('state')
	#def _compute_x_done(self):
	#	for record in self:
	#		if record.state == 'done':
	#			record.x_done = True 






	# Evaluation Nr
	#control_nr = fields.Integer(
	evaluation_nr = fields.Integer(
			string="Control #", 
			default=1, 

			#compute='_compute_control_nr', 
		)














	# Evaluation type 
	evaluation_type = fields.Selection(
			#selection = eval_vars.EVALUATION_TYPE, 
			#string = 'Tipo',
			
			default='control', 
			
			#required=True, 
			)






	# Product
	product = fields.Many2one(
			'product.template',
			string="Producto",
			required=True, 
			)
	










	# Owner 
	owner_type = fields.Char(
			default = 'control',
		)











	indication = fields.Text(
			string="Indicaciones",			
			size=200,

			#required=True,
			required=False,
			)



	#observation = fields.Char(
	observation = fields.Text(
			string="Observación",
			size=200,

			#required=True,
			required=False,
			)


	evaluation_next_date = fields.Date(
			string = "Fecha próximo control", 	
			#compute='_compute_evaluation_next_date', 
			#default = fields.Date.today, 

			#required=True, 
			required=False, 
			)




	# Procedure  
	procedure = fields.Many2one('openhealth.procedure',
			string="Procedimiento",
			readonly=True,
			ondelete='cascade', 
			)
			
			
	


			

# ----------------------------------------------------------- Actions ------------------------------------------------------

	# Open Appointment 
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
		#appointment_date = datetime.now(GMT).strftime("%Y-%m-%d %H:%M:%S")
		appointment_date = datetime.datetime.now(GMT).strftime("%Y-%m-%d %H:%M:%S")
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
							'default_control': owner_id,

							'default_treatment': treatment_id,
							'default_patient': patient_id,
							'default_doctor': doctor_id,

							'default_x_type': owner_type,


							'default_appointment_date': appointment_date,
							}
				}






	# Open Line 
	@api.multi
	def open_line_current(self):  

		return {
				'type': 'ir.actions.act_window',
				'name': 'Edit Control Current', 
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






# ----------------------------------------------------------- CRUD ------------------------------------------------------

	@api.multi
	def unlink(self):
		#print 
		#print 'Unlink - Override'
		#print self.appointment
		#self.appointment.unlink() 
		#print 
		return models.Model.unlink(self)



