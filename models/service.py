# -*- coding: utf-8 -*-
#
# 	Service 
# 
# Created: 				20 Sep 2016
# Last updated: 	 	12 Oct 2016


from openerp import models, fields, api
from datetime import datetime

import jxvars


import exc
import ipl

import prodvars

import service_vars


	

class Service(models.Model):
	_name = 'openhealth.service'


	# Name 
	name = fields.Char(
			default='SE',
			string='Servicio #',
			compute='_compute_name', 
			#required=True, 
			)

	@api.multi
	def _compute_name(self):
		for record in self:
			record.name = 'SE00' + str(record.id) 



	# Service 
	service = fields.Many2one(
			'product.template',

			domain = [
						('type', '=', 'service'),
					],

			string="Servicio",
			required=True, 
			)





	# Canonical 

	family = fields.Selection(
		selection=prodvars._family_list,
		)	

	laser = fields.Selection(
			#selection = jxvars._laser_type_list, 
			selection = service_vars._laser_type_list, 
			string="Láser", 			
			default='none',			
			#required=True, 
			index=True
			)



	x_treatment = fields.Selection(
		selection=prodvars._treatment_list,
		)	



	zone = fields.Selection(
			selection = jxvars._zone_list, 
			string="Zona", 
			)


	pathology = fields.Selection(
			#selection = jxvars._pathology_list, 
			selection = service_vars._pathology_list, 
			string="Patología", 
			)



	sessions = fields.Selection(
			#selection = jxvars._pathology_list, 
			selection = prodvars._sessions_list, 
			string="Sesiones", 
			)






# ----------------------------------------------------------- Relationals ------------------------------------------------------

	# Treatement 
	treatment = fields.Many2one('openhealth.treatment',
			ondelete='cascade', 			
			string="Tratamiento", 
			)


	cosmetology = fields.Many2one('openhealth.cosmetology',
			ondelete='cascade', 			
			string="Cosmiatría", 
			)





	# Consultation 
	consultation = fields.Many2one('openhealth.consultation',
			ondelete='cascade', 		
			string="Consulta", 
			)









	# Commons 
	def clear_all(self,token):
		
		print
		print 'jx'
		print 'Clear All'

		self.clear_commons()
		self.clear_local() 
		return token


		
	def clear_commons(self):	

		print
		print 'jx'
		print 'Clear Commons'

		self.zone = 'none'
		self.pathology = 'none'
		


	def clear_times(self,token):
		self.time = ''
		self.time_1 = 'none'		
		return token
		
		

		
		

	
	# Time 
	time = fields.Char(
			default='',
	)
	
	time_1 = fields.Selection(
			selection = exc._time_list, 
			string="Tiempo", 
			default='none',	
			)


	@api.onchange('time_1')
	def _onchange_time_1(self):
	
		if self.time_1 != 'none':				
			self.time_1 = self.clear_times(self.time_1)
			self.time = self.time_1
			
			return {
				'domain': {'service': [('x_treatment', '=', self.laser),('x_zone', '=', self.zone),('x_pathology', '=', self.pathology),('x_time', '=', self.time)]},				
			}





	
	# Nr sessions
	
	nr_sessions = fields.Char(
			default='',	
	)
	
	
	nr_sessions_1 = fields.Selection(
			selection = ipl._nr_sessions_list, 
			string="Número de sesiones", 
			default='none',	
	)

	@api.onchange('nr_sessions_1')
	def _onchange_nr_sessions_1(self):
	
		if self.nr_sessions_1 != 'none':	
			self.nr_sessions = self.nr_sessions_1
			
			return {
				'domain': {'service': [('x_treatment', '=', self.laser),('x_zone', '=', self.zone),('x_pathology', '=', self.pathology),('x_time', '=', self.time),('x_sessions', '=', self.nr_sessions) ]},
			}
			



		

	# Service
	@api.onchange('service')
	def _onchange_service(self):
	
		if self.service != 'none':
			self.time_1 = self.service.x_time
		
			
































	# Code 
	code = fields.Char(
			compute='_compute_code', 
			string='Code'
			)

	@api.depends('service')
	def _compute_code(self):
		for record in self:
			record.code= record.service.name 






	# Name short 
	name_short = fields.Char(
			compute='_compute_name_short', 
			#string='Short name'
			#string='Código'
			#string='Código interno'
			)

	@api.depends('service')

	def _compute_name_short(self):
		for record in self:
			record.name_short = record.service.x_name_short 






	#Price 
	price = fields.Float(
			compute='_compute_price', 
			#string='Price'
			string='Precio (S/.)'
			) 

	#@api.multi
	@api.depends('service')

	def _compute_price(self):
		for record in self:
			record.price= (record.service.list_price)






	# Price VIP
	price_vip = fields.Float(
			compute='_compute_price_vip', 
			#string='price_vip'
			string='Precio VIP (S/.)'
			) 

	#@api.multi
	@api.depends('service')

	def _compute_price_vip(self):
		for record in self:
			record.price_vip= (record.service.x_price_vip)






	# Other
	vspace = fields.Char(
			' ', 
			readonly=True
			)
			
	title = fields.Char(
			string='Title', 
			default='',
			readonly=True,
			)
	
	notebook_over = fields.Char(
			string='Over notebook', 
			default='',
			readonly=True,
			)






	# ---------------------------------------------- Open Line --------------------------------------------------------

	@api.multi
	def open_line_current(self): 

		service_id = self.id 

		return {
				'type': 'ir.actions.act_window',
				'name': ' Edit Service Current', 
				'view_type': 'form',
				'view_mode': 'form',
				'res_model': self._name,
				'res_id': service_id,
				'target': 'current',
				'flags': {
						'form': {'action_buttons': True, }
						},

				'context': {
				}
		}

	# open_line_current 



