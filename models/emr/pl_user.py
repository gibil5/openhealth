# -*- coding: utf-8 -*-
"""
		user.py - DEP ?

 		Created: 			13 Aug 2018
 		Last up: 	 		27 Jul 2020
"""

#------------------------------------------------ Get Actual Doctor -------------------------------
# Get Actual Doctor
def get_actual_doctor(self):
	"""
    USed by Treatment
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
