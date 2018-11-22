

# 02 Feb 2018


		#date_format = "%Y-%m-%d %H:%M:%S"
		#app_date = datetime.strptime(self.evaluation_start_date, date_format).strftime("%Y-%m-%d ")
		#app_date = self.evaluation_start_date
		
		#print GMT
		#print evaluation_start_date 
		#print app_date
		#print 
		#print 
		


# Clean Appointments 
		#print 
		#print 'Clean Appointments'

		#rec_set = self.env['oeh.medical.appointment'].search([
																#('procedure', '=', self.id), 	
																#('procedure_cos', '=', self.id), 
		#														(self.key, '=', self.id), 
		#													])
		#ret = rec_set.unlink()
		#print "ret: ", ret


		#therapist_name = self.therapist.name 




		#print 
		#print 'Clean Sessions'

		#rec_set = self.env['openhealth.session.cos'].search([
		#rec_set = self.env[self.model].search([

		#print "ret: ", ret




				#print 'appointment_date: ', appointment_date
																		#'procedure_cos': self.id,




			# Create Session 
			#print 'Create Session'
			#print session_date
			#print patient_id
			#print doctor_id
			#print evaluation_type
			#print 
			#print product_id
			#print laser
			#print appointment_id
			#print 
			#print treatment_id
			#print cosmetology_id
			#print chief_complaint
			#print 
			#print procedure_id

			#session = self.env['openhealth.session.cos'].create(
			#session = self.env[self.model].create(




			# Update - Deprecated - For Cos 
			#ret = jrfuncs.update_appointment_go(self, appointment_id, session_id, 'session')

			#print appointment
			#print appointment.session
			#print appointment.session.id
			#print 
			#print 
			#print 




# 22 Jun 2018 


# Create Controls 
@api.multi
def create_controls_go(self):

	...


	# Clean Appointments 
	#print 
	#print 'Clean Appointments'

	#rec_set = self.env['oeh.medical.appointment'].search([
																#('procedure', '=', self.id), 	
																#('procedure_cos', '=', self.id), 
	#														(self.key, '=', self.id), 
	#													])
	#ret = rec_set.unlink()
	#print "ret: ", ret





#------------------------------------------------ Create Appointment  ---------------------------------------------------

#@api.multi
#def create_appointment_control(self, appointment_date, duration, x_type, state, chief_complaint, patient_id, doctor_id, treatment_id):
#	x_create_procedure_automatic = False 
#	appointment = self.env['oeh.medical.appointment'].create({
#																'appointment_date': appointment_date,
#																'patient': patient_id,	
#																'doctor': doctor_id,
#																'duration': duration,
#																'state': state,
#																'x_type': x_type,
#																'x_chief_complaint': chief_complaint, 
#																'x_create_procedure_automatic': x_create_procedure_automatic,
#																'x_target': 'doctor',
#																'treatment': treatment_id, 
#															})
#	return appointment











