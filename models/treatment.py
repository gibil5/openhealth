# -*- coding: utf-8 -*-
#
# 	*** OPEN HEALTH
# 
# Created: 			26 Aug 2016
# Last updated: 	 20 Sep 2016

from openerp import models, fields, api
from datetime import datetime

import jxvars






class Treatment(models.Model):
	#_name = 'openhealth.treatment'
	_inherit = 'openextension.treatment'






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



	# Number of procedures 
	nr_procedures = fields.Integer(
			string="Procedimientos",
			compute="_compute_nr_procedures",
	)
	#@api.multi
	@api.depends('procedure_ids')
	def _compute_nr_procedures(self):
		for record in self:
			ctr = 0 
			for c in record.procedure_ids:
				ctr = ctr + 1
			record.nr_procedures = ctr




	# Number of controls 
	nr_controls = fields.Integer(
			string="Controles",
			compute="_compute_nr_controls",
	)
	@api.multi
	def _compute_nr_controls(self):
		for record in self:
			ctr = 0 
			for p in record.procedure_ids:
				for c in p.control_ids:
					ctr = ctr + 1
			record.nr_controls = ctr

	
	
	
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





	# Number of appointments
	
	nr_apps = fields.Integer(
				string="Citas",
				compute="_compute_nr_apps",
	)

	@api.multi
	
	def _compute_nr_apps(self):
		for record in self:

			ctr = 0 
			
			#for c in record.consultation_ids:
			#	for o in c.order:
			#		ctr = ctr + 1		

			record.nr_apps = ctr









	# Consultations 
	# --------------
	consultation_ids = fields.One2many(
			#'oeh.medical.evaluation', 
			'openhealth.consultation', 

			#'treatment_id', 
			'treatment', 

			string = "Consultas", 
			)

	procedure_ids = fields.One2many(
			#'oeh.medical.evaluation', 
			'openhealth.procedure', 

			#'treatment_id', 
			'treatment', 
			string = "Procedimientos", 
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

						#('state', '=', 'draft'),
						('state', 'in', ['draft', 'sent', 'sale', 'done'])
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





	
	
	# Patient 
	patient = fields.Many2one(
			'oeh.medical.patient',
			string="Paciente", 
			#required=True, 
			#index=True
			)
			







	# Clean procedures
	@api.multi
	def clean_procedures(self):
		self.procedure_ids.unlink()



			
	# Create procedure 
	@api.multi
	def create_procedure(self):
		print 
		print 'jx'
		print 'Create Procedure'
		
		name = 'name'
		patient = self.patient.id
		doctor = self.physician.id
		treatment = self.id
		
		
		chief_complaint = self.chief_complaint


		#for service in self.consultation_ids.service_co2_ids:
		#	product = service.service.id
		
		
		
		#for line in self.consultation_ids.order.order_line:	
		for line in self.sale_ids.order_line:
			
			
			#if (not line.procedure_created) and (self.consultation_ids.order):

			if not line.procedure_created:
				
				line.procedure_created = True
				
				product = line.product_id.id
				
				ret = self.procedure_ids.create({
											'patient':patient,
											'doctor':doctor,
											'chief_complaint':chief_complaint,
											'treatment':treatment,										
											'product':product,
									})
				print ret 


		print 
	
	



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
			selection = jxvars._pathology_list, 
			#default = '', 
			required=True, 
			)





	# Physician 
	physician = fields.Many2one(
			'oeh.medical.physician',
			#string="Physician", 
			string="Médico", 
			required=True, 
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

		patient_id = self.patient.id
		doctor_id = self.physician.id
		treatment_id = self.id 

		chief_complaint = self.chief_complaint

		return {

			# Mandatory 
			'type': 'ir.actions.act_window',
			'name': 'Open Consultation Current',

			# Window action 
			'res_model': 'openhealth.consultation',

			# Views 
			"views": [[False, "form"]],

			'view_mode': 'form',

			'target': 'current',

			#'view_id': view_id,
			#'view_id': 'oeh_medical_evaluation_view',
			#'view_id': 'oehealth.oeh_medical_evaluation_view',

			#"domain": [["patient", "=", self.patient.name]],
			#'auto_search': False, 
			#'flags': {'form': {'action_buttons': True}}, 

			'context':   {
				'search_default_treatment': treatment_id,

				'default_patient': patient_id,
				'default_doctor': doctor_id,
				#'default_treatment_id': treatment_id,
				'default_treatment': treatment_id,
				
				'default_chief_complaint': chief_complaint,
			}
		}






	# Button - Procedure 
	# -------------------
	@api.multi
	def open_procedure_current(self):  

		patient_id = self.patient.id
		doctor_id = self.physician.id

		#chief_complaint = self.chief_complaint
		
		treatment_id = self.id 

		return {

			# Mandatory 
			'type': 'ir.actions.act_window',
			'name': 'Open Procedure Current',

			# Window action 
			'res_model': 'openhealth.procedure',

			# Views 
			"views": [[False, "form"]],

			'view_mode': 'form',

			'target': 'current',

			'context':   {
				'search_default_treatment': treatment_id,

				'default_patient': patient_id,
				'default_doctor': doctor_id,
				'default_treatment': treatment_id,
				
				#'default_chief_complaint': chief_complaint,
				
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

