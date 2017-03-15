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




class ProcedureCos(models.Model):
	
	_name = 'openhealth.procedure.cos'
	
	#_inherit = 'oeh.medical.evaluation'
	_inherit = 'openhealth.procedure'





# ----------------------------------------------------------- Relational ------------------------------------------------------

	session_ids = fields.One2many(

			#'openhealth.session', 
			'openhealth.session.cos', 
			
			'procedure', 

			string = "sessiones", 
			)




	treatment = fields.Many2one(
			'openhealth.treatment',
			#string="Tratamiento", 
			#ondelete='cascade', 

			required=False, 
			)




	doctor = fields.Many2one(
			'oeh.medical.physician',

			string = "Cosmeatra", 	
			
			)





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















# ----------------------------------------------------------- Keys  ------------------------------------------------------

	key = fields.Char(
			string='key', 
			
			default='procedure_cos', 
		)


	model = fields.Char(
			string='model', 

			default='openhealth.session.cos', 
		)


	target = fields.Char(
			string='target', 

			default='therapist', 
		)


# ----------------------------------------------------------- Create Sessions - Cos ------------------------------------------------------

	@api.multi
	def create_sessions(self): 

		print 
		print 
		print 
		print 'jx' 
		print 'Create Sessions - Cos'


		model = 'openhealth.session.cos'
		ret = procedure_funcs.create_sessions_go(self, model)


		print 
		print 

	# create_sessions





 # ----------------------------------------------------------- Create Session One ------------------------------------------------------

	@api.multi
	def create_session_one(self): 

		print 
		print 
		print 'Create session one'


		# Data
		procedure_id = self.id 

		patient_id = self.patient.id

		doctor_id = self.doctor.id

		chief_complaint = self.chief_complaint
		
		evaluation_type = 'Session'
		
		product_id = self.product.id


		#treatment_id = self.treatment.id
		treatment_id = False
		cosmetology_id = self.cosmetology.id


		laser = self.laser
		


		# Date 		
		GMT = time_funcs.Zone(0,False,'GMT')
		evaluation_start_date = datetime.now(GMT).strftime("%Y-%m-%d %H:%M:%S")



		# Apointment 
		appointment = self.env['oeh.medical.appointment'].search([ 	
																	('patient', 'like', self.patient.name),		
																	('doctor', 'like', self.doctor.name), 	
																	('x_type', 'like', 'procedure'), 
																], 
																order='appointment_date desc', limit=1)

		appointment_id = appointment.id


		print 'procedure_id: ', procedure_id
		print 'patient_id: ', patient_id
		print 'doctor_id: ', doctor_id
		print 'chief_complaint: ', chief_complaint
		print 'evaluation_type: ', evaluation_type
		print 'product_id: ', product_id

		print 'treatment_id: ', treatment_id
		print 'cosmetology_id: ', cosmetology_id

		print 'laser: ', laser

		print 
		print 'GMT: ', GMT
		print 'evaluation_start_date: ', evaluation_start_date 
		print 'appointment: ', appointment
		print 'appointment_id: ', appointment_id
		print 


		# session 
		print 'create session'
		print 
		

		#session = self.env['openhealth.session'].create(
		session = self.env['openhealth.session.cos'].create(
		

												{
													'patient': patient_id,

													'doctor': doctor_id,													

													
													'chief_complaint': chief_complaint,

													'evaluation_start_date': evaluation_start_date,
													'evaluation_type':evaluation_type,
													
													'product': product_id,
													'laser': laser,


													'procedure': procedure_id,				
													'appointment': appointment_id,

													'treatment': treatment_id,				
													'cosmetology': cosmetology_id,				
												}
											)
		session_id = session.id 
		print session
		print session_id


		# Update
		#self.update_appointment(appointment_id, session_id, 'session')
		ret = jrfuncs.update_appointment_go(self, appointment_id, session_id, 'session')

		print appointment
		print appointment.session
		print appointment.session.id
		print 





		return {

			# Mandatory 
			'type': 'ir.actions.act_window',
			'name': 'Open session Current',
		
			# Optional 
			#'res_model': 'openhealth.session',
			'res_model': 'openhealth.session.cos',

			'res_id': session_id,

			'view_mode': 'form',
			"views": [[False, "form"]],
			'target': 'current',

			'flags': {
					#'form': {'action_buttons': True, }
					'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
					},			

			'context':   {
							'default_patient': patient_id,
							'default_doctor': doctor_id,

							'default_chief_complaint': chief_complaint,
							
							'default_evaluation_start_date': evaluation_start_date,
							'default_evaluation_type':evaluation_type,
							'default_product': product_id,
							'default_laser': laser,



							'default_procedure': procedure_id,
							'default_appointment': appointment_id,

							'default_treatment': treatment_id,
							'default_cosmetology': cosmetology_id,
						}
		}


	# create_session_one





