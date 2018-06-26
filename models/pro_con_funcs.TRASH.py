#from . import time_funcs
#from . import procedure_funcs_cos




	# Doctor 
	#doctor_id = self.doctor.id
	doctor_id = treatment_funcs.get_actual_doctor(self)
	if doctor_id == False: 
		doctor_id = self.doctor.id 
	#print doctor_id
	#print doctor_name


	# Start date 
	#GMT = time_funcs.Zone(0,False,'GMT')	
	#evaluation_start_date = datetime.datetime.now(GMT).strftime("%Y-%m-%d %H:%M:%S")
	#evaluation_start_date = datetime.now(GMT).strftime("%Y-%m-%d %H:%M:%S")
	evaluation_start_date = self.evaluation_start_date


		#appointment = create_appointment_control(self, appointment_date_str, duration, x_type, state, chief_complaint, patient_id, doctor_id, treatment_id)


		#appointment_date_str = check_max_number(self, appointment_date, x_type, doctor_name)					# Deprecated ?


		# Prints 
		#print control 
		#print control_id
		#print appointment
		#print appointment.control
		#print appointment.control.id
		#print 





#------------------------------------------------ Check Max Nr Controls - Deprecated ? ---------------------------------------------------

# The Limit of Controls per Day, for each Doctor is 4. 
# After that, it changes the day. 
@api.multi
def	check_max_number(self, appointment_date, x_type, doctor_name):

	import datetime

	#print 
	#print 'Check Max Number'

	date_format = "%Y-%m-%d %H:%M:%S"

	appointment_date_dt = datetime.datetime.strptime(appointment_date, date_format)

	delta_var = datetime.timedelta(days=1)

	#print delta_var

	ret = 1


	while not ret == 0:

		appointment_date = appointment_date_dt.strftime("%Y-%m-%d %H:%M:%S")
		appointment_date_str = appointment_date[2:10]
		
		#print appointment_date
		#print appointment_date_str

		app_ids = self.env['oeh.medical.appointment'].search([
																('appointment_date', 'like', appointment_date_str),  
																('doctor', '=', doctor_name), 

																('x_type', '=', x_type), 

														 	])
		#print app_ids
		#print len(app_ids)


		# If more than 4, add a day 
		if len(app_ids) < 4:
			#print 'Max number check - Success !!!'
			ret = 0

		else:
			#print 'Alert. Max reached. Check next day.'
			appointment_date_dt = datetime.datetime.strptime(appointment_date, date_format)
			appointment_date_dt = appointment_date_dt + delta_var
			#print appointment_date_dt
		#print 

	return appointment_date






#------------------------------------------------ Check Push and Create ---------------------------------------------------
@api.multi
def check_and_push(self, appointment_date, duration, x_type, doctor_name):

		# Check for collisions 
		#ret, doctor_name, start, end = appfuncs.check_for_collisions(self, appointment_date_str, doctor_name, duration, False, 'doctor', x_type)

		#if ret == 0: 		# Success ! - No Collisions
		#	tra = 1 
			#print 'Collision check - Success !!!'
			#print k
		#else:				# Collision - Keep going... 
		#	k = k + 1





