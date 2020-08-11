# -*- coding: utf-8 -*-
"""
	Procedure Control Funcs
	Created: 				  1 Nov 2016
	Last updated: 	 	 	 10 Jan 2020
"""
from __future__ import print_function
from openerp.addons.openhealth.models.libs import user, lib

#------------------------------------------------ Create Controls ---------------------------------
# Create Controls
def create_controls(self, nr_controls, nr_ctl_created):
	"""
	Creates Controls for the Procedure Class.
	"""
	print()
	print('oh - pro_con_funcs - create_controls')

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
	for k in range(nr_controls):

		# Init
		delta = 0
		nr_days = k_dic[k] + delta

		# Control date
		control_date = lib.get_next_date(self, evaluation_start_date, nr_days)
		control_date_str = control_date.strftime("%Y-%m-%d")
		control_date_str = control_date_str + ' 14:00:00'			# 09:00:00

		# Appointment
		appointment_id = False

		# Create Control
		control = self.control_ids.create({
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
	return ret

# create_controls
