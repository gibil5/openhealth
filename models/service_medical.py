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
						('x_treatment', '=', 'medical'),
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
	med_hia = fields.Selection(
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

			self.treatment = 'medical'
			self.zone = 'legs'
			self.pathology = 'varices'
			
			return {
				'domain': {'service': [
										('x_treatment', '=', self.treatment),
										('x_zone', '=', self.zone),
										('x_pathology', '=', self.pathology),

										('x_subtreatment', '=', self.subtreatment),

										]},
			}





