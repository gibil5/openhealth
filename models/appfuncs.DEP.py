

# 14 Aug 2018

	slots = [
				'09:00:00', 
				'09:15:00', 
				'09:30:00', 
				'09:45:00', 

				'10:00:00', 
				'10:15:00', 
				'10:30:00', 
				'10:45:00', 

				'11:00:00', 
				'11:15:00', 
				'11:30:00', 
				'11:45:00', 

				'12:00:00', 
				'12:15:00', 
				'12:30:00', 
				'12:45:00', 

				'13:00:00', 
				'13:15:00', 
				'13:30:00', 
				'13:45:00', 


				'14:00:00', 
				'14:15:00', 
				'14:30:00', 
				'14:45:00', 


				'15:00:00', 
				'15:15:00', 
				'15:30:00', 
				'15:45:00', 

				'16:00:00', 
				'16:15:00', 
				'16:30:00', 
				'16:45:00', 

				'17:00:00', 
				'17:15:00', 
				'17:30:00', 
				'17:45:00', 

				'18:00:00', 
				'18:15:00', 
				'18:30:00', 
				'18:45:00', 

				'19:00:00', 
				'19:15:00', 
				'19:30:00', 
				'19:45:00', 

				'20:00:00', 
				'20:15:00', 
				'20:30:00', 
				'20:45:00', 

				'21:00:00', 
			]


# 16 Aug 2018

	# Debug 
	#debug = True
	debug = False
	if debug: 
		print now
		print now_date_str
		print app_date_str
		print app_date_dt
		#print 
		print app_limit_str
		print app_limit_dt
		#print
		print delta 
		print delta_sec
		#print 
		print flag
		print 

	return flag 

#doctor_available






# ----------------------------------------------------------- Check for Collisions  ------------------------------------------------------

# Check for Collisions
@api.multi
def check_for_collisions(self, appointment_date, doctor_name, duration, x_machine, target, x_type):

	#print 
	#print 'jx'
	#print 'Check for collision'
	#print appointment_date, doctor_name, duration, x_machine
	#print 

	# Init 
	dt = appointment_date[2:10]


	# Build the existing appointments array
	if target == 'doctor':
		app_ids = self.env['oeh.medical.appointment'].search([
																('appointment_date', 'like', dt), 
																('doctor', '=', doctor_name), 
															])
	if target == 'machine':
		app_ids = self.env['oeh.medical.appointment'].search([
																('appointment_date', 'like', dt), 
																('x_machine', '=', x_machine),
															])

	# Cosmetology  
	#if target == 'therapist':
	#	if x_type == 'consultation':
	#		app_ids = self.env['oeh.medical.appointment'].search([
	#																('appointment_date', 'like', dt), 
	#																('x_therapist', '=', doctor_name), 
	#															])
	#	else:
	#		app_ids = self.env['oeh.medical.appointment'].search([
	#																('appointment_date', 'like', dt), 
	#																('x_machine', '=', x_machine),
	#															])

	#print 'app_ids'
	#print app_ids 
	#for app in app_ids:
		#print app.name
	#print
	#print 


	# Build the Appointment end 
	date_format = "%Y-%m-%d %H:%M:%S"
	delta = datetime.timedelta(hours=duration)
	sd = datetime.datetime.strptime(appointment_date, date_format)
	ae_dt = delta + sd
	ae = ae_dt.strftime("%Y-%m-%d %H:%M:%S")


	#print delta
	#print sd 
	#print ae_dt
	#print 



	# Check if Collision 
	ad = appointment_date

	for app in app_ids:

		#print app

		start = app.appointment_date
		end = app.appointment_end


		if 	app.state != 'pre_scheduled_control' and  	(	
														(ad >= start and ae <= end)  or  (ad <= start and ae >= end)  	or    (ad < start and ae > start)  or  (ad < end and ae > end)
														): 


			#print 'Collision !!!'



			# Local
			delta = datetime.timedelta(hours=5)


			# Start 
			sd = datetime.datetime.strptime(start, date_format)
			sl =  sd - delta 
			#sl = start_local.strftime("%Y-%m-%d %H:%M:%S")
			start_local = sl.strftime("%H:%M")


			# End 
			sd = datetime.datetime.strptime(end, date_format)
			el =  sd - delta 
			end_local = el.strftime("%H:%M")


			#print delta
			#print end_local
			#print el


			# Did not pass 
			return -1, doctor_name, start_local, end_local

	# Passed test - All is Ok 
	return 0, '', '', '' 

# check_for_collisions


# ----------------------------------------------------------- Create Procedure  ------------------------------------------------------

@api.multi
def create_appointment_procedure(self, adate_base, doctor_id, patient_id, treatment_id, x_create_procedure_automatic):

	print 
	print 'Create App Procedure'
	print 'Gotcha !'

	# Print 
	#print appointment_date
	#print doctor_id
	#print patient_id
	#print adate_con


	# Init 

	# Doctor 
	doctor = self.env['oeh.medical.physician'].search([('id', '=', doctor_id)])
	doctor_name = doctor.name

	# Target
	if doctor.x_therapist:
		x_target = 'therapist'
	else:
		x_target = 'doctor'

	k = 0
	duration = 0.5 
	ret = 1

	# Deltas
	delta_var = datetime.timedelta(hours=0.25)

	# Loop 
	while not ret == 0:

		# Procedure 
		adate_pro = adate_base + k * delta_var
		adate_pro_str = adate_pro.strftime("%Y-%m-%d %H:%M:%S")


		# Check for collisions 
		ret, doctor_name, start, end = check_for_collisions(self, adate_pro_str, doctor_name, duration, False, 'doctor', 'procedure')



		if ret == 0: 					# Success - No Collisions
		
			#print 'CRUD: Create !!!'


			# Create Appointment - Doctor  
			app = self.env['oeh.medical.appointment'].create(
																{
																	'appointment_date': adate_pro_str,
																	'doctor': 		doctor_id,
																	'patient': 		patient_id,	
																	'duration': 	duration,
																	'x_type':		'procedure',
																	'x_create_procedure_automatic': x_create_procedure_automatic,
																	'state':		'pre_scheduled',
						                    						'x_target': 	x_target,
																	#'x_chief_complaint': x_chief_complaint, 

																	#'cosmetology': 	cosmetology_id, 
																	'treatment': 	treatment_id, 
														}
												)
		
		else:							# Collision - Change appointment time 
			k = k + 1


	#print 
	#print 'k'
	#print k
	#print 

	return app 

# create_app_procedure










