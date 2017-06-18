# -*- coding: utf-8 -*-
#
# 	*** Treatment - OeHealth - new model 
# 
# Created: 			 26 Aug 2016
# Last updated: 	 21 Feb 2017


from openerp import models, fields, api
from datetime import datetime
from datetime import tzinfo

#from . import jxvars	 - DEPRECATED
from . import treatment_funcs
from . import time_funcs
from . import treatment_vars




class Treatment(models.Model):

	#_inherit = 'openextension.treatment'

	_inherit = 'openhealth.process'	
	_name = 'openhealth.treatment'




# ----------------------------------------------------------- Canonical ------------------------------------------------------

	# Name 
	name = fields.Char(
			string="Tratamiento #", 
			compute='_compute_name', 
			)

	vspace = fields.Char(
			' ', 
			readonly=True
			)




	# Open Myself
	@api.multi 
	def open_myself(self):

		#print 
		#print 'Open Myself'

		treatment_id = self.id  

		return {

			# Mandatory 
			'type': 'ir.actions.act_window',
			'name': 'Open Consultation Current',


			# Window action 
			'res_model': 'openhealth.treatment',
			'res_id': treatment_id,


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

			'context':   {

			}
		}
	# open_myself







	# Partner 
	partner_id = fields.Many2one(

			'res.partner',
		
			string = "Cliente", 	

			#required=True, 
			compute='_compute_partner_id', 
		)


	#@api.multi
	@api.depends('patient')


	def _compute_partner_id(self):
		for record in self:

			partner = record.env['res.partner'].search([

															#('order','=', record.id),
															('name','like', record.patient.name),
				
														],
														#order='appointment_date desc',
														limit=1,)

			record.partner_id = partner 
	# _compute_partner_id






	@api.multi 
	def reset(self):

		#print 
		#print 
		#print 'jx'
		#print 'Treatment - Reset'

		#self.state = 'draft'
		#self.x_payment_method.unlink()
		#self.x_appointment.x_machine = False


		# Unlinks
		#print 'Unlinks'
		self.service_co2_ids.unlink()
		self.service_excilite_ids.unlink()
		self.service_ipl_ids.unlink()
		self.service_ndyag_ids.unlink()
		self.service_medical_ids.unlink()
		self.consultation_ids.unlink()
		self.procedure_ids.unlink()
		self.session_ids.unlink()
		self.control_ids.unlink()
		self.appointment_ids.unlink()


		# Numbers 
		self.nr_budgets_cons = 0 
		self.nr_invoices_cons = 0 
		self.nr_budgets_pro = 0 
		self.nr_invoices_pro = 0 



		# Orders 
		#self.order_ids.unlink()
		for order in self.order_ids:
			#print order 
			#print order.name

			order.remove_myself()






		#print 
		#print 
		#print 

	# x_reset





	# Family 
	x_family = fields.Selection(
			string = "Tipo", 	
			
			#selection = jxvars._family_list, 
			selection = treatment_vars._family_list, 
		)





	duration = fields.Integer(
			#string="Días", 
			default = 0,
			compute='_compute_duration', 
			)


# ----------------------------------------------------------- Relational ------------------------------------------------------
	
	# Service 
	service_ids = fields.One2many(
			'openhealth.service', 	
			'treatment', 
			string="Servicios"
		)



	# Co2
	service_co2_ids = fields.One2many(
			'openhealth.service.co2', 
			'treatment', 
			string="Servicios Co2"
			)

	# Excilite
	service_excilite_ids = fields.One2many(
			'openhealth.service.excilite', 
			'treatment', 
			string="Servicios Excilite"
			)

	# Ipl
	service_ipl_ids = fields.One2many(
			'openhealth.service.ipl', 
			'treatment', 
			string="Servicios ipl"
			)


	# Ndyag
	service_ndyag_ids = fields.One2many(
			'openhealth.service.ndyag', 
			'treatment', 
			string="Servicios ndyag"
			)

	# Medical
	service_medical_ids = fields.One2many(
			'openhealth.service.medical', 
			'treatment', 
			string="Servicios medical"
			)








	# Consultation progress
	consultation_progress = fields.Float(

			default = 0, 
			compute="_compute_progress",
		)

	@api.multi
	#@api.depends('consultation_ids')

	def _compute_progress(self):
		for record in self:

			for con in record.consultation_ids:
				record.consultation_progress = con.progress




	# State 
	state = fields.Selection(

			#selection = _state_list, 
			selection = treatment_vars._state_list, 
		
			string='Estado', 			

			#default = False, 
			default = 'empty', 

			compute="_compute_state",
		)



	@api.multi
	#@api.depends('consultation_ids')

	def _compute_state(self):
		for record in self:


			#state = False
			state = 'empty'



			if record.nr_appointments > 0:
				state = 'appointment'




			if record.nr_budgets_cons > 0:
				state = 'budget_consultation'

			if record.nr_invoices_cons > 0:
				state = 'invoice_consultation'




			#if record.nr_consultations > 0:
			if record.consultation_progress == 100:
				state = 'consultation'


			if record.nr_services > 0:
				state = 'service'





			if record.nr_budgets_pro > 0:
				state = 'budget_procedure'

			if record.nr_invoices_pro > 0:
				state = 'invoice_procedure'




			if record.nr_procedures > 0:
				state = 'procedure'

			if record.nr_sessions > 0:
				state = 'sessions'

			if record.nr_controls > 0:
				state = 'controls'



			record.state = state







# ----------------------------------------------------------- Number ofs ------------------------------------------------------




	# Number of appointments 
	nr_appointments = fields.Integer(
			string="Citas",
			compute="_compute_nr_appointments",
	)
	@api.multi
	def _compute_nr_appointments(self):
		for record in self:

			record.nr_appointments=self.env['oeh.medical.appointment'].search_count([

																	('treatment','=', record.id),
																	('x_target','=', 'doctor'),
				
																	]) 





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


			record.nr_services = co2 + exc + ipl + ndyag + medical






	# Co2
	nr_services_co2 = fields.Integer(
			string="Servicios",
			compute="_compute_nr_services_co2",
	)
	@api.multi
	def _compute_nr_services_co2(self):
		for record in self:

			services =		self.env['openhealth.service.co2'].search_count([('treatment','=', record.id),]) 
			
			record.nr_services_co2 = services 





	# excilite
	nr_services_excilite = fields.Integer(
			string="Servicios",
			compute="_compute_nr_services_excilite",
	)
	@api.multi
	def _compute_nr_services_excilite(self):
		for record in self:
			services = 		self.env['openhealth.service.excilite'].search_count([('treatment','=', record.id),]) 
			record.nr_services_excilite = services 


	# ipl
	nr_services_ipl = fields.Integer(
			string="Servicios",
			compute="_compute_nr_services_ipl",
	)
	@api.multi
	def _compute_nr_services_ipl(self):
		for record in self:
			services = 		self.env['openhealth.service.ipl'].search_count([('treatment','=', record.id),]) 
			record.nr_services_ipl = services 



	# ndyag
	nr_services_ndyag = fields.Integer(
			string="Servicios",
			compute="_compute_nr_services_ndyag",
	)
	@api.multi
	def _compute_nr_services_ndyag(self):
		for record in self:
			services = 		self.env['openhealth.service.ndyag'].search_count([('treatment','=', record.id),]) 
			record.nr_services_ndyag = services 


	# medical
	nr_services_medical = fields.Integer(
			string="Servicios",
			compute="_compute_nr_services_medical",
	)
	@api.multi
	def _compute_nr_services_medical(self):
		for record in self:
			services = 		self.env['openhealth.service.medical'].search_count([('treatment','=', record.id),]) 
			record.nr_services_medical = services 















	# Number of budgets - Consultations
	nr_budgets_cons = fields.Integer(
			string="Presupuestos Consultas",
			compute="_compute_nr_budgets_cons",
	)
	@api.multi
	def _compute_nr_budgets_cons(self):
		for record in self:

			record.nr_budgets_cons=self.env['sale.order'].search_count([
																	('treatment','=', record.id),
																	('x_family','=', 'consultation'),

																	('state','=', 'draft'),
																	]) 

	# Number of invoices - Consultations
	nr_invoices_cons = fields.Integer(
			string="Facturas Consultas",
			compute="_compute_nr_invoices_cons",
	)
	@api.multi
	def _compute_nr_invoices_cons(self):
		for record in self:

			record.nr_invoices_cons=self.env['sale.order'].search_count([
																	('treatment','=', record.id),

																	('x_family','=', 'consultation'),

																	('state','=', 'sale'),
																	]) 








	# Number of budgets - Proc
	nr_budgets_pro = fields.Integer(
			string="Presupuestos - Pro",
			compute="_compute_nr_budgets_pro",
	)
	@api.multi
	def _compute_nr_budgets_pro(self):
		for record in self:

			record.nr_budgets_pro=self.env['sale.order'].search_count([
																		('treatment','=', record.id),
																		
																		('x_family','=', 'procedure'),

																		('state','=', 'draft'),
																	]) 

	# Number of invoices - Proc
	nr_invoices_pro = fields.Integer(
			string="Facturas",
			compute="_compute_nr_invoices_pro",
	)
	@api.multi
	def _compute_nr_invoices_pro(self):
		for record in self:

			record.nr_invoices_pro=self.env['sale.order'].search_count([
																
																	('treatment','=', record.id),
																	
																	('x_family','=', 'procedure'),

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

			#record.nr_sessions=self.env['openhealth.session'].search_count([
			record.nr_sessions=self.env['openhealth.session.med'].search_count([
																					('treatment','=', record.id),
																				]) 




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

						('x_machine', '!=', 'false'),
						
						#('x_target', '!=', 'doctor'),
						#('x_target', 'in', 'doctor'),
						#('treatment', 'like', 'TR000073'),
					],
			)





	# Appointments 
	appointment_ids = fields.One2many(


			'oeh.medical.appointment', 
			#'openhealth.appointment', 
		

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

	recommendation_ids = fields.One2many(
			'openhealth.recommendation', 
			'treatment', 
			string = "Recomendaciones", 
			)



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
			#'openhealth.session', 
			'openhealth.session.med', 
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
	#quotation_ids = fields.One2many(
	#		'sale.order',			 
	#		'treatment', 			
	#		string="Presupuestos",
	#		domain = [
						#('state', '=', 'pre-draft'),
						#('state', 'in', ['draft', 'sent', 'sale', 'done'])
						#('x_family', '=', 'private'),
	#				],
	#		)

	# Sales 
	#sale_ids = fields.One2many(
	#		'sale.order',			 
	#		'treatment', 
	#		string="Ventas",
	#		domain = [
						#('state', '=', 'sale'),
	#					('state', 'in', ['sale', 'done'])
	#				],
	#		)



	# orders 
	order_ids = fields.One2many(
			'sale.order',			 
			'treatment', 
			string="Presupuestos",
			domain = [
						#('state', '=', 'order'),
						#('state', 'in', ['order', 'done'])
					],
			)


	order_pro_ids = fields.One2many(
			'sale.order',			 
			'treatment', 
			
			string="Presupuestos",

			domain = [
						('x_family', '=', 'procedure'),
					],
			)



	
# ----------------------------------------------------------- Indexes ------------------------------------------------------
	

			









	@api.multi
	def update_appointment(self, appointment_id, procedure_id, x_type):

		#print 
		#print 'Update Appointment'


		#ret = treatment_funcs.create_procedure_go(self)
		ret = treatment_funcs.update_appointment_go(self, appointment_id, procedure_id, x_type)


		#print ret 
		#print 





	# Clean procedures
	@api.multi
	def clean_procedures(self):
		self.procedure_ids.unlink()



			





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













	end_date = fields.Date(
			string="Fecha fin", 
			default = fields.Date.today
			)


	today_date = fields.Date(
			string="Fecha hoy", 
			default = fields.Date.today
			)





	@api.multi
	#@api.depends('start_date', 'end_date')


	def _compute_duration(self):
		for record in self:
			date_format = "%Y-%m-%d"
			a = datetime.strptime(record.start_date, date_format)
			
			if record.treatment_open:
				b = datetime.strptime(record.today_date, date_format)
				
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






	#@api.multi
	#@api.depends('service_ids')

	#def _compute_price_total(self):
	#	for record in self:
	#		sub_total = 0.0 
	#		for se in record.service_ids:   
	#			#print se.price
	#			sub_total = sub_total + se.price 
	#		record.price_total = sub_total  

















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








	# ----------------------------------------------------- Open Appointment ------------------------------------------------------------

	# Open Appointment
	# -----------------
	@api.multi
	def open_appointment(self):  

		#print 
		#print 'open appointment'


		owner_id = self.id 
		#owner_type = self.owner_type


		patient_id = self.patient.id


		doctor_id = self.physician.id
		#therapist_id = self.therapist.id


		
		#treatment_id = self.treatment.id 
		#cosmetology_id = self.cosmetology.id 



		GMT = time_funcs.Zone(0,False,'GMT')
		appointment_date = datetime.now(GMT).strftime("%Y-%m-%d %H:%M:%S")
		#appointment_date = '2016-12-23'


		return {
				'type': 'ir.actions.act_window',

				'name': ' New Appointment', 
				
				'view_type': 'form',
				
				#'view_mode': 'form',			
				'view_mode': 'calendar',			
				
				'target': 'current',
				

				'res_model': 'oeh.medical.appointment',				
				
				'flags': 	{
							#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
							'form': {'action_buttons': True, }
							},


				'context': {
							#'default_consultation': owner_id,					
							'default_treatment': owner_id,
							
							'default_patient': patient_id,
							'default_doctor': doctor_id,
							
							#'default_x_type': owner_type,

							'default_appointment_date': appointment_date,
							}
				}





	# ----------------------------------------------------- Open Consultation ------------------------------------------------------------

	# Consultation - NEW
	# --------------------


	@api.multi
	def open_consultation_current(self):  

		#print 
		#print 'jx'
		#print 'Open Consultation Current'

		patient_id = self.patient.id
		doctor_id = self.physician.id
		treatment_id = self.id 
		chief_complaint = self.chief_complaint

		# Date 
		GMT = time_funcs.Zone(0,False,'GMT')
		#print 'GMT: ', GMT
		evaluation_start_date = datetime.now(GMT).strftime("%Y-%m-%d %H:%M:%S")
		#print 'evaluation_start_date: ', evaluation_start_date 

		# Apointment 
		appointment = self.env['oeh.medical.appointment'].search([ 	
																('patient', 'like', self.patient.name),		
																('doctor', 'like', self.physician.name), 	
																('x_type', 'like', 'consultation'), 
															], 
															order='appointment_date desc', limit=1)
		#print 'appointment: ', appointment
		appointment_id = appointment.id




		# Search  
		consultation = self.env['openhealth.consultation'].search([
																		('treatment','=', self.id),
																],
																#order='appointment_date desc',
																limit=1,)

		# Create if it does not exist 
		if consultation.name == False:
			#print 'create consultation'



			# Consultation 
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
			#print 'consultation: ', consultation
			#print 'consultation_id', consultation_id


			# Update
			rec_set = self.env['oeh.medical.appointment'].browse([
																	appointment_id																
																])
			#print 'rec_set: ', rec_set

			ret = rec_set.write({
									'consultation': consultation_id,
								})

			#print ret 
			#print appointment
			#print appointment.consultation
			#print appointment.consultation.id



		#print 
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
			#'view_id': 'oeh_medical_evaluation_view',
			#'view_id': 'oehealth.oeh_medical_evaluation_view',

			#"domain": [["patient", "=", self.patient.name]],
			#'auto_search': False, 


			'flags': {
					'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
					#'form': {'action_buttons': True, }
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














# ----------------------------------------------------------- Buttons ------------------------------------------------------

	# Treatment - EDIT 
	# --------------------

	@api.multi
	def open_line_current(self):  

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

	#@api.multi 
	#def create_invoice(self):			# Do Nothing  
		#print 'jx'
		#print 'Create Invoice'

	# create_invoice 







# ----------------------------------------------------------- Button - Create Service  ------------------------------------------------------

	@api.multi
	def create_service(self):
		treatment_id = self.id

		#print 'jx'
		#print 'Create Service'
		#consultation = self.env['openhealth.consultation'].search([('treatment','=', self.id)]) 
		#consultation_id = consultation.id

		return {

			# Mandatory 
			'type': 'ir.actions.act_window',
			'name': 'Open Consultation Current',


			# Window action 
			#'res_model': 'openhealth.consultation',
			#'res_id': consultation_id,

			#'res_model': 'openhealth.service',
			'res_model': 'openhealth.recommendation',




			# Views 
			"views": [[False, "form"]],

			'view_mode': 'form',
			'target': 'current',



			#'view_id': view_id,
			#"domain": [["patient", "=", self.patient.name]],
			#'auto_search': False, 

			'flags': {
					#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
					#'form': {'action_buttons': True, }
					'form': {'action_buttons': False, }
					},			


			'context':   {
							#'default_consultation': consultation_id,

							'default_treatment': treatment_id,					
					}
		}




	# create_recommendation







# ----------------------------------------------------------- Button - Create Order Pro  ------------------------------------------------------
	@api.multi 
	def create_order_con(self):

		target = 'consultation'


		order = self.create_order(target)		
		#print order 



		return {

			# Mandatory 
			'type': 'ir.actions.act_window',
			'name': 'Open Order Current',


			# Window action 
			'res_model': 'sale.order',
			'res_id': order.id,


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


			'context': {}
		}

	# create_order_con




# ----------------------------------------------------------- Button - Create Order Pro  ------------------------------------------------------
	@api.multi 
	def create_order_pro(self):

		target = 'procedure'


		order = self.create_order(target)		
		#print order 



		return {

			# Mandatory 
			'type': 'ir.actions.act_window',
			'name': 'Open Order Current',


			# Window action 
			'res_model': 'sale.order',
			'res_id': order.id,


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


			'context': {}
		}

	# create_order_pro






# ----------------------------------------------------------- Button - Create Order  ------------------------------------------------------
#jz


	@api.multi 
	#def create_order(self):
	def create_order(self, target):

		#print 
		#print 'jx'
		#print 'Create Order'


		#print self.x_family
		#print target


		order = self.env['sale.order'].create(
													{
														'treatment': self.id,

														'partner_id': self.partner_id.id,
														
														'patient': self.patient.id,	
														
														'x_doctor': self.physician.id,	
														
														#'consultation':self.id,
														
														'state':'draft',

														#'x_chief_complaint':chief_complaint,

														
														'x_family': target, 
													}
												)



		# Create order lines 
		if target == 'consultation':
			if self.chief_complaint in ['monalisa_touch']:
				target_line = 'con_gyn'
			else:
				target_line = 'con_med'

			#print target_line 
			ret = order.x_create_order_lines_target(target_line)
			#print ret 



		#elif target == 'procedure':
		else:
#jz
			order_id = order.id

			ret = treatment_funcs.create_order_lines(self, 'co2', order_id)
			#print ret

			ret = treatment_funcs.create_order_lines(self, 'excilite', order_id)
			#print ret 

			ret = treatment_funcs.create_order_lines(self, 'ipl', order_id)
			#print ret 

			ret = treatment_funcs.create_order_lines(self, 'ndyag', order_id)
			#print ret 

			ret = treatment_funcs.create_order_lines(self, 'medical', order_id)
			#print ret 




		#print 

		return order
	# create_order







# ----------------------------------------------------------- Button - Create Budget  ------------------------------------------------------

	@api.multi 
	def create_budget(self):

		#print 'jx'
		#print 'Create Budget'


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

		#print 
		#print 
		#print 'Create Procedure'


		#if self.nr_invoices > 0:
		if self.nr_invoices_pro > 0:

			ret = treatment_funcs.create_procedure_go(self)


		#print ret 
		#print 
		#print 

	# create_procedure 






# ----------------------------------------------------------- Create Sessions ------------------------------------------------------

	@api.multi 
	def create_sessions(self):

		#print 'jx'
		#print 'Create Sessions'


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

		#print 'jx'
		#print 'Create Controls'


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



