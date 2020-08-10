# -*- coding: utf-8 -*-
"""
	Procedure
	Created: 				 1 Nov 2016
	Last updated: 	 	 	09 Aug 2020
"""
from openerp import models, fields, api
from . import pro_con_funcs
from . import pro_ses_funcs

class Procedure(models.Model):
	"""
	Procedure class
	Used by -
	"""
	_name = 'openhealth.procedure'
	_inherit = 'oeh.medical.evaluation'
	_description = 'Procedure'
	#_order = 'write_date desc'


# ---------------------------------------------------- Create controls ---------
	# Create Controls
	@api.multi
	def create_controls(self):
		"""
		Create controls
		"""
		# Init
		if self.configurator.name != False:
			if self.laser in ['laser_co2']:
				nr_controls = self.configurator.nr_controls_co2
			elif self.laser in ['laser_quick']:
				nr_controls = self.configurator.nr_controls_quick
			elif self.laser in ['laser_exc']:
				nr_controls = self.configurator.nr_controls_exc
			elif self.laser in ['laser_ipl']:
				nr_controls = self.configurator.nr_controls_ipl
			elif self.laser in ['laser_ndyag']:
				nr_controls = self.configurator.nr_controls_ndyag
			else:
				nr_controls = 0
		else:
			nr_controls = 0

		self.number_controls = nr_controls

		nr_ctl_created = self.env['openhealth.control'].search_count([
																		('procedure', '=', self.id),
																	])
		# Create
		ret = pro_con_funcs.create_controls(self, nr_controls, nr_ctl_created)

	# create_controls


# --------------------------------------------------------- Create sessions ----
	# Create Sessions
	@api.multi
	def create_sessions(self):
		"""
		Create sessions
		"""
		# Init
		if self.configurator.name != False:
			if self.laser in ['laser_co2']:
				nr_sessions = self.configurator.nr_sessions_co2
			elif self.laser in ['laser_quick']:
				nr_sessions = self.configurator.nr_sessions_quick
			elif self.laser in ['laser_exc']:
				nr_sessions = self.configurator.nr_sessions_exc
			elif self.laser in ['laser_ipl']:
				nr_sessions = self.configurator.nr_sessions_ipl
			elif self.laser in ['laser_ndyag']:
				nr_sessions = self.configurator.nr_sessions_ndyag
			else:
				nr_sessions = 0
		else:
			nr_sessions = 0

		self.number_sessions = nr_sessions

		nr_ses_created = self.env['openhealth.session.med'].search_count([
																			('procedure', '=', self.id),
																	])
		# Create
		ret = pro_ses_funcs.create_sessions(self, nr_sessions, nr_ses_created)

	# create_sessions



# ----------------------------------------------------------- Creates control Man -------------------------
	# Create Controls Manual
	@api.multi
	def create_controls_manual(self):
		"""
		Create controls man
		"""
		#print()
		#print('Create Controls Manual')
		nr_controls = 1
		nr_ctl_created = self.env['openhealth.control'].search_count([
																		('procedure', '=', self.id),
																	])
		# Create
		ret = pro_con_funcs.create_controls(self, nr_controls, nr_ctl_created)



# ----------------------------------------------------------- Creates sessions Man -------------------------
	# Create Sessions Manual
	@api.multi
	def create_sessions_manual(self):
		"""
		Create sessions man
		"""
		#print()
		#print('Create Sessions Manual')
		nr_sessions = 1
		nr_ses_created = self.env['openhealth.session.med'].search_count([
																			('procedure', '=', self.id),
																	])
		# Create
		ret = pro_ses_funcs.create_sessions(self, nr_sessions, nr_ses_created)



# ----------------------------------------------------------- PL -----------------------------
	pl_laser = fields.Char()


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
	#@api.depends('state')
	def _compute_session_date(self):
		for record in self:
			first = True
			for session in record.session_ids:
				if first:
					record.session_date = session.evaluation_start_date
					first = False

# --------------------------------------------------------- Redefinition -------
	# Default - HC Number
	@api.model
	def _get_default_id_code(self):
		#print
		#print 'Get Default App - 2'
		patient = self.treatment.patient
		doctor = self.treatment.physician
 		app = self.env['oeh.medical.appointment'].search([
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
 		app = self.env['oeh.medical.appointment'].search([
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
		#print
		#print 'Update Appointment'
		patient = self.patient
		doctor = self.doctor
		x_type = 'procedure'
 		app = self.env['oeh.medical.appointment'].search([
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
