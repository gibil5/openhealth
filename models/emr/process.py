# -*- coding: utf-8 -*-
"""
		*** OPEN HEALTH - Process - Dep !!!

		Created: 				18 Feb 2017
		Last updated: 	 		20 Sep 2019
"""
from openerp import models, fields, api
from openerp.addons.openhealth.models.libs import eval_vars

class Process(models.Model):
	
	_name = 'openhealth.process'
	
	# Important - Inherited by: Treatment, Cosmetology 




# ----------------------------------------------------------- Used ------------------------------------------------------
	# Patient 
	patient = fields.Many2one(
			'oeh.medical.patient',
			string="Paciente",
			index=True, 
			ondelete='cascade', 
			#required=True, 
			
			readonly=True, 
			states=READONLY_STATES, 
		)


	# States 
	READONLY_STATES = {
		'empty': 		[('readonly', False)], 
		#'done': 		[('readonly', True)], 	
	}



	# Physician
	physician = fields.Many2one(
			'oeh.medical.physician',
			string="Médico",
			index=True,
	
			#readonly=True, 
			readonly=False, 

			states=READONLY_STATES, 
		)



	chief_complaint = fields.Selection(
			string = 'Motivo de consulta', 						
			selection = eval_vars._chief_complaint_list, 
			required=False, 

			#readonly=True, 
			readonly=False, 
			#states=READONLY_STATES, 
		)



	start_date = fields.Date(
			string="Fecha inicio", 
			default = fields.Date.today, 

			readonly=True, 
			states=READONLY_STATES, 
		)




# ----------------------------------------------------------- Not Used ------------------------------------------------------


	end_date = fields.Date(
			string="Fecha fin", 
			default = fields.Date.today
			)

	
	name = fields.Char(
			string="Proceso #", 
			#required=True, 
		)


	duration = fields.Integer(
			string="Días", 
			default = 0,
			)


	price_total = fields.Float(
			string='Total', 
			default = 0, 
			) 


	_state_list = [
        			('one', 		'Uno'),
        			('two', 		'Dos'),
        			('three', 		'Tres'),
        			('done', 		'Completo'),
        		]
	
	state = fields.Selection(
	
			selection = _state_list, 
			#selection = treatment_vars._state_list, 
	
			string='Estado', 	
			default = False, 
		)


	# Progress 
	_hash_progress = {
					'empty':          0, 
					'appointment': 			10, 
					'budget_consultation':  15, 
					'invoice_consultation': 20,
					'consultation': 	30,
					'service': 			40, 
					'budget_procedure': 			50, 
					'invoice_procedure': 			60,
					'procedure': 		70, 
					'sessions': 		80, 
					'controls': 		90, 
					'done': 			100, 
	}


	progress = fields.Float(
			string='Progreso', 			
			default = 0., 

			compute='_compute_progress', 
		)


	@api.multi
	#@api.depends('state')

	def _compute_progress(self):
		for record in self:

			#record.progress = treatment_vars._hash_progress[record.state]
			record.progress = _hash_progress[record.state]



	nr_procedures = fields.Integer(
			string="Procedimientos",
			#compute="_compute_nr_procedures",
	)

# Process
