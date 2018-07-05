# -*- coding: utf-8 -*-
#
# 	*** Procedure 	
#
# Created: 				 1 Nov 2016
# Last updated: 	 	 22 Jun 2017
#

from openerp import models, fields, api
from datetime import datetime
from . import time_funcs
from . import cosvars
from . import app_vars
from . import pro_con_funcs
from . import pro_ses_funcs



class Procedure(models.Model):

	_name = 'openhealth.procedure'

	#_inherit = ['oeh.medical.evaluation', 'openhealth.base']
	_inherit = 'oeh.medical.evaluation'




# ----------------------------------------------------------- Deprecated ------------------------------------------------------
	#appointment_ids = fields.One2many(
	#		'oeh.medical.appointment', 
	#		'procedure', 
	#		string = "Citas", 
	#		)





# ----------------------------------------------------------- Redefinition ------------------------------------------------------

	# Default - HC Number 
	@api.model
	def _get_default_id_code(self):

		print 
		print 'Get Default App - 2'

		#patient = self.patient
		patient = self.treatment.patient

		doctor = self.treatment.physician

		print patient
		print doctor

 		app = self.env['oeh.medical.appointment'].search([
																('patient', '=', patient), 
																('doctor', '=', doctor), 
														],
															#order='write_date desc',
															limit=1,
														)
 		print app

		return app




	def _get_default_appointment(self):
		
		print 
		print 'Get Default App'
		#print x_type
		
		print self.patient
		print self.doctor

		patient = self.patient
		doctor = self.doctor

 		app = self.env['oeh.medical.appointment'].search([
																('patient', '=', patient), 
																('doctor', '=', doctor), 
														],
															#order='write_date desc',
															limit=1,
														)
 		print app

		return app
	# _get_default_appointment





	# Appointment 
	appointment = fields.Many2one(
			'oeh.medical.appointment',			
			string='Cita #', 
			required=False, 			
			#ondelete='cascade', 

			#default=lambda self: self._get_default_appointment(),
			#default=_get_default_id_code, 
		)



	# Update App  
	@api.multi	
	def update_appointment(self):

		print 
		print 'Update Appointment'

		patient = self.patient
		doctor = self.doctor
		x_type = 'procedure'

 		app = self.env['oeh.medical.appointment'].search([
																('patient', '=', patient.name), 
																('doctor', '=', doctor.name), 
																('x_type', '=', x_type), 
														],
															#order='write_date desc',
															order='appointment_date desc',
															limit=1,
														)
 		print app 

 		self.appointment = app






# ----------------------------------------------------------- Actions ------------------------------------------------------

	# Create Controls 
	@api.multi	
	def create_controls(self):
		ret = pro_con_funcs.create_controls(self)
	# create_controls



	# Create Sessions 
	@api.multi	
	def create_sessions(self): 
		ret = pro_ses_funcs.create_sessions(self)
	# create_sessions








# ----------------------------------------------------------- Primitives ------------------------------------------------------

	# Name 
	name = fields.Char(
			#string = 'Procedimiento #',
			string = 'Proc #',
		)


	# Owner 
	owner_type = fields.Char(
			default = 'procedure',
		)


	# Redefinition 
	evaluation_type = fields.Selection(
			default = 'Ambulatory', 
			)



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

			#sessions = self.env['openhealth.session'].search([
																#('name','like', record.patient.name),	
			#													('procedure','=', record.id),
			#												],
			#												order='evaluation_start_date asc',
															#limit=1,
			#										)
			#ctr = 1
			#for session in sessions: 
			#	session.evaluation_nr = ctr
			#	ctr = ctr + 1




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







	# Sessions for the Procedure 
	number_sessions = fields.Integer(
			string="Sesiones",

			compute="_compute_number_sessions",
	)

	#@api.multi
	@api.depends('product')
	def _compute_number_sessions(self):
		for record in self:
			record.number_sessions = record.product.x_sessions





	# Machine 
	machine = fields.Selection(
			string="Sala", 
			#selection = app_vars._machines_list, 
			selection = app_vars._subtype_list, 
			#required=True, 

			#compute="_compute_machine",
		)

	#@api.multi
	#@api.depends('product')
	#def _compute_machine(self):
	#	for record in self:
	#		tre = record.product.x_treatment
	#		mac = cosvars._hash_tre_mac[tre]
	#		record.machine = mac







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

				#if record.laser == 'laser_co2':
				if record.laser == 'laser_co2'  		or 		record.laser == 'laser_quick':
					record.number_controls = 6
				
				else: 
					record.number_controls = 0






# ----------------------------------------------------------- Relational ------------------------------------------------------

	session_ids = fields.One2many(
			'openhealth.session.med', 
			'procedure', 
			string = "sessiones", 
			)




	control_ids = fields.One2many(
			'openhealth.control', 
			'procedure', 

			string = "Controles", 
			)


	treatment = fields.Many2one(
			'openhealth.treatment',
			string="Tratamiento", 
			ondelete='cascade', 
			)



# ----------------------------------------------------------- Buttons ------------------------------------------------------

	# Open Line   
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

	# open_line_current
