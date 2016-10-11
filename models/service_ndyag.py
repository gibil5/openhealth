# -*- coding: utf-8 -*-
#
# 	Service Ndyag 
# 

from openerp import models, fields, api
from datetime import datetime

import ndyag



class ServiceNdyag(models.Model):
	_name = 'openhealth.service.ndyag'

	_inherit = 'openhealth.service'
	
	
	
	# Service 
	service = fields.Many2one(
			'product.template',

			domain = [
						('type', '=', 'service'),
						('x_treatment', '=', 'laser_ndyag'),
					],
	)
	
	
	
	time_1 = fields.Selection(
			selection = ndyag._time_list, 
			#string="Tiempo", 
			#default='none',	
	)
			
			
			
	
	
	face = fields.Selection(
			selection = ndyag._face_list, 
			string="Todo rostro", 
			default='none',	
	)
			
	body = fields.Selection(
			selection = ndyag._body_list, 
			string="Todo cuerpo", 
			default='none',	
	)
			
			
			
			
			
			
	@api.onchange('face')
	def _onchange_face(self):
	
		if self.face != 'none':	
			self.face = self.clear_all(self.face)

			self.pathology = self.face
			self.zone = 'face_local'
			
			return {
				'domain': {'service': [('x_treatment', '=', self.laser),('x_zone', '=', self.zone),('x_pathology', '=', self.pathology)]},
			}


	@api.onchange('body')
	def _onchange_body(self):
	
		if self.body != 'none':	
			self.body = self.clear_all(self.body)

			self.pathology = self.body
			self.zone = 'body_local'
			
			return {
				'domain': {'service': [('x_treatment', '=', self.laser),('x_zone', '=', self.zone),('x_pathology', '=', self.pathology)]},
			}
			
		

	# Clear 
		
	def clear_all(self,token):
		
		# Service
		#self.zone = 'none'
		#self.pathology = 'none'
		#self.time_1 = 'none'
		#self.nr_sessions = 'none'
		self.clear_commons
		
		
		# First
		self.face = 'none'
		self.body = 'none'

		return token
		

	