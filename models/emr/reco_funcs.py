# -*- coding: utf-8 -*-
"""
	Reco Funcs - Openhealth
	Created: 				 15 Apr 2019
	Last up: 				 28 Jul 2020
"""
from openerp import models, fields, api

# ---------------------------------------------- Create Service -----------------------------
#def create_service(treatment_id, family=False, subfamily=False):
def create_service(treatment_id, family, subfamily, physician_id):
	"""
	Generic method for creating Services. 
	Compact. And easy to maintain. 
	"""
	print()
	print('Create Service Generic - ', subfamily)

	model_dic = {
					'co2': 			'openhealth.service_co2',

					'excilite': 	'openhealth.service_excilite',					
					'ipl': 			'openhealth.service_ipl',
					'ndyag': 		'openhealth.service_ndyag',
					'quick': 		'openhealth.service_quick',
					'cosmetology': 	'openhealth.service_cosmetology',
					'medical': 		'openhealth.service_medical',
					'gynecology': 	'openhealth.service_gynecology',
					'echography': 	'openhealth.service_echography',
					'promotion': 	'openhealth.service_promotion',
					'product': 		'openhealth.service_product',
		}

	model = model_dic[subfamily]

	# Open 	
	return {
			'type': 'ir.actions.act_window',
			'name': ' New Service Current', 
			'res_model':  	model,			
			#'res_id': consultation_id,
			"views": [[False, "form"]],
			#'view_type': 'form',
			'view_mode': 'form',	
			'target': 'current',
			'flags': 	{
							'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
							#'form': {'action_buttons': False, }
						},
			'context': {							
							'default_family': family,
							'default_physician': physician_id,
							#'default_pl_subfamily': subfamily,
							'default_treatment': treatment_id,
						}
			}
# create_service
