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











	#x_therapist = fields.Many2one(
			#'openhealth.therapist',
	#		'oeh.medical.physician',

	#		domain = [						
	#					('x_therapist', '=', True),
	#				],
			
	#		string = "Cosmeatra", 	

			#default=defaults._therapist,

	#		required=False, 
	#		readonly = False, 
	#		)






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

	#_hash_therapist_code = {
	#						False:				'', 

	#						'Eulalia':		'EU',
	#						'Eulalia 2':	'EU2',
	#						'Eulalia 3':	'EU3',
	#	}


	# X Doctor Code 
	#x_doctor_code = fields.Char(
	#		compute='_compute_x_doctor_code',
	#	)

	#@api.multi
	#@api.depends('x_therapist')
	#@api.depends('doctor', 'x_therapist')
	@api.depends('doctor')

	def _compute_x_doctor_code(self):
		for record in self:

			#if record.doctor.name != False:
			#	record.x_doctor_code = self._hash_doctor_code[record.doctor.name]
			#else: 
			#	record.x_doctor_code = self._hash_therapist_code[record.x_therapist.name]


			#record.x_doctor_code = self._hash_doctor_code[record.doctor.name]
			record.x_doctor_code = app_vars._hash_doctor_code[record.doctor.name]








