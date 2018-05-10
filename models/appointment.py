# -*- coding: utf-8 -*-
#
# 	*** Appointment
#

# Created: 				14 Nov 2016
# Last updated: 	 	01 Dec 2017

from openerp import models, fields, api
import datetime
from . import app_vars
from . import eval_vars
import appfuncs


class Appointment(models.Model):
	_inherit = 'oeh.medical.appointment'


	name = fields.Char(
			string="Cita #", 
			required=True, 
		)

	vspace = fields.Char(
			' ', 
			readonly=True
		)







	# ----------------------------------------------------------- Dates ------------------------------------------------------
	
	# Date 
	appointment_date = fields.Datetime(
			string="Fecha", 
			readonly=False,
			#states={'Scheduled': [('readonly', False)]}), 
		
			default = fields.Date.today, 
		)

	#'appointment_date': fields.datetime('Appointment Date',required=True, readonly=True,states={'Scheduled': [('readonly', False)]}),



	# Date end 
	appointment_end = fields.Datetime(
			string="Fecha fin", 		
			readonly=True, 
			)






	# X Date 
	x_date = fields.Date(
			string="Fecha", 

			compute="_compute_x_date",
		)

	#@api.multi
	@api.depends('appointment_date')
	def _compute_x_date(self):
		date_format = "%Y-%m-%d %H:%M:%S"
		for record in self:

			dt = datetime.datetime.strptime(record.appointment_date, date_format)
			
			#record.x_date = dt.strftime(date_format)
			record.x_date = dt.strftime("%Y-%m-%d")








	# ----------------------------------------------------------- Treatment ------------------------------------------------------

	# Treatement 
	treatment = fields.Many2one(			
			'openhealth.treatment',
			string="Tratamiento",
			ondelete='cascade', 

			#required=True, 
			required=False, 
		)



	# Treatement assignment
	@api.onchange('patient','doctor')
	def _onchange_patient_doctor(self):

		print 'jx'
		print 'On change - Patient Doctor'


		#if self.patient.name != False and self.doctor.name != False:
		if self.patient.name != False and self.doctor.name != False		and 	self.x_target != 'therapist'	:


			treatment = self.env['openhealth.treatment'].search([
																		('patient', '=', self.patient.name),			
																		('physician', '=', self.doctor.name),					
																	],
																	order='start_date desc',
																	limit=1,
																)

			if treatment.name == False: 
				print 
				print 'Create Treatement'
				treatment = self.env['openhealth.treatment'].create({
																		'patient': self.patient.id,
																		'physician': self.doctor.id,
																	})


			if treatment.name != False: 

				self.treatment = treatment
			
			else: 
				print 
				print 'ERROR !!!'
				print 'This sould not happem !'
				print 


		print self.treatment
		print 
	# _onchange_patient_doctor




# ----------------------------------------------------------- Fields - Canonical ------------------------------------------------------





	# Doctor 
	doctor = fields.Many2one(
			'oeh.medical.physician',			
			string = "Médico", 

			required=True, 
			#required=False, 
			
			readonly = False, 
		)




	# State 
	APPOINTMENT_STATUS = [			
			
			('Scheduled', 				'Confirmado'),
			
			('pre_scheduled',	 		'No confirmado'),
			
			('pre_scheduled_control', 	'Pre-cita'),
			
			('error', 					'Error'),




			#('completed', 				'Completo'),
			('invoiced', 				'Facturado'),




			# Oe Health 
			#('Scheduled', 'Scheduled'),
			#('Completed', 'Completed'),
			#('Invoiced', 'Invoiced'),

		]

	state = fields.Selection(
			selection = APPOINTMENT_STATUS, 
			string="Estado",
			default='pre_scheduled',
			readonly=False, 
			required=True, 
		)





	# Patient
	patient = fields.Many2one(
			'oeh.medical.patient',
			string = "Paciente", 	
			ondelete='cascade', 			
			#required=True, 
			readonly = False, 
		)



	# Target 
	x_target = fields.Selection(
			string="Target", 
			selection = app_vars._target_list, 
			index=True,
			required=True, 
		)




	# Duration 
	duration = fields.Float(
			string="Duración (h)", 			
			compute='_compute_duration', 
			readonly=True, 
		)

	#@api.multi
	@api.depends('x_type')
	def _compute_duration(self):
		for record in self:	
			if record.x_type == 'consultation'   or   record.x_type == 'procedure'   or   record.x_type == 'session':
				record.duration = 0.5
			elif record.x_type == 'control':
				record.duration = 0.25





	# Machine 
	x_machine = fields.Selection(
			string="Sala", 

			selection = app_vars._machines_list, 
			
			#required=True, 
		)





	#@api.onchange('x_target')
	#def _onchange_x_target(self):
	
	#	if self.x_target == 'therapist':	
			
			#self.x_machine = [
			#					('laser_triactive','Triactivo'), 
			#					('chamber_reduction','Cámara de reducción'), 
			#					('carboxy_diamond','Carboxiterapia - Punta de Diamante'), 								
			#				]


			#return {
			#			'domain': 	{	'x_machine': [
			#											#('x_pathology', '=', self.pathology)
			#											('x_zone', '=', self.zone),
			#										]
			#						},
			#}


















	# Create procedure 
	x_create_procedure_automatic = fields.Boolean(			
			string="¿ Crear Cita para el Procedimiento ?",
			default=True, 
		)





	# Type 
	_type_list = [
        			('consultation', 'Consulta'),
        			('procedure', 'Procedimiento'),
        			('session', 'Sesión'),
        			('control', 'Control'),

        			('cosmetology', 'Cosmiatría'),

        		]

	x_type = fields.Selection(
				selection = _type_list, 
				string="Tipo",
				required=True, 
				)








# ----------------------------------------------------------- Relational  ------------------------------------------------------

	consultation = fields.Many2one('openhealth.consultation',
			string="Consulta",
			#ondelete='cascade', 			# Very important. 
		)

	procedure = fields.Many2one('openhealth.procedure',
			string="Procedimiento",
			#ondelete='cascade', 
		)

	procedure_cos = fields.Many2one('openhealth.procedure.cos',
			string="Proc. - Cos",
			#ondelete='cascade', 
		)

	session = fields.Many2one('openhealth.session',
			string="Sesión",
			#ondelete='cascade', 
		)

	control = fields.Many2one('openhealth.control',
			string="Control",		
			#ondelete='cascade', 
		)













	# Number of clones  
	nr_clones = fields.Integer(
			string="nr_clones",
			compute="_compute_nr_clones",
	)
	@api.multi
	def _compute_nr_clones(self):
		for record in self:
			record.nr_clones =	self.env['oeh.medical.appointment'].search_count([
																						('appointment_date','=', record.appointment_date),
																						('doctor','=', record.doctor.name),
																					]) 
			if record.nr_clones > 1:
				record.state = 'error'






	# Number of mac_clones  
	nr_mac_clones = fields.Integer(
			string="nr_mac_clones",
			compute="_compute_nr_mac_clones",
	)
	@api.multi
	def _compute_nr_mac_clones(self):
		for record in self:

			if record.x_machine != False: 

				record.nr_mac_clones =	self.env['oeh.medical.appointment'].search_count([

																						('appointment_date','=', record.appointment_date),

																						('x_machine','=', record.x_machine),
					
																					]) 
				if record.nr_mac_clones > 1:
					record.state = 'error'

			else:
				record.nr_mac_clones = 1 












	# Display 
	x_display = fields.Char(
			compute='_compute_x_display', 
		)


	@api.multi
	#@api.depends('x_appointment')

	def _compute_x_display(self):
		for record in self:

			#record.x_display = record.x_patient_name_short + ' - '  + record.x_doctor_code + ' - ' + record.x_type_cal 


			#record.x_display = record.x_patient_name_short + ' - '  + record.x_doctor_code 
			record.x_display = record.x_patient_name_short + ' - '  + record.x_doctor_code + ' - ' + record.x_type_cal + ' - ' + record.x_state_short
			





			#if record.x_machine != False	or 	record.x_machine_cos != False:
			if record.x_machine != False:
				record.x_display = record.x_display + ' - ' + record.x_machine_short






	# State short 
	_hash_state = {
						#False:				'', 
						'Scheduled':				'1',
						'pre_scheduled':			'2',
						'pre_scheduled_control':	'3',
						'error':					'55',


						
						#'completed':				'20',
						'invoiced':					'10',
					}



	x_state_short = fields.Char(
			compute='_compute_x_state_short',
		)

	#@api.multi
	@api.depends('state')
	def _compute_x_state_short(self):
		for record in self:

			if record.state != False:
				record.x_state_short = self._hash_state[record.state]





	

	_hash_x_machine = {
							False:				'', 



							'laser_quick':		'Quick',
					
							'criosurgery':		'Crio',


							'botulinum_toxin': 			'Botox', 
							'hyaluronic_acid': 			'Hial', 
							'hyaluronic_acid_repair': 	'Hial - R', 
							'intravenous_vitamin': 		'Vit Intra', 
							'lepismatic': 				'Lepi', 
							'mesotherapy_nctf': 		'Meso', 
							'plasma': 					'Plas', 
							'sclerotherapy': 			'Escle', 




							'laser_co2_1':		'C1',
							'laser_co2_2':		'C2',
							'laser_co2_3':		'C3',
							
							'laser_excilite':	'Exc',

							'laser_m22':		'M22',

							'laser_triactive':		'Tri',
							'chamber_reduction':	'Cam',
							'carboxy_diamond':		'CaDi',
						}

	x_machine_short = fields.Char(
			compute='_compute_x_machine_short',
		)


	#@api.multi
	@api.depends('x_machine')
	def _compute_x_machine_short(self):
		for record in self:
			if record.x_machine != False:
				record.x_machine_short = self._hash_x_machine[record.x_machine]



































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













	# X Doctor Code 
	x_doctor_code = fields.Char(
			compute='_compute_x_doctor_code',
		)

	#@api.multi
	@api.depends('doctor')
	def _compute_x_doctor_code(self):
		for record in self:
			#record.x_doctor_code = self._hash_doctor_code[record.doctor.name]
			record.x_doctor_code = app_vars._hash_doctor_code[record.doctor.name]













	# On change - Machine
	@api.onchange('x_machine')
	def _onchange_x_machine(self):
		if self.x_machine != False:	
			self.x_error = 0


			# Check for collisions 
			ret, doctor_name, start, end = appfuncs.check_for_collisions(self, self.appointment_date, self.doctor.name, self.duration, self.x_machine, 'machine', self.x_type)


			if ret != 0:	# Error 
				self.x_error = 1
				self.x_machine = False
				return {
							'warning': {
									'title': "Error: Colisión !",
									'message': 'La sala ya está reservada: ' + start + ' - ' + end + '.',
						}}

			else: 			# Success 				

				# Treatment 
				self.treatment = self.env['openhealth.treatment'].search([

															('patient', 'like', self.patient.name),
															('physician', 'like', self.doctor.name),

															],
															order='start_date desc',
															limit=1,
														)

				#print self.treatment 
		#print









# ----------------------------------------------------------- On change - Doctor  ------------------------------------------------------

	@api.onchange('doctor', 'x_type')

	def _onchange_doctor(self):

		#print 
		#print 'On change Doctor'



		if self.doctor.name != False:

			self.x_error = 0




			# Check for collisions
			#ret = 0 
			ret = 1


			#appointment_date = self.appointment_date
			date_format = "%Y-%m-%d %H:%M:%S"
			delta = datetime.timedelta(hours=self.duration)



			# Auto behavior - Look for free slot 		
			while ret !=0:

				print self.appointment_date
				print 

				ret, doctor_name, start, end = appfuncs.check_for_collisions(self, self.appointment_date, self.doctor.name, self.duration, False, 'doctor', self.x_type)



				if ret != 0: 

					# New ad 
					sd = datetime.datetime.strptime(self.appointment_date, date_format)
					ad_dt = delta + sd
					ad = ad_dt.strftime("%Y-%m-%d %H:%M:%S")
					

					self.appointment_date = ad



			# Check - Deprecated 
			#if ret == 0:	# Success 
			#	tra = 1
			#else: 			#   Error
			#	self.x_error = 1
			#	self.doctor = False
			#	return {'warning': {'title': "Error: Colisión !",
			#						'message': 'Cita ya existente, con el ' + doctor_name + ": " + start + ' - ' + end + '.',
			#						}}

	# _onchange_doctor

















	x_time = fields.Char(
			string="Hora", 

			compute="_compute_x_time",
		)

	#@api.multi
	@api.depends('appointment_date')

	def _compute_x_time(self):

		#print 
		#print 'compute x_time'

		date_format = "%Y-%m-%d %H:%M:%S"
		#date_format = "%H:%M:%S"

		for record in self:
			#record.x_time = record.appointment_date
			
			#record.x_time = record.appointment_date.strftime("%H:%M:%S")


			dt = datetime.datetime.strptime(record.appointment_date, date_format)
			delta = datetime.timedelta(hours=5)
			dt = dt - delta
			#print dt

			record.x_time = dt.strftime("%H:%M:%S")

			if record.state == 'pre_scheduled_control':
				record.x_time = ''


		#print 













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
				#print 'Gotcha !!!'
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

				compute='_compute_x_type_cal', 
		)

	#@api.multi
	@api.depends('x_type')
	
	def _compute_x_type_cal(self):
		for record in self:	
			record.x_type_cal = self._type_cal_dic[record.x_type]















# ----------------------------------------------------------- Open ------------------------------------------------------

	def open_popup(self):

		return {
		        	'type': 'ir.actions.act_window',
		        	'name': 'Import Module',
		        	'view_type': 'form',
		        	'view_mode': 'form',
					#'target': 'new',
					'target': 'current',
		        	'res_model': 'oeh.medical.appointment',
		        	#'context': {
		        	#		#'default_partner_id':value, 			
		        	#		#'default_other_field':othervalues        			
		        	#		},
		    	}
	# open_popup










# ----------------------------------------------------------- Buttons - Appointment  ------------------------------------------------------

	@api.multi
	def remove_appointment(self):  

		#print 
		#print 'Remove Appointment'

		appointment_id = self.id
		#print "id: ", appointment_id
		
		rec_set = self.env['oeh.medical.appointment'].browse([appointment_id])
		#print "rec_set: ", rec_set
		
		ret = rec_set.unlink()
		#print "ret: ", ret
		#print 






# ----------------------------------------------------------- Treatment  ------------------------------------------------------


	# Button - Treatment 
	# -------------------
	@api.multi
	def open_treatment_current(self):  

		#print 
		#print 'Open Treatment'

		patient_id = self.patient.id 
		#print patient_id


		doctor_id = self.doctor.id
		#print doctor_id 


		return {

			# Mandatory 
			'type': 'ir.actions.act_window',
			'name': 'Open Treatment Current',

			# Window action 
			'res_model': 'openhealth.treatment',

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






	# Search Treatment
	@api.multi
	def search_treatment(self):

		#print 
		#print 'Search Treatment'


		treatment = self.env['openhealth.treatment'].search([

															#('patient', 'like', 'Revilla')], 
															('patient', 'like', self.patient.name),

															#('physician', 'like', 'Chavarri'),
															('physician', 'like', self.doctor.name),

															],
															order='start_date desc',
															limit=1,
														)

		self.treatment = treatment.id
		#print self.treatment  






	# Create Treatment
	@api.multi
	def create_treatment(self):

		#print 
		#print 'Create Treatment'

		patient_id = self.patient.id
		doctor_id = self.doctor.id
		start_date = self.appointment_date

		#chief_complaint = self.x_chief_complaint


		treatment = self.env['openhealth.treatment'].create(
																{
																'patient': patient_id,	

																'physician': doctor_id,

																'start_date': start_date, 

																#'chief_complaint': chief_complaint, 
																}
														)
				
		self.treatment = treatment.id

		#print self.treatment  











# ----------------------------------------------------------- CRUD ------------------------------------------------------

	@api.model
	def create(self,vals):

		#print 
		#print 'jx Create - Override'
		#print 
		#print vals
		#print 
	

		# Create Procedure 

		appointment_date = vals['appointment_date']
		x_type = vals['x_type']
		if 'doctor' in vals:
			doctor = vals['doctor']		
		if 'patient' in vals:
			patient = vals['patient']
		if 'treatment' in vals:
			treatment = vals['treatment']
		if 'cosmetology' in vals:
			cosmetology = vals['cosmetology']
		x_create_procedure_automatic = vals['x_create_procedure_automatic']

		if x_type == 'consultation'  and  x_create_procedure_automatic:
			date_format = "%Y-%m-%d %H:%M:%S"
			adate_con = datetime.datetime.strptime(appointment_date, date_format)
			delta_fix = datetime.timedelta(hours=1.5)
			adate_base = adate_con + delta_fix
			app = appfuncs.create_appointment_procedure(self, adate_base, doctor, patient, treatment, cosmetology, x_create_procedure_automatic)




		# Return 
		res = super(Appointment, self).create(vals)

		return res
	# create - CRUD

# CRUD

