# -*- coding: utf-8 -*-
#
# 	Service Ipl 
# 

from openerp import models, fields, api
from datetime import datetime

import ipl



class ServiceIpl(models.Model):
	_name = 'openhealth.service.ipl'

	_inherit = 'openhealth.service'
	

	
	# Service 
	service = fields.Many2one(
			'product.template',

			domain = [
						('type', '=', 'service'),
						('x_treatment', '=', 'laser_ipl'),
					],
	)
			
			
			
		
			





	# First



	depilation = fields.Selection(
			selection = ipl._depilation_list, 
			string="Depilación", 
			default='none',	
			)





	face = fields.Selection(
			selection = ipl._face_list, 
			string="Todo rostro", 
			default='none',	
			)





	# On Change - Clear the rest

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
			
		

	# Clear 
		
	def clear_all(self,token):
		
		# Service
		#self.zone = 'none'
		#self.pathology = 'none'
		#self.time_1 = 'none'
		#self.nr_sessions = 'none'
		self.clear_commons
		
		
		# First
		self.depilation = 'none'

		return token 
	
	
	
	
	
	