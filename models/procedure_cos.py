# -*- coding: utf-8 -*-
#
# 	*** Procedure Cos
#

# Created: 				 1 Nov 2016
# Last updated: 	 	 7 Dec 2016 



from openerp import models, fields, api
from datetime import datetime

import jxvars
import cosvars

import time_funcs
import jrfuncs
import procedure_funcs
import procedure_funcs_cos


import app_vars


class ProcedureCos(models.Model):
	
	_name = 'openhealth.procedure.cos'
	
	#_inherit = 'oeh.medical.evaluation'
	_inherit = 'openhealth.procedure'





	_hash_tre = {

		'carboxytherapy': 'carboxy_diamond', 

		'triactive_carboxytherapy_reductionchamber': 'chamber_reduction',

		'diamond_tip' : 'carboxy_diamond', 

	}





	machine_cos = fields.Selection(
			string="Sala", 

			selection = app_vars._machines_cos_list, 

			#required=True, 

			compute="_compute_machine_cos",
		)


	#@api.multi
	@api.depends('product')
	
	def _compute_machine_cos(self):

		for record in self:
		
			tre = record.product.x_treatment

			mac = self._hash_tre[tre]

			#record.machine_cos = record.product.x_treatment
			record.machine_cos = mac








	#cosmetology = fields.Many2one(
	#		'openhealth.cosmetology',
	#		string="Cosmiatría", 
	#		ondelete='cascade', 
	#		)



	chief_complaint = fields.Selection(			# Necessary 
			string = 'Motivo de consulta', 

			selection = cosvars._chief_complaint_list, 

			#required=True, 
			required=False, 
			)



	session_ids = fields.One2many(
			#'openhealth.session', 
			'openhealth.session.cos', 
			
			'procedure', 

			string = "sessiones", 
			)















# ----------------------------------------------------------- Create Session - Cos ------------------------------------------------------

	@api.multi
	def create_session(self): 

		print 
		print 
		print 
		print 'jx' 
		print 'Create Sessions - Cos'




		# Initial conditions 
		procedure_id = self.id 
		patient_id = self.patient.id

		therapist_id = self.therapist.id
		
		chief_complaint = self.chief_complaint
		evaluation_type = 'Session'
		product_id = self.product.id
		cosmetology_id = self.cosmetology.id
		laser = self.laser
		


		duration = 0.5
		x_type = 'session'
		#state = 'pre_scheduled_control'
		state = 'pre_scheduled'
		x_create_procedure_automatic = False 




		#machine = 'triactive'
		machine = self.machine_cos




		# Date 		
		GMT = time_funcs.Zone(0,False,'GMT')
		evaluation_start_date = datetime.now(GMT).strftime("%Y-%m-%d %H:%M:%S")
		app_date = datetime.now(GMT).strftime("%Y-%m-%d ")
		print GMT
		print evaluation_start_date 
		print app_date



# Loop 
		# Date dictionary - Number of days for controls 
		k_dic = {
					0 :	0,

					#1 :	7,
					#2 :	15,
					1 :	1,
					2 :	2,

					3 :	21,
					3 :	30,
					4 :	60,
					5 :	120,
				}



		#for k in range(0,6): 
		#for k in range(0,1): 
		for k in range(0,2): 

			delta = 0 
			nr_days = k_dic[k] + delta 





			# session date 
			session_date = procedure_funcs.get_control_date(self, evaluation_start_date, nr_days)
			session_date_str = session_date.strftime("%Y-%m-%d")		
			





			# First - Today - The app already exists !  
			if k == 0:
				
				appointment_date = session_date_str + ' '
				print 'appointment_date: ', appointment_date



				# Search Appointment 
				appointment = self.env['oeh.medical.appointment'].search([ 	
																			('appointment_date', 'like', app_date),	



																			('patient', 'like', self.patient.name),	
																			('x_therapist', 'like', self.therapist.name), 	
																			('x_type', 'like', 'procedure'), 
																		], 
																			order='appointment_date desc', limit=1)

				#print appointment




			#if appointment == False: 

			else: 	# Create Appointment 

	
				#appointment_date = session_date_str
				appointment_date_str = session_date_str + ' 14:0:0'




				#appointment_date_str = procedure_funcs_cos.check_and_push(self, appointment_date_str, duration, x_type, doctor_name, machine)




				print 'appointment_date: ', appointment_date

				appointment = self.env['oeh.medical.appointment'].create({
																		'appointment_date': appointment_date_str,



																		'duration': duration,
															
																		'x_type': x_type,

																		'state': state,

																		'patient': patient_id,	

																		#'doctor': doctor_id,
																		'x_therapist': therapist_id,

																		#'x_chief_complaint': chief_complaint, 

																		'x_create_procedure_automatic': x_create_procedure_automatic,

																		#'treatment': treatment_id, 
																		'cosmetology': cosmetology_id, 

																		'x_target': 'therapist',



																		'x_machine_cos': machine,
																	})







			appointment_id = appointment.id
			print appointment
			print appointment_id


			# Crate Session 
			print 'create session'
			session = self.env['openhealth.session.cos'].create(
												{

													#'evaluation_start_date': evaluation_start_date,
													'evaluation_start_date':session_date,


													'procedure': procedure_id,				

													'patient': patient_id,

													'therapist': therapist_id,													
													
													'chief_complaint': chief_complaint,


													'evaluation_type':evaluation_type,

													'product': product_id,
													
													'laser': laser,

													'appointment': appointment_id,

													'cosmetology': cosmetology_id,				
												}
											)
			session_id = session.id 
			print session
			print session_id



			# Update - Deprecated - For Cos 
			#ret = jrfuncs.update_appointment_go(self, appointment_id, session_id, 'session')



			#print appointment
			#print appointment.session
			#print appointment.session.id
			print 
			print 
			print 





		#return {
		#	'type': 'ir.actions.act_window',
		#	'name': 'Open session Current',		
		#	'res_model': 'openhealth.session.cos',
		#	'res_id': session_id,
		#	'view_mode': 'form',
		#	"views": [[False, "form"]],
		#	'target': 'current',
		#	'flags': {
		#			'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
		#			},			
		#	'context':   {
		#					'default_procedure': procedure_id,
		#					'default_patient': patient_id,
		#					'default_therapist': therapist_id,
		#					'default_chief_complaint': chief_complaint,
		#					'default_evaluation_start_date': evaluation_start_date,
		#					'default_evaluation_type':evaluation_type,
		#					'default_product': product_id,
		#					'default_laser': laser,
		#					'default_appointment': appointment_id,
		#					'default_cosmetology': cosmetology_id,
		#				}
		#}

		ret = 0
		return ret	


	# create_session




