

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





