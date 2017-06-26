# -*- coding: utf-8 -*-
#
# 	Service Co2 
# 

from openerp import models, fields, api
from datetime import datetime


#from . import jxvars
from . import service_co2_vars

from . import serv_funcs



class ServiceCo2(models.Model):
	_name = 'openhealth.service.co2'
	_inherit = 'openhealth.service'
	
	



	# Service 
	service = fields.Many2one(
			'product.template',

			domain = [
						('type', '=', 'service'),
						('x_treatment', '=', 'laser_co2'),
					],
	)
	
	




	
# ---------------------------------------------- Fourth - Body Zone --------------------------------------------------------

	# Hands 
	co2_hands = fields.Selection(
			selection = service_co2_vars._co2_hands_list, 
			string="Manos Rejuvenecimiento", 
			default='none',	
			)

	# Neck
	co2_neck = fields.Selection(
			selection = service_co2_vars._co2_neck_list, 
			string="Cuello Rejuvenecimiento", 
			default='none',	
			)

	# Cheekbone				
	co2_cheekbone = fields.Selection(
			selection = service_co2_vars._co2_acneseq_list,  
			string="Pómulos Acné Secuelas", 
			default='none',	
			)

	co2_cheekbone_stains = fields.Selection(
			selection = service_co2_vars._co2_stains_list, 
			string="Pómulos Manchas", 
			default='none',	
			)


	co2_vagina = fields.Selection(
			selection = service_co2_vars._co2_vag_list, 
			string="Vagina", 
			default='none',	
			)
			
	#co2_packages = fields.Selection(
	#		selection = service_co2_vars._co2_pac_list, 
	#		string="Paquetes Rejuvenecimiento", 
	#		default='none',	
	#		)





			
	# On Change - Clear the rest
	# ---------------------------

	@api.onchange('co2_hands')
	def _onchange_co2_hands(self):
	
		if self.co2_hands != 'none':	
			self.co2_hands = self.clear_all(self.co2_hands)

			self.zone = 'hands'
			self.pathology = self.co2_hands
			

			serv_funcs.product(self)

			return {
				'domain': {'service': [
										('x_treatment', '=', self.laser),
										('x_zone', '=', self.zone),
										('x_pathology', '=', self.pathology)
							]},
			}





	@api.onchange('co2_neck')
	def _onchange_co2_neck(self):

		if self.co2_neck != 'none':	
			self.co2_neck = self.clear_all(self.co2_neck)

			self.zone = 'neck'
			self.pathology = self.co2_neck
				

			serv_funcs.product(self)

			return {
				'domain': {'service': [('x_treatment', '=', self.laser),('x_zone', '=', self.zone),('x_pathology', '=', self.pathology)]},
			}




	@api.onchange('co2_cheekbone')
	def _onchange_co2_cheekbone(self):

		if self.co2_cheekbone != 'none':	
			self.co2_cheekbone = self.clear_all(self.co2_cheekbone)
			
			self.zone = 'cheekbones'
			self.pathology = self.co2_cheekbone
				

			serv_funcs.product(self)

			return {
				'domain': {'service': [('x_treatment', '=', self.laser),('x_zone', '=', self.zone),('x_pathology', '=', self.pathology)]},
			}


	@api.onchange('co2_cheekbone_stains')
	def _onchange_co2_cheekbone_stains(self):

		if self.co2_cheekbone_stains != 'none':	
			self.co2_cheekbone_stains = self.clear_all(self.co2_cheekbone_stains)
			
			self.zone = 'cheekbones'
			self.pathology = self.co2_cheekbone_stains
				

			serv_funcs.product(self)

			return {
				'domain': {'service': [('x_treatment', '=', self.laser),('x_zone', '=', self.zone),('x_pathology', '=', self.pathology)]},
			}



	@api.onchange('co2_vagina')
	def _onchange_co2_vagina(self):

		if self.co2_vagina != 'none':	
			self.co2_vagina = self.clear_all(self.co2_vagina)

			self.zone = 'vagina'
			self.pathology = self.co2_vagina
				

			serv_funcs.product(self)

			return {
				'domain': {'service': [('x_treatment', '=', self.laser),('x_zone', '=', self.zone),('x_pathology', '=', self.pathology)]},
			}
		
		
		
	#@api.onchange('co2_packages')
	#def _onchange_co2_packages(self):
	#	if self.co2_packages != 'none':	
	#		self.co2_packages = self.clear_all(self.co2_packages)
	#		self.zone = 'package'
	#		self.pathology = self.co2_packages
	#		return {
	#			'domain': {'service': [('x_treatment', '=', self.laser),('x_zone', '=', self.zone),('x_pathology', '=', self.pathology)]},
	#		}	






# ---------------------------------------------- Second - All Face --------------------------------------------------------

	# Second - All Face 
	
	co2_allface_rejuvenation = fields.Selection(
			selection = service_co2_vars._co2_rejuv_list, 
			string="Rejuvenecimiento facial", 
			default='none',	
			)

	co2_allface_acnesequels = fields.Selection(
			selection = service_co2_vars._co2_acneseq_list, 
			string="Acné y secuelas", 
			default='none',	
			)
	



	co2_allface_stains = fields.Selection(
			selection = service_co2_vars._co2_stains_list, 
			string="Manchas", 
			default='none',	
			)





	
	# On change
	
	# Rejuvenation All Face 
	@api.onchange('co2_allface_rejuvenation')
	def _onchange_co2_allface_rejuvenation(self):
		if self.co2_allface_rejuvenation != 'none':	
			self.co2_allface_rejuvenation = self.clear_all(self.co2_allface_rejuvenation)

			self.zone = 'face_all'
			self.pathology = self.co2_allface_rejuvenation
			

			serv_funcs.product(self)

			return {
				'domain': {'service': [('x_treatment', '=', self.laser),('x_zone', '=', self.zone),('x_pathology', '=', self.pathology)]},
			}	

		
	# Acne sequels 
	@api.onchange('co2_allface_acnesequels')
	def _onchange_co2_allface_acnesequels(self):
		if self.co2_allface_acnesequels != 'none':	
			self.co2_allface_acnesequels = self.clear_all(self.co2_allface_acnesequels)

			self.zone = 'face_all'
			self.pathology = self.co2_allface_acnesequels


			serv_funcs.product(self)

			return {
				'domain': {'service': [('x_treatment', '=', self.laser),('x_zone', '=', self.zone),('x_pathology', '=', self.pathology)]},
			}	
		

	# Stains 
	@api.onchange('co2_allface_stains')
	def _onchange_co2_allface_stains(self):
		if self.co2_allface_stains != 'none':	
			self.co2_allface_stains = self.clear_all(self.co2_allface_stains)

			self.zone = 'face_all'
			self.pathology = self.co2_allface_stains


			serv_funcs.product(self)

			return {
				'domain': {'service': [('x_treatment', '=', self.laser),('x_zone', '=', self.zone),('x_pathology', '=', self.pathology)]},
			}	
		
		


		
		

		
		


	# Third
	co2_lf_stains = fields.Selection(
			#selection = service_co2_vars._co2_lfstains_list, 
			selection = service_co2_vars._co2_stains_list, 
			string="Manchas", 
			default='none',	
			)

	co2_lf_keratosis = fields.Selection(
			#selection = service_co2_vars._co2_lfkeratosis_list, 
			selection = service_co2_vars._co2_keratosis_list, 
			string="Queratosis", 
			default='none',	
			)

	co2_lf_mole = fields.Selection(
			#selection = service_co2_vars._co2_lfmole_list, 
			selection = service_co2_vars._co2_mole_list, 
			string="Lunar", 
			default='none',	
			)
			
			
			
	co2_lf_scar = fields.Selection(
			#selection = service_co2_vars._co2_lfscar_list, 
			selection = service_co2_vars._co2_scar_list, 
			string="Cicatriz", 
			default='none',	
			)

	co2_lf_cyst = fields.Selection(
			#selection = service_co2_vars._co2_lfcyst_list, 
			selection = service_co2_vars._co2_cyst_list, 
			string="Quiste", 
			default='none',	
			)

	co2_lf_wart = fields.Selection(
			#selection = service_co2_vars._co2_lfwart_list, 
			selection = service_co2_vars._co2_wart_list, 
			string="Verruga", 
			default='none',	
			)





	# On change
	
	@api.onchange('co2_lf_scar')
	def _onchange_co2_lf_scar(self):
		if self.co2_lf_scar != 'none':	

			self.co2_lf_scar = self.clear_all(self.co2_lf_scar)			
			self.zone = 'face_local'
			self.pathology = self.co2_lf_scar

			
			serv_funcs.product(self)

			return {
				'domain': {'service': [('x_treatment', '=', self.laser),('x_zone', '=', self.zone),('x_pathology', '=', self.pathology)]},
			}	
			
				
		
		
	@api.onchange('co2_lf_mole')
	def _onchange_co2_lf_mole(self):
		if self.co2_lf_mole != 'none':	

			self.co2_lf_mole = self.clear_all(self.co2_lf_mole)
			self.zone = 'face_local'
			self.pathology = self.co2_lf_mole


			serv_funcs.product(self)

			return {
				'domain': {'service': [('x_treatment', '=', self.laser),('x_zone', '=', self.zone),('x_pathology', '=', self.pathology)]},
			}




	@api.onchange('co2_lf_stains')
	def _onchange_co2_lf_stains(self):
		if self.co2_lf_stains != 'none':	

			self.co2_lf_stains = self.clear_all(self.co2_lf_stains)			
			self.zone = 'face_local'
			self.pathology = self.co2_lf_stains
			

			serv_funcs.product(self)

			return {
				'domain': {'service': [('x_treatment', '=', self.laser),('x_zone', '=', self.zone),('x_pathology', '=', self.pathology)]},
			}


	@api.onchange('co2_lf_keratosis')
	def _onchange_co2_lf_keratosis(self):
		if self.co2_lf_keratosis != 'none':	

			self.co2_lf_keratosis = self.clear_all(self.co2_lf_keratosis)			
			self.zone = 'face_local'
			self.pathology = self.co2_lf_keratosis
			

			serv_funcs.product(self)

			return {
				'domain': {'service': [('x_treatment', '=', self.laser),('x_zone', '=', self.zone),('x_pathology', '=', self.pathology)]},
			}
			
			
	@api.onchange('co2_lf_cyst')
	def _onchange_co2_lf_cyst(self):
		if self.co2_lf_cyst != 'none':	
			self.co2_lf_cyst = self.clear_all(self.co2_lf_cyst)
			
			self.zone = 'face_local'
			self.pathology = self.co2_lf_cyst
			

			serv_funcs.product(self)

			return {
				'domain': {'service': [('x_treatment', '=', self.laser),('x_zone', '=', self.zone),('x_pathology', '=', self.pathology)]},
			}
			
			
	@api.onchange('co2_lf_wart')
	def _onchange_co2_lf_wart(self):
		if self.co2_lf_wart != 'none':	
			self.co2_lf_wart = self.clear_all(self.co2_lf_wart)
			
			self.zone = 'face_local'
			self.pathology = self.co2_lf_wart
			

			serv_funcs.product(self)

			return {
				'domain': {'service': [('x_treatment', '=', self.laser),('x_zone', '=', self.zone),('x_pathology', '=', self.pathology)]},
			}
			
			







	# Fourth
	co2_lb_acneseq = fields.Selection(

			selection = service_co2_vars._co2_acneseq_list, 
			
			string="Acné y secuelas", 
			default='none',	
			)



			
	co2_lb_scar = fields.Selection(
			selection = service_co2_vars._co2_scar_list, 
			string="Cicatriz", 
			default='none',	
			)
			
	co2_lb_mole = fields.Selection(
			selection = service_co2_vars._co2_mole_list, 
			string="Lunar", 
			default='none',	
			)
						
	co2_lb_stains = fields.Selection(
			#selection = service_co2_vars._co2_lbstains_list, 
			selection = service_co2_vars._co2_stains_list, 
			string="Manchas", 
			default='none',	
			)

	co2_lb_keratosis = fields.Selection(
			selection = service_co2_vars._co2_keratosis_list, 
			string="Queratosis", 
			default='none',	
			)
			
	co2_lb_cyst = fields.Selection(
			selection = service_co2_vars._co2_cyst_list, 
			string="Quiste", 
			default='none',	
			)

	co2_lb_wart = fields.Selection(
			selection = service_co2_vars._co2_wart_list, 
			string="Verruga", 
			default='none',	
			)
			
			
					



	
	
	# On change

	@api.onchange('co2_lb_acneseq')
	def _onchange_co2_lb_acneseq(self):	

		if self.co2_lb_acneseq != 'none':	

			self.co2_lb_acneseq = self.clear_all(self.co2_lb_acneseq)

			self.zone = 'body_local'

			self.pathology = self.co2_lb_acneseq
			
#jx			


			#self.service = self.env['product.template'].search([	
																	#('x_treatment', '=', 'laser_co2'),	
																	#('x_zone', '=', 'body_local'),	
																	#('x_pathology', '=', 'acne_sequels_1')

			#														('x_treatment', '=', self.laser),	
			#														('x_zone', '=', self.zone),	
			#														('x_pathology', '=', self.pathology)
			#													])



			#self.service = serv_funcs.product(self.laser, self.zone, self.pathology)
			serv_funcs.product(self)

			return {
				'domain': {'service': [('x_treatment', '=', self.laser),('x_zone', '=', self.zone),('x_pathology', '=', self.pathology)]},
			}	
	

	
	
	
	@api.onchange('co2_lb_scar')
	def _onchange_co2_lb_scar(self):
		if self.co2_lb_scar != 'none':	
			self.co2_lb_scar = self.clear_all(self.co2_lb_scar)

			self.zone = 'body_local'
			self.pathology = self.co2_lb_scar
			

			#self.service = self.env['product.template'].search([	
			#														('x_treatment', '=', self.laser),	
			#														('x_zone', '=', self.zone),	
			#														('x_pathology', '=', self.pathology)
			#													])


			serv_funcs.product(self)

			return {
				'domain': {'service': [('x_treatment', '=', self.laser),('x_zone', '=', self.zone),('x_pathology', '=', self.pathology)]},
			}	


	
	
	@api.onchange('co2_lb_mole')
	def _onchange_co2_lb_mole(self):
		if self.co2_lb_mole != 'none':	
			self.co2_lb_mole = self.clear_all(self.co2_lb_mole)

			self.zone = 'body_local'
			self.pathology = self.co2_lb_mole
	

			#self.service = self.env['product.template'].search([	
			#														('x_treatment', '=', self.laser),	
			#														('x_zone', '=', self.zone),	
			#														('x_pathology', '=', self.pathology)
			#													])

			serv_funcs.product(self)

			return {
				'domain': {'service': [('x_treatment', '=', self.laser),('x_zone', '=', self.zone),('x_pathology', '=', self.pathology)]},
			}	
	
	
	
	@api.onchange('co2_lb_stains')
	def _onchange_co2_lb_stains(self):
		if self.co2_lb_stains != 'none':	
			self.co2_lb_stains = self.clear_all(self.co2_lb_stains)

			self.zone = 'body_local'
			self.pathology = self.co2_lb_stains
	

			serv_funcs.product(self)

			return {
				'domain': {'service': [('x_treatment', '=', self.laser),('x_zone', '=', self.zone),('x_pathology', '=', self.pathology)]},
			}
		
		
		
	@api.onchange('co2_lb_keratosis')
	def _onchange_co2_lb_keratosis(self):		
		if self.co2_lb_keratosis != 'none':	

			self.co2_lb_keratosis = self.clear_all(self.co2_lb_keratosis)

			self.zone = 'body_local'
			self.pathology = self.co2_lb_keratosis
	

			serv_funcs.product(self)

			return {
				'domain': {'service': [('x_treatment', '=', self.laser),('x_zone', '=', self.zone),('x_pathology', '=', self.pathology)]},
			}
		
		
	@api.onchange('co2_lb_cyst')
	def _onchange_co2_lb_cyst(self):
		if self.co2_lb_cyst != 'none':	
			self.co2_lb_cyst = self.clear_all(self.co2_lb_cyst)

			self.zone = 'body_local'
			self.pathology = self.co2_lb_cyst

	
			serv_funcs.product(self)

			return {
				'domain': {'service': [('x_treatment', '=', self.laser),('x_zone', '=', self.zone),('x_pathology', '=', self.pathology)]},
			}
			
			
	
	@api.onchange('co2_lb_wart')
	def _onchange_co2_lb_wart(self):
		if self.co2_lb_wart != 'none':	
			self.co2_lb_wart = self.clear_all(self.co2_lb_wart)

			self.zone = 'body_local'
			self.pathology = self.co2_lb_wart
	

			serv_funcs.product(self)

			return {
				'domain': {'service': [('x_treatment', '=', self.laser),('x_zone', '=', self.zone),('x_pathology', '=', self.pathology)]},
			}
			
			
		
		
		
	# Clear 
		
	#def clear_all(self,token):
	#	self.clear_commons		
	#	self.clear_local  
	#	return token 
	
	
	
	
	
	# jx 
	@api.multi
	def clear_local(self):
		
		#print 
		#print 'jx'
		#print 'Clear Local'

		# Fourth
		self.co2_lb_acneseq = 'none'
		self.co2_lb_scar = 'none'
		self.co2_lb_mole = 'none'
		self.co2_lb_stains = 'none'
		self.co2_lb_keratosis = 'none'
		self.co2_lb_cyst = 'none'
		self.co2_lb_wart = 'none'

		# Second 
		self.co2_allface_acnesequels = 'none'
		self.co2_allface_rejuvenation = 'none'
		self.co2_allface_stains = 'none'

		# Third
		self.co2_lf_scar = 'none'
		self.co2_lf_mole = 'none'
		self.co2_lf_stains = 'none'
		self.co2_lf_keratosis = 'none'		
		self.co2_lf_cyst = 'none'
		self.co2_lf_wart = 'none'
		
		# First
		self.co2_hands = 'none'
		self.co2_neck = 'none'
		self.co2_cheekbone = 'none'
		self.co2_cheekbone_stains = 'none'
		self.co2_vagina = 'none'
		#self.co2_packages = 'none'



		
