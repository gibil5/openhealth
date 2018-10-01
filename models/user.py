# -*- coding: utf-8 -*-
#
# 		user.py
# 
# 		Bussiness oriented. 
# 		Can not be Unit-tested (depends on a third-party library: Odoo). 
# 
# 		Created: 			13 Aug 2018
# 		Last up: 	 		14 Aug 2018
#
import datetime
import creates as cre




#------------------------------------------------ Get Delta ---------------------------------------------------
# Get the Counter QC Delta 
def get_counter_value(self):
	print 
	print 'User - Get Counter value'

	# Order 
	order = self.env['sale.order'].search([
												('state', '=', 'sale'),
												('x_type', '=', self.x_type),
											],
										#order='date_order desc',
										#order='create_date desc',
										order='x_counter_value desc',
										limit=1,
									)
	print order 
	print order.name
	print order.x_counter_value

	return order.x_counter_value + 1




#------------------------------------------------ Get Delta ---------------------------------------------------
# Get the Counter QC Delta 
def get_delta(self):
	#print 
	#print 'User - Get Delta'

	#print self
	#print self.name 
	#print self.x_type
	#print self.value

	# Order 
	order = self.env['sale.order'].search([
												('x_type', '=', self.name),
												('state', '=', 'sale'),
											],
											order='date_order desc',
											limit=1,
										)
	order.x_counter_value


	#print order
	#print order.date_order
	#print order.x_type
	#print order.x_serial_nr
	#print order.x_counter_value 


	#if order.x_counter_value != False: 
	#if order.x_counter_value != 55: 
	#	delta = self.value - order.x_counter_value
	#else:
	#	delta = 55

	delta = self.value - order.x_counter_value

	return delta



# ----------------------------------------------------------- Get Product ------------------------------------------------------

# Returns the Product Id 
def get_product(self, shortname):

	#print 
	#print 'Get Default Id'

	product_id = self.env['product.template'].search([
														('x_name_short', '=', shortname),
													],
													#order='date_order desc',
													limit=1,
												).id
	
	return product_id



#------------------------------------------------ Check and Push ---------------------------------------------------
#@api.multi
def check_and_push(self, appointment_date, duration, x_type, doctor_name, states):

	#print 
	#print 'Check and push'
	
	# Print 
	#print appointment_date
	#print duration
	#print x_type
	#print doctor_name
	#print states
	#print 


	# Init 
	delta_var = datetime.timedelta(hours=duration)
	date_format = "%Y-%m-%d %H:%M:%S"
	appointment_date_dt = datetime.datetime.strptime(appointment_date, date_format)
	k = 0
	ret = 1
	

	# Loop 
	while not ret == 0:

		# Increase 
		appointment_date = appointment_date_dt +  k * delta_var
		appointment_date_str = appointment_date.strftime("%Y-%m-%d %H:%M:%S")

		appointment_end = appointment_date_dt +  (k + 1) * delta_var 
		appointment_end_str = appointment_end.strftime("%Y-%m-%d %H:%M:%S")

		#print appointment_date_str
		#print appointment_end_str


		# Search
		if states == False: 

			appointment = self.env['oeh.medical.appointment'].search([ 	
																		('appointment_date', '=', appointment_date_str),	
																		('doctor', '=', doctor_name), 
																		#('x_type', '=', x_type), 
																		#('state', 'in', '['pre_scheduled_control']'), 
																	], 
																	#order='appointment_date desc', 
																	limit=1
																	)

			appointment_bis = self.env['oeh.medical.appointment'].search([ 	
																			('appointment_end', '=', appointment_end_str),	
																			('doctor', '=', doctor_name), 
																		], 
																		#order='appointment_date desc', 
																		limit=1
																	)

		else: 

			appointment = self.env['oeh.medical.appointment'].search([ 	
																		#('state', '=', state), 
																		('state', 'in', states), 

																		('appointment_date', '=', appointment_date_str),	
																		('doctor', '=', doctor_name), 
																	], 
																	#order='appointment_date desc', 
																	limit=1
																)
		
			appointment_bis = self.env['oeh.medical.appointment'].search([ 	
																			#('state', '=', state), 
																			('state', 'in', states), 

																			('appointment_end', '=', appointment_end_str),	
																			('doctor', '=', doctor_name), 
																		], 
																		#order='appointment_date desc', 
																		limit=1
																	)
		#print appointment
		#print appointment_bis
		#print 


		# Check 
		if (appointment.name == False)		and 	(appointment_bis.name == False)	: 	# Success
			#print 'Success'
			ret = 0 
		else: 
			#print 'Error. Repeat.'
			k = k + 1					# Error. Repeat. 

	return appointment_date_str

# check_and_push






#------------------------------------------------ Appointment Handlers ---------------------------------------------------

# Update App Handlers 
#@api.multi
def update_appointment_handlers(self, appointment_id, consultation_id, procedure_id, session_id, control_id):

	#print 
	#print 'Update Appointment Handlers'

	# Get all Apps 	
	rec_set = self.env['oeh.medical.appointment'].browse([
															appointment_id
														])

	ret = rec_set.write({
							'consultation': consultation_id,
							'procedure': 	procedure_id,
							'session': 		session_id,
							'control': 		control_id,
						})

# update_appointment_handlers




#------------------------------------------------ Get Actual Doctor - Procedure ---------------------------------------------------

# Get Actual Doctor 
#@api.multi
#def get_actual_doctor(self):
def get_actual_doctor_pro(self):

	#print 
	#print 'Get Actual Doctor'

	user_name =  self.env.user.name 	

	doctor = self.env['oeh.medical.physician'].search([ 	
																('x_user_name', '=', user_name),		
															], 
															#order='appointment_date desc', 
															limit=1
															)
	doctor_id = doctor.id 

	if doctor_id == False: 
		doctor_id = self.doctor.id 


	# Print 
	#print user_name
	#print doctor.id 
	#print doctor.name 

	return doctor_id

# get_actual_doctor_pro



#------------------------------------------------ Get Actual Doctor ---------------------------------------------------

# Get Actual Doctor 
def get_actual_doctor(self):

	#print
	#print 'Get Actual Doctor'

	#print self.env.user.name
	#print self.env.user
	#print self.env
	#print self 

	user_name =  self.env.user.name 
		
	doctor = self.env['oeh.medical.physician'].search([ 	
															('x_user_name', '=', user_name),		
														], 
														#order='appointment_date desc', 
														limit=1
													)
	#print doctor
	#print doctor.id 
	
	#doctor_id = doctor.id 
	#return doctor_id
	return doctor

# get_actual_doctor



# ----------------------------------------------------------- Defaults ------------------------------------------------------

# Returns the Default Model Id 
#@api.multi
def _get_default_id(self, x_type):

	#print 
	#print 'Get Default Id'

	_h_vars = {
				'patient' : 	('oeh.medical.patient',		'REVILLA RONDON JOSE JAVIER'), 
				'doctor' : 		('oeh.medical.physician',	'Dr. Chavarri'), 
				#'product' : 	('product.product', 		'PROTECTOR SOLAR'), 
				'product' : 	('product.product', 		'TOKEN'), 
			}

	model = _h_vars[x_type][0]
	name = _h_vars[x_type][1]
	
	obj = self.env[model].search([
									('name', '=', name), 
								],
								#order='write_date desc',
								limit=1,
							)
	# Print 
	#print x_type
	#print model
	#print name 
	#print obj

	return obj.id

# _get_default_id

