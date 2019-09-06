# 6 Sep 2019
# Duplication !

	x_test_scenario = fields.Selection(
			[
				('co2', 'Co2'),
				('exc', 'Exc'),
				('quick', 'Quick'),
				('ipl', 'Ipl'),
				('ndyag', 'Ndyag'),

				('all', 'All'),
			],
			string="Scenarios",
		)







# 27 Aug 2019
# Appointment is Highly Deprecated !
#




# ----------------------------------------------------------- Create Appointment  -----------------

	# Create Appointment Consultation
	@api.multi
	def create_appointment_consultation(self):

		# Consultation
		x_type = 'consultation'
		subtype = 'consultation'
		state = 'pre_scheduled'

		self.create_appointment_nex(x_type, subtype, state)

	# create_appointment_consultation




	# Create Appointment Nex
	@api.multi
	#def create_appointment_nex(self):
	def create_appointment_nex(self, x_type, subtype, state):
		#print
		#print 'Create Appointment'


		# Init
		doctor_name = self.physician.name



		# Consultation, Procedure
		if x_type in ['consultation', 'procedure']: 	# Appointment is Today. With time. So check for availability.


			# Get Next Slot - Real Time version
			appointment_date = lib.get_next_slot(self)						# Get Next Slot
			#print appointment_date


			if appointment_date != False:


				# Init
				states = False
				duration = 0.5



				# Check and Push
				#appointment_date_str = procedure_funcs.check_and_push(self, appointment_date, duration, x_type, doctor_name, states)
				#appointment_date_str = user.check_and_push(self, appointment_date, duration, x_type, doctor_name, states)
				appointment_date_str = user.check_and_push(self, appointment_date, duration, doctor_name, states)
				#print appointment_date_str



				# Create
				#print 'Create'
				#appointment = self.env['oeh.medical.appointment'].create({
				appointment = self.appointment_ids.create({
																			'appointment_date': appointment_date_str,
																			'patient':			self.patient.id,
																			'doctor':			self.physician.id,

																			#'state': 			'pre_scheduled',
																			#'x_type': 			'consultation',
																			#'x_subtype': 		'consultation',

																			'state': 			state,
																			'x_type': 			x_type,
																			'x_subtype': 		subtype,

																			'treatment':	self.id,
																	})
				#print appointment



		# Session, Control
		else: 	# Appointment is not Today. Without time.

			#print 'Appointment not Today'


			# Init
			if x_type == 'control':
				duration = 0.25
				state = 'pre_scheduled_control'
				states = ['pre_scheduled_control']
			else:
				duration = 0.5
				state = 'pre_scheduled_session'
				states = ['pre_scheduled_session']
				#state = 'pre_scheduled_control'
				#states = ['pre_scheduled_control']




			# Control
			nr_days = 0
			#nr_days = 1


			#start_date = self.start_date
			start_date = datetime.datetime.now() + datetime.timedelta(hours=-5, minutes=0)
			#date_2_format = "%Y-%m-%d"
			date_format = "%Y-%m-%d %H:%M:%S"
			start_date_str = start_date.strftime(date_format)




			# Control date
			#appointment_date = procedure_funcs.get_next_date(self, start_date_str, nr_days)
			appointment_date = lib.get_next_date(self, start_date_str, nr_days)

			#print appointment_date


			# Cut Time out
			appointment_date_str = appointment_date.strftime("%Y-%m-%d")
			appointment_date_str = appointment_date_str + ' 14:00:00'			# 09:00:00
			#print appointment_date_str



			# Check and Push
			#appointment_date_str = procedure_funcs.check_and_push(self, appointment_date_str, duration, x_type, doctor_name, states)
			#appointment_date_str = user.check_and_push(self, appointment_date_str, duration, x_type, doctor_name, states)
			appointment_date_str = user.check_and_push(self, appointment_date_str, duration, doctor_name, states)



			# Create
			appointment = self.env['oeh.medical.appointment'].create({
																			'appointment_date': appointment_date_str,
																			'patient':			self.patient.id,
																			'doctor':			self.physician.id,
																			'duration': duration,

																			#'x_create_procedure_automatic': False,
																			#'x_chief_complaint': chief_complaint,
																			#'x_target': 'doctor',

																			'state': state,
																			'x_type': x_type,
																			'x_subtype': subtype,

																			'treatment':	self.id,
																	})
	# create_appointment_nex





# ----------------------------------------------------------- Update Apps  ------------------------

	# Update Appointments
	@api.multi
	def update_appointments(self):

		#print
		#print 'Update Appointments'

		# Consultations
		for consultation in self.consultation_ids:
			if consultation.appointment.appointment_date != False: 
				consultation.evaluation_start_date = consultation.appointment.appointment_date

		# Sessions
		for session in self.session_ids:
			if session.appointment.appointment_date != False:
				session.evaluation_start_date = session.appointment.appointment_date

	# update_appointments
