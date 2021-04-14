# -*- coding: utf-8 -*-
"""
	Control

	Created: 			01 Nov 2016
	Previous: 	 		19 Sep 2019
	Last: 	 			14 apr 2021
"""
import datetime
from openerp import models, fields, api

from . import eval_vars, control_vars

class Control(models.Model):
	"""
	Class Control
	Defines the Data Model.
	Should not define the Business Rules. 
	"""	
	_name = 'openhealth.control'
	_description = 'Control'
	_inherit = ['oeh.medical.evaluation', 'base_multi_image.owner']


# ----------------------------------------------------------- Relationals ------
	# Treatment 
	treatment = fields.Many2one(
		'openhealth.treatment',
		ondelete='cascade',
		readonly=False,
		required=True,
	)

	# Procedure  
	procedure = fields.Many2one('openhealth.procedure',
		string="Procedimiento",
		readonly=True,
		ondelete='cascade', 
	)

	# Patient 
	patient = fields.Many2one(
		'oeh.medical.patient',
		string = "Paciente", 	
		ondelete='cascade', 
		readonly=False, 
		required=True, 
	)

	# Product
	product = fields.Many2one(
		'product.template',
		string="Producto",
		required=False, 			
	)


# ----------------------------------------------------------- Descriptors -------
	# Name 
	name = fields.Char(
		string = 'Control #',
		default='CONTR',
		required=True,
	)

	# Evaluation type
	evaluation_type = fields.Selection(
		selection=eval_vars.EVALUATION_TYPE,
		string='Tipo',
		required=True,
		default='control', 
	)

	# Owner 
	owner_type = fields.Char(
		default = 'control',
	)

# ----------------------------------------------------------- Consts -----------

# ---------------------------------------------------------------- Dates -------
	# Date
	evaluation_start_date = fields.Datetime(
			string = "Fecha", 	
			required=False, 		
		)


# ----------------------------------------------------------- State ------------
	# State 
	state = fields.Selection(
			selection = control_vars._state_list, 
			
			compute='_compute_state', 
		)
	@api.multi
	def _compute_state(self):
		for record in self:
			state = 'draft'
			if record.x_done: 
				state = 'done'
			record.state = state



# ----------------------------------------------------------- Fields ----------------------------------------
	# Evaluation Nr
	evaluation_nr = fields.Integer(
		string="#", 
		default=1, 
	)

	# Indications
	indication = fields.Text(
		string="Indicaciones",			
		size=200,
		required=False,
	)

	# Observation
	observation = fields.Text(
		string="Observación",
		size=200,
		required=False,
	)

# ----------------------------------------------------------- not Dep --------------
	maturity = fields.Integer()
	nr_days = fields.Integer()
	control_date = fields.Datetime()
	first_date = fields.Datetime()
	real_date = fields.Datetime()
	evaluation_next_date = fields.Date()


# ----------------------------------------------------------- Actions ------------------------------------------------------
	# Open Line 
	@api.multi
	def open_line_current(self):  
		return {
				'type': 'ir.actions.act_window',
				'name': 'Edit Control Current', 
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
