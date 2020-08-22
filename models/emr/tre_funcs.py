# -*- coding: utf-8 -*-
"""
	Tre Funcs

	Created: 			22 aug 2020
	Last up: 	 		22 aug 2020
"""
from datetime import datetime,tzinfo,timedelta

#------------------------------------------------ Get Actual Doctor ------------
def get_actual_doctor(self):
	"""
	Used by Treatment
	"""
	user_name = self.env.user.name
	doctor = self.env['oeh.medical.physician'].search([
															('x_user_name', '=', user_name),
														],
														#order='appointment_date desc',
														limit=1
													)
	return doctor
# get_actual_doctor


#------------------------------------------------ Time -------------------------
class Zone(tzinfo):
	"""
	Used by Treatment
	"""
	def __init__(self,offset,isdst,name):
		self.offset = offset
		self.isdst = isdst
		self.name = name
	def utcoffset(self, dt):
		return timedelta(hours=self.offset) + self.dst(dt)
	def dst(self, dt):
			return timedelta(hours=1) if self.isdst else timedelta(0)
	def tzname(self,dt):
		 return self.name
