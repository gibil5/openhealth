# -*- coding: utf-8 -*-
#
# 	Service Medical treatment 
# 

from openerp import models, fields, api
from datetime import datetime
import jxvars

import service_medical_vars


class ServiceMedical(models.Model):
	_name = 'openhealth.service.medical'
	_inherit = 'openhealth.service'
	
	
		
	# Service 
	service = fields.Many2one(
			'product.template',

			domain = [
						('type', '=', 'service'),
						('x_family', '=', 'medical'),						

						#('x_treatment', '=', 'criosurgery'),
						#('x_treatment', '=', 'hyaluronic_acid'),
						#('x_treatment', '=', 'sclerotherapy'),
						#('x_treatment', '=', 'lepismatic'),
						#('x_treatment', '=', 'plasma'),
						#('x_treatment', '=', 'botulinum_toxin'),
						#('x_treatment', '=', 'intravenous_vitamin'),
					],
	)
	
	



# ----------------------------------------------------------- Variables ------------------------------------------------------
	

	# Consultation
	#med_con = fields.Selection(
	#		selection = service_medical_vars._med_con_list, 
	#		default='none',	
	#		string="Consulta",
	#		)


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

		print 'clear_local_med'
		
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


			print 
			print 'med_crio'
			print self.med_crio
			print self.sessions
			print self.x_treatment

			print 

			#self.med_crio = self.clear_all_med(self.med_crio)
			#self.family = 'medical'

			#self.laser = 'medical'
			#self.zone = ''
			#self.pathology = ''
			

			return {
				'domain': {'service': [
										('x_treatment', '=', self.x_treatment),
										('x_sessions', '=', self.sessions),

										#('x_family', '=', self.family),
										#('laser', '=', self.laser),
										#('x_zone', '=', self.zone),
										#('x_pathology', '=', self.pathology),
						]},
			}





	# Hyaluronic Acid
	@api.onchange('med_hya')
	def _onchange_med_hya(self):
		
		if self.med_hya != 'none':
			print 
			print 'med_hya'
			print 

			self.med_hya = self.clear_all_med(self.med_hya)
			#self.clear_local()


			self.x_treatment = 'hyaluronic_acid'

			return {
				'domain': {'service': [
										('x_treatment', '=', self.x_treatment),
										]},
			}




	# Sclerotherapy 
	@api.onchange('med_scle')
	def _onchange_med_scle(self):
		
		if self.med_scle != 'none':
			print 
			print 'med_scle'
			print 

			self.med_scle = self.clear_all_med(self.med_scle)

			self.x_treatment = 'sclerotherapy'

			return {'domain': {'service': [('x_treatment', '=', self.x_treatment),]},}


















	# Botulinum Toxyn 
	@api.onchange('med_bot')
	def _onchange_med_bot(self):
		
		if self.med_bot != 'none':
			print 
			print 'med_bot'
			print 
			self.med_bot = self.clear_all_med(self.med_bot)


			self.x_treatment = 'botulinum_toxin'

			return {
				'domain': {'service': [
										('x_treatment', '=', self.x_treatment),
										]},
			}




	# Vitamin Intravenous
	@api.onchange('med_int')
	def _onchange_med_int(self):
		
		if self.med_int != 'none':
			print 
			print 'med_int'
			print 
			self.med_int = self.clear_all_med(self.med_int)


			self.x_treatment = 'intravenous_vitamin'

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
		#if self.med_lep != False:

			print 
			print 'on change - med_lep'


			self.zone = 		service_medical_vars._lep_dic_zone[self.med_lep]
			self.pathology = 	service_medical_vars._lep_dic_pathology[self.med_lep]
			self.x_treatment = 'lepismatic' 


			print self.med_lep 
			print self.zone
			print self.pathology
			print 

			#print self.med_lep['zone']
			#print self.med_lep['pathology']
			#self.x_treatment = self.med_lep 
			#self.zone = self.med_lep['zone']
			#self.pathology = self.med_lep['pathology']
			#self.x_treatment = 'lepismatic'

			self.med_lep = self.clear_all_med(self.med_lep)

			return {'domain': {'service': [
											('x_treatment', '=', self.x_treatment),
											('x_zone', '=', self.zone),
											('x_pathology', '=', self.pathology),
										]},}


	# Plasma
	@api.onchange('med_pla')
	def _onchange_med_pla(self):
		
		if self.med_pla != 'none':
			print 
			print 'med_pla'
			print 
			self.med_pla = self.clear_all_med(self.med_pla)


			self.x_treatment = 'plasma'
			#self.zone = 		service_medical_vars._pla_dic_zone[self.med_pla]
			#self.pathology = 	service_medical_vars._pla_dic_pathology[self.med_pla]


			pla_dic = service_medical_vars._pla_dic[self.med_pla]

			#self.pathology = 		service_medical_vars._pla_dic[self.med_pla]['pathology']
			#self.zone = 			service_medical_vars._pla_dic[self.med_pla]['zone']
			#self.sessions = 		service_medical_vars._pla_dic[self.med_pla]['sessions']

			self.pathology = 		pla_dic['pathology']
			self.zone = 			pla_dic['zone']
			self.sessions = 		pla_dic['sessions']



			print self.med_pla 
			print self.zone
			print self.pathology
			print self.sessions
			print 



			return {
				'domain': {'service': [
											('x_treatment', '=', self.x_treatment),
											('x_zone', '=', self.zone),
											('x_pathology', '=', self.pathology),										
											('x_sessions', '=', self.sessions),
										]},
			}


