# -*- coding: utf-8 -*-
#
# 	Consultation 
# 
# Created: 				20 Sep 2016
# Last updated: 	 	20 Sep 2016

from openerp import models, fields, api
from datetime import datetime

import jxvars
import exc
import ipl



	

class Service(models.Model):
	_name = 'openhealth.service'



	# Name 
	name = fields.Char(
			#default='Laser Co2',
			#string='Name',
			#string='Nombre',



			default='SE',
			
			#string='Servicio #',
			string='Servicio #',

			compute='_compute_name', 
			required=True, 
			)

	@api.multi
	def _compute_name(self):
		for record in self:
			#record.name = 'SE0000' + str(record.id) 
			record.name = 'SE00' + str(record.id) 










	# Smart factorization
	
	
	vspace = fields.Char(
			' ', 
			readonly=True
			)
	
	
	
	time = fields.Char(
			default='',
	)
			
	client_type = fields.Char(
			default='',	
	)
			

	


	# Time 
	
	time_1 = fields.Selection(
			selection = exc._time_list, 
			string="Tiempo", 
			default='none',	
			)


	@api.onchange('time_1')
	def _onchange_time_1(self):
	
		if self.time_1 != 'none':	
			
			self.time_1 = self.clear_all_times(self.time_1)

			self.time = self.time_1
			
			return {
				'domain': {'service': [('x_treatment', '=', self.laser),('x_zone', '=', self.zone),('x_pathology', '=', self.pathology),('x_time', '=', self.time)]},
			}

	
	
	def clear_all_times(self,token):
	
		# Second
		self.time_1 = 'none'
		
		return token 
	
	
	
	
	
	
	# Client type 
	
	client_type_1 = fields.Selection(
			selection = ipl._ctype_list, 
			string="Tipo de cliente", 
			default='none',	
			)


	@api.onchange('client_type_1')
	def _onchange_client_type_1(self):
	
		if self.client_type_1 != 'none':	
			#self.client_type_1 = self.clear_all(self.client_type_1)

			self.client_type = self.client_type_1
			
			return {
				'domain': {'service': [('x_treatment', '=', self.laser),('x_zone', '=', self.zone),('x_pathology', '=', self.pathology),('x_time', '=', self.time),('x_client_type', '=', self.client_type) ]},
			}

		
		

		
		





	# Consultation 
	consultation = fields.Many2one('openhealth.consultation',
			ondelete='cascade', 
			#string="Treatment", 
			string="Consulta", 
			)

	# Quotation 
	quotation = fields.Many2one('openhealth.quotation',
			ondelete='cascade', 
			#string="Treatment", 
			string="Quotation", 
			)







	# Service 
	service = fields.Many2one(
			'product.template',

			domain = [
						('type', '=', 'service'),
			#			('x_treatment', '=', _jx_laser_type),
					],

			#string="Service", 
			string="Servicio",
			#required=True, 
			)


	# Treatment 
	treatment_id = fields.Many2one('openextension.treatment',
			ondelete='cascade', 
			#string="Treatment", 
			string="Tratamiento", 
			)



	#required=True,





	# Laser type 
	_laser_type_list = [
			('laser_co2','Laser Co2'), 
			('laser_excilite','Laser Excilite'), 
			('laser_ipl','Laser Ipl'), 
			('laser_ndyag','Laser Ndyag'), 
			
			('none','None'), 
			
			]

	laser = fields.Selection(
			selection = _laser_type_list, 
			#string="Tratamiento", 
			string="Tipo", 
			
			#default='laser_co2',
			default='none',
			
			required=True, 
			index=True
			)


	def get_domain_service(self,cr,uid,ids,context=None):

		#print context

		#return {
		#	'warning': {
		#		'title': "Laser",
		#		'message': context,
		#}}

		mach = []
		lids = self.pool.get('product.template').search(cr,uid,[
																('x_treatment', '=', context)
																])
		return {'domain':{'service':[('id','in',lids)]}}








	zone = fields.Selection(
			selection = jxvars._zone_list, 

			string="Zona", 
			#default='areola',
			default='none',
			#required=True, 
			)




	# Pathology
	pathology = fields.Selection(
	
			#selection = _pathology_list, 
			selection = jxvars._pathology_list, 
	
			string="Patología", 
			#default='acne_active',
			default='none',
			#required=True, 
			)







	#def get_domain_service_zone(self,cr,uid,ids,context=None):
	#def get_domain_service_multi(self,cr,uid,ids,context_1=None,context_2=None):
	def get_domain_service_multi(self,cr,uid,ids,context_1=None,context_2=None,context_3=None):

		#print context
		print 'jx'
		print context_1, context_2, context_3
		print 'jx'

		#return {
		#	'warning': {
		#		'title': "Zone domain",
		#		'message': context_1 + ' ' + context_2 + ' ' + context_3,
		#}}



		mach = []
		lids = self.pool.get('product.template').search(cr,uid,[
																	('x_treatment', '=', 	context_1), 
																	('x_zone', '=', 		context_2), 
																	('x_pathology', '=', 	context_3), 
																])
		return {'domain':{'service':[('id','in',lids)]}}






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
			string='Código interno'
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






	#------------------------------------ Buttons -----------------------------------------
	#

	# Service - Quick Self Button 
	# ---------------------------------

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




#------------------------------------ Classes -----------------------------------------

class ServiceExcilite(models.Model):
	#_name = 'openhealth.service.laserexcilite'
	_name = 'openhealth.service.excilite'

	_inherit = 'openhealth.service'
	
	
	

class ServiceIpl(models.Model):
	#_name = 'openhealth.service.laseripl'
	_name = 'openhealth.service.ipl'

	_inherit = 'openhealth.service'



class ServiceNdyag(models.Model):
	#_name = 'openhealth.service.laserndyag'
	_name = 'openhealth.service.ndyag'

	_inherit = 'openhealth.service'


