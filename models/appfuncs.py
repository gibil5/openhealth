# -*- coding: utf-8 -*-


from openerp import models, fields, api
import datetime



# ----------------------------------------------------------- Collisions  ------------------------------------------------------

@api.multi

#def check_for_collisions(self, appointment_date, doctor_name, duration):
def check_for_collisions(self, appointment_date, doctor_name, duration, x_machine):


		#print 
		#print 'Check for collision'


		dt = appointment_date[2:10]
		#print dt
		#print 


		if x_machine == False:
			app_ids = self.env['oeh.medical.appointment'].search([('appointment_date', 'like', dt),  ('doctor', '=', doctor_name)  ])
		else:
			app_ids = self.env['oeh.medical.appointment'].search([('appointment_date', 'like', dt),  ('x_machine', '=', x_machine)  ])


		#print app_ids 





		# Appointment end 
		date_format = "%Y-%m-%d %H:%M:%S"

		delta = datetime.timedelta(hours=duration)

		sd = datetime.datetime.strptime(appointment_date, date_format)
		
		ae_dt = delta + sd

		ae = ae_dt.strftime("%Y-%m-%d %H:%M:%S")


		#print delta
		#print sd 
		#print ae_dt
		#print 



		# Check if Collision 
		ad = appointment_date

		for app in app_ids:

			#print app

			start = app.appointment_date

			end = app.appointment_end


			if 	app.state != 'pre_scheduled_control' and  	(	
															(ad >= start and ae <= end)  or  (ad <= start and ae >= end)  	or    (ad < start and ae > start)  or  (ad < end and ae > end)
															): 


				#print 'Collision !!!'



				# Local
				delta = datetime.timedelta(hours=5)


				# Start 
				sd = datetime.datetime.strptime(start, date_format)
				sl =  sd - delta 
				#sl = start_local.strftime("%Y-%m-%d %H:%M:%S")
				start_local = sl.strftime("%H:%M")


				# End 
				sd = datetime.datetime.strptime(end, date_format)
				el =  sd - delta 
				end_local = el.strftime("%H:%M")



				#print delta
				#print end_local
				#print el



				# Did not pass 
				return -1, doctor_name, start_local, end_local




		# Passed test - All is Ok 
		return 0, '', '', '' 




