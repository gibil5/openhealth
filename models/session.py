# -*- coding: utf-8 -*-
#
# 	session 	
# 

from openerp import models, fields, api
from datetime import datetime

import jxvars




class Session(models.Model):
	_name = 'openhealth.session'
	_inherit = 'oeh.medical.evaluation'


	name = fields.Char(
			string = 'Sesión #',
			)
			
	procedure = fields.Many2one('openhealth.procedure',
			string="Procedimiento",
			readonly=True,
			ondelete='cascade', 
			)
			

	# Motivo de consulta
	chief_complaint = fields.Selection(
			string = 'Motivo de consulta', 
			selection = jxvars._pathology_list, 
			#default = '', 
			required=True, 
			)
			
			
			
	# Product 
	product = fields.Many2one(
			'product.template',
			string="Producto",
			readonly=True,
			required=True, 
			)
	
	laser = fields.Selection(
			selection = jxvars._laser_type_list, 
			string="Láser", 			
			readonly=True,
			#compute='_compute_laser', 
			#default='none',
			#required=True, 
			#index=True
			)