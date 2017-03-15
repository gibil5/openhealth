

# 24 nov 2016


	# On change
	@api.onchange('appointment_date')
	def _onchange_appointment_date(self):

		print 
		print 
		print 'on change appointment date'

		date_format = "%Y-%m-%d"
				
		delta = datetime.timedelta(hours=1)
		#delta = datetime.timedelta(weeks=1)
		print delta



		to = datetime.datetime.today()
		print to

		#sd = datetime.datetime.strptime(self.appointment_date, date_format)
		#print sd



		#nex = delta + sd 
		#print nex 

		#record.appointment_end = delta + sd

		print
		print 



	# Compute
	#@api.multi
	@api.depends('appointment_date')
	
	def _compute_appointment_end(self):

		print
		print 'compute appointment end'

		for record in self:

			if record.appointment_date != False: 
				#record.appointment_end = record.appointment_date + record.duration 


				date_format = "%Y-%m-%d"
				
				#delta = datetime.timedelta(hours=1)
				delta = datetime.timedelta(weeks=1)

				#to = datetime.datetime.today()

				sd = datetime.datetime.strptime(record.appointment_date, date_format)
				print sd
				
				#record.appointment_end = delta + sd

		print 




# 26 nov 2016
	# Doctor id 
	x_doctor_id = fields.Integer(
			#default=2,

			compute="_compute_x_doctor_id",
		)

	#@api.multi
	@api.depends('doctor')
	def _compute_x_doctor_id(self):
		for record in self:	
			record.x_doctor_id = record.doctor.id






			#ad = datetime.datetime.strptime(self.appointment_date, date_format)
			#ad = datetime.datetime.strptime(self.x_date, date_format)
			#ad = datetime.datetime.strptime(date_format)
			#ad = datetime.datetime.strptime(dt, date_format)
			#print ad 

			#a = self.env['oeh.medical.appointment'].search([('appointment_date', 'like', '26')])
			#a = self.env['oeh.medical.appointment'].search([('appointment_date', 'like', '2016-11-26')])

			#a = self.env['oeh.medical.appointment'].search([('appointment_date', 'like', '16-11-26')])

			#a = self.env['oeh.medical.appointment'].search([('appointment_date', 'like', dt)])
			#a = self.env['oeh.medical.appointment'].search([('appointment_date', 'like', dt),  ('doctor_id', '=', '1')  ])
			#a = self.env['oeh.medical.appointment'].search([('appointment_date', 'like', dt),  ('doctor_id', '=', doctor_id)  ])




			
			#a = self.env['oeh.medical.appointment'].search([('appointment_date', 'like', ad)])
			#a = self.env['oeh.medical.appointment'].search([('appointment_date', 'like', fields.Date.today)])

			#b = self.env['oeh.medical.appointment'].search([('x_date', 'like', '26')])
			#b = self.env['oeh.medical.appointment'].search([('x_date', '=', '2016-11-26')])
			#b = self.env['oeh.medical.appointment'].search([('x_date', 'like', '2016-11-26')])




		dt = vals['appointment_date'][:10]

		
		print dt
		#doctor_id = vals['x_doctor_id']
		#print doctor_id

		#a = self.env['oeh.medical.appointment'].search([('appointment_date', 'like', dt),  ('doctor_id', '=', doctor_id)  ])
		a = self.env['oeh.medical.appointment'].search([('appointment_date', 'like', dt),  ('x_doctor_id', '=', '1')  ])

		print a 
		print 



# 27 nov 2016

	#@api.multi
	#@api.model
	#def write(self,vals):

		#print 
		#print 'jx Write - Override'
		#print
		
		#res = super(Appointment, self).write(vals)

		#return res









# 27 Feb 2017

				# Treatment 
				#treatment = self.env['openhealth.treatment'].search([
				#											('patient', 'like', self.patient.name),
				#											('physician', 'like', self.doctor.name),
				#											],
				#											order='start_date desc',
				#											limit=1,
				#										)
				#print treatment 

				#if treatment.name == False:
				#	print 'Gotcha !!!'
				#	treatment = self.env['openhealth.treatment'].search([
				#											('patient', 'like', self.patient.name),
				#											],
				#											order='start_date desc',
				#											limit=1,
				#										)
				#	print treatment
				#self.treatment = treatment


			# Create Procedure 
			#if self.x_error == 0:
			#	print 
			#	print 'Create Appointment for procedure !'
			#	app = self.create_app_procedure()
			#	print app 


			







# 7 Mar 2017
# ----------------------------------------------------------- Search Machine Button ------------------------------------------------------

	@api.multi

	def search_machine_button(self):

		print 
		date_format = "%Y-%m-%d %H:%M:%S"
		adate_con = datetime.datetime.strptime(self.appointment_date, date_format)
		delta_fix = datetime.timedelta(hours=0)			
		adate_base = adate_con + delta_fix


		# Unlink Old 
		rec_set = self.env['oeh.medical.appointment'].search([
																('appointment_date', 'like', self.appointment_date), 
																('doctor', '=', self.doctor.name), 
																('patient', '=', self.patient.name), 
																#('x_machine', '=', self.x_machine),
																('x_target', '=', 'machine'), 

															])
		ret = rec_set.unlink()
		print "ret: ", ret


		# Create Proc 
		doctor_id = self.doctor.id
		patient_id = self.patient.id
		treatment_id = self.treatment.id
		x_create_procedure_automatic = True

		flag_machine = True 
		
		
		#app = appfuncs.create_app_procedure(self, appointment_date, doctor_id, patient_id, treatment_id, x_create_procedure_automatic, flag_machine)
		app = appfuncs.create_app_procedure(self, adate_base, doctor_id, patient_id, treatment_id, x_create_procedure_automatic, flag_machine)


		self.appointment_date = app.appointment_date
		self.x_machine = app.x_machine

		print app

	# search_machine_button






#	x_therapist = fields.Many2one(
#			'openhealth.therapist',
#			string = "Cosmeatra", 	
#			default=defaults._therapist,
			#required=True, 
#			required=False, 
#			readonly = False, 
#			)






