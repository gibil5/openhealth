# -*- coding: utf-8 -*-
#
# 	Service Ndyag 
# 
from openerp import models, fields, api
from datetime import datetime
import serv_funcs

import ndyag

class ServiceNdyag(models.Model):
	_name = 'openhealth.service.ndyag'
	_inherit = 'openhealth.service'
	
	
	
# ----------------------------------------------------------- Fields ------------------------------------------------------
	# Service 
	service = fields.Many2one(
			'product.template',

			domain = [
						('type', '=', 'service'),
						('x_treatment', '=', 'laser_ndyag'),
					],
	)
	
	# Time 
	time_1 = fields.Selection(
			selection = ndyag._time_list, 
			#selection = _time_list, 
			string="Tiempo", 
			default='none',	
	)
	
	# Face 
	face = fields.Selection(
			selection = ndyag._face_list, 
			#selection = _face_list, 
			string="Todo rostro", 
			default='none',	
	)

	# Body 
	body = fields.Selection(
			selection = ndyag._body_list, 
			#selection = _body_list, 
			string="Todo cuerpo", 
			default='none',	
	)



# ----------------------------------------------------------- Actions ------------------------------------------------------
	@api.multi
	def clear_local(self):
		
		# Fields
		self.face = 'none'
		self.body = 'none'
		
		# Times
		self.time = ''
		self.time_1 = 'none'

		# Sessions
		self.nr_sessions = ''
		self.nr_sessions_1 = 'none'



# ----------------------------------------------------------- On Changes ------------------------------------------------------
	@api.onchange('nr_sessions_1')
	def _onchange_nr_sessions_1(self):
		if self.nr_sessions_1 != 'none':	
			self.nr_sessions = self.nr_sessions_1
			serv_funcs.product_m22(self)
			return {
				'domain': {'service': [('x_treatment', '=', self.laser),('x_zone', '=', self.zone),('x_pathology', '=', self.pathology),('x_time', '=', self.time),('x_sessions', '=', self.nr_sessions) ]},
			}

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
