# -*- coding: utf-8 -*-
#
#
# 		*** OPEN HEALTH - Cosmetology
# 
# Created: 				18 Feb 2017
# Last updated: 	 	Id.



from openerp import models, fields, api

import jxvars


#import treatment_funcs
import cos_funcs


import time_funcs
from datetime import datetime


import cosvars

import procedure_funcs



class Cosmetology(models.Model):
	
	_inherit = 'openhealth.process'	
	_name = 'openhealth.cosmetology'
	


# ----------------------------------------------------------- Canonicals ------------------------------------------------------

	name = fields.Char(
			string="Cosmiatría #", 
			compute='_compute_name', 
		)







	# Reservations 
	reservation_ids = fields.One2many(

			'oeh.medical.appointment', 

			'cosmetology', 

			string = "Reserva de sala", 

			domain = [						
						#('x_target', '!=', 'doctor'),
						#('x_target', 'in', 'doctor'),
						#('treatment', 'like', 'TR000073'),
						('x_machine', '!=', 'false'),
					],
			)






	consultation_ids = fields.One2many(
			#'openhealth.consultation', 
			'openhealth.consultation.cos', 
			'cosmetology', 
			string = "Consultas", 
			)







	#therapist = fields.Many2one(
	physician = fields.Many2one(
			#'openhealth.therapist',
			'oeh.medical.physician',


			string = "Cosmeatra", 	


			domain = [						
						('x_therapist', '=', True),
					],


			#required=True, 
			)





	patient = fields.Many2one(
			'oeh.medical.patient',
			string='Paciente', 
			required=True, 
			)



	chief_complaint = fields.Selection(

			#selection = jxvars._chief_complaint_list, 
			selection = cosvars._chief_complaint_list, 
		
			required=True, 
			)




	# State 
	_state_list = [
        			#('empty', 			'Inicio'),


        			('appointment', 	'Cita'),

        			('service', 		'Servicio'),
        			
        			('budget', 			'Presupuesto'),

        			('invoice', 		'Facturado'),
        			
					('consultation', 	'Consulta'),

        			('procedure', 		'Procedimiento'),

        			('sessions', 		'Sesiones'),

        			#('controls', 		'Controles'),

        			#('done', 			'Completo'),
        		]


	state = fields.Selection(
			selection = _state_list, 
			string='State', 			
			default = False, 

			compute="_compute_state",
		)



	def _compute_state(self):
		for record in self:


			state = False





			if record.nr_appointments > 0:
				state = 'appointment'


			if record.nr_services > 0:
				state = 'service'

			if record.nr_budgets > 0:
				state = 'budget'

			if record.nr_invoices > 0:
				state = 'invoice'



			if record.nr_consultations > 0:
				state = 'consultation'



			if record.nr_procedures > 0:
				state = 'procedure'

			if record.nr_sessions > 0:
				state = 'sessions'



			#if record.nr_controls > 0:
			#	state = 'controls'



			record.state = state






# ----------------------------------------------------------- Number ofs ------------------------------------------------------


	# Number of Appointments  
	nr_appointments = fields.Integer(
			string="Nr Citas",
			compute="_compute_nr_appointments",
		)
	
	@api.multi
	def _compute_nr_appointments(self):
		for record in self:

			appointments =		self.env['oeh.medical.appointment'].search_count([
																						('cosmetology','=', record.id),
																					])

			record.nr_appointments = appointments 





	# Number of Services  
	nr_services = fields.Integer(
			string="Servicios",
			compute="_compute_nr_services",
		)
	
	@api.multi
	def _compute_nr_services(self):
		for record in self:

			services =		self.env['openhealth.service.cosmetology'].search_count([
																						('cosmetology','=', record.id),
																					]) 
			record.nr_services = services 





	# Budgets
	nr_budgets = fields.Integer(
			string="Presupuestos",
			compute="_compute_nr_budgets",
	)
	@api.multi
	def _compute_nr_budgets(self):
		for record in self:

			record.nr_budgets=self.env['sale.order'].search_count([
																		('cosmetology','=', record.id),

																		#('state','=', 'draft'),

																		#('x_family','=', 'private'),
																	]) 



	# Number of invoices 
	nr_invoices = fields.Integer(
			string="Facturas",
			compute="_compute_nr_invoices",
	)
	@api.multi
	def _compute_nr_invoices(self):
		for record in self:

			record.nr_invoices=self.env['sale.order'].search_count([
																		('cosmetology','=', record.id),
																		
																		('state','=', 'sale'),
																	]) 






	# Number of consultations 
	nr_consultations = fields.Integer(
			string="Consultas",
			compute="_compute_nr_consultations",
	)
	@api.multi
	def _compute_nr_consultations(self):
		for record in self:

			record.nr_consultations=self.env['openhealth.consultation.cos'].search_count([
																						('cosmetology','=', record.id),
																					]) 










	# Number of Procedures 
	nr_procedures = fields.Integer(
			string="Procedimientos",
			compute="_compute_nr_procedures",
	)
	@api.multi
	def _compute_nr_procedures(self):
		for record in self:

			record.nr_procedures=self.env['openhealth.procedure.cos'].search_count([
																						('cosmetology','=', record.id),
																					]) 






	# Number of Sessions 
	nr_sessions = fields.Integer(
			string="Sesiones",
			compute="_compute_nr_sessions",
	)
	@api.multi
	def _compute_nr_sessions(self):
		for record in self:

			record.nr_sessions=self.env['openhealth.session.cos'].search_count([
																				('cosmetology','=', record.id),
																			]) 










# ----------------------------------------------------------- Relationals ------------------------------------------------------



	service_ids = fields.One2many(
			'openhealth.service.cosmetology', 	

			'cosmetology', 
			string="Servicios"
		)





	procedure_ids = fields.One2many(
			#'openhealth.procedure', 
			'openhealth.procedure.cos', 

			'cosmetology', 
			string = "Procedimientos", 
			)





	session_ids = fields.One2many(
		
			#'openhealth.session', 
			'openhealth.session.cos', 

			'cosmetology', 

			string = "Sesiones", 
			)




	#quotation_ids = fields.One2many(
	#		'sale.order',	
	#		'cosmetology', 		
	#		string="Presupuestos",
	#		domain = [
						#('state', '=', 'pre-draft'),
						#('state', 'in', ['draft', 'sent', 'sale', 'done'])
						#('x_family', '=', 'private'),
	#				],
	#		)

	#sale_ids = fields.One2many(
	#		'sale.order',			 
	#		'cosmetology', 
	#		string="Ventas",
	#		domain = [
						#('state', '=', 'sale'),
	#					('state', 'in', ['sale', 'done'])
	#				],
	#		)





	order_ids = fields.One2many(
			'sale.order',	
			'cosmetology', 		
			string="Presupuestos",
			)







	appointment_ids = fields.One2many(


			'oeh.medical.appointment', 
			#'openhealth.appointment.cos', 
			

			'cosmetology', 
			string = "Citas", 

			domain = [
						('x_target', '=', 'therapist'),
					],
			
			)



# ----------------------------------------------------------- Computes ------------------------------------------------------
	@api.multi
	#@api.depends('start_date')

	def _compute_name(self):
		for record in self:
			record.name = 'CO0000' + str(record.id) 







# ----------------------------------------------------------- Open Line Current ------------------------------------------------------
	@api.multi
	def open_line_current(self):  

		cosmetology_id = self.id 

		return {
				'type': 'ir.actions.act_window',
				'name': ' Edit Cosmetology Current', 
				'view_type': 'form',
				'view_mode': 'form',

				#'res_model': 'openhealth.cosmetology',
				'res_model': self._name,

				'res_id': cosmetology_id,

				#'target': 'inline'.
				'target': 'current',

				'flags': 	{
								#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
								'form': {'action_buttons': True, }
							},

				'context': 	{
							}
		}







# ----------------------------------------------------------- Create Appointment ------------------------------------------------------
	#@api.multi 
	#def create_appointment(self):
		#print 
		#print 'jx'
		#print 'Create Appointment'








# ----------------------------------------------------------- Create consultation ------------------------------------------------------
	@api.multi 
	def create_consultation(self):

		#print 
		#print 'jx'
		#print 'begin'
		#print 'Create Consultation'


		#treatment_id = self.id 
		cosmetology_id = self.id 
		patient_id = self.patient.id
		chief_complaint = self.chief_complaint


		doctor_id = self.physician.id
		#therapist_id = self.therapist.id





		# Date 
		GMT = time_funcs.Zone(0,False,'GMT')		
		evaluation_start_date = datetime.now(GMT).strftime("%Y-%m-%d %H:%M:%S")
		#print 'GMT: ', GMT
		#print 'evaluation_start_date: ', evaluation_start_date 




		# Apointment 
		appointment = self.env['oeh.medical.appointment'].search([ 	
														
															('patient', 'like', self.patient.name),		
															

															('doctor', 'like', self.physician.name), 	
															#('x_therapist', 'like', self.therapist.name), 	
															

															('x_type', 'like', 'consultation'), 
														
														], 
														order='appointment_date desc', limit=1)

		appointment_id = appointment.id
		#print 'appointment: ', appointment






		# Consultation 
		#print 'create consultation'
		#print 
		consultation = self.env['openhealth.consultation.cos'].create(
																	{

																	#'treatment': treatment_id,	
																	'cosmetology': cosmetology_id,	

																	'appointment': appointment_id,

																	'patient': patient_id,


																	'doctor': doctor_id,
																	#'therapist': therapist_id,


																	'evaluation_start_date': evaluation_start_date,

																	'chief_complaint': chief_complaint,
																	}
																)
		consultation_id = consultation.id 

		#print 
		#print 'consultation: ', consultation
		#print 'consultation_id: ', consultation_id

		#print 



		# Update
		#print 'Update'
		rec_set = self.env['oeh.medical.appointment'].browse([
																appointment_id																
															])
		#print 'rec_set: ', rec_set



		#ret = rec_set.write({
		#						'consultation': consultation_id,
		#					})
		#print ret 


		#print appointment
		#print appointment.consultation
		#print appointment.consultation.id



		#print 'end'

		return {

			# Mandatory 
			'type': 'ir.actions.act_window',
			'name': 'Open Consultation Current',



			# Window action 
			#'res_model': 'openhealth.consultation',
			'res_model': 'openhealth.consultation.cos',

			'res_id': consultation_id,



			# Views 
			"views": [[False, "form"]],

			'view_mode': 'form',

			'target': 'current',

			#'view_id': view_id,
			#'view_id': 'oeh_medical_evaluation_view',
			#'view_id': 'oehealth.oeh_medical_evaluation_view',

			#"domain": [["patient", "=", self.patient.name]],
			#'auto_search': False, 


			'flags': {
					#'form': {'action_buttons': True, }
					'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
					},			



			'context':   {

				#'search_default_treatment': treatment_id,
				'search_default_cosmetology': cosmetology_id,

				'default_patient': patient_id,


				'default_doctor': doctor_id,
				#'default_therapist': therapist_id,


				#'default_treatment': treatment_id,		
				'default_cosmetology': cosmetology_id,		

				'default_evaluation_start_date': evaluation_start_date,
				
				'default_appointment': appointment_id,

				#'default_chief_complaint_cos': chief_complaint_cos,
				'default_chief_complaint': chief_complaint,
			}
		}

	# create_consultation





# ----------------------------------------------------------- Create Service ------------------------------------------------------
	@api.multi 
	def create_service(self):

		#print 
		#print 'jx'
		#print 'Create Service'


		cosmetology_id = self.id 

		family = 'cosmetology'
		laser = 'cosmetology'

		#zone = ''	
		#pathology = ''

		return {
				'type': 'ir.actions.act_window',
				'name': ' New Service Current', 

				'view_type': 'form',
				'view_mode': 'form',				

				#'res_model': 'openhealth.service',	
				'res_model': 'openhealth.service.cosmetology',	

				#'res_id': consultation_id,
				
				'target': 'current',
				'flags': 	{
							'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
							#'form': {'action_buttons': True, }
							},

				'context': {
							'default_cosmetology': cosmetology_id,

							'default_family': family,
							'default_laser': laser,

							#'default_zone': zone,
							#'default_pathology': pathology,
							}
				}

	# create_service







# ----------------------------------------------------------- Create order ------------------------------------------------------
	@api.multi 
	def create_order(self):

		#print 
		#print 'jx'
		#print 'Create order'



		# Initial conditions 
		patient_id = self.patient.id
		cosmetology_id = self.id 
		chief_complaint = self.chief_complaint
		doctor_id = self.physician.id
		partner_id = self.env['res.partner'].search([('name','like',self.patient.name)],limit=1).id
		#consultation_id = self.id





		# Order - Search
		order_id = self.env['sale.order'].search([
													('cosmetology','=',cosmetology_id),	
													('state','=','draft'),													
												]).id

		#print 'order_id: ', order_id




		# Order - Create 
		if order_id == False:

			#print 'create order'
			#print 
			order = self.env['sale.order'].create(
													{
														#'treatment': treatment_id,
														'cosmetology': cosmetology_id,

														'partner_id': partner_id,
														'patient': patient_id,	
														'x_doctor': doctor_id,														
														'state':'draft',
														'x_chief_complaint':chief_complaint,


														#'x_appointment': appointment_id,	
														#'consultation':self.id,
													}
												)
			order_id = order.id 
			#print order_id


			# Create order lines 
			ret = order.x_create_order_lines()
			#print ret 


		#print 

		return {

			# Mandatory 
			'type': 'ir.actions.act_window',
			'name': ' Create Quotation Current', 
			'view_type': 'form',
			'view_mode': 'form',
						

			'res_model': 'sale.order',
			
			'res_id': order_id,
			
			
			'flags': {
					'form': {'action_buttons': True, }
					#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
					},			
			
			'target': 'current',

			'context':   {

							#'default_treatment': treatment_id,
							#'default_consultation': consultation_id,


							'default_cosmetology': cosmetology_id,
							'default_partner_id': partner_id,
							'default_patient': patient_id,	



							'default_x_doctor': doctor_id,	
							#'default_x_therapist': therapist_id,	


							
							'default_x_chief_complaint': chief_complaint,	
							#'default_x_appointment': appointment_id,	
						}
			}


	# create_order_current







# ----------------------------------------------------------- Create invoice ------------------------------------------------------
	#@api.multi 
	#def create_invoice(self):
		#print 
		#print 'jx'
		#print 'Create invoice'







# ----------------------------------------------------------- Create procedure ------------------------------------------------------
	@api.multi 
	def create_procedure(self):

		#print 
		#print 'jx'
		#print 'Create procedure'



		if self.nr_invoices > 0:
			ret = cos_funcs.create_procedure_go(self)



		#print ret 
		#print 

	# create_procedure 







# ----------------------------------------------------------- Create Sessions ------------------------------------------------------
	@api.multi 
	def create_sessions(self):

		#print 
		#print 'jx'
		#print 'Create Sessions - Through Procedure'


		#model = 'openhealth.session.cos'
		#ret = procedure_funcs.create_sessions_go(self, model)


		procedure = self.env['openhealth.procedure.cos'].search([('cosmetology','=', self.id)]) 
		procedure_id = procedure.id


		return {

			# Mandatory 
			'type': 'ir.actions.act_window',
			'name': 'Open Procedure Cos - Current',


			# Window action 
			'res_model': 'openhealth.procedure.cos',
			'res_id': procedure_id,


			# Views 
			"views": [[False, "form"]],
			'view_mode': 'form',

			#'target': 'new',
			'target': 'current',

			'context':   {
			}
		}

	# create_session



# ----------------------------------------------------------- Create session ------------------------------------------------------
	@api.multi 
	def create_session(self):

		#print 
		#print 'jx'
		#print 'Create Sessions'



		procedure = self.env['openhealth.procedure'].search([('cosmetology','=', self.id)]) 
		procedure_id = procedure.id


		return {

			# Mandatory 
			'type': 'ir.actions.act_window',
			'name': 'Open Procedure Current',


			# Window action 
			'res_model': 'openhealth.procedure',
			'res_id': procedure_id,


			# Views 
			"views": [[False, "form"]],
			'view_mode': 'form',

			#'target': 'new',
			'target': 'current',

			'context':   {
			}
		}

	# create_session










