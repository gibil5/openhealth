# -*- coding: utf-8 -*-
#
# 	*** Appointment
#

# Created: 				14 Nov 2016
# Last updated: 	 	 7 Dec 2016 



from openerp import models, fields, api
#from datetime import datetime
import datetime

import appfuncs
import time_funcs
import jxvars



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


	x_error = fields.Integer(
			
			default = 0, 
			required=True, 
		)




	# Create procedure 
	x_create_procedure_automatic = fields.Boolean(
			
			#string="¿ Crear procedimiento de manera automática ?",
			string="¿ Crear procedimiento ?",

			default=True, 
			
			#required=True, 
		)






	# Chief complaint 
	x_chief_complaint = fields.Selection(			# Necessary 
			string = 'Motivo de consulta', 

			#selection = jxvars._pathology_list, 
			selection = jxvars._chief_complaint_list, 

			#required=True, 
			)


	#jxx
	@api.onchange('x_chief_complaint')

	def _onchange_x_chief_complaint(self):

		print 
		print 'On change Chief complaint'


		if self.x_chief_complaint != False:	

			#t = self.env['openextension.treatment'].search([	
			#													('chief_complaint', 'like', self.x_chief_complaint), 
			#													('patient', 'like', self.patient.name),
			#												])

			t = self.env['openextension.treatment'].search([
																#('chief_complaint', 'like', 'acne_active'), 
																('chief_complaint', 'like', self.x_chief_complaint), 

																#('patient', 'like', 'Revilla')], 
																('patient', 'like', self.patient.name),


																#('physician', 'like', 'Chavarri'),
																('physician', 'like', self.doctor.name),


																],
																order='start_date desc',
																limit=1,
															)


			print t
			#if not (t == False  or  t == nil):



			#if t != False:
			if len(t) == 1:
				print 'found'
				self.treatment = t.id



			else:
				print 'empty'

				#self.open_treatment_current()

				#return {
				#	'warning': {
				#		'Cita': "Error: El Tratamiento no existe.",
						#'Para el paciente': self.patient.name,
				#	}}


			
			print self.treatment 

		print 







	APPOINTMENT_STATUS = [
			

			# jx 
			#('pre_scheduled', 			'Pre-scheduled'),
			#('pre_scheduled_control', 	'Pre-scheduled Control'),

			('pre_scheduled_control', 	'Pre-cita control'),
			('pre_scheduled', 			'No confirmado'),



			# OeHealth 
			#('Scheduled', 'Scheduled'),
			#('Completed', 'Completed'),
			#('Invoiced', 'Invoiced'),

			('Scheduled', 'Confirmado'),
			
			#('Completed', 'Completo'),
			#('Invoiced', 'Facturado'),

		]


	state = fields.Selection(
			selection = APPOINTMENT_STATUS, 
			readonly=False, 
		)





	APPOINTMENT_STATUS_PROXY = [
									('pre_scheduled', 	'No confirmado'),
									('Scheduled', 		'Confirmado'),
								]

	x_state_proxy = fields.Selection(
			selection = APPOINTMENT_STATUS_PROXY, 
		)








	# Patient

	patient = fields.Many2one(
			'oeh.medical.patient',
			
			string = "Paciente", 	

			default=3025, 		# Revilla 
			#default=3052, 		# Suarez Vertiz

			#required=True, 
		)







	x_patient_name_short = fields.Char(
			compute='_compute_x_patient_name_short', 
		)


	#@api.multi
	@api.depends('patient')

	def _compute_x_patient_name_short(self):
		for record in self:

			patient_name = record.patient.name

			first_half = patient_name.split(' ')[0]

			record.x_patient_name_short = first_half









	# Hash 

	_hash_doctor_code = {
							'Dra. Acosta':		'Dra. A',

							'Dr. Canales':		'Dr. Ca',

							'Dr. Chavarri':		'Dr. Ch',

							'Dr. Gonzales':		'Dr. Go',

							'Dr. Escudero':		'Dr. Es',

							'Dr. Vasquez':		'Dr. Va',

							#'Pre-control':		'Pre-control',
							'Pre-cita':		'Pre-cita',
		}



	# Doctor 

	doctor = fields.Many2one(
			'oeh.medical.physician',
			
			#default=1, 		# Chavarri

			#string = "Médico", 	
			#required=True, 
			)



	x_doctor_code = fields.Char(
			compute='_compute_x_doctor_code',
		)

	#@api.multi
	@api.depends('doctor')

	def _compute_x_doctor_code(self):
		for record in self:

			record.x_doctor_code = self._hash_doctor_code[record.doctor.name]





	#@api.onchange('doctor', 'duration')
	@api.onchange('doctor', 'x_type')

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
			#self.x_create_procedure_automatic = True



			# Check for collisions
			#ret, doctor_name, start, end = self.check_for_collision(self.appointment_date, self.doctor.name, self.duration)
			ret, doctor_name, start, end = appfuncs.check_for_collisions(self, self.appointment_date, self.doctor.name, self.duration)



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

			#readonly=True,
			readonly=False,

			#states={'Scheduled': [('readonly', False)]})
			)


	x_date = fields.Date(
			string="Fecha", 

			#default = fields.Date.today, 
			compute="_compute_x_date",
			#required=True, 
		)

	#@api.multi
	@api.depends('appointment_date')

	def _compute_x_date(self):

		date_format = "%Y-%m-%d %H:%M:%S"
		#date_format = "%Y-%m-%d"

		for record in self:
			#record.x_date = record.appointment_date
			#record.x_date = record.appointment_date.strftime("%Y-%m-%d")

			dt = datetime.datetime.strptime(record.appointment_date, date_format)


			record.x_date = dt.strftime("%Y-%m-%d")




	#x_time = fields.Date(
	#x_time = fields.Datetime(
	x_time = fields.Char(
			string="Hora", 

			compute="_compute_x_time",
		)

	#@api.multi
	@api.depends('appointment_date')

	def _compute_x_time(self):

		print 
		print 'compute x_time'

		date_format = "%Y-%m-%d %H:%M:%S"
		#date_format = "%H:%M:%S"

		for record in self:
			#record.x_time = record.appointment_date
			
			#record.x_time = record.appointment_date.strftime("%H:%M:%S")


			dt = datetime.datetime.strptime(record.appointment_date, date_format)
			delta = datetime.timedelta(hours=5)
			dt = dt - delta
			print dt


			record.x_time = dt.strftime("%H:%M:%S")


		print 





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


			'Procedimiento': 1,
			'procedure': 1,

			'Consulta': 2,
			'consultation': 2,



			'procedure_pre_scheduled': 3,
			

			'Sesion': 4,
			'session': 4,

			
			'Control': 5,
			'control': 5,
			
		}


	color_x_type_id = fields.Integer(
			default=1,
			compute='_compute_color_x_type_id', 
		)


	#@api.multi
	@api.depends('x_type')
	def _compute_color_x_type_id(self):
		for record in self:	

			if record.x_type == 'procedure'   and   record.state == 'Pre-scheduled':
				print 'Gotcha !!!'
				record.color_x_type_id = self._hash_colors_x_type['procedure_pre_scheduled']

			else:
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
		
			#default = '0.5',
			#default = '0.25',

			#readonly=True,
		)





	#@api.onchange('x_type')

	#def _onchange_x_type(self):

	#	if self.x_type != False:	

	#		if self.x_type == 'consultation'  or  self.x_type == 'procedure':

	#			self.x_duration_min = '0.5'

	#		elif self.x_type == 'control':

	#			self.x_duration_min = '0.25'







	#@api.onchange('x_duration_min')
	#def _onchange_x_duration_min(self):
	#	if self.x_duration_min != False:	
			#self.duration = self._hash_duration[self.x_duration_min]
	#		self.duration = self._hash_duration[self.x_duration_min]









	# Duration 


	duration = fields.Float(
			string="Duración (h)", 
			
			#default = 0.5,
			#default = 0.25,

			compute='_compute_duration', 

			readonly=True, 
		)

	#@api.multi
	@api.depends('x_type')
	
	def _compute_duration(self):

		for record in self:	

			#if record.x_type == 'consultation'  or  record.x_type == 'procedure':
			if record.x_type == 'consultation'   or   record.x_type == 'procedure'   or   record.x_type == 'session':

				record.duration = 0.5

			elif record.x_type == 'control':
			#elif record.x_type == 'control'  or  record.x_type == 'session':

				record.duration = 0.25








	


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
        			
        			#'control': 			'X',


        			'Consulta': 	'C',
        			'Procedimiento': 		'P',
        			'Sesion': 			'S',


        			#'X': 			'Ctl',
        			'control': 			'Ctl',
        			'Control': 			'Ctl',
        		}



	_type_cal_list = [
        			('C', 'C'),
        			('P', 'P'),
        			('S', 'S'),

        			#('X', 'Ctl'),
        			('Ctl', 'Ctl'),

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
			ondelete='cascade', 

			#required=False, 
			#required=True, 
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

	@api.model
	def create(self,vals):

		#print 
		#print 'jx Create - Override'
		#print 
		#print vals
		#print 
	

		appointment_date = vals['appointment_date']
		x_type = vals['x_type']
		doctor = vals['doctor']
		patient = vals['patient']
		treatment = vals['treatment']
		x_create_procedure_automatic = vals['x_create_procedure_automatic']
		x_chief_complaint = vals['x_chief_complaint']


		#print appointment_date
		#print x_type
		#print doctor
		#print patient
		#print treatment
		#print x_create_procedure_automatic 
		#print x_chief_complaint
		#print



		# Create Procedure 
		#if x_type == 'consultation':
		if x_type == 'consultation'  and  x_create_procedure_automatic:
			#print 
			#print 'Create Appointment for procedure !'

			app = self.create_app_procedure(appointment_date, doctor, patient, treatment, x_chief_complaint, x_create_procedure_automatic)
			
			#print app 


		# Return 
		res = super(Appointment, self).create(vals)

		return res






# ----------------------------------------------------------- Create procedure  ------------------------------------------------------

	# Create app 
	@api.multi
	def create_app_procedure(self, appointment_date, doctor_id, patient_id, treatment_id,  x_chief_complaint, x_create_procedure_automatic):

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
		#delta_fix = datetime.timedelta(hours=0.5)
		delta_fix = datetime.timedelta(hours=1.5)

		delta_var = datetime.timedelta(hours=0.25)
		k = 0



		#doctor_name = 'Dr. Chavarri'
		doctor = self.env['oeh.medical.physician'].search([('id', '=', doctor_id)])
		doctor_name = doctor.name



		duration = 0.5 


		ret = 1



		# Loop 
		while not ret == 0:


			# Procedure 
			ad_pro = ad_con + delta_fix + k*delta_var
			#print ad_pro

			ad_pro_str = ad_pro.strftime("%Y-%m-%d %H:%M:%S")
			#print ad_pro_str




			# Check for collisions 
			#ret, doctor_name, start, end = self.check_for_collision(ad_pro_str, doctor_name, duration)
			ret, doctor_name, start, end = appfuncs.check_for_collisions(self, ad_pro_str, doctor_name, duration)




			if ret == 0: 	# Success ! - No Collisions
			

				print 'CRUD: Create !!!'

				app = self.env['oeh.medical.appointment'].create(
															{
															'appointment_date': ad_pro_str,
															
															'duration': duration,
															

															'x_type':'procedure',
															
															#'state':'Pre-scheduled',
															'state':'pre_scheduled',

															'patient': patient_id,	
															'doctor': doctor_id,

															'treatment': treatment_id, 

															'x_create_procedure_automatic': x_create_procedure_automatic,
															'x_chief_complaint': x_chief_complaint, 

															}
													)
			else:			# Collision 
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









# ----------------------------------------------------------- Treatment  ------------------------------------------------------


	# Button - Treatment 
	# -------------------
	@api.multi
	def open_treatment_current(self):  

		print 
		print 'Open Treatment'

		#patient_id = self.id 
		patient_id = self.patient.id 
		print patient_id


		doctor_id = self.doctor.id
		print doctor_id 


		return {

			# Mandatory 
			'type': 'ir.actions.act_window',
			'name': 'Open Treatment Current',

			# Window action 
			'res_model': 'openextension.treatment',

			# Views 
			"views": [[False, "form"]],
			'view_mode': 'form',


			#'target': 'current',
			#'target': 'inline'.
			'target': 'new',


			'flags': {
						'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
						#'form': {'action_buttons': True, }
					},


			'context':   {
				'search_default_patient': patient_id,

				'default_patient': patient_id,

				'default_doctor': doctor_id,

			}

		}





	# Create Treatment
	@api.multi
	def create_treatment(self):

		print 
		print 'Create Treatment'

		patient_id = self.patient.id
		doctor_id = self.doctor.id
		start_date = self.appointment_date

		chief_complaint = self.x_chief_complaint


		treatment = self.env['openextension.treatment'].create(
																{

																'patient': patient_id,	

																'physician': doctor_id,

																'start_date': start_date, 

																'chief_complaint': chief_complaint, 

																}
														)
				
		self.treatment = treatment.id

		print self.treatment  




