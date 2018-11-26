# -*- coding: utf-8 -*-
#
# 	*** Control 	
# 
# 	Created: 			 1 Nov 2016
# 	Last updated: 	 	 2 Sep 2018
#
import datetime
from openerp import models, fields, api
from . import app_vars
from . import time_funcs
from . import lib
from . import control_vars

class Control(models.Model):
	
	_name = 'openhealth.control'

	_inherit = ['oeh.medical.evaluation', 'base_multi_image.owner']



# ----------------------------------------------------------- Deprecated ------------------------------------------------------
	#@api.onchange('appointment')
	#def _onchange_appointment(self):
	#	print 
	#	print 'On Change - Appointment'
		#self.control_date = self.appointment.appointment_date



# ----------------------------------------------------------- Dates ------------------------------------------------------

	# Date
	evaluation_start_date = fields.Datetime(
			string = "Fecha", 	
			required=False, 
		
			#compute='_compute_evaluation_start_date', 
			#compute='_compute_evaluation_start_date_nex', 
		)

	@api.multi
	#@api.depends('state')
	def _compute_evaluation_start_date_nex(self):
		#print
		#print 'Compute - Eval Start Date'
		for record in self:
			record.evaluation_start_date = record.appointment.appointment_date




	# Real date 
	control_date = fields.Datetime(
			string = "Fecha Real",
			readonly=True, 	

			compute='_compute_control_date', 
		)
	@api.multi
	#@api.depends('state')
	def _compute_control_date(self):
		#print
		#print 'Compute - Control Date'
		for record in self:
			record.control_date = record.appointment.appointment_date




	# First date 
	first_date = fields.Datetime(
			string = "Fecha Inicial", 		
			readonly=True, 	
		)


# ----------------------------------------------------------- State ------------------------------------------------------
	
	# State 
	state = fields.Selection(

			selection = control_vars._state_list, 
			
			compute='_compute_state', 
		)


	@api.multi
	#@api.depends('state')
	def _compute_state(self):
		for record in self:

			state = 'draft'

			if record.appointment.state in ['Scheduled']: 
				state = 'app_confirmed'

			if record.x_done: 
				state = 'done'

			elif record.maturity > 90: 
				state = 'cancel'



			record.state = state



	# Done
	x_done = fields.Boolean(
			#string="Realizado", 			
			string="R", 			
			default=False,
			readonly=True, 
		)



	# Maturity
	maturity = fields.Integer(
			string="Madurez", 

			compute='_compute_maturity', 
		)

	@api.multi
	#@api.depends('state')
	def _compute_maturity(self):
		#print
		#print 'Compute Maturity'
		
		for record in self:

			#today = datetime.datetime.now
			#date_format = "%Y-%m-%d"
			#date_format = "%Y-%m-%d "

			date_format = "%Y-%m-%d %H:%M:%S"
			now = datetime.datetime.now() + datetime.timedelta(hours=-5,minutes=0)	
			now_date_str = now.strftime(date_format)

			first_date_str = record.first_date


			nr = lib.get_nr_days(self, first_date_str, now_date_str)

			record.maturity = nr 

			#print now_date_str
			#print first_date_str
			#print nr



# ----------------------------------------------------------- Nr Days ------------------------------------------------------

	# Nr Days after Session
	nr_days = fields.Integer(
			'Nr Dias', 

			compute='_compute_nr_days', 
		)

	@api.multi
	#@api.depends('state')
	def _compute_nr_days(self):
		for record in self:
			
			if record.control_date == False: 
				record.nr_days = lib.get_nr_days(self, record.procedure.session_date, record.first_date)

			else:
				record.nr_days = lib.get_nr_days(self, record.procedure.session_date, record.control_date)













# ----------------------------------------------------------- Re Definitions ------------------------------------------------------

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



	# Appointment 
	appointment = fields.Many2one(
			'oeh.medical.appointment',			
			
			#'Cita #', 
			'Cita', 
			
			required=False, 
			#required=True, 
			
			#ondelete='cascade', 
		)






	# State Appointment 
	state_app = fields.Selection(
			selection = app_vars._state_list, 

			string = 'Estado Cita', 

			compute='_compute_state_app', 
		)
	
	@api.multi
	#@api.depends('state')
	def _compute_state_app(self):
		for record in self:
			
			record.state_app = record.appointment.state










# ----------------------------------------------------------- Primitives ------------------------------------------------------

	# Name 
	name = fields.Char(
			#string = 'Control #',
			string = 'Nombre',
		)


	# Evaluation Nr
	evaluation_nr = fields.Integer(
			string="#", 
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

			#required=True, 
			required=False, 			
		)
	


	# Owner 
	owner_type = fields.Char(
			default = 'control',
		)




	# Indications
	indication = fields.Text(
			string="Indicaciones",			
			size=200,

			#required=True,
			required=False,
			)



	# Observation
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




# ----------------------------------------------------------- Update ------------------------------
	# Update Done  
	@api.multi	
	def update_done(self):
		#print
		#print 'Update Done'

		# Done 
		if self.x_done == False: 
			self.x_done = True
			#self.control_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		else:
			self.x_done = False

		# Treatment Flag 
		self.treatment.update()


		# Actual Doctor 
		#doctor = user.get_actual_doctor(self)
		#print doctor
		#self.doctor = doctor




	# Update App  
	@api.multi	
	def update_dates(self):
		#print
		#print 'Update Dates'

		self.evaluation_start_date = self.appointment.appointment_date

		# Real 
		#self.control_date = self.appointment.appointment_date

		# First
		self.first_date = self.appointment.appointment_date

		# Treatment Flag 
		self.treatment.update()



# ----------------------------------------------------------- CRUD ------------------------------------------------------

	#@api.multi
	#def unlink(self):
		#print 
		#print 'Unlink - Override'
		#print self.appointment
		#self.appointment.unlink() 
		#print 
	#	return models.Model.unlink(self)


