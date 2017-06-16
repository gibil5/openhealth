# -*- coding: utf-8 -*-

from openerp import models, fields, api
import datetime
from . import time_funcs
from . import jrfuncs
from . import appfuncs

#------------------------------------------------ Check Push and Create ---------------------------------------------------
@api.multi
def check_and_push(self, appointment_date, duration, x_type, therapist_name, machine):
	delta_var = datetime.timedelta(hours=duration)
	date_format = "%Y-%m-%d %H:%M:%S"
	ret = 1
	appointment_date_dt = datetime.datetime.strptime(appointment_date, date_format)
	k = 0
	while not ret == 0:
		appointment_date = appointment_date_dt +  k * delta_var
		appointment_date_str = appointment_date.strftime("%Y-%m-%d %H:%M:%S")

		# Check for collisions 
		ret, doctor_name, start, end = appfuncs.check_for_collisions(self, appointment_date_str, therapist_name, duration, machine, 'therapist', 'procedure')

		if ret == 0: 		# Success ! - No Collisions			
			tra = 1
		else:				# Collision - Keep going... 
			k = k + 1
	return appointment_date_str
# check_and_push