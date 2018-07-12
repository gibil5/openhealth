






			# Check and Push 
			appointment_date_str = procedure_funcs.check_and_push(self, appointment_date, duration, x_type, doctor_name, states)


			appointment = self.env['oeh.medical.appointment'].create({
																			'appointment_date': appointment_date_str,
																			'patient':			self.patient.id,
																			'doctor':			self.physician.id,
																			'duration': duration,
																			
																			'x_create_procedure_automatic': False,
																			
																			#'x_chief_complaint': chief_complaint, 
																			#'x_target': 'doctor',

																			'state': state,
																			'x_type': x_type,
																			'x_subtype': subtype,

																			'treatment':	self.id, 
																	})
