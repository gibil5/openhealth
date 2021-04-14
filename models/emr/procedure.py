# -*- coding: utf-8 -*-
"""
	Procedure
	Created: 			 1 Nov 2016
	Last: 	 			13 apr 2021
"""
from __future__ import print_function
from __future__ import absolute_import

from datetime import datetime
from openerp import models, fields, api

from openerp.addons.openhealth.models.commons.libs import commons_user, commons_lib

from .commons import tre_funcs as time_funcs

_model_control = "openhealth.control"
_model_session = "openhealth.session.med"
_model_app = "oeh.medical.appointment"


class Procedure(models.Model):
	"""
	Procedure class
	Used by
	"""
	_name = 'openhealth.procedure'
	_description = 'Procedure'
	_inherit = 'oeh.medical.evaluation'
	#_order = 'write_date desc'


# ----------------------------------------------------------- Creates control Man -------------------------
	# Create Controls Manual
	@api.multi
	def btn_create_controls_manual(self):
		"""
		Create controls manual
		"""
		print()
		print('oh - procedure - btn_create_controls_manual')

		nr_ctl_created = self.env[_model_control].search_count([
																		('procedure', '=', self.id),
																	])
		# Create
		nr_controls = 1
		#ret = pro_con_funcs.create_controls(self, nr_controls, nr_ctl_created)
		self.create_controls_for_me(nr_controls, nr_ctl_created)


# ---------------------------------------------------- Create controls ---------
	# Create Controls
	@api.multi
	def create_controls(self):
		"""
		Create controls
		"""
		print()
		print('oh - procedure - create_controls')

		self.number_controls = self.configurator.get_number(self.laser, 'control')

		already_created = self.env[_model_control].search_count([
																		('procedure', '=', self.id),
																	])
		# Create
		#ret = pro_con_funcs.create_controls(self, self.number_controls, already_created)
		self.create_controls_for_me(self.number_controls, already_created)

	# create_controls

# ----------------------------------------------------------- Creates sessions Man -------------------------
	# Create Sessions Manual
	@api.multi
	def btn_create_sessions_manual(self):
		"""
		Create sessions man
		"""
		print()
		print('oh - procedure - btn_create_sessions_manual')

		nr_ses_created = self.env[_model_session].search_count([
																			('procedure', '=', self.id),
																	])
		# Create
		nr_sessions = 1
		#ret = pro_ses_funcs.create_sessions(self, nr_sessions, nr_ses_created)
		self.create_sessions_for_me(nr_sessions, nr_ses_created)

# --------------------------------------------------------- Create sessions ----
	# Create Sessions
	@api.multi
	def create_sessions(self):
		"""
		Create sessions
		"""
		print()
		print('oh - procedure - create_sessions')

		self.number_sessions = self.configurator.get_number(self.laser, 'session')

		already_created = self.env[_model_session].search_count([
																			('procedure', '=', self.id),
																	])
		# Create
		#ret = pro_ses_funcs.create_sessions(self, self.nr_sessions, already_created)
		self.create_sessions_for_me(self.nr_sessions, already_created)

	# create_sessions

# ---------------------------------------------- Fields ------------------------------------------
	# Laser
	pl_laser = fields.Char(
			string="Pl Láser",

			compute='_compute_pl_laser',
		)

	#@api.multi
	@api.depends('product')
	def _compute_pl_laser(self):
		for record in self:
			record.pl_laser = record.product.pl_treatment


# ----------------------------------------------------------- Relational --------------------------
	session_ids = fields.One2many(
			'openhealth.session.med',
			'procedure',
			string="sessiones",
			)

	control_ids = fields.One2many(
			'openhealth.control',
			'procedure',
			string="Controles",
			)

	treatment = fields.Many2one(
			'openhealth.treatment',
			string="Tratamiento",
			ondelete='cascade',
			)

# ----------------------------------------------------------- Dates ------------
	# Date
	evaluation_start_date = fields.Datetime(
		string="Fecha y hora",
		default=fields.Date.today,
		required=False,
		readonly=False,
	)

	# Session Date
	session_date = fields.Datetime(
			string="Fecha Sesion",
			readonly=True,

			compute='_compute_session_date',
		)

	@api.multi
	def _compute_session_date(self):
		for record in self:
			for session in record.session_ids:
				if not record.session_date:
					record.session_date = session.evaluation_start_date

# --------------------------------------------------------- Redefinition -------
	# Default - HC Number
	@api.model
	def _get_default_id_code(self):
		#print
		#print 'Get Default App - 2'
		patient = self.treatment.patient
		doctor = self.treatment.physician
		app = self.env[_model_app].search([
																('patient', '=', patient),
																('doctor', '=', doctor),
														],
															#order='write_date desc',
															limit=1,
														)
		#print patient
		#print doctor
		#print app
		return app


	def _get_default_appointment(self):
		#print
		#print 'Get Default App'
		patient = self.patient
		doctor = self.doctor
		app = self.env[_model_app].search([
																('patient', '=', patient),
																('doctor', '=', doctor),
														],
															#order='write_date desc',
															limit=1,
														)
		#print self.patient
		#print self.doctor
		#print app
		return app
	# _get_default_appointment


	# Update App
	@api.multi
	def update_appointment(self):
		"""
		Update appointments
		"""
		patient = self.patient
		doctor = self.doctor
		x_type = 'procedure'
		app = self.env[_model_app].search([
																('patient', '=', patient.name),
																('doctor', '=', doctor.name),
																('x_type', '=', x_type),
														],
															#order='write_date desc',
															order='appointment_date desc',
															limit=1,
														)
		#print app
		self.appointment = app



# --------------------------------------------------------- Primitives ---------
	# Appointment
	appointment = fields.Many2one(
			'oeh.medical.appointment',
			string='Cita #',
			required=False,
			#ondelete='cascade',
			#default=lambda self: self._get_default_appointment(),
			#default=_get_default_id_code,
		)


	# Name
	name = fields.Char(
			string='Proc #',
		)

	# Owner
	owner_type = fields.Char(
			default='procedure',
		)

	# Redefinition
	evaluation_type = fields.Selection(
			default='Ambulatory',
			)

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


	# Sessions for the Procedure
	number_sessions = fields.Integer(
			string="Sesiones",
			compute="_compute_number_sessions",
	)

	#@api.multi
	@api.depends('product')
	def _compute_number_sessions(self):
		for record in self:
			record.number_sessions = record.product.x_sessions


	# Controls - Quantity
	number_controls = fields.Integer(
			string="Controles",
			compute="_compute_number_controls",
	)

	#@api.multi
	@api.depends('laser')
	def _compute_number_controls(self):
		for record in self:
			if record.laser != 'consultation':
				if record.laser == 'laser_co2' or record.laser == 'laser_quick':
					record.number_controls = 6
				else:
					record.number_controls = 0

# ----------------------------------------------------------- Buttons -----------------------------
	# Open Line
	@api.multi
	def open_line_current(self):
		"""
		Open line current
		"""
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
	# open_line_current

# ----------------------------------------------------------- Clears ------------------------------
	# Clear Sessions
	@api.multi
	def clear_sessions(self):
		"""
		Clear sessions
		"""
		self.session_ids.unlink()

	# Clear Controls
	@api.multi
	def clear_controls(self):
		"""
		Clear controls
		"""
		self.control_ids.unlink()


# --------------------------------------------------------- Funcs ---------------------------------

	#def get_session_date(self):
	#	first = True
	#	for session in self.session_ids:
	#		if first:
	#			session_date = session.evaluation_start_date
	#			first = False
	#	return session_date

#---------------------------------------------------------- Create Controls ----
	# Create Controls
	#def create_controls(self, nr_controls, nr_ctl_created):
	def create_controls_for_me(self, nr_controls, nr_ctl_created):
		"""
		Creates Controls for the Procedure Class.
		"""
		print()
		print('oh - pro_con_funcs - create_controls')

		# Init
		patient_id = self.patient.id
		doctor_name = self.doctor.name
		product_id = self.product.id
		chief_complaint = self.chief_complaint
		procedure_id = self.id
		treatment_id = self.treatment.id
		#subtype = self.product.x_treatment

		# Start date
		if self.session_date:
			evaluation_start_date = self.session_date
			#evaluation_start_date = self.get_session_date()
		else:
			evaluation_start_date = self.evaluation_start_date
		

		# Doctor
		doctor_id = user.get_actual_doctor_pro(self)

		# Date dictionary - Days between controls
		k_dic = {
					0 :	7,
					1 :	15,
					2 :	30,
					3 :	60,
					4 :	120,
					5 :	180,
			}

		ret = 0


		# Loop
		for k in range(nr_controls):

			# Init
			delta = 0
			nr_days = k_dic[k] + delta

			# Control date
			control_date = lib.get_next_date(self, evaluation_start_date, nr_days)
			control_date_str = control_date.strftime("%Y-%m-%d")
			control_date_str = control_date_str + ' 14:00:00'			# 09:00:00

			# Appointment
			appointment_id = False

			# Create Control
			control = self.control_ids.create({
												'control_date':control_date,
												'patient':patient_id,
												'doctor':doctor_id,
												'product':product_id,
												'chief_complaint':chief_complaint,
												'evaluation_nr': k+1,
												'procedure':procedure_id,
												'appointment': appointment_id,
												'treatment': treatment_id,
										})
		return ret

	# create_controls


#------------------------------------------------ Create Sessions ---------------------------------------------------
	@api.multi
	#def create_sessions(self, nr_sessions, nr_ses_created):
	def create_sessions_for_me(self, nr_sessions, nr_ses_created):
		"""
		Create Sessions. For Procedure.
		"""
		print()
		print('oh - pro_ses_funcs - create_sessions')

		# Init
		procedure_id = self.id
		patient_id = self.patient.id
		chief_complaint = self.chief_complaint
		evaluation_type = 'Session'
		product_id = self.product.id
		treatment_id = self.treatment.id
		laser = self.laser

		# Actual Doctor
		doctor_id = user.get_actual_doctor_pro(self)

		# Appointment
		#duration = 0.5

		#x_type = 'session'
		#subtype = self.product.x_treatment

		#doctor_name = self.doctor.name

		# Date
		gmt = time_funcs.Zone(0, False, 'GMT')
		evaluation_start_date = datetime.now(gmt).strftime("%Y-%m-%d %H:%M:%S")
		#app_date = datetime.now(GMT).strftime("%Y-%m-%d ")

		# Loop
		# Date dictionary - Number of days for controls
		#k_dic = {
					#0 :	0,
					#1 :	7,
					#2 :	15,
					#3 :	21,
					#3 :	30,
					#4 :	60,
					#5 :	120,
		#			0 : 0,
		#			1 :	1,
		#			2 :	2,
		#			3 :	3,
		#			4 :	4,
		#			5 :	5,
		#			6 :	6,
		#			7 :	7,
		#			8 :	8,
		#			9 :	9,
					#10 :	10,
					#11 :	11,
		#		}

		#for k in range(0, nr_sessions):
		for _ in range(0, nr_sessions):
			# Init
			nr_days = nr_ses_created

			# Session date
			session_date = lib.get_next_date(self, evaluation_start_date, nr_days)
			#session_date_str = session_date.strftime("%Y-%m-%d")

			# Create Session
			appointment_id = False
			self.env[_model_session].create({
																	'evaluation_start_date':session_date,
																	'patient': patient_id,
																	'doctor': doctor_id,
																	'evaluation_type':evaluation_type,
																	'product': product_id,
																	'laser': laser,
																	'chief_complaint': chief_complaint,
																	'appointment': appointment_id,
																	'procedure': procedure_id,
																	'treatment': treatment_id,
												})
		return 0

	# create_sessions_go
