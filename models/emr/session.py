# -*- coding: utf-8 -*-
"""
	*** Session

	Created: 			01 Nov 2016
	Previous: 	 		22 aug 2020
	Last: 	 			14 apr 2021
"""
from openerp import models, fields, api
from datetime import datetime
from . import eval_vars
from .lib import tre_funcs as time_funcs

class Session(models.Model):
	"""
	Class Session
	"""	
	_name = 'openhealth.session'
	#_inherit = ['oeh.medical.evaluation', 'base_multi_image.owner']
	_inherit = ['oeh.medical.evaluation']


# ----------------------------------------------------------- Relational -------
	# Treatment 
	treatment = fields.Many2one(
			'openhealth.treatment',
			'Tratamiento', 
			ondelete='cascade', 
			)

	# Procedure  
	procedure = fields.Many2one(
			'openhealth.procedure',			
			string="Procedimiento",			
			readonly=True,
			ondelete='cascade', 
		)


# ----------------------------------------------------------- Descriptors -------
	# Name 
	name = fields.Char(
		string='Sesion #',
		default='SES',
		required=True,
	)

	# Evaluation type
	evaluation_type = fields.Selection(
		selection=eval_vars.EVALUATION_TYPE,
		string='Tipo',
		required=True,
		default='session',
	)

	# Owner 
	owner_type = fields.Char(
			default = 'session',
		)

	# Date
	evaluation_start_date = fields.Datetime(
		string = "Fecha", 	
		required=False, 		
	)

# --------------------------------------------------------------- Fields -------
	# Evaluation Number 
	evaluation_nr = fields.Integer(
			string="Sesión #",
			default=1,
		)

	# Date 
	evaluation_start_date = fields.Datetime(
			string = "Fecha y hora",
			default = fields.Date.today,
			required=True,
		)

#--------------------------------------------------------------- Computes ------
	# state 
	state = fields.Selection(
			selection = eval_vars._state_list,
			default='draft',

			compute='_compute_state', 
		)
	@api.multi
	def _compute_state(self):
		for record in self:
			state = 'draft'
			if record.x_done: 
				state = 'done'
			record.state = state


#----------------------------------------------------------- Quick Button ------
	@api.multi
	def open_line_current(self):
		return {
				'type': 'ir.actions.act_window',
				'name': 'Edit Session Current', 
				'view_type': 'form',
				'view_mode': 'form',
				'res_model': self._name,
				'res_id': self.id,
				'target': 'current',
				'flags': {
						'form': {'action_buttons': True, }
						},
				'context': {}
		}
