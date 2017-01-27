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
		self.med_lep = 'none'
		self.med_pla = 'none'
		self.med_bot = 'none'
		self.med_int = 'none'



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


			#self.family = 'medical'
			#self.treatment = 'hyaluronic_acid'
			self.x_treatment = 'hyaluronic_acid'

			return {
				'domain': {'service': [
										#('x_family', '=', self.family),
										#('x_treatment', '=', self.treatment),
										('x_treatment', '=', self.x_treatment),
										]},
			}



