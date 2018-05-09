# -*- coding: utf-8 -*-
#
# 	*** Consultation 
# 
# Created: 				 1 Nov 2016
# Last updated: 	 	 7 Dec 2016 
#

from openerp import models, fields, api
from datetime import datetime,tzinfo,timedelta
from . import eval_vars
from . import app_vars

#from . import cosvars
#from . import jrfuncs
#from . import time_funcs

class Consultation(models.Model):

	_name = 'openhealth.consultation'

	#_inherit = ['openhealth.base', 'oeh.medical.evaluation']
	_inherit = 'oeh.medical.evaluation'
	




	#----------------------------------------------------------- Deprecated ------------------------------------------------------------

	#service_co2_ids = fields.Char()

	#service_excilite_ids = fields.Char()

	#service_ipl_ids = fields.Char()

	#service_ndyag_ids = fields.Char()

	#service_medical_ids = fields.Char()

	#service_ids = fields.Char()



	# Target 
	#x_target = fields.Selection(
	#		string="Target", 
	#		selection = app_vars._target_list, 
	#		default="doctor", 
			#required=True, 
	#	)

	# Owner 
	#owner_type = fields.Char(
	#		default = 'consultation',
	#	)

	#evaluation_type = fields.Selection(
	#		default = 'Pre-arraganged Appointment', 
	#		)

	# Appointments 
	#appointment_ids = fields.One2many(
	#		'oeh.medical.appointment', 

	#		'consultation', 
	#		string = "Citas", 
	#		required=True, 
	#	)

	# Number of appointments
	#nr_apps = fields.Integer(
	#			string="Citas",
	#			compute="_compute_nr_apps",
	#)

	#@api.multi
	#def _compute_nr_apps(self):
	#	for record in self:
	#		ctr = 0 
	#		for a in record.appointment_ids:
	#			ctr = ctr + 1		
	#		record.nr_apps = ctr





# ----------------------------------------------------------- Primitives ------------------------------------------------------

	# Name 
	name = fields.Char(
			string = 'Consulta #',
			)


	# Profile 
	x_profile = fields.Selection(
			string="Perfil psicológico", 
			selection=app_vars._profile_list, 
		)


	# Complaint
	chief_complaint = fields.Selection(			# Necessary 
			string = 'Motivo de consulta', 
			selection = eval_vars._chief_complaint_list, 
			required=False, 
			)



	# State 
	state = fields.Selection(

			selection = eval_vars._state_list, 
		
			#string='Estado',	
			#default='draft',

			compute='_compute_state', 
			)

	@api.multi
	def _compute_state(self):
		for record in self:


			pro = 0

			if record.x_fitzpatrick != False:
				pro = pro + 1

			if record.x_photo_aging != False:
				pro = pro + 1
			
			if record.x_diagnosis != False:
				pro = pro + 1
			
			if record.x_antecedents != False:
				pro = pro + 1


			if record.x_allergies_medication != False:
				pro = pro + 1

			if record.x_observations != False:
				pro = pro + 1

			if record.x_indications != False:
				pro = pro + 1


			if pro == 0:
				record.state = 'draft'
			elif pro == 7:
				record.state = 'done'
			elif 0 < pro < 7: 
				record.state = 'inprogress'




	# Progress
	progress = fields.Float(
			string='Progreso', 			
			default = 0., 

			compute='_compute_progress', 
		)


	@api.multi
	def _compute_progress(self):
		for record in self:
			#print 
			#print 'jx'
			#print 'Compute progress'
			record.progress = eval_vars._hash_progress[record.state]
			#print 






	# ----------------------------------------------------------- Relational ------------------------------------------------------

	treatment = fields.Many2one(
			'openhealth.treatment',
			ondelete='cascade', 
			string="Tratamiento",
			#required=True, 
		)





	# --------------------------------------------------------- Consultation Fundamentals ------------------------------------------------------
	
	x_reason_consultation = fields.Text(
			string = 'Motivo de consulta (detalle)', 
			)
	
	x_observation = fields.Text(
			string="Observación",
			size=200,
			)

	x_next_evaluation_date = fields.Date(
			string = "Próxima cita", 	
			#default = fields.Date.today, 
			)

	x_fitzpatrick = fields.Selection(
			selection = eval_vars.FITZ_TYPE, 
			string = 'Fitzpatrick',
			default = '', 
			)

	x_photo_aging = fields.Selection(
			selection = eval_vars.PHOTO_TYPE, 
			string = 'Foto-envejecimiento',
			default = '', 
			)



	

	# --------------------------------------------------------- Consultation First ------------------------------------------------------

	#x_diagnosis = fields.Text(
	#		string = 'Diagnóstico', 
	#		required=False, 
	#	)

	#x_antecedents = fields.Text(
	#		string = 'Antecedentes médicos', 
	#		required=False, 
	#	)

	#x_allergies_medication = fields.Text(
	#		string = 'Alergias a medicamentos', 
	#		required=False, 
	#	)

	#x_observations = fields.Text(
	#		string = 'Observaciones',
	#		required=False, 
	#	)

	#x_indications = fields.Text(
	#		string = 'Indicaciones',
	#		required=False, 
	#	)

	#x_analysis_lab = fields.Boolean(
	#		string = 'Análisis de laboratorio', 			
	#		default=False, 
	#	)





# ----------------------------------------------------------- Autofill ------------------------------------------------------

	# Autofill 
	@api.onchange('x_autofill')
	def _onchange_x_autofill(self):
		if self.x_autofill == True:
			self.x_fitzpatrick = 'two'	
			self.x_photo_aging = 'three'
			self.x_diagnosis = '1. Acné activo. 2. Secuelas de acné.'
			self.x_antecedents = 'Demostración con Punta de Diamante. Niega enfermedades y cirugías.'
			self.x_allergies_medication = 'Niega AMs.'
			self.x_observations = 'Cicatriz plana hiperpigmentada en pómulo derecho. Pápulas en pómulos.'
			self.x_indications = 'Láser Co2 Fraccional.'
	# _onchange_x_autofill




	#----------------------------------------------------------- Open Line ------------------------------------------------------------

	@api.multi
	def open_line_current(self):  
		consultation_id = self.id 
		return {
				'type': 'ir.actions.act_window',
				'name': ' Edit Consultation Current', 
				'view_type': 'form',
				'view_mode': 'form',
				'res_model': self._name,
				'res_id': consultation_id,
				'target': 'current',
				'flags': {
						#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
						'form': {'action_buttons': True, }
						},
				'context': {}
		}
	# open_line_current


