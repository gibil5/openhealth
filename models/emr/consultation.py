# -*- coding: utf-8 -*-
"""
		Consultation 

		Created: 			 1 nov 2016
		Last updated: 	 	10 oct 2020
"""
from datetime import datetime,tzinfo,timedelta
from openerp import models, fields, api

#from openerp.addons.openhealth.models.libs import eval_vars
#from openerp.addons.openhealth.models.commons.libs import eval_vars
from . import eval_vars

class Consultation(models.Model):
	_name = 'openhealth.consultation'
	_inherit = 'oeh.medical.evaluation'
	
# ----------------------------------------------------------- Primitives -------
	# Name 
	name = fields.Char(
			string = 'Consulta #',
			)

	# Profile 
	x_profile = fields.Selection(
			[
				('normal','Normal'), 
				('anxious','Ansioso'), 
				('psychiatric','Psiquiátrico'), 
				('plaintif','Quejoso'), 
				('depressed','Deprimido'), 
				('histroinic','Histriónico'), 
				('other','Otro'), 		
			],
			string="Perfil psicológico", 
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

			compute='_compute_state', 
		)

	@api.multi
	def _compute_state(self):

		dic = {	0: 'draft',
				7: 'done' }

		for record in self:

			#pro = record.x_fitzpatrick + record.x_photo_aging + record.x_diagnosis + record.x_antecedents + record.x_allergies_medication + record.x_observations + record.x_indications

			# Calc
			pro = 0
			for p in [record.x_fitzpatrick, record.x_photo_aging, record.x_diagnosis, record.x_antecedents, record.x_allergies_medication, record.x_observations, record.x_indications]:
				pro+=1 if p else 0
			if pro in dic:
				record.state = dic[pro]
			else: 
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

			record.progress = eval_vars._hash_progress[record.state]




# ----------------------------------------------------------- Relational -------
	treatment = fields.Many2one(
			'openhealth.treatment',
			ondelete='cascade', 
			string="Tratamiento",
			#required=True, 
		)

# --------------------------------------------- Consultation Fundamentals ------
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
			default = 'one', 
			)

	x_photo_aging = fields.Selection(
			selection = eval_vars.PHOTO_TYPE, 
			string = 'Foto-envejecimiento',
			default = 'one', 
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
			#self.x_fitzpatrick = 'two'	
			#self.x_photo_aging = 'three'
			#self.x_diagnosis = '1. Acné activo. 2. Secuelas de acné.'
			#self.x_antecedents = 'Demostración con Punta de Diamante. Niega enfermedades y cirugías.'
			#self.x_allergies_medication = 'Niega AMs.'
			#self.x_observations = 'Cicatriz plana hiperpigmentada en pómulo derecho. Pápulas en pómulos.'
			#self.x_indications = 'Láser Co2 Fraccional.'
			
			self.autofill()

	# _onchange_x_autofill



	# Autofill 
	@api.multi
	def autofill(self):  
		self.x_fitzpatrick = 'two'	
		self.x_photo_aging = 'three'
		self.x_diagnosis = '1. Acné activo. 2. Secuelas de acné.'
		self.x_antecedents = 'Demostración con Punta de Diamante. Niega enfermedades y cirugías.'
		self.x_allergies_medication = 'Niega AMs.'
		self.x_observations = 'Cicatriz plana hiperpigmentada en pómulo derecho. Pápulas en pómulos.'
		self.x_indications = 'Láser Co2 Fraccional.'




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


