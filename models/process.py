# -*- coding: utf-8 -*-
#
#
# 		*** OPEN HEALTH - Process
# 
# Created: 				18 Feb 2017
# Last updated: 	 	Id.



from openerp import models, fields, api

import jxvars

import treatment_vars



class Process(models.Model):
	
	_name = 'openhealth.process'
	






	# ----------------------------------------------------------- Variables ------------------------------------------------------
	
	name = fields.Char(
			string="Proceso #", 
			#required=True, 
		)






	patient = fields.Many2one(
			'oeh.medical.patient',

			string="Paciente",
			
			index=True, 
			ondelete='cascade', 
			#required=True, 
			)



	physician = fields.Many2one(

			'oeh.medical.physician',
		
			string="Médico",
			
			index=True
			)
	


	#therapist = fields.Many2one(
			#'oeh.medical.therapist',
	#		'oeh.medical.physician',


			#string="Terapeuta",
	#		string = "Cosmeatra", 	


	#		index=True
	#		)






	chief_complaint = fields.Selection(
			string = 'Motivo de consulta', 			
			#selection = tre_vars._chief_complaint_list, 
			selection = jxvars._chief_complaint_list, 
			)





	duration = fields.Integer(
			string="Días", 
			default = 0,
			)

	start_date = fields.Date(
			string="Fecha inicio", 
			default = fields.Date.today
			)

	price_total = fields.Float(
			string='Total', 
			default = 0, 
			) 




#	_state_list = [
#        			#('empty', 			'Inicio'),
#        			('one', 	'Uno'),
#        			('two', 		'Dos'),
#        			('three', 			'Tres'),
#        			('done', 			'Completo'),
#        		]


	state = fields.Selection(

			#selection = _state_list, 
			selection = treatment_vars._state_list, 

			string='Estado', 	
					
			default = False, 
		)






	progress = fields.Float(
			string='Progreso', 			
			default = 0., 

			compute='_compute_progress', 
		)

	@api.multi
	#@api.depends('state')

	def _compute_progress(self):
		for record in self:
			print 
			print 'jx'
			print 'Compute progress'
			record.progress = treatment_vars._hash_progress[record.state]
			print 







	# Open 
	process_open = fields.Boolean(
			string="Abierto",
			default=True,
	)


	end_date = fields.Date(
			string="Fecha fin", 
			default = fields.Date.today
			)


	nr_procedures = fields.Integer(
			string="Procedimientos",
			#compute="_compute_nr_procedures",
	)



# Process
