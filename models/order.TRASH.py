


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




# 29 Aug 2017


	@api.multi 
	def action_confirm_deprecated(self):

		#print 
		#print 'jx'
		#print 'Action confirm - Over ridden'
		 
		#Write your logic here


		# Validate 
		#if self.x_machine != False:

		#print 'x_doctor.name: ', self.x_doctor.name
		#print 'x_machine', self.x_machine
		#print 'x_state', self.x_state



		#if self.x_doctor.name != False   and   self.x_machine == False:
		#if self.x_doctor.name != False   and   self.x_machine == False	 and 	self.x_machine_req != 'consultation':

		if self.x_treatment == 'laser_co2'   and   self.x_machine == False:
			#print 'Warning: Sala no Reservada !'
			tra = 1 
		else:
			#print 'Success !!!'

			#self.x_state = 'sale'
			#self.x_confirmed = True 


			#if self.x_family == 'consultation': 
			if self.x_family == 'consultation'	or 	self.x_family == 'procedure': 
				self.x_appointment.state = 'Scheduled'

				#self.state = 'confirmed'


			# State is changed here ! 
			res = super(sale_order, self).action_confirm()
			
			#self.state = 'confirmed'

		#else: 
			
		#res = super(sale_order, self).action_confirm()
		#Write your logic here
		
		#print
	# action_confirm
	









