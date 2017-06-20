# -*- coding: utf-8 -*-
#
# 	*** Procedure 	
#
# Created: 				 1 Nov 2016
# Last updated: 	 	 20 Jun 2017



from openerp import models, fields, api
from datetime import datetime

#from . import jxvars
from . import time_funcs
from . import procedure_funcs
from . import cosvars
from . import app_vars



class Procedure(models.Model):

	_inherit = 'oeh.medical.evaluation'
	_name = 'openhealth.procedure'


	name = fields.Char(
			#string = 'Procedimiento #',
			string = 'Proc #',
			)


	# Machine 
	machine = fields.Selection(
			string="Sala", 
			selection = app_vars._machines_list, 
			#required=True, 
			compute="_compute_machine",
		)

	#@api.multi
	@api.depends('product')
	def _compute_machine(self):
		for record in self:
			tre = record.product.x_treatment
			mac = cosvars._hash_tre_mac[tre]
			record.machine = mac



	# Sessions - Quantity 
	number_sessions = fields.Integer(
			string="Sesiones",
			compute="_compute_number_sessions",
	)
	
	#@api.multi
	@api.depends('product')
	def _compute_number_sessions(self):
		for record in self:
			record.number_sessions = record.product.x_sessions



	# Controls - Quantity 
	number_controls = fields.Integer(
			string="Controles",
			compute="_compute_number_controls",
	)
	
	#@api.multi
	@api.depends('laser')
	
	def _compute_number_controls(self):
		for record in self:
			if record.laser != 'consultation':
				if record.laser == 'laser_co2':
					record.number_controls = 6
				else: 
					record.number_controls = 0



	# Owner 
	owner_type = fields.Char(
			default = 'procedure',
		)


	# Redefinition 
	evaluation_type = fields.Selection(
			default = 'Ambulatory', 
			)



# ----------------------------------------------------------- Relational ------------------------------------------------------

	session_ids = fields.One2many(
			'openhealth.session.med', 
			'procedure', 
			string = "sessiones", 
			)


	appointment_ids = fields.One2many(
			'oeh.medical.appointment', 
			'procedure', 
			string = "Citas", 
			)


	#jx 

	control_ids = fields.One2many(
			'openhealth.control', 
			'procedure', 

			string = "Controles", 
			)
			
			

# ----------------------------------------------------------- Indexes ------------------------------------------------------

	treatment = fields.Many2one(
			'openhealth.treatment',
			string="Tratamiento", 
			ondelete='cascade', 
			)



	
	# Controls - Number

	nr_controls = fields.Integer(
			string="Controles",
			compute="_compute_nr_controls",
	)
	
	#@api.multi
	@api.depends('control_ids')
	def _compute_nr_controls(self):
		for record in self:
			ctr = 0 
			for c in record.control_ids:
				ctr = ctr + 1
			record.nr_controls = ctr		






	# Sessions - Number
	nr_sessions = fields.Integer(
			string="Sesiones",
			compute="_compute_nr_sessions",
	)
	
	#@api.multi
	@api.depends('session_ids')
	def _compute_nr_sessions(self):
		for record in self:
			ctr = 0 
			for c in record.session_ids:
				ctr = ctr + 1
			record.nr_sessions = ctr

	
	
	




	#------------------------------------ Buttons -----------------------------------------


	# Create Controls 
	@api.multi
	def create_controls(self):
		ret = procedure_funcs.create_controls_go(self)






	# Consultation - Quick Self Button  

	@api.multi
	def open_line_current(self):  
		procedure_id = self.id 

		return {
				'type': 'ir.actions.act_window',
				'name': ' Edit Consultation Current', 
				'view_type': 'form',
				'view_mode': 'form',
				'res_model': self._name,
				'res_id': procedure_id,
				'target': 'current',
				'flags': {
						'form': {'action_buttons': True, }
						},

				'context':   {}
		}








	# Open Control 

	@api.multi
	def open_control(self):  

		# Data
		procedure_id = self.id 
		patient_id = self.patient.id
		doctor_id = self.doctor.id
		chief_complaint = self.chief_complaint
		evaluation_type = 'Periodic Control'
		product_id = self.product.id
		laser = self.laser
		
		# Date 		
		GMT = time_funcs.Zone(0,False,'GMT')
		evaluation_start_date = datetime.now(GMT).strftime("%Y-%m-%d %H:%M:%S")

		return {

			# Mandatory 
			'type': 'ir.actions.act_window',
			'name': 'Open control Current',

			# Optional 
			'res_model': 'openhealth.control',

			'view_mode': 'form',
			"views": [[False, "form"]],

			'target': 'current',

			'context':   {
				'default_patient': patient_id,
				'default_doctor': doctor_id,
				'default_chief_complaint': chief_complaint,
				'default_evaluation_type':evaluation_type,				
				'default_product': product_id,
				'default_laser': laser,
				'default_evaluation_start_date': evaluation_start_date,
				'default_procedure': procedure_id,
			}
		}
	# open_control







# ----------------------------------------------------------- Keys  ------------------------------------------------------
	key = fields.Char(
			string='key', 
			default='procedure', 
		)

	model = fields.Char(
			string='model', 
			default='openhealth.session.med', 
		)

	target = fields.Char(
			string='target', 

			default='doctor', 
		)



# ----------------------------------------------------------- Create Sessions  ------------------------------------------------------
	@api.multi
	def create_sessions(self): 

		model = 'openhealth.session.med'
		ret = procedure_funcs.create_sessions_go(self, model)
	# create_sessions


