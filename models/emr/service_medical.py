# -*- coding: utf-8 -*-
"""
		Service Medical treatment 

		Created: 				 1 Nov 2016
		Last: 				 	29 Nov 2018

"""
from datetime import datetime
from openerp import models, fields, api
from . import prodvars
from . import service_medical_vars

class ServiceMedical(models.Model):

	_name = 'openhealth.service.medical'
	
	_inherit = 'openhealth.service'
	


# ----------------------------------------------------------- Natives ------------------------------
	# Service 
	service = fields.Many2one(
			'product.template',
			domain = [
						('type', '=', 'service'),
						('x_family', '=', 'medical'),						
					],
	)
	





# ---------------------------------------------- Default --------------------------------------------------------
	# Laser 
	laser = fields.Selection(
			selection = prodvars._laser_type_list, 
			string="Láser", 			
	
			default='medical',			

			index=True,
		)


# ----------------------------------------------------------- Variables ------------------------------------------------------

	# Criosurgery
	med_crio = fields.Selection(
			selection = service_medical_vars._med_crio_list, 
			default='none',	
			string="Criocirugía",
			)

	# Hialuronic
	med_hya = fields.Selection(
			selection = service_medical_vars._med_hia_list, 
			default='none',	
			string="Acido Hialurónico",
			)

	# Sclerotherapy
	med_scle = fields.Selection(
			selection = service_medical_vars._med_scle_list, 
			default='none',	
			string="Escleroterapia",
			)

	# Lepismatic
	med_lep = fields.Selection(
			selection = service_medical_vars._med_lep_list, 
			default='none',	
			string="Lepismático",
			)


	# Plasma
	med_pla = fields.Selection(
			selection = service_medical_vars._med_pla_list, 
			default='none',	
			string="Plasma",
			)


	# Botulinic Toxin
	med_bot = fields.Selection(
			selection = service_medical_vars._med_bot_list, 
			default='none',	
			string="Toxina Botulínica",
			)

	# Intravenous
	med_int = fields.Selection(
			selection = service_medical_vars._med_int_list, 
			default='none',	
			string="Endovenoso",
			)




# ----------------------------------------------------------- Functions ------------------------------------------------------

	def clear_all_med(self,token):		
		#self.clear_commons()
		self.clear_local_med()
		return token

	@api.multi
	def clear_local_med(self):
		self.med_crio = 'none'
		self.med_hya = 'none'
		self.med_scle = 'none'
		self.med_bot = 'none'
		self.med_int = 'none'
		self.med_lep = 'none'
		self.med_pla = 'none'
		



# ----------------------------------------------------------- On changes ------------------------------------------------------

	# Change the Domain


	# Criosurgery
	@api.onchange('med_crio')
	def _onchange_med_crio(self):
		if self.med_crio != 'none':

			self.x_treatment = 'criosurgery'
			self.sessions = self.med_crio


			self.zone = 'face_all'
			self.pathology = 'acne' 

			self.get_product_medical()

			return {
				'domain': {'service': [
										('x_treatment', '=', self.x_treatment),
										('x_sessions', '=', self.sessions),
						]},
			}




	# Hyaluronic Acid
	@api.onchange('med_hya')
	def _onchange_med_hya(self):
		
		if self.med_hya != 'none':

			self.med_hya = self.clear_all_med(self.med_hya)

			self.x_treatment = 'hyaluronic_acid'


			self.zone = '1_hypodermic'
			self.pathology = 'rejuvenation_face'

			#self.sessions = '1'

			
			#self.get_product_medical()


			return {
				'domain': {'service': [
										
										('x_treatment', '=', self.x_treatment),

										('x_origin', '=', False),

										]},
			}




	# Sclerotherapy 
	@api.onchange('med_scle')
	def _onchange_med_scle(self):
		if self.med_scle != 'none':
			self.med_scle = self.clear_all_med(self.med_scle)
			self.x_treatment = 'sclerotherapy'

			self.get_product_medical()
			return {'domain': {'service': [('x_treatment', '=', self.x_treatment),]},}

	# Botulinum Toxyn 
	@api.onchange('med_bot')
	def _onchange_med_bot(self):
		
		if self.med_bot != 'none':
			self.med_bot = self.clear_all_med(self.med_bot)
			self.x_treatment = 'botulinum_toxin'

			self.get_product_medical()
			return {
				'domain': {'service': [
										('x_treatment', '=', self.x_treatment),
										]},
			}

	# Vitamin Intravenous
	@api.onchange('med_int')
	def _onchange_med_int(self):
		if self.med_int != 'none':
			self.med_int = self.clear_all_med(self.med_int)
			self.x_treatment = 'intravenous_vitamin'

			self.get_product_medical()
			return {
				'domain': {'service': [
										('x_treatment', '=', self.x_treatment),
										]},
			}





# ----------------------------------------------------------- In Progress ------------------------------------------------------

	# Lepismatic 
	@api.onchange('med_lep')
	def _onchange_med_lep(self):
		
		if self.med_lep != 'none':
			self.zone = 		service_medical_vars._lep_dic_zone[self.med_lep]
			self.pathology = 	service_medical_vars._lep_dic_pathology[self.med_lep]
			self.x_treatment = 'lepismatic' 
			self.med_lep = self.clear_all_med(self.med_lep)


			self.get_product_medical()
			return {'domain': {'service': [
											('x_treatment', '=', self.x_treatment),
											('x_zone', '=', self.zone),
											('x_pathology', '=', self.pathology),
										]},}


	# Plasma
	@api.onchange('med_pla')
	def _onchange_med_pla(self):
		if self.med_pla != 'none':
			self.med_pla = self.clear_all_med(self.med_pla)
			self.x_treatment = 'plasma'
			pla_dic = service_medical_vars._pla_dic[self.med_pla]
			self.pathology = 		pla_dic['pathology']
			self.zone = 			pla_dic['zone']
			self.sessions = 		pla_dic['sessions']


			#self.get_product_medical()

			return {
				'domain': {'service': [
											('x_treatment', '=', self.x_treatment),
											('x_zone', '=', self.zone),
											('x_pathology', '=', self.pathology),										
											('x_sessions', '=', self.sessions),

											('x_origin', '=', False),
										]},
			}



