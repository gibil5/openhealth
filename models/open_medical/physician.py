# -*- coding: utf-8 -*-
"""
	*** Oeh Medical Physician
	
	Kill coupling with OeHealth 
 
	Created: 		 6 Mar 2017
	Previous: 		11 dec 2020
	Last up: 		 7 apr 2021
"""
from openerp import models, fields, api

class Physician(models.Model):
	"""
	Overwrites the oh class
	"""
	_inherit = 'oeh.medical.physician'	
	#_name = 'oeh.medical.physician'	


# ----------------------------------------------------------- Relational -------
	#configurator_id = fields.Many2one(
	#		'openhealth.configurator.emr',
	#	)


# ----------------------------------------------------------- Fields -----------
	idx = fields.Char(
		)

	x_therapist = fields.Boolean(
			string='Terapeuta', 
			default=False,
		)	
	
	x_user_name = fields.Many2one(		
			'res.users',
			string = "Nombre de usuario", 	
		)

	consultancy_type = fields.Selection(			
			string='Tipo', 
		)

	vspace = fields.Char(
			' ', 
			readonly=True
		)


# ---------------------------------------------------- Static methods ----------
	# Get
	@staticmethod
	def get_doctors(obj):
		env = obj.env['oeh.medical.physician']
		doctors_active = Physician.get_active(env)
		doctors_inactive = Physician.get_inactive(env)
		return doctors_active - doctors_inactive

	# Get
	#@staticmethod
	def get_active(env):
		# Doctors Inactive
		doctors = env.search([
								('active', '=', True),
							],
							#order='date_begin,name asc',
							#limit=1,
							)
		return 	doctors	

	# Get
	#@staticmethod
	def get_inactive(env):
		# Doctors Inactive
		doctors = env.search([
								('active', '=', False),
							],
							#order='date_begin,name asc',
							#limit=1,
							)
		return 	doctors	


# ------------------------------------------------------ Getter ----------------
	#@api.multi
	def get_name_code(self):
		"""
		Getter
		"""
		code = 'x'
		if self.name not in [False]:
			words = self.name.upper().split()
			if len(words) > 1:
				code = words[0] + '_' + words[1][0:3]
				code = code.replace('.', '')
		return code

