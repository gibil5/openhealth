

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
