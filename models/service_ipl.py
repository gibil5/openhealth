# -*- coding: utf-8 -*-
#
# 	Service Ipl 
# 

from openerp import models, fields, api
from datetime import datetime


from . import ipl

from . import serv_funcs



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

	# Time 
	time_1 = fields.Selection(
			
			#selection = ndyag._time_list, 
			selection = ipl._time_list, 
			
			string="Tiempo", 
			default='none',	
	)





# ----------------------------------------------------------- On Changes ------------------------------------------------------
	@api.onchange('nr_sessions_1')
	def _onchange_nr_sessions_1(self):
	
		if self.nr_sessions_1 != 'none':	
			self.nr_sessions = self.nr_sessions_1
			

			serv_funcs.product_m22(self)

			return {
				'domain': {'service': [('x_treatment', '=', self.laser),('x_zone', '=', self.zone),('x_pathology', '=', self.pathology),('x_time', '=', self.time),('x_sessions', '=', self.nr_sessions) ]},
			}
			




	









			

	# Propietary
			
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
	
	#def clear_all(self,token):
	#	self.clear_commons
	#	self.clear_local  
	#	return token 
		
		

		
	@api.multi
	def clear_local(self):
		
		# First
		self.depilation = 'none'
		self.face = 'none'

		# Times
		self.time = ''
		self.time_1 = 'none'
		#self.clear_common_times
		
		# Sessions
		self.nr_sessions = ''
		self.nr_sessions_1 = 'none'
		
	
	
	