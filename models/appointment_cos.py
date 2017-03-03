# -*- coding: utf-8 -*-
#
# 	*** Appointment - Cos
#

# Created: 				25 Feb 2017
# Last updated: 	 	25 Feb 2017 





from openerp import models, fields, api

#import datetime
#import time_funcs
#import jxvars


import defaults
import app_vars
import appfuncs


class AppointmentCos(models.Model):

	#_name = 'openhealth.appointment.cos'

	#_inherit = 'openhealth.appointment'
	_inherit = 'oeh.medical.appointment'











	x_therapist = fields.Many2one(
			'openhealth.therapist',
			
			string = "Cosmeatra", 	

			#default=defaults._therapist,

			#required=True, 
			required=False, 
			readonly = False, 
			)




	cosmetology = fields.Many2one(
			'openhealth.cosmetology',
			string="Cosmiatría",
			ondelete='cascade', 

			required=False, 
			#required=True, 
			)





	#appointment_date = fields.Datetime(
	#		string="Fecha", 
	#		readonly=False,
			#states={'Scheduled': [('readonly', False)]})
	#		)

	#appointment_end = fields.Datetime(
	#		string="Fecha fin", 		
	#		readonly=True, 
	#		)

	#duration = fields.Float(
	#		string="Duración (h)", 			
	#		compute='_compute_duration', 
	#		readonly=True, 
	#	)







	# ----------------------------------------------------------- Computes ------------------------------------------------------

	# Hash 

	_hash_therapist_code = {
							False:				'', 

							'Eulalia':		'EU',
		}


	# X Doctor Code 
	#x_doctor_code = fields.Char(
	#		compute='_compute_x_doctor_code',
	#	)

	#@api.multi
	#@api.depends('x_therapist')
	@api.depends('doctor', 'x_therapist')

	def _compute_x_doctor_code(self):
		for record in self:

			if record.doctor.name != False:
				record.x_doctor_code = self._hash_doctor_code[record.doctor.name]
			else: 
				record.x_doctor_code = self._hash_therapist_code[record.x_therapist.name]














	# ----------------------------------------------------------- On Change - Patient Therapist ------------------------------------------------------

	@api.onchange('patient','x_therapist')
	def _onchange_patient_therapist(self):

		print 
		print 'jx'
		print 'On Change PT'

		if self.patient != False and self.x_therapist != False:
				

			cosmetology = self.env['openhealth.cosmetology'].search([
																				('patient', 'like', self.patient.name),
																				('therapist', 'like', self.x_therapist.name),
																			],
																				order='start_date desc',
																				limit=1,
																			)
			self.cosmetology = cosmetology

			print 'jx'

		# _onchange_patient_therapist






	# ----------------------------------------------------------- On Change - Therapist ------------------------------------------------------


	#@api.onchange('x_therapist', 'x_type')
	#@api.onchange('x_therapist', 'x_type')
	@api.onchange('x_therapist')

	def _onchange_x_therapist(self):

		print 
		print 'jx'
		print 'On change - Therapist'

		#print self.x_machine_cos
		print self.x_therapist.name



		if self.x_therapist.name != False:

			print self.x_therapist.name
			print self.patient.name
			print self.appointment_date
			print self.x_date
			print self.duration
			print self.appointment_end

			print self.x_type  
			print 

			#self.x_error = 0




			# Check for collisions
			ret = 0 

			#ret, x_therapist_name, start, end = appfuncs.check_for_collisions(self, self.appointment_date, self.x_therapist.name, self.duration, False, 'therapist')
			ret, x_therapist_name, start, end = appfuncs.check_for_collisions(self, self.appointment_date, self.x_therapist.name, self.duration, False, 'therapist', self.x_type)

			print ret 




			if ret != 0:	# Error 

				print 'Error: Collision !'
				print 


				#self.x_error = 1
				self.x_therapist = False

				return {
							'warning': {
									'title': "Error: Colisión !",
									'message': 'Cita ya existente, con la Cosmeatra ' + x_therapist_name + ": " + start + ' - ' + end + '.',
						}}


			else: 			# Success  

				print 'Success !'
				print 


		print 

	# _onchange_x_therapist



