# -*- coding: utf-8 -*-
"""
# 	*** Procedure Control Funcs
#
# 	Created: 				  1 Nov 2016
# 	Last updated: 	 	 	 21 Jan 2019
"""
#from libs import user
#from libs import lib
from openerp.addons.openhealth.models.libs import user, lib


#------------------------------------------------ Create Controls ---------------------------------
# Create Controls
def create_controls(self, nr_controls, nr_ctl_created):
	"""
	Creates Controls for the Procedure Class.
	"""
	#print
	#print 'Create Controls'

	# Clean - Deprecated
	#rec_set = self.env['openhealth.control'].search([
	#													('procedure', '=', self.id),
	#												])
	#ret = rec_set.unlink()

	# Init
	patient_id = self.patient.id
	doctor_name = self.doctor.name
	product_id = self.product.id
	chief_complaint = self.chief_complaint
	procedure_id = self.id
	treatment_id = self.treatment.id
	subtype = self.product.x_treatment

	# Start date
	if self.session_date != False:
		evaluation_start_date = self.session_date
	else:
		evaluation_start_date = self.evaluation_start_date

	# Doctor
	doctor_id = user.get_actual_doctor_pro(self)

	# Date dictionary - Days between controls
	k_dic = {
				0 :	7,
				1 :	15,
				2 :	30,
				3 :	60,
				4 :	120,
				5 :	180,
		}

	ret = 0


	# Loop
	#for k in range(0, nr_controls):
	for k in range(nr_controls):


		# Init
		delta = 0
		nr_days = k_dic[k] + delta

		#if nr_ctl_created < 6:
		#	nr_days = k_dic[nr_ctl_created]
		#else:
		#	nr_days = 7


		# Control date
		control_date = lib.get_next_date(self, evaluation_start_date, nr_days)

		control_date_str = control_date.strftime("%Y-%m-%d")
		control_date_str = control_date_str + ' 14:00:00'			# 09:00:00




		# Appointment

		# Create App - Dep !
		if False:
			duration = 0.25
			state = 'pre_scheduled_control'
			states = ['pre_scheduled_control']
			x_type = 'control'

			# Check and Push
			appointment_date_str = user.check_and_push(self, control_date_str, duration, doctor_name, states)

			# Create Appointment
			appointment = self.env['oeh.medical.appointment'].create({
																		'appointment_date': appointment_date_str,

																		'patient': patient_id,
																		'doctor': doctor_id,
																		'duration': duration,
																		'state': state,
																		'x_chief_complaint': chief_complaint,
																		'x_create_procedure_automatic': False,
																		'x_target': 'doctor',
																		'x_type': x_type,
																		'x_subtype': subtype,

																		'treatment': treatment_id,
																	})
			appointment_id = appointment.id





		appointment_id = False

		# Create Control
		control = self.control_ids.create({
											#'evaluation_start_date':control_date,

											#'first_date':control_date,
											'control_date':control_date,


											'patient':patient_id,
											'doctor':doctor_id,
											'product':product_id,
											'chief_complaint':chief_complaint,
											'evaluation_nr': k+1,

											'procedure':procedure_id,
											'appointment': appointment_id,
											'treatment': treatment_id,
									})
		control_id = control.id



		# Update Appointments
		if False:
			rec_set = self.env['oeh.medical.appointment'].browse([appointment_id])
			ret = rec_set.write({
									'control': control_id,
									'procedure': procedure_id,
								})

	return ret

# create_controls
