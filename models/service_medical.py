# -*- coding: utf-8 -*-
#
# 	Service Medical treatment 
# 

from openerp import models, fields, api
from datetime import datetime
import jxvars


class ServiceMedical(models.Model):
	_name = 'openhealth.service.medical'
	_inherit = 'openhealth.service'
	
	
		
	# Service 
	service = fields.Many2one(
			'product.template',

			domain = [
						('type', '=', 'service'),
						('x_family', '=', 'medical'),

						#('x_treatment', '=', 'medical'),
						#('x_treatment', '=', 'laser_co2'),

					],
	)
	
	



	#------------------------------------- Medical ----------------------------------------
	

	# Consultation
	#med_con = fields.Selection(
	#		selection = jxvars._med_con_list, 
	#		default='none',	
	#		string="Consulta",
	#		)




	# Criosurgery
	med_crio = fields.Selection(
			selection = jxvars._med_crio_list, 
			default='none',	
			string="Criocirugía",
			)

	# Hialuronic
	med_hya = fields.Selection(
			selection = jxvars._med_hia_list, 
			default='none',	
			string="Acido Hialurónico",
			)

	# Sclerotherapy
	med_scle = fields.Selection(
			selection = jxvars._med_scle_list, 
			default='none',	
			string="Escleroterapia",
			)





	# Lepismatic
	med_lep = fields.Selection(
			selection = jxvars._med_lep_list, 
			default='none',	
			string="Lepismático",
			)

	# Plasma
	med_pla = fields.Selection(
			selection = jxvars._med_pla_list, 
			default='none',	
			string="Plasma",
			)

	# Botulinic Toxin
	med_bot = fields.Selection(
			selection = jxvars._med_bot_list, 
			default='none',	
			string="Toxina Botulínica",
			)





	# Intravenous
	med_int = fields.Selection(
			selection = jxvars._med_int_list, 
			default='none',	
			string="Endovenoso",
			)







	# On Change - Change the Domain
	# -------------------------------

	@api.onchange('med_crio')
	def _onchange_med_crio(self):
		
		if self.med_crio != 'none':
			print 
			print 'med_crio'
			print 

			self.med_crio = self.clear_all(self.med_crio)
			#self.clear_local()




			self.family = 'medical'
			self.treatment = 'criosurgery'

			#self.zone = 'legs'
			#self.pathology = 'varices'
			
			return {
				'domain': {'service': [
										('x_family', '=', self.family),
										('x_treatment', '=', self.treatment),

										#('x_zone', '=', self.zone),
										#('x_pathology', '=', self.pathology),
										]},
			}



	@api.onchange('med_hya')
	def _onchange_med_hya(self):
		
		if self.med_hya != 'none':
			print 
			print 'med_hya'
			print 

			self.med_hya = self.clear_all(self.med_hya)
			#self.clear_local()


			self.family = 'medical'
			self.treatment = 'hyaluronic_acid'

			return {
				'domain': {'service': [
										('x_family', '=', self.family),
										('x_treatment', '=', self.treatment),
										]},
			}


	@api.onchange('med_scle')
	def _onchange_med_scle(self):
		
		if self.med_scle != 'none':
			print 
			print 'med_scle'
			print 

			self.med_scle = self.clear_all(self.med_scle)


			self.family = 'medical'
			self.treatment = 'sclerotherapy'

			return {
				'domain': {'service': [
										('x_family', '=', self.family),
										('x_treatment', '=', self.treatment),
										]},
			}






	@api.onchange('med_lep')
	def _onchange_med_lep(self):
		
		if self.med_lep != 'none':
			print 
			print 'med_lep'
			print 

			self.med_lep = self.clear_all(self.med_lep)

			self.family = 'medical'
			self.treatment = 'lepismatic'

			return {
				'domain': {'service': [
										('x_family', '=', self.family),
										('x_treatment', '=', self.treatment),
										]},
			}

	@api.onchange('med_pla')
	def _onchange_med_pla(self):
		
		if self.med_pla != 'none':
			print 
			print 'med_pla'
			print 

			self.med_pla = self.clear_all(self.med_pla)

			self.family = 'medical'
			self.treatment = 'plasma'

			return {
				'domain': {'service': [
										('x_family', '=', self.family),
										('x_treatment', '=', self.treatment),
										]},
			}

	@api.onchange('med_bot')
	def _onchange_med_bot(self):
		
		if self.med_bot != 'none':
			print 
			print 'med_bot'
			print 

			self.med_bot = self.clear_all(self.med_bot)

			self.family = 'medical'
			self.treatment = 'botulinum_toxin'

			return {
				'domain': {'service': [
										('x_family', '=', self.family),
										('x_treatment', '=', self.treatment),
										]},
			}



	@api.onchange('med_int')
	def _onchange_med_int(self):
		
		if self.med_int != 'none':
			print 
			print 'med_int'
			print 


			self.med_int = self.clear_all(self.med_int)

			self.family = 'medical'
			self.treatment = 'intravenous_vitamin'

			return {
				'domain': {'service': [
										('x_family', '=', self.family),
										('x_treatment', '=', self.treatment),
										]},
			}




	# Clear

	def clear_all(self,token):
		
		#self.clear_commons()
		self.clear_local()

		return token




	@api.multi
	def clear_local(self):

		print 'clear_local_med'
		
		self.med_crio = 'none'
		self.med_hya = 'none'
		self.med_scle = 'none'

		self.med_lep = 'none'
		self.med_pla = 'none'
		self.med_bot = 'none'

		self.med_int = 'none'


