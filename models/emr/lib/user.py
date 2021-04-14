# -*- coding: utf-8 -*-
"""
	User 
	Used by 
        Procedure

 	Created: 			14 apr 2021
	Last up: 			14 apr 2021
"""
from __future__ import print_function
import datetime

#------------------------------------------------ Constants --------------------
_date_format = "%Y-%m-%d %H:%M:%S"
_date_format_day = "%Y-%m-%d"


#------------------------------------------------ Get Next Date ----------------
def get_next_date(self, evaluation_start_date, nr_days):
	"""
	Get Next Date
    Used by 
	"""
	date_format = _date_format
	delta = datetime.timedelta(days=nr_days)
	start = datetime.datetime.strptime(evaluation_start_date, date_format)
	next_date = delta + start
	return next_date
# get_next_date


# ----------------------------------------------------------- Get Nr Days--------------------------
def get_nr_days(self, date_ref_str, date_str):
	"""
	Get Nr Days
    Used by 
        Session
	"""
	# Init
	delta_days = 0
	if date_ref_str != False and date_str != False:
		date_format = _date_format_day
		date_ref_str = date_ref_str.split()[0]
		date_ref_dt = datetime.datetime.strptime(date_ref_str, date_format)
		date_str = date_str.split()[0]
		date_dt = datetime.datetime.strptime(date_str, date_format)
		delta = date_dt - date_ref_dt
		delta_days = delta.days
	return delta_days


#------------------------------------------------ Get Actual Doctor - Procedure -------------------
# Get Actual Doctor
def get_actual_doctor_pro(self):
	"""
    Gets actual doctor, for procedure
	"""
	user_name = self.env.user.name
	doctor = self.env['oeh.medical.physician'].search([
																('x_user_name', '=', user_name),
															],
															#order='appointment_date desc',
															limit=1
															)
	doctor_id = doctor.id

	if not doctor_id:
		doctor_id = self.doctor.id

	return doctor_id

# get_actual_doctor_pro

