# -*- coding: utf-8 -*-
"""
	Productivity Funcs

	Used by
		update productivity

	Created: 		 7 Dec 2019
	Last up: 		26 oct 2020

	Signature
		create_days
		update_day_cumulative
		update_day_avg
"""
import datetime
from openerp import models, fields, api


# ----------------------------------------------------------- Create Days ------
# Create Days
@api.multi
def create_days(self):
	"""
	Used by
		Update productivity
	"""
	print()
	print('Create Days')

	_dic_weekday = {
					0: 	'monday',
					1: 	'tuesday',
					2: 	'wednesday',
					3: 	'thursday',
					4: 	'friday',
					5: 	'saturday',
					6: 	'sunday',
	}

	# Clean
	#self.day_line.unlink()
	self.productivity_day.unlink()

	# Get Holidays - Fro config
	days_inactive = self.configurator.get_inactive_days()					# Respects the LOD !
	print()
	print('Holidays')
	print(days_inactive)
	print()

	# Get nr of days 
	#date_format = "%Y-%m-%d %H:%M:%S"
	date_format = "%Y-%m-%d"
	date_end_dt = datetime.datetime.strptime(self.date_end, date_format)
	date_begin_dt = datetime.datetime.strptime(self.date_begin, date_format)
	delta = date_end_dt - date_begin_dt
	#print(delta)

	# For each day
	for i in range(delta.days + 1):
		#print(i)
		date_dt = date_begin_dt + datetime.timedelta(i)
		weekday = date_dt.weekday()
		weekday_str = _dic_weekday[weekday]			
		#print(date_dt, weekday)

		# Duration
		if weekday in [5]:
			duration = 0.5
		else:
			duration = 1

		# Not Sunday
		if weekday in [0, 1, 2, 3, 4, 5]:
			date_s = date_dt.strftime(date_format)				
			#print(date_s)

			# Not holiday
			if date_s not in days_inactive:

				# Create Productivity Days
				#day = self.day_line.create({
				# Create
				day = self.productivity_day.create({
														'name': weekday_str,
														'date': date_dt,
														'weekday': weekday_str,
														'duration': duration,
														'management_id': self.id,
								})
				print(day)

				day.update_amount()		# Update total amount

				#print(day)
				#print(date_dt, weekday, weekday_str)
				#print(date_dt)
				#print(date_s)
		else:
			#print('Sunday, not counted')
			pass

# create_days


# ------------------------------------------------------- Update Cumulative ----
# Update Cumulative
@api.multi
def update_day_cumulative(self):
	"""
	Update Day Cumulative
	Used by
		Update productivity
	"""
	print()
	print('Update - Cumulative')

	# Init
	amount_total = 0
	duration_total = 0

	# Clean
	#for day in self.day_line:
	#	if day.amount in [0]:
			#day.duration = 0
	#		day.unlink()

	# Update Cumulative and Nr Days
	#for day in self.day_line:
	for day in self.productivity_day:
		#print(day.name)
		#print(day.date)
		amount_total = amount_total  + day.amount
		day.cumulative = amount_total
		duration_total = duration_total + day.duration
		day.nr_days = duration_total

	# Update Nr Days Total
	#for day in self.day_line:
	for day in self.productivity_day:	
		day.nr_days_total = duration_total

# update_day_cumulative


# --------------------------------------------------------- Update Averages ----
# Update Averages
@api.multi
def update_day_avg(self):
	"""
	Update Day Average
	Used by
		Update productivity
	"""
	print()
	print('X - Update - Average')

	# Update
	#for day in self.day_line:
	for day in self.productivity_day:
		#print(day.date)
		day.update_avg()
		day.update_projection()

# update_day_avg
