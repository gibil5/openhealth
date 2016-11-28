# -*- coding: utf-8 -*-
#
# 	*** OPEN HEALTH
#

# Created: 				14 Nov 2016
# Last updated: 	 	27 Nov 2016 



from openerp import models, fields, api

#from datetime import datetime
import datetime
import time_funcs

#import appfuncs



class Appointment(models.Model):
	#_name = 'openhealth.appointment'

	_inherit = 'oeh.medical.appointment'



	name = fields.Char(

			string="Cita #", 

			#default='',

			#compute='_compute_name', 
			required=True, 
			)

	vspace = fields.Char(
			' ', 
			readonly=True
			)




	# Patient
	patient = fields.Many2one(
			'oeh.medical.patient',
			
			string = "Paciente", 	

			default=3025, 		# Revilla 

			#required=True, 
	)




	x_error = fields.Integer(
			
			default = 0, 
			required=True, 
		)






	# Doctor 
	doctor = fields.Many2one(
			'oeh.medical.physician',
			
			#default=1, 		# Chavarri

			#string = "Médico", 	
			#required=True, 
			)




	#@api.onchange('doctor')
	@api.onchange('doctor', 'duration')

	def _onchange_doctor(self):

		print 
		print 'On change Doctor'


		if self.doctor.name != False:	

			print self.doctor.name
			print self.patient.name
			print self.appointment_date
			print self.x_date
			print self.duration
			print self.appointment_end
			print 


			self.x_error = 0



			# Check for collision 

			#ret = self.check_for_collision()
			#ret, doctor_name, start, end = self.check_for_collision()
			#ret, doctor_name, start, end = self.check_for_collision(self.appointment_date)
			ret, doctor_name, start, end = self.check_for_collision(self.appointment_date, self.doctor.name)

			print ret 


			if ret != 0:

				self.x_error = 1
				self.doctor = False
				#self.duration = 0.5
				#self.x_duration_min = '0.5'


				return {
							'warning': {
									'title': "Error: Colisión !",
									#'message': 'Cita ya existente, con el ' + self.doctor.name,
									#'message': 'Cita ya existente, con el ' + self.doctor.name + ": " + start + ' - ' + end + '.',
									'message': 'Cita ya existente, con el ' + doctor_name + ": " + start + ' - ' + end + '.',
						}}



			# Create Procedure 
			#if self.x_error == 0:
			#	print 
			#	print 'Create Appointment for procedure !'
			#	app = self.create_app_procedure()
			#	print app 
		print 















	# Date 
	appointment_date = fields.Datetime(

			string="Fecha", 

			)

	x_date = fields.Date(
			#default = fields.Date.today, 
			#compute="_compute_x_date",
			#required=True, 
		)


	#@api.multi
	@api.depends('appointment_date')

	def _compute_x_date(self):
		for record in self:
			record.x_date = record.appointment_date







	# Date end 
	appointment_end = fields.Datetime(
			string="Fecha fin", 
			#compute="_compute_appointment_end",
		
			readonly=True, 
			)








	# Colors 
	color_patient_id = fields.Integer(
			default=2,
		)



	# Color Doctor id 
	_hash_colors_doctor = {

			'Dra. Acosta': 1,
			'Dr. Canales': 2,
			'Dr. Chavarri': 3,
			'Dr. Escudero': 4,
			'Dr. Gonzales': 5,
			'Dr. Vasquez': 6,

		}


	color_doctor_id = fields.Integer(
			default=1,
			compute='_compute_color_doctor_id', 
		)


	#@api.multi
	@api.depends('doctor')
	def _compute_color_doctor_id(self):
		for record in self:	
			record.color_doctor_id = self._hash_colors_doctor[record.doctor.name]






	# Color x_type id 
	_hash_colors_x_type = {


			'Consulta': 2,
			'consultation': 2,


			'Procedimiento': 1,
			'procedure': 1,
			

			'Sesion': 3,
			'session': 3,

			
			'Control': 4,
			'control': 4,
			
		}


	color_x_type_id = fields.Integer(
			default=1,
			compute='_compute_color_x_type_id', 
		)


	#@api.multi
	@api.depends('x_type')
	def _compute_color_x_type_id(self):
		for record in self:	
			record.color_x_type_id = self._hash_colors_x_type[record.x_type]








	# Duration


	_hash_duration = {
					'0.25' 	: 0.25, 
     				'0.5' 	: 0.5, 

     				#'0.75' 	: 0.75, 
     				#'1.0' 	: 1.0, 
     				#'2.0' 	: 2.0, 
				}




	_duration_list = [
        			('0.25', 	'15 min'),
        			('0.5', 	'30 min'),

					#('0.75', 	'45 min'),
        			#('1.0', 	'60 min'),
        			#('2.0', 	'120 min'),
        		]




     # Duration min 

	x_duration_min = fields.Selection(

			selection = _duration_list, 

			string="Duración (min)", 
		
			#default = '1.0',

			default = '0.5',

			#readonly=True,
		)




	@api.onchange('x_type')

	def _onchange_x_type(self):

		if self.x_type != False:	

			if self.x_type == 'consultation'  or  self.x_type == 'procedure':

				self.x_duration_min = '0.5'

			elif self.x_type == 'control':

				self.x_duration_min = '0.25'






	@api.onchange('x_duration_min')

	def _onchange_x_duration_min(self):

		if self.x_duration_min != False:	

			self.duration = self._hash_duration[self.x_duration_min]









	# Duration 

	duration = fields.Float(

			string="Duración (h)", 

			default = 0.5,

			readonly=True, 
		)










	


	# Type 
	_type_list = [
        			('consultation', 'Consulta'),
        			('procedure', 'Procedimiento'),
        			('session', 'Sesión'),
        			('control', 'Control'),

        			#('Consulta', 'Consulta'),
        			#('Procedimiento', 'Procedimiento'),
        			#('Sesion', 'Sesión'),
        			#('Control', 'Control'),
        		]

	x_type = fields.Selection(
				selection = _type_list, 
				
				string="Tipo",

				default="consultation",
				required=True, 
				)






	_type_cal_dic = {
        			'consultation': 	'C',
        			'procedure': 		'P',
        			'session': 			'S',
        			'control': 			'X',

        			'Consulta': 	'C',
        			'Procedimiento': 		'P',
        			'Sesion': 			'S',
        			'Control': 			'X',
        		}



	_type_cal_list = [
        			('C', 'C'),
        			('P', 'P'),
        			('S', 'S'),
        			('X', 'X'),

        			#('consultation', 'C'),
        			#('procedure', 'P'),
        			#('session', 'S'),
        			#('control', 'X'),
        		]


	x_type_cal = fields.Selection(
				selection = _type_cal_list, 
				#string="Tipo",

				
				compute='_compute_x_type_cal', 
				)


	#@api.onchange('x_type')
	#def _onchange_x_type(self):
	#	self.x_type_cal = self._type_cal_dic[self.x_type]



	#@api.multi
	@api.depends('x_type')
	
	def _compute_x_type_cal(self):

		for record in self:	

			record.x_type_cal = self._type_cal_dic[record.x_type]






	# ----------------------------------------------------------- Indexes ------------------------------------------------------

	treatment = fields.Many2one('openextension.treatment',
			string="Tratamiento",
			required=False, 
			ondelete='cascade', 
			)


	consultation = fields.Many2one('openhealth.consultation',
		string="Consulta",
		ondelete='cascade', 
	)


	procedure = fields.Many2one('openhealth.procedure',
		string="Procedimiento",
		ondelete='cascade', 
	)


	session = fields.Many2one('openhealth.session',
		string="Sesión",
		ondelete='cascade', 
	)

	control = fields.Many2one('openhealth.control',
		string="Control",
		ondelete='cascade', 
	)






	#@api.multi
	#@api.depends('start_date')

	#def _compute_name(self):
	#	print 'compute name'
	#	for record in self:
	#		idx = record.id
	#		if idx < 10:
	#			pre = 'AP000'
	#		elif idx < 100:
	#			pre = 'AP00'
	#		elif idx < 1000:
	#			pre = 'AP0'
	#		else:
	#			pre = 'AP'
	#		record.name =  pre + str(idx) 
	#	print self.name 
	#	print 






# ----------------------------------------------------------- Open ------------------------------------------------------

	def open_popup(self):
	#def open_current(self):

		#the best thing you can calculate the default values 
		# however you like then pass them to the context

		print 
		print 'open popup'
		print 

		return {

        	'type': 'ir.actions.act_window',

        	'name': 'Import Module',

        	'view_type': 'form',

        	'view_mode': 'form',


			#'target': 'new',
			'target': 'current',


        	'res_model': 'oeh.medical.appointment',


        	'context': {

        			#'default_partner_id':value, 			
        			#'default_other_field':othervalues
        			
        			'default_patient':3025, 			
        			},

    		}








# ----------------------------------------------------------- CRUD ------------------------------------------------------

	#@api.multi
	#def create(self):


	@api.model
	def create(self,vals):

		print 
		print 'jx Create - Override'
		print 
		print vals
		print 
	

		print vals['appointment_date']
		appointment_date = vals['appointment_date']
		print appointment_date


		#x_date = vals['x_date']
		#print x_date

		
		x_type = vals['x_type']
		print x_type

		doctor = vals['doctor']
		print doctor

		patient = vals['patient']
		print patient


	#	print vals['duration']
	#	print vals['appointment_end']
		#print vals['x_error']
		
		print



		# Create Procedure 
		#if self.x_error == 0:
		#if True:
		if x_type == 'consultation':
			print 
			print 'Create Appointment for procedure !'



			#appointment_date = appointment_date.strftime("%Y-%m-%d %H:%M:%S")



			#app = self.create_app_procedure(appointment_date, x_date, doctor, patient)
			app = self.create_app_procedure(appointment_date, doctor, patient)
			print app 




		res = super(Appointment, self).create(vals)

		return res



	






# ----------------------------------------------------------- Create procedure  ------------------------------------------------------

	# Create app 
	@api.multi
	#def create_app_procedure(self, appointment_date, x_date, doctor_id, patient_id):
	def create_app_procedure(self, appointment_date, doctor_id, patient_id):

		date_format = "%Y-%m-%d %H:%M:%S"

		print 
		print 'create app procedure'
		#print appointment_date
		#print doctor_id
		#print patient_id


		# Consultation 
		ad_con = datetime.datetime.strptime(appointment_date, date_format)
		#print ad_con



		#delta_fix = datetime.timedelta(hours=1)
		delta_fix = datetime.timedelta(hours=0.5)
		delta_var = datetime.timedelta(hours=0.25)
		k = 0


		doctor_name = 'Dr. Chavarri'

		ret = 1



		# Loop 
		while not ret == 0:


			# Procedure 
			ad_pro = ad_con + delta_fix + k*delta_var
			#print ad_pro

			ad_pro_str = ad_pro.strftime("%Y-%m-%d %H:%M:%S")
			#print ad_pro_str



			# Check for collisions 

			ret, doctor_name, start, end = self.check_for_collision(ad_pro_str, doctor_name)



			if ret == 0: 
			

				print 'CRUD: Create !!!'

				app = self.env['oeh.medical.appointment'].create(
															{
															'appointment_date': ad_pro_str,
															'duration': 0.5,
															'patient': patient_id,	
															'doctor': doctor_id,	

															'x_type':'procedure',
															
															}
													)
			else:
				k = k + 1


		
			#if ret != 0:
			
			#			return {
			#						'warning': {
			#							'title': "Error: Colisión !",
			#							'message': 'Cita ya existente, con el ' + doctor_name + ": " + start + ' - ' + end + '.',
			#					}}


		print 
		print 'k'
		print k
		print 

		return app 





# ----------------------------------------------------------- Collision  ------------------------------------------------------

	@api.multi

	#def check_for_collision(self, appointment_date, appointment_end, duration, doctor_name, app_ids):
	#def check_for_collision(self):
	def check_for_collision(self, appointment_date, doctor_name):


		print 
		print 'Check for collision'



		#dt = self.appointment_date[2:10]
		dt = appointment_date[2:10]
		print dt
		print 


		#app_ids = self.env['oeh.medical.appointment'].search([('appointment_date', 'like', dt),  ('doctor', '=', self.doctor.name)  ])
		app_ids = self.env['oeh.medical.appointment'].search([('appointment_date', 'like', dt),  ('doctor', '=', doctor_name)  ])
		print app_ids 





		# Appointment end 
		date_format = "%Y-%m-%d %H:%M:%S"



		#delta = datetime.timedelta(hours=self.duration)
		delta = datetime.timedelta(hours=0.5)



		#sd = datetime.datetime.strptime(self.appointment_date, date_format)
		sd = datetime.datetime.strptime(appointment_date, date_format)
		
		#self.appointment_end = delta + sd
		appointment_end = delta + sd
				
		ae = appointment_end.strftime("%Y-%m-%d %H:%M:%S")






		print delta
		print sd 
		#print self.appointment_end
		print appointment_end
		print 





		# Check if Collision 
		#ad = self.appointment_date
		ad = appointment_date

		#ae = self.appointment_end
		#ae = appointment_end



		for app in app_ids:

			#print app

			start = app.appointment_date

			end = app.appointment_end


			if 	(	
					#(ad >= start and ae <= end)  or  (ad <= start and ae >= end)  or  (ad < start and ae > start)  or  (ad < end and ae > end)
					(ad >= start and ae <= end)  or  (ad <= start and ae >= end)  	or    (ad < start and ae > start)  or  (ad < end and ae > end)
				): 


				print 'Collision !!!'



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
				#return -1, self.doctor.name, start_local, end_local
				return -1, doctor_name, start_local, end_local



		# Passed test - All is Ok 
		return 0, '', '', '' 






