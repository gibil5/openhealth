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
			#compute='_compute_co2_neck', 
			#store=True,
			#edit=True,
			)






	# Booleans
	
	co2_hands_stains = fields.Boolean(
			string="Manchas", 
			default=False,	
			#compute='_compute_co2_hands_stains', 
			)
	#@api.depends('co2_hands_scar')
	#def _compute_co2_hands_stains(self):
	#	for record in self:
	#		record.hands_stains=True
	
	
	
			
	co2_hands_scar = fields.Boolean(
			string="Cicatriz", 
			default=False,	
			)
	co2_hands_wart = fields.Boolean(
			string="Verruga", 
			default=False,	
			)
	co2_hands_rejuvenation = fields.Boolean(
			string="Rejuvenecimiento", 
			default=False,	
			)





	# On change 

	# Smart 

	#@api.onchange('co2_hands_stains', 'co2_hands_scar', 'co2_hands_wart', 'co2_hands_rejuvenation')
	#@api.onchange('field1', 'field2')
	
	@api.onchange('co2_hands_stains', 'co2_hands_scar')
	def _onchange_co2_hands(self):
		
		print
		print 'jx'
		print
		
		if self.co2_hands_stains == True:		
			#self.co2_hands_stains = False
			self.co2_hands_scar = False
			self.co2_hands_wart = False
			self.co2_hands_rejuvenation = False

		if self.co2_hands_scar == True:	
			self.co2_hands_stains = False
			#self.co2_hands_scar = False
			self.co2_hands_wart = False
			self.co2_hands_rejuvenation = False

		if self.co2_hands_wart == True:		
			self.co2_hands_stains = False
			self.co2_hands_scar = False
			#self.co2_hands_wart = False
			self.co2_hands_rejuvenation = False

		if self.co2_hands_rejuvenation == True:		
			self.co2_hands_stains = False
			self.co2_hands_scar = False
			self.co2_hands_wart = False
			#self.co2_hands_rejuvenation = False

			



	co2_neck_scar = fields.Boolean(
			string="Cuello Cicatriz", 
			default=False,	
			#compute='_compute_co2_neck', 
			)





			
	@api.depends('co2_hands')
	def _compute_co2_neck(self):
		for record in self:
			record.co2_neck=False


			
	# Clear Procedures
	# ------------------

	#@api.onchange('co2_hands')
	@api.onchange('co2_hands')
	def _onchange_co2_hands(self):
	#def _onchange_co2_hands(self,context):
	    #self.message = "Dear %s" % (self.partner_id.name or "")


		print 
		print self
		print 
		print self.co2_hands
		
		self.co2_neck_scar = False
		self.co2_neck = ''
				
		#self.co2_cheekbone = 'nil'
		self.co2_cheekbone = 'none'
		#self.co2_cheekbone = False
		
		self.co2_vagina = ''
		
		
		#for record in self:
			#record.code = record.service.x_name_short
		#	record.co2_cheekbone = ''
		
		
		
		#self.co2_neck = 'none'

		#self.co2_neck = 'scar'
		#self.co2_neck = nil

		#print self.co2_neck
		
		#self.co2_hands = False
		#self.co2_cheekbone = False
		#self.co2_vagina = False
		#self.co2_packages = False
		#self.write({'co2_neck': False})
		#print self.co2_neck		
		print 
		
		return {
		    'co2_cheekbone': False,
		    #'co2_neck': False,
			'domain': {'service': [('x_treatment', '=', 'laser_co2'),('x_zone', '=', 'hands'),('x_pathology', '=', self.co2_hands)]},
		    #'warning': {'title': "Warning", 'message': "What is this?"},
		}
		
		
		
		

	#def clear_others(self,cr,uid,ids,context=None):
	#def clear_all(self,cr,uid,ids,context=None):

	#def clear_others(self,context=None):
	
	@api.multi
	def clear_all(self):
	#def clear_all(self,cr,uid,ids,context=None):
		
		
		self.co2_hands = False
		self.co2_cheekbone = False
		self.co2_neck = False
		self.co2_vagina = False
		self.co2_packages = False

		self.co2_neck_scar = False
		
		print
		print self.co2_hands
		print
		
		#print 'jx: Mark'
		#print context 

		return {}
	
	
	

