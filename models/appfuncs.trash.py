

# 7 Mar 2017

					#if flag_machine:			# Create Appointment - Machine 
						
						#app = self.env['oeh.medical.appointment'].create(
						#											{
						#												'appointment_date': adate_pro_str,
						#												'doctor': 		doctor_id,
						#												'patient': 		patient_id,	
						#												'treatment': 	treatment_id, 
						#												'duration': 	duration,
						#												'x_type': 		'procedure',
						#												'x_create_procedure_automatic': False, 
						#												'x_machine': 	x_machine,

						#	                    						'x_target': 	'machine',
						#											}
						#										)

						

					#else:
					


# 8 Mar 2017


		# Search for the rec set
		#if x_machine == False:
		#	app_ids = self.env['oeh.medical.appointment'].search([
		#															('doctor', '=', doctor_name), 
		#															('appointment_date', 'like', dt), 
		#															('x_machine', '=', x_machine),
		#														])
		#else:
		#	app_ids = self.env['oeh.medical.appointment'].search([
		#															('appointment_date', 'like', dt), 
		#															('x_machine', '=', x_machine)  
		#														])
