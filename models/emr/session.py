# -*- coding: utf-8 -*-
"""
	*** Session - Dep ?
	Created: 			01 Nov 2016
	Last up: 	 		22 aug 2020
"""
from openerp import models, fields, api
from datetime import datetime

#from openerp.addons.openhealth.models.libs import eval_vars
#from openerp.addons.openhealth.models.commons.libs import eval_vars
from . import eval_vars

#from . import time_funcs
from .commons import tre_funcs as time_funcs


class Session(models.Model):
	"""
	Class Session
	"""	
	_name = 'openhealth.session'
	_inherit = ['oeh.medical.evaluation', 'base_multi_image.owner']

# ----------------------------------------------------------- Primitives -------
	# Evaluation Number 
	evaluation_nr = fields.Integer(
			string="Sesión #",
			default=1,
		)

	# Procedure  
	procedure = fields.Many2one(
			'openhealth.procedure',			
			string="Procedimiento",			
			readonly=True,
			ondelete='cascade', 
		)

	# Date 
	evaluation_start_date = fields.Datetime(
			string = "Fecha y hora",
			default = fields.Date.today,
			required=True,
		)

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

	# Evaluation type 
	evaluation_type = fields.Selection(
			default='session', 
			)

# ----------------------------------------------------------- Relational -------
	# Treatment 
	treatment = fields.Many2one(
			'openhealth.treatment',
			'Tratamiento', 
			ondelete='cascade', 
			)

	# Owner 
	owner_type = fields.Char(
			default = 'session',
		)

	name = fields.Char(
			string = 'Nombre',
			)

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
						#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
						'form': {'action_buttons': True, }
						},
				'context': {}
		}
