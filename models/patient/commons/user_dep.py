# -*- coding: utf-8 -*-
"""
		user.py - Dep ?
		Used by 
			Counter

 			Bussiness oriented. Can not be Unit-tested (depends on a third-party library: Odoo).

 	Created: 			13 aug 2018
	Last up: 			29 mar 2021
"""
import datetime
from openerp.addons.openhealth.models.order import ord_vars

#------------------------------------------------ Get Counter - Dep -------------------------------------
def get_next_counter_value(self, x_type, state):
	"""
	Get Next Counter value. Given type and state.
	If State in Validated or Sale.
	"""
	print()
	print('Get Counter Value')
	print(x_type)
	print(state)

	# Sale, Cancel
	#if state in ['validated']:
	if state in ['validated', 'sale']:

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


#------------------------------------------------ Get Serial Nr - Dep -----------------------------------
def get_serial_nr(x_type, counter_value, state):
	"""
	Get the Serial Nr, given the type, counter and state.
	"""
	print()
	print('Get Serial Nr')

	# Separator
	separator = '-'

	# Prefix
	if state in ['credit_note']:
		prefix = ord_vars.get_prefix_cn(x_type)
	else:
		prefix = ord_vars.get_prefix(x_type)

	# Padding
	padding = ord_vars.get_padding(x_type)

	# Serial Nr
	serial_nr = prefix  +  separator  +  str(counter_value).zfill(padding)

	return serial_nr


#------------------------------------------------ Get Counter From Serial Nr ----------------------
# Get Counter From Serial Nr
def get_counter_from_serial_nr(serial_nr):
	"""
	Get Counter. From Serial Nr.
	"""
	#print()
	#print('Get Counter From Serial Nr')
	#print(serial_nr)
	counter = int(serial_nr.split('-')[1])
	return counter


#------------------------------------------------ Check and Push ----------------------------------
def check_and_push(self, appointment_date, duration, doctor_name, states):
	"""
	Check if Dr available and if not check next time slot.
	Returns a Date sring.
	"""
	#print()
	#print('User - Check and push')
	#print(appointment_date)
	#print(duration)
	#print(doctor_name)
	#print(states)


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
		if not states:

			appointment = self.env['oeh.medical.appointment'].search([
																		('appointment_date', '=', appointment_date_str),
																		('doctor', '=', doctor_name),
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
																		('appointment_date', '=', appointment_date_str),
																		('doctor', '=', doctor_name),

																		('state', 'in', states),
																	],
																	#order='appointment_date desc',
																	limit=1
																)

			appointment_bis = self.env['oeh.medical.appointment'].search([
																			('appointment_end', '=', appointment_end_str),
																			('doctor', '=', doctor_name),

																			('state', 'in', states),
																		],
																		#order='appointment_date desc',
																		limit=1
																	)
		#print appointment
		#print appointment_bis
		#print


		# Check
		if (not appointment.name) and (not appointment_bis.name): 	# Success. Return
			ret = 0
		else:
			k = k + 1												# Error. Repeat

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




#------------------------------------------------ Get Delta ---------------------------------------
# Get the Counter QC Delta
def get_delta(self):
	"""
	For Delta QC.
	"""

	# Search
	order = self.env['sale.order'].search([
												('x_type', '=', self.name),
												('state', '=', 'sale'),
											],
											order='date_order desc',
											limit=1,
										)

	delta = self.value - order.x_counter_value

	return delta


# ----------------------------------------------------------- Get Product Id ----------------------
def get_product(self, shortname):
	"""
	Get the Product Id given the Shortname.
	"""
	# Search
	product_id = self.env['product.template'].search([
														('x_name_short', '=', shortname),
													],
													#order='date_order desc',
													limit=1,
												).id
	return product_id
