# -*- coding: utf-8 -*-

from openerp import models, fields, api

#from datetime import datetime,tzinfo,timedelta
import datetime


import time_funcs

import jrfuncs

import appfuncs




#------------------------------------------------ Check Push and Create ---------------------------------------------------
@api.multi
#def check_and_push(self, appointment_date, duration, x_type, doctor_name):
def check_and_push(self, appointment_date, duration, x_type, therapist_name, machine):

	debug = False 

	if debug: 
		#print 
		#print 'Chech and push - Cos'
		#print appointment_date



	delta_var = datetime.timedelta(hours=duration)
	date_format = "%Y-%m-%d %H:%M:%S"

	ret = 1




	appointment_date_dt = datetime.datetime.strptime(appointment_date, date_format)
	k = 0

	while not ret == 0:

		appointment_date = appointment_date_dt +  k * delta_var

		appointment_date_str = appointment_date.strftime("%Y-%m-%d %H:%M:%S")





		# Check for collisions 
		#ret, doctor_name, start, end = appfuncs.check_for_collisions(self, appointment_date_str, doctor_name, duration, False, 'doctor')
		ret, doctor_name, start, end = appfuncs.check_for_collisions(self, appointment_date_str, therapist_name, duration, machine, 'therapist', 'procedure')




		if ret == 0: 		# Success ! - No Collisions
			
			if debug: 
				#print 'Collision check - Success !!!'
				#print k



		else:				# Collision - Keep going... 
			k = k + 1

	return appointment_date_str


