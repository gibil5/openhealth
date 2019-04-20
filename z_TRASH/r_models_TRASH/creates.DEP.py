#import datetime
#import time_funcs







#------------------------------------------------ Create Procedure --------------------------------
# Create procedure
def create_procedure_go(self, app_date_str, subtype, product_id):

	"""
	high level support for doing this and that.
	"""
	#print
	#print 'Create Procedure - Go'
	#print app_date_str
	#print subtype
	#print product_id


	# Init
	treatment_id = self.id
	patient = self.patient.id
	chief_complaint = self.chief_complaint


	# Print
	#print treatment
	#print patient
	#print chief_complaint


	# Doctor
	doctor = user.get_actual_doctor(self)
	doctor_id = doctor.id
	if doctor_id == False:
		doctor_id = self.physician.id


	# Time
	#GMT = time_funcs.Zone(0, False, 'GMT')
	#evaluation_start_date = datetime.datetime.now(GMT).strftime("%Y-%m-%d %H:%M:%S")




# Appointment

	# Search
	appointment = self.env['oeh.medical.appointment'].search([
																('patient', '=', self.patient.name),
																('doctor', '=', self.physician.name),
																('x_type', '=', 'procedure'),
																('x_subtype', '=', subtype),
														],
															order='appointment_date desc', limit=1)
	#print appointment


	# Check if existing App is in the Future
	if appointment.name != False:

		# Delta
		future = appointment.appointment_date
		delta, delta_sec = lib.get_delta_now(self, future)


	if appointment.name == False or delta_sec < 0: 		# If no appointment or appointment in the past

		# Is the hour before 21:00
		app_date_ok = lib.doctor_available(self, app_date_str)

		if app_date_ok:

			# Create App
			appointment = self.env['oeh.medical.appointment'].create({
																		'appointment_date': app_date_str,
																		'patient':			self.patient.id,
																		'doctor':			self.physician.id,
																		'state': 			'pre_scheduled',
																		'x_type': 			'procedure',
																		'x_subtype': 		subtype,

																		'treatment':		self.id,
																})
	appointment_id = appointment.id
	#print appointment





	# Search Product Product
	product_product = self.env['product.product'].search([
																('id', '=', product_id),
													])
	# Search Product Template
	product_template = self.env['product.template'].search([
																('x_name_short', '=', product_product.x_name_short),
																('x_origin', '=', False),
														])



# Create Proc

	# Init
	consultation_id = False
	procedure_id = False
	session_id = False
	control_id = False

	ret = 0


	app_date_ok = lib.doctor_available(self, app_date_str)

	if app_date_ok:

		# Create Procedure
		procedure = self.procedure_ids.create({
												'evaluation_start_date':app_date_str,
												'appointment': appointment_id,
												'patient':patient,
												'doctor':doctor_id,
												'product':product_template.id,
												'chief_complaint':chief_complaint,

												'treatment':treatment_id,
											})
		procedure_id = procedure.id



		# Create Session - New
		session = self.env['openhealth.session.med'].create({
																'evaluation_start_date':app_date_str,
																'appointment': appointment_id,
																'patient': patient,
																'doctor': doctor_id,
																'product': product_template.id,
																'chief_complaint': chief_complaint,
																#'evaluation_type':evaluation_type,
																#'laser': laser,

																'procedure': procedure_id,
																'treatment': treatment_id,
														})
		session_id = session.id



	# Update Appointment
	if procedure_id != False:

		ret = user.update_appointment_handlers(self, appointment_id, consultation_id, procedure_id, session_id, control_id)


	return ret
# create_procedure_go



# -------------------------------------------------------------------------------------------------
# Create Order
def update_order(order, date_order=False, serial_nr=False, counter=False):
	"""
	high level support for doing this and that.
	"""
	#print
	#print 'Update Order'

	# Update
	if date_order != False:
		order.write({
							'date_order': date_order,
						})

	if serial_nr != False:
		order.write({
							'x_serial_nr': serial_nr,
						})

	if counter != False:
		order.write({
							'x_counter_value': counter,
						})
# update_order

