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

	_name = 'openhealth.appointment.cos'





	x_machine = fields.Selection(
			string="Sala", 

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

	_hash_doctor_code = {
							False:				'', 

							'Eulalia':		'EU',
		}






	# X Doctor Code 
	x_doctor_code = fields.Char(
			compute='_compute_x_doctor_code',
		)

	#@api.multi
	@api.depends('x_therapist')
	def _compute_x_doctor_code(self):
		for record in self:

			record.x_doctor_code = self._hash_doctor_code[record.x_therapist.name]









	# ----------------------------------------------------------- On Change - Patient Therapist ------------------------------------------------------

#	@api.onchange('patient','x_therapist')
#	def _onchange_patient_therapist(self):

#		print 
#		print 'jx'
#		print 'On Change PT'

#		if self.patient != False and self.x_therapist != False:
				

#			cosmetology = self.env['openhealth.cosmetology'].search([
#																				('patient', 'like', self.patient.name),
#																				('therapist', 'like', self.x_therapist.name),
#																			],
#																				order='start_date desc',
#																				limit=1,
#																			)
#			self.cosmetology = cosmetology

#			print 'jx'









