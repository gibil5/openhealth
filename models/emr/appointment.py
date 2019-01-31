# -*- coding: utf-8 -*-
"""
 		Appointment

 		Created: 			14 Nov 2016
		Last updated: 	 	23 Jan 2019
"""
from __future__ import print_function

import datetime
from openerp import models, fields, api
from openerp.addons.openhealth.models.libs import user, lib
from openerp.addons.openhealth.models.order import ord_vars
from openerp.addons.openhealth.models.patient import pat_vars
from . import app_vars

class Appointment(models.Model):
	"""
	high level support for doing this and that.
	"""

	_inherit = 'oeh.medical.appointment'

	#_order = 'appointment_date desc'
	_order = 'appointment_date asc'



# ----------------------------------------------------------- Id Doc ------------------------------

	# Id Doc Type
	x_id_doc_type = fields.Selection(
			selection=pat_vars.get_id_doc_type_list(),
			string='Tipo doc.',
			readonly=True,
		)

	# Id Doc
	x_id_doc = fields.Char(
			'Nr doc.',
			readonly=True,
		)


# ----------------------------------------------------------- Group By ----------------------------

	# Day
	#x_day = fields.Char(
	x_day = fields.Selection(
			selection=ord_vars._day_order_list,
			string='Dia',
			readonly=True,
		)




	# Month
	x_month = fields.Selection(
			selection=ord_vars._month_order_list,
			string='Mes',
			readonly=True,
		)

	# Year
	x_year = fields.Selection(
			selection=ord_vars._year_order_list,
			string='Año',
			readonly=True,
		)



	# Time
	x_time = fields.Datetime(
			string='Hora',
			#readonly=True,
			readonly=False,
		)



# ----------------------------------------------------------- Handles (Relational) ----------------
	# Treatement
	treatment = fields.Many2one(
			'openhealth.treatment',
			string="Tratamiento",
			ondelete='cascade',
			readonly=False,
			required=True,
		)

	# Appointment is NOT Deleted if Session/Control IS Deleted
	consultation = fields.Many2one('openhealth.consultation',
			string="Consulta",
			#ondelete='cascade', 			# Very important
		)


	# Appointment IS Deleted if Evaluation is Deleted	***
	procedure = fields.Many2one('openhealth.procedure',
			string="Procedimiento",
			ondelete='cascade',
		)

	session = fields.Many2one('openhealth.session.med',
			string="Sesión",
			ondelete='cascade',
		)


	# Default - Control
	@api.model
	def _get_default_patient_name(self):

		patient_name = 'SAUCEDO SAUCEDO SALVADOR'

		return patient_name





# ----------------------------------------------------------- Defaults ---------------------------


	# Default - Control
	@api.model
	def _get_default_control(self):

		print()
		print('Get Default Control')

		for record in self:
			print(record.patient)


		#print(model.patient)

		patient_name = 'SAUCEDO SAUCEDO SALVADOR'

 		control = self.env['openhealth.control'].search([
																('patient', '=', patient_name),
														],
															order='first_date asc',
															limit=1,
														)
		return control



	control = fields.Many2one('openhealth.control',
			string="Control",
			ondelete='cascade',

			#domain=[
						#('patient', '=', 'SAUCEDO SAUCEDO SALVADOR'),
			#			('patient', '=', _get_default_patient_name),
			#		],

			#default=_get_default_control,
		)





# ----------------------------------------------------------- Dates -------------------------------
	# Date Start
	appointment_date = fields.Datetime(
			string="Fecha",
			#string="Fecha y hora",
			readonly=False,

			index=True,
		)

	# Date only
	appointment_date_date = fields.Date(
			string="Fecha F",
			#readonly=False,
		)


	# Today
	#x_today = fields.Boolean(
	#		'Hoy',
	#		default=False,
	#	)




# ----------------------------------------------------------- Confirmation ------------------------
	# Confirmable
	x_confirmable = fields.Boolean(
			'Confirmable',

			compute='_compute_x_confirmable',
		)

	@api.multi
	#@api.depends('patient')
	def _compute_x_confirmable(self):
		for record in self:

			#if lib.is_today_and_not_scheduled(record.appointment_date, record.state):

			if lib.is_today(record.appointment_date):

				record.x_confirmable = True

			else:
				record.x_confirmable = False



# ----------------------------------------------------------- Canonical ---------------------------
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

	# Type
	x_type = fields.Selection(
			selection=app_vars._type_list,
			string="Tipo",
			required=True,
		)

	# Sub type
	x_subtype = fields.Selection(
			selection=app_vars._subtype_list,
			string="Sub-tipo",
			required=True,
		)

	# Date End
	appointment_end = fields.Datetime(
			string="Fecha fin",
			readonly=True,
		)

	# Doctor
	doctor = fields.Many2one(
			'oeh.medical.physician',
			string="Médico",
			required=True,
			readonly=False,
		)

	# Patient
	patient = fields.Many2one(
			'oeh.medical.patient',
			string="Paciente",
			ondelete='cascade',
			required=False,
			readonly=False,
		)

	# State
	state = fields.Selection(
			selection=app_vars._state_list,
			string="Estado",
			default='pre_scheduled',
			required=True,

			#readonly=False,
			readonly=True,
		)

	# Comments
	comments = fields.Text(
			'Observaciones',
			readonly=False,
		)

	# Duration
	duration = fields.Float(
			string="Duración (h)",

			default=0.5,

			required=True,
			
			#compute='_compute_duration', 		# duration should not change manually - Deprecated?
			readonly=True,
		)





# ----------------------------------------------------------- Relational --------------------------

	# Treatement Instantiation or Creation
	@api.onchange('patient', 'doctor')
	def _onchange_patient_doctor(self):
		"""
		On change Patient or Doctor, search or create Treatment.
		"""
		#print
		#print 'On change - Patient Doctor'

		# Avoid invalid input
		if self.patient.name != False and self.doctor.name != False:


			# Search - If Treatment existant
			treatment = self.env['openhealth.treatment'].search([
																		('patient', '=', self.patient.name),
																		('physician', '=', self.doctor.name),
																	],
																	order='start_date desc',
																	limit=1,
																)
			# Create - If Treatment not existant
			if not treatment.name:

				treatment = self.env['openhealth.treatment'].create({
																		'patient': self.patient.id,
																		'physician': self.doctor.id,
																	})
			# Assign
			if treatment.name != False:
				self.treatment = treatment
			#else:
			#	pass
				#print
				#print 'ERROR !!!'
				#print 'This sould Never happem !'
				#print


		#print self.treatment
		#print

	# _onchange_patient_doctor




# ----------------------------------------------------------- Computes  ---------------------------
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
				selection=app_vars._type_cal_list,

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
			#print()
			#print('Compute State short')
			#print(record.state)
			if record.state != False:
				record.x_state_short = app_vars._hash_state[record.state]




	# Display
	x_display = fields.Char(

			compute='_compute_x_display',
		)


	@api.multi
	#@api.depends('x_appointment')
	def _compute_x_display(self):
		for record in self:
			#print()
			#print('Compute Display')
			sep = ' '
			# Patient or Event
			record.x_display = record.x_patient_name_short + sep  + record.x_doctor_code + sep +\
																					record.x_type_cal + sep + record.x_state_short + sep + \
																					app_vars._h_subtype[record.x_subtype]








# ----------------------------------------------------------- Confirm  ----------------------------
	# Confirm
	@api.multi
	def confirm(self):
		"""
		high level support for doing this and that.
		"""
		#print
		#print 'Confirm'


		# Only for Controls
		if self.x_type in ['control', 'session']:

			# Get Next Slot - Real Time version
			appointment_date = lib.get_next_slot(self)						# Next Slot


			# Init
			duration = self.duration
			x_type = self.x_type
			doctor_name = self.doctor.name
			states = ['pre_scheduled', 'Scheduled']


			# Check and Push
			#appointment_date_str = user.check_and_push(self, appointment_date, duration, x_type,\
			#			 																	doctor_name, states)
			appointment_date_str = user.check_and_push(self, appointment_date, duration, doctor_name, states)


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
		"""
		high level support for doing this and that.
		"""
		#print
		#print 'Un Confirm'
		self.state = 'pre_scheduled'
		self.treatment.update()





# ----------------------------------------------------------- On Change - Bug ! -------------------

	#@api.onchange('state')
	#def _onchange_state(self):
	#	print
	#	print 'On change - State'
		# Confirm if Control or Session
	#	if 	(self.state in ['Scheduled', 'pre_scheduled']) and (self.x_type in ['control', 'session']):
	#		self.confirm()





# ----------------------------------------------------------- Remove Myself  ----------------------
	# Remove Myself
	@api.multi
	def remove_myself(self):
		"""
		high level support for doing this and that.
		"""
		appointment_id = self.id
		rec_set = self.env['oeh.medical.appointment'].browse([appointment_id])
		ret = rec_set.unlink()



#----------------------------------------------------------- Hot Button - For Treatment -----------
	# For Treatments Quick access
	@api.multi
	def open_line_current(self):
		"""
		high level support for doing this and that.
		"""
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



# ----------------------------------------------------------- CRUD --------------------------------
	# Create
	@api.model
	def create(self, vals):
		"""
		high level support for doing this and that.
		"""
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







# ----------------------------------------------------------- Check and Pull ----------------------

	# Check and pull
	@api.multi
	def check_and_pull(self):
		"""
		Check and pull. Using the User lib.
		"""
		print()
		print('Check and Pull')


		# Init
		appointment_date = self.appointment_date

		#duration = -self.duration  		# Here !
		duration = -0.25  		# Here !

		x_type = self.x_type
		doctor_name = self.doctor.name
		states = ['pre_scheduled', 'Scheduled']

		appointment_date_str = user.check_and_push(self, appointment_date, duration, doctor_name, states)

		self.appointment_date = appointment_date_str

		return appointment_date_str



# ----------------------------------------------------------- Check and Push ----------------------

	# Check and Push
	@api.multi
	def check_and_push(self):
		"""
		Check and Push. Using the User lib.
		"""
		print()
		print('Check and Push')

		# Init
		#appointment_date = lib.get_next_slot(self)						# Get Next Slot - Real Time version
		appointment_date = self.appointment_date

		#duration = self.duration
		duration = 0.25  		# Here !

		x_type = self.x_type
		doctor_name = self.doctor.name
		states = ['pre_scheduled', 'Scheduled']

		appointment_date_str = user.check_and_push(self, appointment_date, duration, doctor_name, states)

		#print(appointment_date_str)

		self.appointment_date = appointment_date_str

		return appointment_date_str





# ----------------------------------------------------------- Push --------------------------------

	# Move
	@api.multi
	def move(self, delta_min):
		"""
		Push.
		"""
		print()
		print('Move')

		#date_format = "%Y-%m-%d"
		#new = datetime.datetime.now() + datetime.timedelta(hours=-5, minutes=0)
		#new_dt = datetime.datetime.strptime(self.appointment_date, date_format)

		date_format = "%Y-%m-%d %H:%M:%S"

		#new_dt = datetime.datetime.strptime(self.appointment_date, date_format) + datetime.timedelta(hours=0, minutes=15)
		new_dt = datetime.datetime.strptime(self.appointment_date, date_format) + datetime.timedelta(hours=0, minutes=delta_min)

		new_str = new_dt.strftime(date_format)

		print(new_dt)

		print(new_str)

		return new_str



	# Push
	@api.multi
	def push(self):
		"""
		Push.
		"""
		print()
		print('Push')

		delta_min = 15

		new_str = self.move(delta_min)

		self.appointment_date = new_str

		print(self.appointment_date)



	# Pull
	@api.multi
	def pull(self):
		"""
		Pull.
		"""
		print()
		print('Pull')

		delta_min = -15

		new_str = self.move(delta_min)

		self.appointment_date = new_str

		print(self.appointment_date)





# ----------------------------------------------------------- Automatic ------------------------------

	# Check and Push Consultation Auto
	@api.multi
	def check_and_push_consultation_auto(self, doctor, duration, treatment_id):
		"""
		Check and Push. Using the User lib.
		"""
		print()
		print('Check and Push Consultation - Auto')

		print('other')

		appointment_date = lib.get_next_slot(self)			# Get Next Slot - Real Time version
		
		print(appointment_date)

		doctor_name = doctor.name
		states = ['pre_scheduled', 'Scheduled']
			
		appointment_date_str = user.check_and_push(self, appointment_date, duration, doctor_name, states)

		print(appointment_date_str)

		return appointment_date_str







# ----------------------------------------------------------- Automatic ------------------------------

	# Check and Push Auto
	@api.multi
	def check_and_push_auto(self, doctor, duration, treatment_id):
		"""
		Check and Push. Using the User lib.
		"""
		print()
		print('Check and Push Auto')


		# Search
		control = self.env['openhealth.control'].search([
																('treatment', '=', treatment_id),
																('appointment', 'in', [False]),
													],
																order='control_date asc',
																limit=1,
												)
		print(control)


		# Check next Control without an App
		if control.name not in [False]:
			print('control')

			date_format = "%Y-%m-%d %H:%M:%S"
			date_dt = datetime.datetime.strptime(control.control_date, date_format) + datetime.timedelta(hours=-5, minutes=0)
			appointment_date_str = date_dt.strftime(date_format)


		# Check Dr availability
		else:
			print('other')

			appointment_date = lib.get_next_slot(self)			# Get Next Slot - Real Time version
			print(appointment_date)

			doctor_name = doctor.name
			states = ['pre_scheduled', 'Scheduled']
			
			appointment_date_str = user.check_and_push(self, appointment_date, duration, doctor_name, states)


		print(appointment_date_str)

		return appointment_date_str




	# Get Day
	@api.multi
	def get_day(self):
		"""
		Check and Push. Using the User lib.
		"""
		print()
		print('Get Day')
		print()

		date_format = "%Y-%m-%d"
		now = datetime.datetime.now() + datetime.timedelta(hours=-5, minutes=0)
		now_date_str = now.strftime(date_format)

		day = now_date_str.split('-')[2]

		print(day)

		return day


	# Get Month
	@api.multi
	def get_month(self):
		"""
		Check and Push. Using the User lib.
		"""
		print()
		print('Get Month')
		print()

		date_format = "%Y-%m-%d"
		now = datetime.datetime.now() + datetime.timedelta(hours=-5, minutes=0)
		now_date_str = now.strftime(date_format)
		month = now_date_str.split('-')[1]

		print(month)
		return month


	# Get year
	@api.multi
	def get_year(self):
		"""
		Check and Push. Using the User lib.
		"""
		print()
		print('Get Year')
		date_format = "%Y-%m-%d"
		now = datetime.datetime.now() + datetime.timedelta(hours=-5, minutes=0)
		now_date_str = now.strftime(date_format)
		year = now_date_str.split('-')[0]

		print(year)
		return year


	# Get Time
	@api.multi
	def get_time(self):
		"""
		Check and Push. Using the User lib.
		"""
		print()
		print('Get Time')
		#date_format = "%Y-%m-%d"
		#date_format = "%Y-%m-%d %H:%M:%S"
		date_format = "%H:%M:%S"

		#now = datetime.datetime.now() + datetime.timedelta(hours=-5, minutes=0)
		now = datetime.datetime.now() + datetime.timedelta(hours=0, minutes=0)

		#now_date_str = now.strftime(date_format)
		#time = now_date_str

		time = now

		return time





	# Action Create
	@api.model
	def update_action_create(self):
		"""
		Update Action Create
		"""
		print()
		print('Update Action Create')

		appointment_date_str = self.check_and_push()
		print(appointment_date_str)

		#self.appointment_date = appointment_date_str

		# Search
		appointment = self.env['oeh.medical.appointment'].search([
																		('id', '=', self.id),
																	],
																	#order='appointment_date desc',
																	limit=1
																)
		print(appointment)

		appointment.appointment_date = appointment_date_str

		#self.update_date_tags()






# ----------------------------------------------------------- Update ------------------------------

	# Update Date Tags
	@api.multi
	def update_date_tags(self):
		"""
		Date Tags: Time, Day, Month and Year.
		"""
		print()
		print('Update Day Month Year')

		date_format = "%d"
		self.x_day = lib.get_date_with_format(date_format, self.appointment_date)

		date_format = "%m"
		self.x_month = lib.get_date_with_format(date_format, self.appointment_date)

		date_format = "%Y"
		self.x_year = lib.get_date_with_format(date_format, self.appointment_date)

		self.x_time = self.appointment_date



	# Update Id Doc
	@api.multi
	def update_id_doc(self):
		"""
		Update Action Create
		"""
		print()
		print('Update Id Doc')

		#self.x_id_doc = patient.x_id_doc
		#self.x_id_doc_type = patient.x_id_doc_type




	# Update Day Month Year - All
	@api.multi
	def update_all(self):
		"""
		high level support for doing this and that.
		"""
		print()
		print('Update All')

		# Configurator
		configurator = self.env['openhealth.configurator'].search([
																	('name', 'in', ['appointment']),
															],
																	order='date_begin,name asc',
																	limit=1,
														)
		print(configurator)
		print(configurator.name)
		if configurator.name not in [False, '']:
			date_begin = configurator.date_begin
			date_end = configurator.date_end



		# Search Apps
		apps = self.env['oeh.medical.appointment'].search([
																('appointment_date', '>=', date_begin),
																('appointment_date', '<=', date_end),
													],
																order='appointment_date desc',
																#limit=1000,
												)
		# Update
		for app in apps:
			print(app.appointment_date)
			#if app.x_day in [False] and app.x_month in [False]:
			app.update_date_tags()
			#app.update_id_doc()




# ------------------------------------------ Automatic - Get Control, Consultation and Procedure --

	# Get Control Auto
	@api.multi
	def get_control_auto(self, x_type, treatment_id, appointment_id):
		"""
		Get Control Auto 
		"""
		print()
		print('Get Control Auto')
		print(x_type)
		print(treatment_id)
		print(appointment_id)

		# Search
		control = self.env['openhealth.control'].search([
																('treatment', '=', treatment_id),
																('appointment', 'in', [False]),
													],
																order='control_date asc',
																limit=1,
												)
		print(control)

		#if control.name not in [False]:
		if (x_type in ['control']) and (control.name not in [False]):
			control_id = control.id  
			control.appointment = appointment_id
		else:
			control_id = False

		print(control_id)

		return control_id




	# Get consultation Auto
	@api.multi
	def get_consultation_auto(self, x_type, treatment_id, appointment_id):
		"""
		Get consultation Auto 
		"""
		print()
		print('Get consultation Auto')
		print(x_type)
		print(treatment_id)
		print(appointment_id)

		# Search
		consultation = self.env['openhealth.consultation'].search([
																	('treatment', '=', treatment_id),
																	('appointment', 'in', [False]),
													],
																	order='evaluation_start_date asc',
																	limit=1,
												)
		print(consultation)

		#if consultation.name not in [False]:
		if (x_type in ['consultation']) and (consultation.name not in [False]):
			consultation_id = consultation.id  
			consultation.appointment = appointment_id
		else:
			consultation_id = False

		print(consultation_id)

		return consultation_id



	# Get procedure Auto
	@api.multi
	def get_procedure_auto(self, x_type, treatment_id, appointment_id):
		"""
		Get procedure Auto 
		"""
		print()
		print('Get procedure Auto')
		print(x_type)
		print(treatment_id)
		print(appointment_id)

		# Search
		procedure = self.env['openhealth.procedure'].search([
																	('treatment', '=', treatment_id),
																	('appointment', 'in', [False]),
													],
																	order='evaluation_start_date asc',
																	limit=1,
												)
		print(procedure)

		#if procedure.name not in [False]:
		if (x_type in ['procedure']) and (procedure.name not in [False]):
			procedure_id = procedure.id  
			procedure.appointment = appointment_id
		else:
			procedure_id = False

		print(procedure_id)

		return procedure_id




# ----------------------------------------------------------- Automatic - Control Date Synchro ----

	# Is Today Auto
	@api.multi
	def is_today_auto(self, appointment_date):
		"""
		Check and Push. Using the User lib.
		"""
		print()
		print('Is Today Auto')
		
		print(appointment_date)
		
		is_today = lib.is_today(appointment_date)

		print(is_today)
		
		return is_today





	# Get Control Date Auto
	@api.multi
	def get_control_date_auto(self, x_type, appointment_date):
		"""
		Check and Push. Using the User lib.
		"""
		print()
		print('Get Control Date Auto')
		print(x_type)
		print(appointment_date)
		if x_type in ['control']:
			control_date = appointment_date
		else:
			control_date = False
		return control_date









# ----------------------------------------------------------- Update ------------------------------

	# Create All Control
	@api.multi
	def create_all_control(self):
		"""
		Check and Push. Using the User lib.
		"""
		print()
		print('Create All Control')


		# Search
		controls = self.env['openhealth.control'].search([
																('treatment', '=', self.treatment.id),
																('appointment', 'in', [False]),
													],
																order='control_date asc',
																#limit=1,
												)

		#for k in range(1):
		for control in controls:

			print(control)

			control_id = control.id
			treatment_id = self.treatment.id

			control_date = control.control_date
			print(control_date)

			# Create
			app = self.env['oeh.medical.appointment'].create({
																#'appointment_date': control.control_date,

																'patient': self.patient.id,
																'doctor': self.doctor.id,
																'x_type': self.x_type,
																'x_subtype': self.x_subtype,

																'control': control_id,
																'treatment': treatment_id,
															})
			print(app)

			# Update
			app.appointment_date = control_date

			control.appointment = app.id





# ----------------------------------------------------------- On Change ---------------------------

	# Treatment
	@api.onchange('treatment')
	def _onchange_treatment(self):
		print('')
		print('On change Treatment')

		print(self.treatment)
		print(self.patient.name)
		print(self.doctor.name)

		if self.treatment.name != False:

			return {	'domain': {'control': [
												('treatment', '=', self.treatment.id),
												#('patient', '=', self.patient.name),
												#('physician', '=', self.doctor.name),
									]},
				}
