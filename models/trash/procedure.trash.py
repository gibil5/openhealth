

# 17 June 2017



# Open Appointment
	# -----------------
	@api.multi
	def open_appointment(self):  

		owner_id = self.id 
		owner_type = self.owner_type
		patient_id = self.patient.id
		doctor_id = self.doctor.id
		treatment_id = self.treatment.id 
		GMT = time_funcs.Zone(0,False,'GMT')
		appointment_date = datetime.now(GMT).strftime("%Y-%m-%d %H:%M:%S")

		return {
				'type': 'ir.actions.act_window',
				'name': ' New Appointment', 
				'view_type': 'form',
				#'view_mode': 'form',			
				'view_mode': 'calendar',			
				'target': 'current',
				'res_model': 'oeh.medical.appointment',				
				
				'flags': 	{
							#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
							'form': {'action_buttons': True, }
							},

				'context': {
							'default_consultation': owner_id,					
							'default_treatment': treatment_id,
							'default_patient': patient_id,
							'default_doctor': doctor_id,
							'default_x_type': owner_type,
							'default_appointment_date': appointment_date,
							}
				}




# 20 Jun 2017

# ----------------------------------------------------------- Create Session  ------------------------------------------------------

	@api.multi
	def create_session_one(self): 

		# Data
		procedure_id = self.id 
		patient_id = self.patient.id
		doctor_id = self.doctor.id
		chief_complaint = self.chief_complaint
		evaluation_type = 'Session'
		product_id = self.product.id
		treatment_id = self.treatment.id
		laser = self.laser
		
		# Date 		
		GMT = time_funcs.Zone(0,False,'GMT')
		evaluation_start_date = datetime.now(GMT).strftime("%Y-%m-%d %H:%M:%S")

		# Apointment 
		appointment = self.env['oeh.medical.appointment'].search([ 	
																	('patient', 'like', self.patient.name),		
																	('doctor', 'like', self.doctor.name), 	
																	('x_type', 'like', 'procedure'), 
																], 
																order='appointment_date desc', limit=1)
		appointment_id = appointment.id


		# Tampering
		co2_mode_emission = ''
		co2_mode_exposure = ''
		co2_observations = ''

		exc_dose = ''
		exc_observations = ''

		ipl_phototype = ''
		ipl_lesion_type = ''
		ipl_lesion_depth = ''
		ipl_pulse_duration = ''
		ipl_pulse_time_between = ''
		ipl_filter = ''
		ipl_spot = ''
		ipl_observations = ''
		ipl_pulse_type = ''

		ndy_phototype = ''
		ndy_lesion_type = ''
		ndy_lesion_depth = ''	
		ndy_pulse_duration = ''
		ndy_pulse_time_between = ''
		ndy_observations = ''
		ndy_pulse_type = ''
		ndy_pulse_spot = ''

		if laser != 'laser_co2':
			co2_mode_emission = 'x'
			co2_mode_exposure = 'x'
			co2_observations = 'x'

		if laser != 'laser_excilite':
			exc_dose = 'x'
			exc_observations = 'x'

		if laser != 'laser_ipl':
			ipl_phototype = 'x'
			ipl_lesion_type = 'x'
			ipl_lesion_depth = 'x'
			ipl_pulse_duration = 'x'
			ipl_pulse_time_between = 'x'
			ipl_filter = 'x'
			ipl_spot = 'x'
			ipl_observations = 'x'
			ipl_pulse_type = 'one'

		if laser != 'laser_ndyag':
			ndy_phototype = 'x'
			ndy_lesion_type = 'x'
			ndy_lesion_depth = 'x'	
			ndy_pulse_duration = 'x'
			ndy_pulse_time_between = 'x'
			ndy_observations = 'x'
			ndy_pulse_type = 'one'
			ndy_pulse_spot = 'one'



		# Create session 
		session = self.env['openhealth.session.med'].create(
												{
													'patient': patient_id,
													'doctor': doctor_id,													
													'chief_complaint': chief_complaint,
													'evaluation_start_date': evaluation_start_date,
													'evaluation_type':evaluation_type,
													'product': product_id,
													'laser': laser,
													'procedure': procedure_id,				
													'appointment': appointment_id,
													'treatment': treatment_id,				

													'co2_mode_emission': co2_mode_emission, 
													'co2_mode_exposure': co2_mode_exposure, 
													'co2_observations': co2_observations, 

													'exc_dose': exc_dose, 
													'exc_observations': exc_observations, 

													'ipl_phototype': ipl_phototype, 
													'ipl_lesion_type': ipl_lesion_type,
													'ipl_lesion_depth': ipl_lesion_depth, 
													'ipl_pulse_duration': ipl_pulse_duration, 
													'ipl_pulse_time_between': ipl_pulse_time_between, 
													'ipl_filter': ipl_filter,
													'ipl_spot': ipl_spot,
													'ipl_observations': ipl_observations, 
													'ipl_pulse_type': ipl_pulse_type, 

													'ndy_phototype': ndy_phototype, 
													'ndy_lesion_type': ndy_lesion_type, 
													'ndy_lesion_depth': ndy_lesion_depth, 
													'ndy_pulse_duration': ndy_pulse_duration, 
													'ndy_pulse_time_between': ndy_pulse_time_between, 
													'ndy_observations': ndy_observations,
													'ndy_pulse_type': ndy_pulse_type, 
													'ndy_pulse_spot': ndy_pulse_spot, 
												}
											)
		session_id = session.id 


		# Update
		ret = jrfuncs.update_appointment_go(self, appointment_id, session_id, 'session')

		return {

			# Mandatory 
			'type': 'ir.actions.act_window',
			'name': 'Open session Current',
		
			# Optional 
			'res_model': 'openhealth.session.med',
			'res_id': session_id,

			'view_mode': 'form',
			"views": [[False, "form"]],
			'target': 'current',

			'flags': {
						#'form': {'action_buttons': True, }
						'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
					},			

			'context': {
							'default_patient': patient_id,
							'default_doctor': doctor_id,
							'default_chief_complaint': chief_complaint,
							'default_evaluation_start_date': evaluation_start_date,
							'default_evaluation_type':evaluation_type,
							'default_product': product_id,
							'default_laser': laser,
							'default_procedure': procedure_id,
							'default_appointment': appointment_id,
							'default_treatment': treatment_id,
						}
		}
	# create_session_one

