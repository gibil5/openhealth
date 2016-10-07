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
	
	# First
	
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







	# Second
	
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
	

	# Smart 

	@api.onchange('co2_allface_rejuvenation')
	def _onchange_co2_afr(self):
		print 
		print 'a'
		
		if self.co2_allface_rejuvenation != 'none':				
			self.co2_allface_acnesequels = 'none'

		print 
		return {}


	@api.onchange('co2_allface_acnesequels')
	def _onchange_co2_afa(self):
		print 
		print 'b'

		if self.co2_allface_acnesequels != 'none':	
			self.co2_allface_rejuvenation = 'none'
			
		print 
		return {}
		
		
		
		


	# Third
	co2_lf_stains = fields.Selection(
			selection = jxvars._co2_lfstains_list, 
			string="Manchas", 
			default='',	
			)

	co2_lf_queratosis = fields.Selection(
			selection = jxvars._co2_lfqueratosis_list, 
			string="Queratosis", 
			default='',	
			)

	co2_lf_mole = fields.Selection(
			selection = jxvars._co2_lfmole_list, 
			string="Lunar", 
			default='',	
			)
			
			
			
	co2_lf_scar = fields.Selection(
			selection = jxvars._co2_lfscar_list, 
			string="Cicatriz", 
			default='',	
			)

	co2_lf_cyst = fields.Selection(
			selection = jxvars._co2_lfcyst_list, 
			string="Quiste", 
			default='',	
			)

	co2_lf_wart = fields.Selection(
			selection = jxvars._co2_lfwart_list, 
			string="Verruga", 
			default='',	
			)






	@api.onchange('co2_lf_stains')
	def _onchange_co2_lf_stains(self):

		if self.co2_lf_stains != 'none':	
			
			#self.co2_lf_stains = 'none'
			self.co2_lf_queratosis = 'none'
			self.co2_lf_mole = 'none'
			
			self.co2_lf_scar = 'none'
			self.co2_lf_cyst = 'none'
			self.co2_lf_wart = 'none'
				
		return {}


	@api.onchange('co2_lf_queratosis')
	def _onchange_co2_lf_queratosis(self):

		if self.co2_lf_queratosis != 'none':	
			
			self.co2_lf_stains = 'none'
			#self.co2_lf_queratosis = 'none'
			self.co2_lf_mole = 'none'
			
			self.co2_lf_scar = 'none'
			self.co2_lf_cyst = 'none'
			self.co2_lf_wart = 'none'
				
		return {}
		
		
	@api.onchange('co2_lf_mole')
	def _onchange_co2_lf_mole(self):

		if self.co2_lf_mole != 'none':	
			
			self.co2_lf_stains = 'none'
			self.co2_lf_queratosis = 'none'
			#self.co2_lf_mole = 'none'
			
			self.co2_lf_scar = 'none'
			self.co2_lf_cyst = 'none'
			self.co2_lf_wart = 'none'
				
		return {}







	@api.onchange('co2_lf_scar')
	def _onchange_co2_lf_scar(self):

		if self.co2_lf_scar != 'none':	
			
			self.co2_lf_stains = 'none'
			self.co2_lf_queratosis = 'none'
			self.co2_lf_mole = 'none'
			
			#self.co2_lf_scar = 'none'
			self.co2_lf_cyst = 'none'
			self.co2_lf_wart = 'none'
				
		return {}
		
		
	@api.onchange('co2_lf_cyst')
	def _onchange_co2_lf_cyst(self):

		if self.co2_lf_cyst != 'none':	
			
			self.co2_lf_stains = 'none'
			self.co2_lf_queratosis = 'none'
			self.co2_lf_mole = 'none'
			
			self.co2_lf_scar = 'none'
			#self.co2_lf_cyst = 'none'
			self.co2_lf_wart = 'none'
				
		return {}		


	@api.onchange('co2_lf_wart')
	def _onchange_co2_lf_wart(self):

		if self.co2_lf_wart != 'none':	
			
			self.co2_lf_stains = 'none'
			self.co2_lf_queratosis = 'none'
			self.co2_lf_mole = 'none'
			
			self.co2_lf_scar = 'none'
			self.co2_lf_cyst = 'none'
			#self.co2_lf_wart = 'none'
				
		return {}





	# Fourth
	
	co2_lb_acneseq = fields.Selection(
			selection = jxvars._co2_lbacneseq_list, 
			string="Acné y secuelas", 
			default='',	
			)
			
	co2_lb_stains = fields.Selection(
			selection = jxvars._co2_lbstains_list, 
			string="Manchas", 
			default='',	
			)

	co2_lb_queratosis = fields.Selection(
			selection = jxvars._co2_lbqueratosis_list, 
			string="Queratosis", 
			default='',	
			)

	co2_lb_mole = fields.Selection(
			selection = jxvars._co2_lbmole_list, 
			string="Lunar", 
			default='',	
			)
			
			
			
	co2_lb_scar = fields.Selection(
			selection = jxvars._co2_lbscar_list, 
			string="Cicatriz", 
			default='',	
			)

	co2_lb_cyst = fields.Selection(
			selection = jxvars._co2_lbcyst_list, 
			string="Quiste", 
			default='',	
			)

	co2_lb_wart = fields.Selection(
			selection = jxvars._co2_lbwart_list, 
			string="Verruga", 
			default='',	
			)
			
			
			
			
			
			
			
	# On change 		
	
	#def clear_others(self,me):
	#def clear_others(self):
	#def clear_others():
	def clear_others(self,token,arr):
		print token
		
		print 3
		#arr = [ 
			#self.co2_lb_acneseq,
			
		#	self.co2_lb_stains,
		#	self.co2_lb_queratosis,
		#	self.co2_lb_mole,
			
		#	self.co2_lb_scar,
		#	self.co2_lb_cyst,
		#	self.co2_lb_wart,
		#	]
			
		for vax in arr:
			#if me != vax: 
			if not (vax == 'none'  or  vax == False): 
				print vax
				vax = 'none'
				#print vax 		
		
	
	
	@api.onchange('co2_lb_acneseq')
	def _onchange_co2_lb_acneseq(self):
		arr = [ 
			#self.co2_lb_acneseq,
			
			self.co2_lb_stains,
			self.co2_lb_queratosis,
			self.co2_lb_mole,
			
			self.co2_lb_scar,
			self.co2_lb_cyst,
			self.co2_lb_wart,
			]
			
		if self.co2_lb_acneseq != 'none':	
			print 1
			
			#self.clear_others(2)
			self.clear_others(2,arr)

			#self.co2_lb_acneseq = 'none'
			
			#self.co2_lb_stains = 'none'
			#self.co2_lb_queratosis = 'none'
			#self.co2_lb_mole = 'none'
			
			#self.co2_lb_scar = 'none'
			#self.co2_lb_cyst = 'none'
			#self.co2_lb_wart = 'none'
				
		return {}