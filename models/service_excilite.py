# -*- coding: utf-8 -*-
#
# 	Service Excilite 
# 

from openerp import models, fields, api
from datetime import datetime

import exc





class ServiceExcilite(models.Model):
	#_name = 'openhealth.laserexcilite'
	_name = 'openhealth.service.excilite'

	_inherit = 'openhealth.service'
	
	
	
	
	# From Service
	zone = fields.Char(
			default='x',
			)
			
	pathology = fields.Char(
			default='x',
			)
					
	time = fields.Char(
			default='x',
			)
	


	# First
	vitiligo = fields.Selection(
			selection = exc._vitiligo_list, 
			string="Vitiligo", 
			default='',	
			)

	psoriasis = fields.Selection(
			selection = exc._psoriasis_list, 
			string="Psoriasis", 
			default='',	
			)
			
	alopecias = fields.Selection(
			selection = exc._alopecias_list, 
			string="Alopecias", 
			default='',	
			)


	time_pat = fields.Selection(
			selection = exc._time_list, 
			string="Tiempo", 
			default='',	
			)



	# On Change - Clear the rest

	@api.onchange('vitiligo')
	def _onchange_vitiligo(self):
	
		if self.vitiligo != 'none':	
			self.vitiligo = self.clear_all(self.vitiligo)

			self.zone = self.vitiligo
			self.pathology = 'vitiligo'
			
			return {
				'domain': {'service': [('x_treatment', '=', 'laser_excilite'),('x_zone', '=', self.zone),('x_pathology', '=', self.pathology)]},
			}


	@api.onchange('psoriasis')
	def _onchange_psoriasis(self):
	
		if self.psoriasis != 'none':	
			self.psoriasis = self.clear_all(self.psoriasis)

			self.zone = self.psoriasis
			self.pathology = 'psoriasis'
			
			return {
				'domain': {'service': [('x_treatment', '=', 'laser_excilite'),('x_zone', '=', self.zone),('x_pathology', '=', self.pathology)]},
			}
			
			
	@api.onchange('alopecias')
	def _onchange_alopecias(self):
	
		if self.alopecias != 'none':	
			self.alopecias = self.clear_all(self.alopecias)

			self.zone = self.alopecias
			self.pathology = 'alopecia'
			
			return {
				'domain': {'service': [('x_treatment', '=', 'laser_excilite'),('x_zone', '=', self.zone),('x_pathology', '=', self.pathology)]},
				#'domain': {'service': [('x_treatment', '=', 'laser_excilite'),('x_zone', '=', self.zone),('x_pathology', '=', self.pathology),('x_time', '=', self.time)]},
			}
			
			
	
	
	@api.onchange('time_pat')
	def _onchange_time_pat(self):
	
		if self.time_pat != 'none':	
			#self.time_pat = self.clear_all(self.time_pat)

			self.time = self.time_pat
			
			return {
				'domain': {'service': [('x_treatment', '=', 'laser_excilite'),('x_zone', '=', self.zone),('x_pathology', '=', self.pathology),('x_time', '=', self.time)]},
			}
			
			
			


	# Clear 
		
	def clear_all(self,token):
		
		# Service
		self.zone = ''
		self.pathology = ''
		
		
		# First
		self.vitiligo = 'none'
		self.psoriasis = 'none'
		self.alopecias = 'none'

		return token 
	
	
	
	
	
	