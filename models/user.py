# -*- coding: utf-8 -*-
"""
		user.py

 		Bussiness oriented.
 		Can not be Unit-tested (depends on a third-party library: Odoo).

 		Created: 			13 Aug 2018
 		Last up: 	 		19 Nov 2018
"""
import datetime
from . import ord_vars


#------------------------------------------------ Get Serial Nr -----------------------------------
# Get the Counter QC Delta
def get_serial_nr(x_type, counter_value, state):
	"""
	high level support for doing this and that.
	"""
	#print
	#print 'Get Serial Nr'

	# Init
	separator = '-'


	if state in ['credit_note']:
		#prefix = ord_vars._dic_prefix_cn[x_type]
		prefix = ord_vars.get_prefix_cn(x_type)

	else:
		#prefix = ord_vars._dic_prefix[x_type]
		prefix = ord_vars.get_prefix(x_type)



	#padding = ord_vars._dic_padding[x_type]
	padding = ord_vars.get_padding(x_type)



	# Serial Nr
	serial_nr = prefix  +  separator  +  str(counter_value).zfill(padding)


	return serial_nr



#------------------------------------------------ Get Counter -------------------------------------
# Get the Counter
def get_counter_value(self, x_type, state):
	"""
	high level support for doing this and that.
	"""
	#print 'Get Counter value'
	#print state


	# Search

	# Sale, Cancel
	if state in ['validated']:

		order = self.env['sale.order'].search([
													('x_electronic', '=', True),
													('x_type', '=', x_type),
													('state', 'in', ['sale', 'cancel']),
												],
											order='x_counter_value desc',
											limit=1,
										)


	# Credit Note
	elif state in ['credit_note']:

		order = self.env['sale.order'].search([
													('x_electronic', '=', True),
													('x_type', '=', x_type),
													('state', 'in', ['credit_note']),
												],
											order='x_counter_value desc',
											limit=1,
										)

	return order.x_counter_value + 1





#------------------------------------------------ Get Delta ---------------------------------------
# Get the Counter QC Delta
def get_delta(self):
	"""
	high level support for doing this and that.
	"""
	#print
	#print 'User - Get Delta'

	# Order
	order = self.env['sale.order'].search([
												('x_type', '=', self.name),
												('state', '=', 'sale'),
											],
											order='date_order desc',
											limit=1,
										)
	#order.x_counter_value

	delta = self.value - order.x_counter_value

	return delta



# ----------------------------------------------------------- Get Product -------------------------
# Returns the Product Id
def get_product(self, shortname):
	"""
	high level support for doing this and that.
	"""
	#print
	#print 'Get Default Id'
	product_id = self.env['product.template'].search([
														('x_name_short', '=', shortname),
													],
													#order='date_order desc',
													limit=1,
												).id
	return product_id



#------------------------------------------------ Check and Push ----------------------------------
#@api.multi
#def check_and_push(self, appointment_date, duration, x_type, doctor_name, states):
def check_and_push(self, appointment_date, duration, doctor_name, states):
	"""
	high level support for doing this and that.
	"""
	#print
	#print 'Check and push'

	# Init
	delta_var = datetime.timedelta(hours=duration)
	date_format = "%Y-%m-%d %H:%M:%S"
	appointment_date_dt = datetime.datetime.strptime(appointment_date, date_format)
	k = 0
	ret = 1


	# Loop
	#while not ret == 0:
	while ret != 0:

		# Increase
		appointment_date = appointment_date_dt +  k * delta_var
		appointment_date_str = appointment_date.strftime("%Y-%m-%d %H:%M:%S")
		appointment_end = appointment_date_dt +  (k + 1) * delta_var
		appointment_end_str = appointment_end.strftime("%Y-%m-%d %H:%M:%S")


		# Search
		#if states == False:
		if not states:

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
		#if (appointment.name == False) and (appointment_bis.name == False): 	# Success
		if (not appointment.name) and (not appointment_bis.name): 	# Success
			#print 'Success'
			ret = 0
		else:
			#print 'Error. Repeat.'
			k = k + 1					# Error. Repeat.

	return appointment_date_str

# check_and_push






#------------------------------------------------ Appointment Handlers ----------------------------
# Update App Handlers
def update_appointment_handlers(self, app_id, cons_id, proc_id, sess_id, ctrl_id):
	"""
	high level support for doing this and that.
	"""
	#print
	#print 'Update Appointment Handlers'

	# Get all Apps
	rec_set = self.env['oeh.medical.appointment'].browse([
															#appointment_id
															app_id
														])

	rec_set.write({
					#'consultation': consultation_id,
					#'procedure': 	procedure_id,
					#'session': 		session_id,
					#'control': 		control_id,
					'consultation': cons_id,
					'procedure': 	proc_id,
					'session': 		sess_id,
					'control': 		ctrl_id,
			})
# update_appointment_handlers




#------------------------------------------------ Get Actual Doctor - Procedure -------------------
# Get Actual Doctor
def get_actual_doctor_pro(self):
	"""
	high level support for doing this and that.
	"""
	#print
	#print 'Get Actual Doctor'

	user_name = self.env.user.name

	doctor = self.env['oeh.medical.physician'].search([
																('x_user_name', '=', user_name),
															],
															#order='appointment_date desc',
															limit=1
															)
	doctor_id = doctor.id

	#if doctor_id == False:
	#if doctor_id is False:
	if not doctor_id:
		doctor_id = self.doctor.id

	# Print
	#print user_name
	#print doctor.id
	#print doctor.name

	return doctor_id

# get_actual_doctor_pro



#------------------------------------------------ Get Actual Doctor -------------------------------
# Get Actual Doctor
def get_actual_doctor(self):
	"""
	high level support for doing this and that.
	"""
	#print
	#print 'Get Actual Doctor'

	user_name = self.env.user.name

	doctor = self.env['oeh.medical.physician'].search([
															('x_user_name', '=', user_name),
														],
														#order='appointment_date desc',
														limit=1
													)
	return doctor
# get_actual_doctor



# ----------------------------------------------------------- Defaults ----------------------------
# Returns the Default Model Id
def _get_default_id(self, x_type):
	"""
	high level support for doing this and that.
	"""
	#print
	#print 'Get Default Id'

	_h_vars = {
				'patient':		('oeh.medical.patient', 'REVILLA RONDON JOSE JAVIER'),
				'doctor': 		('oeh.medical.physician', 'Dr. Chavarri'),
				#'product': 	('product.product', 'PROTECTOR SOLAR'),
				'product': 		('product.product', 'TOKEN'),
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
