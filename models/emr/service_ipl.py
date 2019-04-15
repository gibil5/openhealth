# -*- coding: utf-8 -*-
"""
	Service Ipl 
"""
from datetime import datetime
from openerp import models, fields, api
from . import ipl
from . import prodvars

class ServiceIpl(models.Model):
	
	_name = 'openhealth.service.ipl'
	
	_inherit = 'openhealth.service'
	



# ----------------------------------------------------------- Natives ------------------------------
	# Service 
	service = fields.Many2one(
			'product.template',

			domain = [
						('type', '=', 'service'),
						('x_treatment', '=', 'laser_ipl'),
					],
	)





# ---------------------------------------------- Default --------------------------------------------------------
	# Laser 
	laser = fields.Selection(
			selection = prodvars._laser_type_list, 
			string="Láser", 			
	
			default='laser_ipl',			

			index=True,
		)



# ----------------------------------------------------------- Fields ------------------------------------------------------

	# Time 
	time_1 = fields.Selection(
			selection = ipl._time_list, 
			string="Tiempo", 
			default='none',	
	)

	# Depilation 
	depilation = fields.Selection(
			selection = ipl._depilation_list, 
			string="Depilación", 
			default='none',	
			)

	# All Face 
	face = fields.Selection(
			selection = ipl._face_list, 
			string="Todo rostro", 
			default='none',	
			)


# ----------------------------------------------------------- Actions ------------------------------------------------------
	@api.multi
	def clear_local(self):
		
		# Fields
		self.depilation = 'none'
		self.face = 'none'

		# Times
		self.time = ''
		self.time_1 = 'none'
		
		# Sessions
		self.nr_sessions = ''
		self.nr_sessions_1 = 'none'
		
	
	
# ----------------------------------------------------------- On Changes ------------------------------------------------------
	# On Change - Clear the rest

	@api.onchange('nr_sessions_1')
	def _onchange_nr_sessions_1(self):
		if self.nr_sessions_1 != 'none':	
			self.nr_sessions = self.nr_sessions_1
			self.get_product_m22()
			return {
				'domain': {'service': [('x_treatment', '=', self.laser),('x_zone', '=', self.zone),('x_pathology', '=', self.pathology),('x_time', '=', self.time),('x_sessions', '=', self.nr_sessions) ]},
			}

	@api.onchange('depilation')
	def _onchange_depilation(self):	
		if self.depilation != 'none':	
			self.depilation = self.clear_all(self.depilation)
			self.zone = self.depilation
			self.pathology = 'depilation'
			return {
				'domain': {'service': [('x_treatment', '=', self.laser),('x_zone', '=', self.zone),('x_pathology', '=', self.pathology)]},
			}

	@api.onchange('face')
	def _onchange_face(self):	
		if self.face != 'none':	
			self.face = self.clear_all(self.face)
			self.pathology = self.face
			self.zone = 'face'
			return {
				'domain': {'service': [('x_treatment', '=', self.laser),('x_zone', '=', self.zone),('x_pathology', '=', self.pathology)]},
			}
