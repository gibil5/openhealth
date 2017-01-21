# -*- coding: utf-8 -*-
#
# 	*** Treatment - OeHealth - new model 
# 
# Created: 			26 Aug 2016
# Last updated: 	 7 Dec 2016


from openerp import models, fields, api
from datetime import datetime
from datetime import tzinfo

import jxvars
import treatment_funcs
import time_funcs






class Treatment(models.Model):
	#_name = 'openhealth.treatment'
	_inherit = 'openextension.treatment'







	# State 

	_state_list = [
        			#('empty', 			'Inicio'),

        			('consultation', 	'Consulta'),

        			('service', 		'Recomendación'),



        			
        			('budget', 			'Presupuesto'),

        			('invoice', 		'Facturado'),
        			
        			('procedure', 		'Procedimiento'),

        			('sessions', 		'Sesiones'),

        			('controls', 		'Controles'),

        			('done', 			'Completo'),
        		]

	state = fields.Selection(
			selection = _state_list, 
			
			#string='Status', 			
			#string='Estado',	
			#readonly=True, 
			#readonly=False, 

			default = False, 

			compute="_compute_state",
		)



	#@api.multi
	@api.depends('consultation_ids')

	def _compute_state(self):
		for record in self:


			#con_count=self.env['openhealth.consultation'].search_count([('treatment','=', self.id)]) 
			#bud_count=self.env['sale.order'].search_count([('treatment','=', self.id)]) 			
			#if record.consultation_ids.search_count() > 0:


			state = False


			if record.nr_consultations > 0:
				state = 'consultation'

			if record.nr_services > 0:
				state = 'service'



			if record.nr_budgets > 0:
				state = 'budget'

			if record.nr_invoices > 0:
				state = 'invoice'

			if record.nr_procedures > 0:
				state = 'procedure'

			if record.nr_sessions > 0:
				state = 'sessions'

			if record.nr_controls > 0:
				state = 'controls'



			record.state = state







# ----------------------------------------------------------- Number ofs ------------------------------------------------------


	# Number of Services  
	nr_services = fields.Integer(
			string="Servicios",
			compute="_compute_nr_services",
	)
	@api.multi
	def _compute_nr_services(self):
		for record in self:

			co2 =		self.env['openhealth.service.co2'].search_count([('treatment','=', record.id),]) 
			exc = 		self.env['openhealth.service.excilite'].search_count([('treatment','=', record.id),]) 
			ipl = 		self.env['openhealth.service.ipl'].search_count([('treatment','=', record.id),]) 
			ndyag = 	self.env['openhealth.service.ndyag'].search_count([('treatment','=', record.id),]) 
			medical =	self.env['openhealth.service.medical'].search_count([('treatment','=', record.id),]) 


			record.nr_services= co2 + exc + ipl + ndyag + medical






	# Number of budgets 
	nr_budgets = fields.Integer(
			string="Presupuestos",
			compute="_compute_nr_budgets",
	)
	@api.multi
	def _compute_nr_budgets(self):
		for record in self:

			record.nr_budgets=self.env['sale.order'].search_count([
																	('treatment','=', record.id),
																	('state','=', 'draft'),
																	('x_family','=', 'private'),
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
																	('treatment','=', record.id),
																	('state','=', 'sale'),
																	]) 




	# Number of procedures 
	nr_procedures = fields.Integer(
			string="Procedimientos",
			compute="_compute_nr_procedures",
	)
	@api.multi
	def _compute_nr_procedures(self):
		for record in self:

			record.nr_procedures=self.env['openhealth.procedure'].search_count([

																	('treatment','=', record.id),

																	]) 




	# Number of sessions 
	nr_sessions = fields.Integer(
			string="Sesiones",
			compute="_compute_nr_sessions",
	)
	@api.multi
	def _compute_nr_sessions(self):
		for record in self:

			record.nr_sessions=self.env['openhealth.session'].search_count([
																	('treatment','=', record.id),
																	]) 
			record.nr_sessions=0



	# Number of controls 
	nr_controls = fields.Integer(
			string="Controles",
			compute="_compute_nr_controls",
	)
	@api.multi
	def _compute_nr_controls(self):
		for record in self:

			record.nr_controls=0
			record.nr_controls=self.env['openhealth.control'].search_count([
																	('treatment','=', record.id),	
																	])																	
																	#order='appointment_date desc', limit=1)







# ----------------------------------------------------------- Relational ------------------------------------------------------


	# Reservations 
	reservation_ids = fields.One2many(
			'oeh.medical.appointment', 
			'treatment', 

			string = "Reserva de sala", 

			domain = [

						('x_target', '!=', 'false'),
						('x_target', '!=', 'doctor'),

						#('x_target', 'in', 'doctor'),
						#('treatment', 'like', 'TR000073'),
					],
			)





	# Appointments 

	appointment_ids = fields.One2many(
			'oeh.medical.appointment', 
			'treatment', 

			string = "Citas", 

			domain = [
						('x_target', '=', 'doctor'),
					],
			)




	# Number of appointments
	
	nr_appointments = fields.Integer(
				string="Citas",
				compute="_compute_nr_appointments",
	)

	@api.multi
	
	def _compute_nr_appointments(self):
		for record in self:

			ctr = 0 
			
			for c in record.appointment_ids:
				ctr = ctr + 1		

			record.nr_appointments = ctr






	# Evaluation  

	#evaluation_ids = fields.One2many(
	#		'oeh.medical.evaluation', 
	#		'treatment_id', 
	#		string = "Evaluaciones", 
	#		)

	#nr_evaluations = fields.Integer(
	#		compute='_compute_nr_evaluations', 
	#		string='Nr. evaluaciones', 
	#		default = 0, 
	#		)

	#@api.depends('evaluation_ids')

	#def _compute_nr_evaluations(self):
	#	for record in self:
	#		sub_total = 0 
	#		for se in record.evaluation_ids:   
	#			sub_total = sub_total + 1  
	#		record.nr_evaluations= sub_total  






	# Open 
	treatment_open = fields.Boolean(
			string="Abierto",
			default=True,
	)







	# Number of consultations 
	nr_consultations = fields.Integer(
			string="Nr Consultas",
			compute="_compute_nr_consultations",
	)
	#@api.multi
	@api.depends('consultation_ids')
	def _compute_nr_consultations(self):
		for record in self:
			ctr = 0 
			for c in record.consultation_ids:
				ctr = ctr + 1
			record.nr_consultations = ctr









	
	
	
	# Number of orders 
	nr_orders = fields.Integer(
			string="Presupuestos",
			compute="_compute_nr_orders",
	)
	@api.multi
	def _compute_nr_orders(self):
		for record in self:
			ctr = 0 			
			for c in record.consultation_ids:
				for o in c.order:
					ctr = ctr + 1
			record.nr_orders = ctr








































# ----------------------------------------------------------- Relational ------------------------------------------------------


	consultation_ids = fields.One2many(
			#'oeh.medical.evaluation', 
			'openhealth.consultation', 
			'treatment', 

			string = "Consultas", 
			)


	procedure_ids = fields.One2many(
			#'oeh.medical.evaluation', 
			'openhealth.procedure', 
			'treatment', 

			string = "Procedimientos", 
			)




	session_ids = fields.One2many(
			'openhealth.session', 
			'treatment', 

			string = "Sesiones", 
			)

	control_ids = fields.One2many(
			'openhealth.control', 
			'treatment', 

			string = "Controles", 
			)









	# Order 
	#order = fields.One2many(
	#		'sale.order',
	#		'treatment', 
	#		)







	# Quotations 
	quotation_ids = fields.One2many(
			'sale.order',			 
			'treatment', 
			
			string="Presupuestos",

			domain = [

						#('state', '=', 'pre-draft'),
						#('state', 'in', ['draft', 'sent', 'sale', 'done'])
						('x_family', '=', 'private'),
					],
			)



	# Sales 
	sale_ids = fields.One2many(
			'sale.order',			 
			'treatment', 

			string="Ventas",

			domain = [
						#('state', '=', 'sale'),
						('state', 'in', ['sale', 'done'])
					],
			)









	
# ----------------------------------------------------------- Indexes ------------------------------------------------------
	
	patient = fields.Many2one(
			'oeh.medical.patient',

			string="Paciente", 
			#required=True, 
			#index=True

			ondelete='cascade', 
			)
			









	@api.multi
	def update_appointment(self, appointment_id, procedure_id, x_type):

		print 
		print 'Update Appointment'


		#ret = treatment_funcs.create_procedure_go(self)
		ret = treatment_funcs.update_appointment_go(self, appointment_id, procedure_id, x_type)


		#print ret 
		print 





	# Clean procedures
	@api.multi
	def clean_procedures(self):
		self.procedure_ids.unlink()



			




	# Name 
	name = fields.Char(
			string="Tratamiento #", 
			default='x',
			compute='_compute_name', 
			required=True, 
			)


	@api.multi
	#@api.depends('start_date')

	def _compute_name(self):
		for record in self:
			#record.name = record.patient.name + '-' + record.physician.name + '-' + record.start_date 
			#record.name = 'TR-' + record.start_date 
			#record.name = record.patient.name
			record.name = 'TR0000' + str(record.id) 




	#name = fields.Char(
			#string="Treatment #", 
	#		string="Tratamiento #", 
	#		required=True, 
	#		compute='_compute_name', 
	#		default='.'
	#		)




	# Motivo de consulta
	chief_complaint = fields.Selection(
			string = 'Motivo de consulta', 
			
			#selection = jxvars._pathology_list, 
			selection = jxvars._chief_complaint_list, 
			
			#default = '', 
			#required=True, 
			)






	# Physician 
	physician = fields.Many2one(
			'oeh.medical.physician',
			#string="Physician", 
			string="Médico", 
			#required=True, 
			index=True
			)
	        #default='Fernando Chavarri',





	# Dates 
	start_date = fields.Date(
			string="Fecha inicio", 
			default = fields.Date.today
			)

	end_date = fields.Date(
			string="Fecha fin", 
			default = fields.Date.today
			)


	today_date = fields.Date(
			string="Fecha hoy", 
			default = fields.Date.today
			)





	# Duration 
	duration = fields.Integer(
			#string="Duration (days)", 
			string="Días", 
			compute='_compute_duration', 
			default = 0,
			)

	@api.multi
	#@api.depends('start_date', 'end_date')


	def _compute_duration(self):
		for record in self:
			date_format = "%Y-%m-%d"
			a = datetime.strptime(record.start_date, date_format)
			
			if record.treatment_open:
				#b = datetime.today
				#b = datetime.strptime(datetime.today, date_format)
				b = datetime.strptime(record.today_date, date_format)
				#b = datetime.strptime(fields.Date.today, date_format)
				
			else:
				b = datetime.strptime(record.end_date, date_format)
			
			delta = b - a
			record.duration = delta.days + 1 




	# Number of services
	#nr_services = fields.Integer(
	#		compute='_compute_nr_services', 
			#string='Number of services', 
	#		string='Nr servicios', 
	#		default = 0, 
	#		)



	#@api.depends('service_ids')
	#def _compute_nr_services(self):
	#	for record in self:
	#		sub_total = 0 
	#		for se in record.service_ids:   
				#print se.price
	#			sub_total = sub_total + 1  
	#		record.nr_services= sub_total  
			#record.nr_services = record.service_ids.count 



	# Total Price
	price_total = fields.Float(
			#compute='_compute_price_total', 
			string='Total', 
			default = 0, 
			) 


	#@api.multi
	#@api.depends('service_ids')

	#def _compute_price_total(self):
	#	for record in self:
	#		sub_total = 0.0 
	#		for se in record.service_ids:   
	#			print se.price
	#			sub_total = sub_total + se.price 
	#		record.price_total = sub_total  





	# Service 
	#service_ids = fields.One2many(
	#		'openhealth.service', 
	#		'treatment_id', 
			#string="Services"
	#		string="Servicios"
	#		)



	# Service 
	service_co2_ids = fields.One2many(
			'openhealth.service.co2', 
			'treatment', 

			#string="Services"
			string="Servicios Co2"
			)













	# BUTTONS with Context
	# ----------------------

	# Button - Evaluation  
	# ----------------------
	@api.multi
	def open_evaluation_current(self):  

		patient_id = self.patient.id
		doctor_id = self.physician.id
		treatment_id = self.id 

		return {

			# Mandatory 
			'type': 'ir.actions.act_window',
			'name': 'Open Evaluation Current',

			# Window action 
			'res_model': 'oeh.medical.evaluation',

			# Views 
			"views": [[False, "form"]],

			'view_mode': 'form',

			#'target': 'new',
			'target': 'current',

			'context':   {
				'search_default_treatment': treatment_id,

				'default_patient': patient_id,
				'default_doctor': doctor_id,
				'default_treatment_id': treatment_id,
			}
		}



















	nr_consultations = fields.Integer(
			compute='_compute_nr_consultations', 
			default = 0, 
			)

	@api.depends('consultation_ids')

	def _compute_nr_consultations(self):
		for record in self:
			sub_total = 0 
			for co in record.consultation_ids:   
				sub_total = sub_total + 1  
			record.nr_consultations = sub_total  







	# Procedures 
	# ------------


	nr_procedures = fields.Integer(
			compute='_compute_nr_procedures', 
			default = 0, 
			)

	@api.depends('procedure_ids')

	def _compute_nr_procedures(self):
		for record in self:
			sub_total = 0 
			for co in record.procedure_ids:   
				sub_total = sub_total + 1  
			record.nr_procedures = sub_total  





	# Controls 
	# ---------
	#control_ids = fields.One2many(
			#'oeh.medical.evaluation', 
	#		'openhealth.control', 

	#		'treatment_id', 
	#		string = "Controles", 
	#		)







	# Buttons
	# -----------------------------------------------------------------------------------------------------------------



	# Consultation - NEW
	# --------------------

	@api.multi
	def open_consultation_current(self):  

		print 
		print 'open consultation'

		patient_id = self.patient.id
		doctor_id = self.physician.id
		treatment_id = self.id 

		chief_complaint = self.chief_complaint



		# Date 
		GMT = time_funcs.Zone(0,False,'GMT')
		print GMT
		evaluation_start_date = datetime.now(GMT).strftime("%Y-%m-%d %H:%M:%S")
		print evaluation_start_date 



		# Apointment 
		appointment = self.env['oeh.medical.appointment'].search([ 	
														
															('patient', 'like', self.patient.name),		
															
															('doctor', 'like', self.physician.name), 	
															
															('x_type', 'like', 'consultation'), 
														
														], 
														order='appointment_date desc', limit=1)

		print appointment

		appointment_id = appointment.id






		# Consultation 
		print 'create consultation'
		consultation = self.env['openhealth.consultation'].create(
												{

													'patient': patient_id,
													'doctor': doctor_id,
													'treatment': treatment_id,				
													'evaluation_start_date': evaluation_start_date,

													'chief_complaint': chief_complaint,


													'appointment': appointment_id,

												}
											)
		consultation_id = consultation.id 
		print consultation
		print consultation_id




		# Update
		rec_set = self.env['oeh.medical.appointment'].browse([
																appointment_id																
															])
		print rec_set

		ret = rec_set.write({
								'consultation': consultation_id,
							})

		print ret 
		print appointment
		print appointment.consultation
		print appointment.consultation.id



		print 

		return {

			# Mandatory 
			'type': 'ir.actions.act_window',
			'name': 'Open Consultation Current',



			# Window action 
			'res_model': 'openhealth.consultation',
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

				'search_default_treatment': treatment_id,

				'default_patient': patient_id,
				'default_doctor': doctor_id,
				'default_treatment': treatment_id,				
				'default_evaluation_start_date': evaluation_start_date,

				'default_chief_complaint': chief_complaint,


				'default_appointment': appointment_id,

			}
		}














	# Treatment - EDIT 
	# --------------------

	@api.multi
	def open_line_current(self):  

		#patient_id = self.patient.id
		#doctor_id = self.physician.id

		treatment_id = self.id 

		return {
				'type': 'ir.actions.act_window',
				'name': ' Edit Treatment Current', 
				'view_type': 'form',
				'view_mode': 'form',

				'res_model': self._name,
				#'res_model': 'openhealth.consultation',

				#'res_id': id[0],
				#'res_id': consultation_id,
				'res_id': treatment_id,

				'target': 'current',
				#'target': 'inline'.


				'flags': {
						#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
						'form': {'action_buttons': True, }
						},


				'context':   {
					#'search_default_consultation': consultation_id,

					#'default_patient': patient_id,
					#'default_doctor': doctor_id,

					#'default_consultation_id': consultation_id,
				}
		}





# ----------------------------------------------------------- Button - Create Invoice  ------------------------------------------------------

	@api.multi 
	def create_invoice(self):			# Do Nothing  

		print 'jx'
		print 'Create Invoice'

	# create_invoice 







# ----------------------------------------------------------- Button - Create Service  ------------------------------------------------------

	@api.multi 
	def create_service(self):

		print 'jx'
		print 'Create Service'


		consultation = self.env['openhealth.consultation'].search([('treatment','=', self.id)]) 
		consultation_id = consultation.id


		return {

			# Mandatory 
			'type': 'ir.actions.act_window',
			'name': 'Open Consultation Current',


			# Window action 
			'res_model': 'openhealth.consultation',
			'res_id': consultation_id,



			# Views 
			"views": [[False, "form"]],

			'view_mode': 'form',
			'target': 'current',


			#'view_id': view_id,
			#"domain": [["patient", "=", self.patient.name]],
			#'auto_search': False, 

			'flags': {
					'form': {'action_buttons': True, }
					#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
					},			

			#'context':   {
			#}
		}




	# create_recommedation









# ----------------------------------------------------------- Button - Create Budget  ------------------------------------------------------

	@api.multi 
	def create_budget(self):

		print 'jx'
		print 'Create Budget'


		#consultation_id = self.consultation.id
		

		#con_count=self.env['openhealth.consultation'].search_count([('treatment','=', self.id)]) 
		consultation = self.env['openhealth.consultation'].search([('treatment','=', self.id)]) 

		consultation_id = consultation.id


		return {

			# Mandatory 
			'type': 'ir.actions.act_window',
			'name': 'Open Consultation Current',


			# Window action 
			'res_model': 'openhealth.consultation',
			'res_id': consultation_id,



			# Views 
			"views": [[False, "form"]],

			'view_mode': 'form',
			'target': 'current',


			#'view_id': view_id,
			#"domain": [["patient", "=", self.patient.name]],
			#'auto_search': False, 

			'flags': {
					'form': {'action_buttons': True, }
					#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
					},			


			#'context':   {
			#	'search_default_treatment': treatment_id,
			#	'default_patient': patient_id,
			#	'default_doctor': doctor_id,
			#	'default_treatment': treatment_id,				
			#	'default_evaluation_start_date': evaluation_start_date,
			#	'default_chief_complaint': chief_complaint,
			#	'default_appointment': appointment_id,
			#}
		}




	# create_budget 





# ----------------------------------------------------------- Button - Create Procedure ------------------------------------------------------

	@api.multi
	def create_procedure(self):

		print 
		print 'Create Procedure'

		ret = treatment_funcs.create_procedure_go(self)
		#print ret 
		print 

	# create_procedure 






# ----------------------------------------------------------- Create Sessions ------------------------------------------------------

	@api.multi 
	def create_sessions(self):

		print 'jx'
		print 'Create Sessions'


		procedure = self.env['openhealth.procedure'].search([('treatment','=', self.id)]) 
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





# ----------------------------------------------------------- Create Controls  ------------------------------------------------------

	@api.multi 
	def create_controls(self):

		print 'jx'
		print 'Create Controls'


		procedure = self.env['openhealth.procedure'].search([('treatment','=', self.id)]) 
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


	# create_controls



