# -*- coding: utf-8 -*-
#
# 	*** Evaluation 
# 
# Created: 				26 Aug 2016
#
from openerp import models, fields, api
from datetime import datetime

#from libs import eval_vars
from . import prodvars
from openerp.addons.openhealth.models.libs import eval_vars


#from patient import pat_vars
from openerp.addons.openhealth.models.patient import pat_vars


class Evaluation(models.Model):

	_inherit = 'oeh.medical.evaluation'



# ----------------------------------------------------------- Appointment ------------------------------------------------------

	# Update App  
	@api.multi	
	def update_dates(self):

		#print 
		#print 'Update Dates'

		self.evaluation_start_date = self.appointment.appointment_date





	# Update App  
	@api.multi	
	def update_appointment(self):

		#print 
		#print 'Update Appointment'

		res_id = self.appointment.id  

		# Treatment Flag 
		self.treatment.update()

		return {
			
			# Mandatory 
			'type': 'ir.actions.act_window',
			'name': 'Open Appointment',
			
			# Window action 
			'res_model': 'oeh.medical.appointment',
			'res_id': res_id,
			
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
			'context':   {}
		}
	# update_appointment






# --------------------------------------------------------- Consultation First ------------------------------------------------------

	x_diagnosis = fields.Text(
			string = 'Diagnóstico', 
			required=False, 
		)

	x_antecedents = fields.Text(
			string = 'Antecedentes médicos', 
			required=False, 
		)

	x_allergies_medication = fields.Text(
			string = 'Alergias a medicamentos', 
			required=False, 
		)

	x_observations = fields.Text(
			string = 'Observaciones',
			required=False, 
		)

	x_indications = fields.Text(
			string = 'Indicaciones',
			required=False, 
		)

	x_analysis_lab = fields.Boolean(
			string = 'Análisis de laboratorio', 			
			default=False, 
		)



	x_examination = fields.Text(
			string = 'Examen clínico', 
			required=False, 
		)




	# ----------------------------------------------------------- Patient ------------------------------------------------------

	# Update  
	#@api.multi 
	#def update_patient(self):
	#	print 
		#print 'Update Patient - Evaluation'
		#self.patient_sex = self.patient.sex[0]
		#self.patient_age =  self.patient.age.split()[0]
		#self.patient_city = self.patient.city.title()




	# Sex
	patient_sex = fields.Char(
			string="Sexo", 

			compute='_compute_patient_sex', 
		)

	@api.multi
	def _compute_patient_sex(self):
		for record in self:		
			if record.patient.sex != False: 
				record.patient_sex = record.patient.sex[0]


	# Age
	patient_age = fields.Char(
			string="Edad", 

			compute='_compute_patient_age', 
		)

	@api.multi
	def _compute_patient_age(self):
		for record in self:		
			if record.patient.age != False: 
				record.patient_age = record.patient.age.split()[0]



	# City 
	patient_city = fields.Char(
			string="Lugar de procedencia", 

			compute='_compute_patient_city', 
		)

	@api.multi
	def _compute_patient_city(self):
		for record in self:
			if record.patient.city_char != False: 
				city = record.patient.city_char
				record.patient_city = city.title()










# ----------------------------------------------------------- Primitives ------------------------------------------------------

	# Date 
	evaluation_start_date = fields.Datetime(
			string = "Fecha y hora", 	
			#default = fields.Date.today, 
			required=True, 
			
			readonly=True, 
			#readonly=False, 
		)




	# Space 
	vspace = fields.Char(
			' ', 
			readonly=True
		)




	# Autofill
	x_autofill = fields.Boolean(
			string="Autofill",
			default=False, 
		)
	




	# Done
	x_done = fields.Boolean(
			default=False,
			string="Realizado", 			
		)




	# State 
	state = fields.Selection(
			selection = eval_vars._state_list, 
			string='Estado',	
			default='draft',
		)



	# Evaluation Nr
	evaluation_nr = fields.Integer(
			string="Evaluation #", 
			default=1, 
			required=True, 
		)











# ----------------------------------------------------------- Computed ------------------------------------------------------

	# Zone 
	zone = fields.Selection(
			selection = prodvars._zone_list, 
			string="Zona",

			compute='_compute_zone', 			
		)
	
	#@api.multi
	@api.depends('product')
	def _compute_zone(self):
		for record in self:
			record.zone = record.product.x_zone



	# Pathology 
	pathology = fields.Selection(
			selection = prodvars._pathology_list, 
			string="Patología", 			

			compute='_compute_pathology', 			
		)
	
	#@api.multi
	@api.depends('product')
	def _compute_pathology(self):
		for record in self:
			record.pathology = record.product.x_pathology





	# Level 
	level = fields.Selection(
			selection = prodvars._level_list, 
			string="Nivel",

			compute='_compute_level', 			
		)
	
	#@api.multi
	@api.depends('product')
	def _compute_level(self):
		for record in self:
			record.level = record.product.x_level



	# Nr images 
	nr_images = fields.Integer(
			string = "Nr Visia", 	
			#required=True, 

			compute="_compute_nr_images",
		)

	@api.multi
	def _compute_nr_images(self):
		for record in self:
			ctr = 0
			for image in record.image_ids:
				ctr = ctr + 1
			record.nr_images = ctr










# ----------------------------------------------------------- Relationals ------------------------------------------------------

	treatment = fields.Many2one(
			'openhealth.treatment',			
			ondelete='cascade', 
			required=True, 
			readonly=True, 
		)

	cosmetology = fields.Many2one(
			'openhealth.cosmetology',
			ondelete='cascade', 			
			string="Cosmiatría", 
			)




# ----------------------------------------------------------- Primitive ------------------------------------------------------
	
	# Patient 
	patient = fields.Many2one(
			'oeh.medical.patient',
			string = "Paciente", 	
			ondelete='cascade', 			
			required=True, 
			readonly=True, 
		)



	# Doctor 
	doctor = fields.Many2one(
			'oeh.medical.physician',
			string = "Médico", 				
			required=True, 
			#readonly=True, 
		)




	# Appointment 
	appointment = fields.Many2one(
			'oeh.medical.appointment',			
			string='Cita #', 

			required=False, 
			
			readonly=True, 
			
			#ondelete='cascade', 
		)



	# Chief complaint 
	chief_complaint = fields.Selection(
			string = 'Motivo de consulta', 
			selection = eval_vars._chief_complaint_list, 
			required=True, 
		)



	# Evaluation type 
	evaluation_type = fields.Selection(
			selection = eval_vars.EVALUATION_TYPE, 
			string = 'Tipo',
			#default='', 
			required=True, 
		)




	# Product
	product = fields.Many2one(		
			'product.template',
			string="Producto",
			#required=True, 
			domain = [
						('x_origin', '=', False),
					],
		)
	


	# Laser 
	laser = fields.Selection(

			selection = prodvars._laser_type_list, 
		
			string="Láser",

			compute='_compute_laser', 			
		)
		
	#@api.multi
	@api.depends('product')
	def _compute_laser(self):
		for record in self:
			record.laser = record.product.x_treatment 



# ----------------------------------------------------------- Actions ------------------------------------------------------

	# Open Treatment
	@api.multi 
	def open_treatment(self):
		#print 
		#print 'Open Treatment'
		treatment = self.env['openhealth.treatment'].search([('id','=', self.treatment.id)]) 
		treatment_id = treatment.id  
		ret = treatment.open_myself()
		return ret 
	# open_treatment

