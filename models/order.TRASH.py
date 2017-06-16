


# 16 Jun 2017


# ----------------------------------------------------------- Button - Reseve Machine  ------------------------------------------------------

	@api.multi 
	def reserve_machine_old(self):

		#print 'jx'
		#print 'Reserve Machine - Old'

		#self.x_machine = 'laser_co2_1'


		
		# Create Machine
		appointment_date = 	self.x_appointment_date
		doctor_name = 		self.x_doctor.name
		doctor_id = 		self.x_doctor.id
		patient_id = 		self.patient.id
		treatment_id = 		self.treatment.id
		duration = 			self.x_duration


		x_machine_old = 	self.x_machine




		#start_machine = 	self.x_machine
		start_machine = 	self.x_machine_req





		# New 
		#x_machine = appfuncs.search_machine(self, appointment_date, doctor_name, duration)
		#x_machine = appfuncs.search_machine(self, appointment_date, doctor_name, duration, start_machine)
		x_machine = mac_funcs.search_machine(self, appointment_date, doctor_name, duration, start_machine)
		

		


		self.x_machine = x_machine 
		self.x_appointment.x_machine = x_machine





		# If Sucess create Machine Appointment
		if x_machine != False:


			# Create Appointment - Machine 
			app = self.env['oeh.medical.appointment'].create(
															{
																'appointment_date': appointment_date,

																'patient': 		patient_id,																	

																'x_type': 		'procedure',

																'duration': 	duration,
																																
																'x_create_procedure_automatic': False, 

																'x_machine': 	x_machine,



							                    				#'x_target': 	'machine',
							                    				'x_target': 	self.x_target,


																'doctor': 		doctor_id,

																'treatment': 	treatment_id, 
															}
															)



			if app != False:

				# Unlink Old 
				rec_set = self.env['oeh.medical.appointment'].search([
																			('appointment_date', 'like', appointment_date), 
																			('doctor', '=', doctor_name), 
																			('x_machine', '=', x_machine_old),

																			('patient', '=', self.patient.name), 
																	])
				ret = rec_set.unlink()
				#print "ret: ", ret




		else:
			#print 'Error !'	
			#print 			


			return {	'warning': 	{'title': "Error: Colisión !",
						'message': 	'La sala ya está reservada.',   
			#' + start + ' - ' + end + '.',
						}}

	# reserve_machine



