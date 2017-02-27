# -*- coding: utf-8 -*-
#
# 	*** Appointment - Cos
#

# Created: 				25 Feb 2017
# Last updated: 	 	25 Feb 2017 





from openerp import models, fields, api

#import datetime
#import appfuncs
#import time_funcs
#import jxvars


import defaults
import app_vars


class AppointmentCos(models.Model):


	#_inherit = 'openhealth.appointment'
	_inherit = 'oeh.medical.appointment'

	#_name = 'openhealth.appointment.cos'





	x_machine_cos = fields.Selection(
			string="Sala Cos", 

			selection = app_vars._machines_cos_list, 

			#required=True, 
		)






	x_therapist = fields.Many2one(
			'openhealth.therapist',
			
			string = "Cosmeatra", 	

			default=defaults._therapist,

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






	_hash_x_machine_cos = {
							False:				'', 

							#'laser_co2_1':		'C1',
							#'laser_co2_2':		'C2',
							#'laser_co2_3':		'C3',
							
							'laser_triactive':		'Tri',
							'chamber_reduction':	'Cam',
							'carboxy_diamond':		'CaDi',
						}





	@api.multi
	#@api.depends('x_machine')
	#@api.depends('x_machine', 'x_machine_cos')
	def _compute_x_machine_short(self):
		for record in self:

			#if record.x_machine != '':
			if record.doctor.name != False:
				record.x_machine_short = self._hash_x_machine[record.x_machine]
			else:
				record.x_machine_short = self._hash_x_machine_cos[record.x_machine_cos]





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









