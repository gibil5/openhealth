# -*- coding: utf-8 -*-
"""
		*** Oeh Medical Physician
 
		Created: 		 6 Mar 2017
		Last up:		22 Aug 2020
"""
from openerp import models, fields, api

class Physician(models.Model):
	"""
	Overwrites the oh class
	"""

	_inherit = 'oeh.medical.physician'	

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

# ----------------------------------------------------------- Relational -------
	configurator_id = fields.Many2one(
			'openhealth.configurator.emr',
		)

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
