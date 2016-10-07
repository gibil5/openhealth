# -*- coding: utf-8 -*-
#
# 	Consultation 
# 
# Created: 				20 Sep 2016
# Last updated: 	 	20 Sep 2016

from openerp import models, fields, api
from datetime import datetime

import jxvars





class ServiceCo2(models.Model):
	#_name = 'openhealth.laserco2'
	_name = 'openhealth.service.co2'

	_inherit = 'openhealth.service'
	
	

	# Smart vars
	# ----------
	
	co2_hands = fields.Selection(
			selection = jxvars._co2_han_list, 
			string="Manos", 
			default='',	
			)


	co2_neck = fields.Selection(
			selection = jxvars._co2_nec_list, 
			string="Cuello", 
			#default='',	
			default='scar',	
			)
			
	
	co2_cheekbone = fields.Selection(
			selection = jxvars._co2_che_list, 
			string="Pómulos", 
			default='',	
			)

	
	co2_vagina = fields.Selection(
			selection = jxvars._co2_vag_list, 
			string="Vagina", 
			default='',	
			)
			
	co2_packages = fields.Selection(
			selection = jxvars._co2_pac_list, 
			string="Paquetes Rejuvenecimiento", 
			default='',	
			)









	co2_allface_rejuvenation = fields.Selection(
			selection = jxvars._co2_rejuv_list, 
			string="Rejuvenecimiento facial", 
			default='',	
			)

	co2_allface_acnesequels = fields.Selection(
			selection = jxvars._co2_acneseq_list, 
			string="Acné y secuelas", 
			default='',	
			)



	co2_localface_stains = fields.Selection(
			selection = jxvars._co2_lfstains_list, 
			string="Manchas", 
			default='',	
			)

	co2_localface_queratosis = fields.Selection(
			selection = jxvars._co2_lfqueratosis_list, 
			string="Queratosis", 
			default='',	
			)

	co2_localface_mole = fields.Selection(
			selection = jxvars._co2_lfmole_list, 
			string="Lunar", 
			default='',	
			)
			
	co2_localface_scar = fields.Selection(
			selection = jxvars._co2_lfscar_list, 
			string="Cicatriz", 
			default='',	
			)

	co2_localface_cyst = fields.Selection(
			selection = jxvars._co2_lfcyst_list, 
			string="Quiste", 
			default='',	
			)

	co2_localface_wart = fields.Selection(
			selection = jxvars._co2_lfwart_list, 
			string="Verruga", 
			default='',	
			)




			
			












			
	# On Change - Clear the rest
	# ---------------------------

	@api.onchange('co2_hands')
	def _onchange_co2_hands(self):
		
		if self.co2_hands != 'none':	
			
			#self.co2_hands = 'none'
			self.co2_neck = 'none'
			self.co2_cheekbone = 'none'
			self.co2_vagina = 'none'
			self.co2_packages = 'none'
				
		return {
			'domain': {'service': [('x_treatment', '=', 'laser_co2'),('x_zone', '=', 'hands'),('x_pathology', '=', self.co2_hands)]},
		}


		
	@api.onchange('co2_neck')
	def _onchange_co2_neck(self):

		if self.co2_neck != 'none':	
			
			self.co2_hands = 'none'
			#self.co2_neck = 'none'
			self.co2_cheekbone = 'none'
			self.co2_vagina = 'none'
			self.co2_packages = 'none'
				
		return {
			'domain': {'service': [('x_treatment', '=', 'laser_co2'),('x_zone', '=', 'neck'),('x_pathology', '=', self.co2_neck)]},
		}



	@api.onchange('co2_cheekbone')
	def _onchange_co2_cheekbone(self):

		if self.co2_cheekbone != 'none':	
			self.co2_hands = 'none'
			self.co2_neck = 'none'
			#self.co2_cheekbone = 'none'
			self.co2_vagina = 'none'
			self.co2_packages = 'none'
				
		return {
			'domain': {'service': [('x_treatment', '=', 'laser_co2'),('x_zone', '=', 'cheekbone'),('x_pathology', '=', self.co2_cheekbone)]},
		}



	@api.onchange('co2_vagina')
	def _onchange_co2_vagina(self):

		if self.co2_vagina != 'none':	
			
			self.co2_hands = 'none'
			self.co2_neck = 'none'
			self.co2_cheekbone = 'none'
			#self.co2_vagina = 'none'
			self.co2_packages = 'none'
				
		return {
			'domain': {'service': [('x_treatment', '=', 'laser_co2'),('x_zone', '=', 'vagina'),('x_pathology', '=', self.co2_vagina)]},
		}
		
		
		
	@api.onchange('co2_packages')
	def _onchange_co2_packages(self):

		if self.co2_packages != 'none':	
			
			self.co2_hands = 'none'
			self.co2_neck = 'none'
			self.co2_cheekbone = 'none'
			self.co2_vagina = 'none'
			#self.co2_packages = 'none'
				
		return {
			'domain': {'service': [('x_treatment', '=', 'laser_co2'),('x_zone', '=', 'packages'),('x_pathology', '=', self.co2_packages)]},
		}	


