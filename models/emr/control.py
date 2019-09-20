# -*- coding: utf-8 -*-
"""
Control

Created: 			01 Nov 2016
Last updated: 	 	19 Sep 2019
"""
import datetime
from openerp import models, fields, api
#from openerp.addons.openhealth.models.libs import lib
#from . import time_funcs
from . import control_vars

class Control(models.Model):
	"""
	Class Control
	Defines the Data Model.
	Should not define the Business Rules. 
	"""	
	_name = 'openhealth.control'

	_inherit = ['oeh.medical.evaluation', 'base_multi_image.owner']

	_description = 'Control'


# ----------------------------------------------------------- Dep ------------------------------------------------------

	maturity = fields.Integer()

	nr_days = fields.Integer()



	control_date = fields.Datetime()

	first_date = fields.Datetime()

	real_date = fields.Datetime()

	evaluation_next_date = fields.Date()



# ----------------------------------------------------------- Dates - OK ------------------------------------------------------

	# Date
	evaluation_start_date = fields.Datetime(
			string = "Fecha", 	
			required=False, 		
		)


# ----------------------------------------------------------- State ------------------------------------------------------
	
	# State 
	state = fields.Selection(

			selection = control_vars._state_list, 
			
			#compute='_compute_state', 
		)


	@api.multi
	#@api.depends('state')
	def _compute_state(self):
		for record in self:

			state = 'draft'

			if record.appointment.state in ['Scheduled']: 
				state = 'app_confirmed'

			if record.x_done: 
				state = 'done'

			elif record.maturity > 90: 
				state = 'cancel'

			record.state = state


# ----------------------------------------------------------- Re Definitions ------------------------------------------------------

	# Patient 
	patient = fields.Many2one(
			'oeh.medical.patient',
			string = "Paciente", 	
			ondelete='cascade', 
			readonly=False, 
			required=True, 
		)

	# Treatment 
	treatment = fields.Many2one(
			'openhealth.treatment',
			ondelete='cascade',
			readonly=False,
			required=True,
		)


# ----------------------------------------------------------- Primitives ------------------------------------------------------

	# Name 
	name = fields.Char(
			#string = 'Control #',
			string = 'Nombre',
		)

	# Evaluation Nr
	evaluation_nr = fields.Integer(
			string="#", 
			default=1, 

			#compute='_compute_control_nr', 
		)

	# Evaluation type 
	evaluation_type = fields.Selection(
			#selection = eval_vars.EVALUATION_TYPE, 
			#string = 'Tipo',
			
			default='control', 
			
			#required=True, 
		)

	# Product
	product = fields.Many2one(
			'product.template',
			string="Producto",

			#required=True, 
			required=False, 			
		)

	# Owner 
	owner_type = fields.Char(
			default = 'control',
		)

	# Indications
	indication = fields.Text(
			string="Indicaciones",			
			size=200,

			#required=True,
			required=False,
			)

	# Observation
	observation = fields.Text(
			string="Observación",
			size=200,

			#required=True,
			required=False,
			)

	# Procedure  
	procedure = fields.Many2one('openhealth.procedure',
			string="Procedimiento",
			readonly=True,
			ondelete='cascade', 
			)
			

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
						#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
						'form': {'action_buttons': True, }
						},
				
				'context': {}
		}
