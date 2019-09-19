# -*- coding: utf-8 -*-
"""
Control

Created: 			01 Nov 2016
Last updated: 	 	19 Sep 2019
"""
import datetime
from openerp import models, fields, api
from openerp.addons.openhealth.models.libs import lib
from . import time_funcs
from . import control_vars

class Control(models.Model):
	
	_name = 'openhealth.control'

	_inherit = ['oeh.medical.evaluation', 'base_multi_image.owner']

	_description = 'Control'



# ----------------------------------------------------------- Dates ------------------------------------------------------

	# Date
	evaluation_start_date = fields.Datetime(
			string = "Fecha", 	
			required=False, 		
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
			string = "Fecha Control",

			#compute='_compute_control_date',
		)
	@api.multi
	#@api.depends('state')
	def _compute_control_date(self):
		for record in self:
			record.control_date = record.appointment.appointment_date







	# First date 
	first_date = fields.Datetime(
			string = "Fecha Inicial",
			readonly=True,
		)

	# Real date 
	real_date = fields.Datetime(
			string = "Fecha Real",
		)

	evaluation_next_date = fields.Date(
			string = "Fecha próximo control", 	
			#compute='_compute_evaluation_next_date', 
			#default = fields.Date.today, 

			#required=True, 
			required=False, 
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







	# Procedure  
	procedure = fields.Many2one('openhealth.procedure',
			string="Procedimiento",
			readonly=True,
			ondelete='cascade', 
			)
			
			
	


			

# ----------------------------------------------------------- Actions ------------------------------------------------------
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

