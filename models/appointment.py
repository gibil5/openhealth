# -*- coding: utf-8 -*-
#
# 		***	 Appointment
#
# 		Created: 			14 Nov 2016
# 		Last updated: 	 	28 Aug 2018
#
from openerp import models, fields, api
import datetime
import app_vars
import eval_vars
import lib
import user

class Appointment(models.Model):

	_inherit = 'oeh.medical.appointment'

	_order = 'name asc'



# ----------------------------------------------------------- Deprecated ------------------------------------------------------
	#x_target = fields.Char()
	#x_machine = fields.Char()
	#x_time = fields.Char()
	#x_date = fields.Char()




# ----------------------------------------------------------- Dates ------------------------------------------------------

	# Date Start 
	appointment_date = fields.Datetime(
			string="Fecha", 
			readonly=False,
			#states={'Scheduled': [('readonly', False)]}), 
		
			#default = fields.Date.today, 
		)

	@api.onchange('appointment_date')
	def _onchange_appointment_date(self):
		print
		print 'Change Date'
		#print self.x_type
		
		if self.x_type == 'control': 
			pass 
			#print 'Gotcha !'
			#print self.control.control_date
			#print self.control.evaluation_start_date
			#self.control.control_date = self.appointment_date
			#self.control.evaluation_start_date = self.appointment_date
			#print self.control.control_date
			#print self.control.evaluation_start_date
			#self.control.update_dates(self.appointment_date)




# ----------------------------------------------------------- Confirmation ------------------------------------------------------
	# Confirmable 
	x_confirmable = fields.Boolean(
			'Confirmable', 

			compute='_compute_x_confirmable', 
		)

	@api.multi
	#@api.depends('patient')
	def _compute_x_confirmable(self):
		#print 
		#print 'Compute Confirmable'
		for record in self:
			if lib.is_today(record.appointment_date, record.state): 
				record.x_confirmable = True 				
			else: 
				record.x_confirmable = False 


# ----------------------------------------------------------- Canonical ------------------------------------------------------

	# Type 
	x_type = fields.Selection(

			selection = app_vars._type_list, 
		
			string="Tipo",
			required=True, 
		)

	# Sub type 
	x_subtype = fields.Selection(

			selection = app_vars._subtype_list, 
		
			string="Sub-tipo",
			
			required=True, 
		)





	# Name 
	name = fields.Char(
			string="Cita #", 
			required=True, 
		)


	# Vspace 
	vspace = fields.Char(
			' ', 
			readonly=True
		)

	


	# Date End 
	appointment_end = fields.Datetime(
			string="Fecha fin", 		
			readonly=True, 
			)


	# Doctor 
	doctor = fields.Many2one(
			'oeh.medical.physician',			
			string = "Médico", 
			required=True, 
			#required=False, 
			readonly = False, 
		)


	# Patient
	patient = fields.Many2one(
			'oeh.medical.patient',
			string = "Paciente", 	
			ondelete='cascade', 
			#required=True, 
			required=False, 
			readonly = False, 
		)


	# State 
	state = fields.Selection(
			#selection = APPOINTMENT_STATUS, 
			selection = app_vars._state_list, 
			string="Estado",
			
			default='pre_scheduled',
			
			readonly=False, 
			#readonly=True, 

			required=True, 
		)


	# Comments 
	comments = fields.Text (
			'Observaciones', 
			readonly=False,
			#states={'Scheduled': [('readonly', False)]}
		)


	# Duration 
	duration = fields.Float(
			string="Duración (h)",
			default=0.5,

			#compute='_compute_duration', 				# Very important. So, that the duration will not be changed manually. 
		)

	@api.multi
	@api.depends('x_type')
	def _compute_duration(self):	
		for record in self:	
			if record.x_type in ['consultation', 'procedure', 'session']:
				record.duration = 0.5
			elif record.x_type == 'control':
				record.duration = 0.25
			else: 
				record.duration = 0.5



















	# ----------------------------------------------------------- Relational ------------------------------------------------------

	# Treatement 
	treatment = fields.Many2one(			
			'openhealth.treatment',
			string="Tratamiento",
			ondelete='cascade', 
			readonly=False, 

			#required=False, 
			required=True, 
		)


	# Treatement Instantiation or Creation 
	@api.onchange('patient','doctor')
	def _onchange_patient_doctor(self):

		print
		print 'On change - Patient Doctor'


		if self.patient.name != False and self.doctor.name != False:

			# Search 
			treatment = self.env['openhealth.treatment'].search([
																		('patient', '=', self.patient.name),			
																		('physician', '=', self.doctor.name),					
																	],
																	order='start_date desc',
																	limit=1,
																)
			# Create
			if treatment.name == False: 

				print 'create'

				treatment = self.env['openhealth.treatment'].create({
																		'patient': self.patient.id,
																		'physician': self.doctor.id,

																	})
			# Assign
			if treatment.name != False: 
				self.treatment = treatment
			else: 
				print 
				print 'ERROR !!!'
				print 'This sould Never happem !'
				print 


		print self.treatment
		print 

	# _onchange_patient_doctor










# ----------------------------------------------------------- Handles ------------------------------------------------------

	# Appointment is NOT Deleted if Session/Control IS Deleted 
	consultation = fields.Many2one('openhealth.consultation',
			string="Consulta",
			#ondelete='cascade', 			# Very important. 
		)




	# Appointment IS Deleted if Evaluation is Deleted	***
	procedure = fields.Many2one('openhealth.procedure',
			string="Procedimiento",
			
			ondelete='cascade', 
		)

	#session = fields.Many2one('openhealth.session',
	session = fields.Many2one('openhealth.session.med',
			string="Sesión",

			ondelete='cascade', 
		)

	control = fields.Many2one('openhealth.control',
			string="Control",		

			ondelete='cascade', 
		)





# ----------------------------------------------------------- Display  ------------------------------------------------------

	# Patient name short 
	x_patient_name_short = fields.Char(

			compute='_compute_x_patient_name_short', 
		)

	#@api.multi
	@api.depends('patient')
	def _compute_x_patient_name_short(self):
		for record in self:
			if record.patient.name != False: 
				patient_name = record.patient.name
				first_half = patient_name.split(' ')[0]
			else:
				#first_half = 'EV'
				first_half = 'X'
			record.x_patient_name_short = first_half




	# Doctor Code 
	x_doctor_code = fields.Char(

			compute='_compute_x_doctor_code',
		)

	#@api.multi
	@api.depends('doctor')
	def _compute_x_doctor_code(self):
		for record in self:
			record.x_doctor_code = app_vars._hash_doctor_code[record.doctor.name]




	# Type Calendar 
	x_type_cal = fields.Selection(
				selection = app_vars._type_cal_list, 
	
				compute='_compute_x_type_cal', 
		)

	#@api.multi
	@api.depends('x_type')
	def _compute_x_type_cal(self):
		for record in self:	
			#record.x_type_cal = self._type_cal_dic[record.x_type]
			record.x_type_cal = app_vars._type_cal_dic[record.x_type]




	# State short 
	x_state_short = fields.Char(

			compute='_compute_x_state_short',
		)

	#@api.multi
	@api.depends('state')
	def _compute_x_state_short(self):
		for record in self:
			if record.state != False:
				#record.x_state_short = self._hash_state[record.state]
				record.x_state_short = app_vars._hash_state[record.state]




	# Display 
	x_display = fields.Char(

			compute='_compute_x_display', 
		)


	@api.multi
	#@api.depends('x_appointment')

	def _compute_x_display(self):

		#print 
		#print 'Compute Display'

		for record in self:

			#separator = ' - '
			sep = ' '


			#print record.x_subtype

			# Patient or Event 
			#record.x_display = record.x_patient_name_short + ' - '  + record.x_doctor_code + ' - ' + record.x_type_cal + ' - ' + record.x_state_short
			#record.x_display = record.x_patient_name_short + sep  + record.x_doctor_code + sep + record.x_type_cal + sep + record.x_state_short
			record.x_display = record.x_patient_name_short + sep  + record.x_doctor_code + sep + record.x_type_cal + sep + record.x_state_short + sep + app_vars._h_subtype[record.x_subtype]



			# Control 
			#if record.x_type == 'control': 
			#	record.x_display = record.name + separator  + record.x_doctor_code + separator + record.x_type_cal + separator + record.x_state_short

			# Machine 
			#if record.x_machine != False:
			#	record.x_display = record.x_display + ' - ' + record.x_machine_short

	# _compute_x_display







# ----------------------------------------------------------- Confirm  ------------------------------------------------------

	# Confirm
	@api.multi
	def confirm(self):  

		print
		print 'Confirm'


		# Only for Controls
		if self.x_type in ['control','session']: 

			# Get Next Slot - Real Time version 
			appointment_date = lib.get_next_slot(self)						# Next Slot


			# Init 
			#appointment_date = self.appointment_date
			#state = 'pre_scheduled'
			duration = self.duration
			x_type = self.x_type
			doctor_name = self.doctor.name
			states = ['pre_scheduled','Scheduled']


			# Check and Push
			appointment_date_str = user.check_and_push(self, appointment_date, duration, x_type, doctor_name, states)

			self.appointment_date = appointment_date_str
			
			#print appointment_date_str
			#print


		# All 
		self.state = 'Scheduled'

		# Treatment Flag 
		if self.treatment.name != False: 
			self.treatment.update()

	# confirm 





	# Unconfirm
	@api.multi
	def un_confirm(self):  

		print
		print 'Un Confirm'

		self.state = 'pre_scheduled'

		# Treatment Flag 
		self.treatment.update()





# ----------------------------------------------------------- On Change ------------------------------------------------------

	@api.onchange('state')
	def _onchange_state(self):

		print
		print 'On change - State'

		# Confirm if Control or Session 
		if 	(self.state in ['Scheduled','pre_scheduled'])		and 	(self.x_type in ['control','session']): 

			self.confirm()





# ----------------------------------------------------------- Remove Myself  ------------------------------------------------------

	# Remove Myself
	@api.multi
	def remove_myself(self):  
		appointment_id = self.id
		rec_set = self.env['oeh.medical.appointment'].browse([appointment_id])		
		ret = rec_set.unlink()



#----------------------------------------------------------- Hot Button - For Treatment ------------------------------------------------------------

	# For Treatments Quick access
	@api.multi
	def open_line_current(self):  
		res_id = self.id 
		return {
				'type': 'ir.actions.act_window',
				'name': ' Edit Order Current', 
				'view_type': 'form',
				'view_mode': 'form',
				'res_model': self._name,
				'res_id': res_id,
				'target': 'current',
				'flags': {
						#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
						'form': {'action_buttons': True, }
						},
				'context': {}
		}



# ----------------------------------------------------------- CRUD ------------------------------------------------------
	# Create 
	@api.model
	def create(self,vals):
		#print
		#print 'Appointment - Create'


		# Super 
		#print 'mark'
		res = super(Appointment, self).create(vals)
		#print 'mark'


		# Init 
		appointment_date = res.appointment_date
		x_type = res.x_type
		doctor_id = res.doctor.id
		patient_id = res.patient.id
		treatment_id = res.treatment.id

		return res
	# create

# CRUD
