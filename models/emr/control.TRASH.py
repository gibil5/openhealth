# 19 Sep 2019

# ----------------------------------------------------------- Redefined ------------------------------------------------------

	# Done
	#x_done = fields.Boolean(
			#string="Realizado", 			
	#		string="R", 			
	#		default=False,
	#		readonly=True, 
	#	)




# Deps

# ----------------------------------------------------------- Dates - Dep ------------------------------------------------------

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




# ----------------------------------------------------------- Nr Days ------------------------------------------------------

# Deps
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




# Deps
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





# Deps

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





# Deps

	@api.multi
	#@api.depends('state')
	def _compute_evaluation_start_date_nex(self):
		#print
		#print 'Compute - Eval Start Date'
		for record in self:
			record.evaluation_start_date = record.appointment.appointment_date





# Clean up

#----------------------------------------------------------- Deprecated ------------------------------------------------------------

	# Appointment 
	#appointment = fields.Many2one(
	#		'oeh.medical.appointment',
	#		'Cita', 
	#		required=False, 
	#	)


	# State Appointment 
	#state_app = fields.Selection(
	#		selection = app_vars._state_list, 
	#		string = 'Estado Cita', 

	#		compute='_compute_state_app', 
	#	)
	
	#@api.multi
	#@api.depends('state')
	#def _compute_state_app(self):
	#	for record in self:		
	#		record.state_app = record.appointment.state





# 27 Aug 2019
# Appointment is Highly Deprecated !
#



# ----------------------------------------------------------- Open App ------------------------------------------------------

	# Open Appointment 
	@api.multi
	def open_appointment(self):  

		owner_id = self.id 
		owner_type = self.owner_type
		patient_id = self.patient.id
		doctor_id = self.doctor.id
		treatment_id = self.procedure.treatment.id 

		GMT = time_funcs.Zone(0,False,'GMT')
		appointment_date = datetime.datetime.now(GMT).strftime("%Y-%m-%d %H:%M:%S")

		return {
				'type': 'ir.actions.act_window',
				'name': ' New Appointment', 
				'view_type': 'form',	
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

















# ----------------------------------------------------------- Deprecated ------------------------------------------------------
	#@api.onchange('appointment')
	#def _onchange_appointment(self):
	#	print 
	#	print 'On Change - Appointment'
		#self.control_date = self.appointment.appointment_date



# ----------------------------------------------------------- CRUD ------------------------------------------------------

	#@api.multi
	#def unlink(self):
		#print 
		#print 'Unlink - Override'
		#print self.appointment
		#self.appointment.unlink() 
		#print 
	#	return models.Model.unlink(self)
