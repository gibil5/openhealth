# -*- coding: utf-8 -*-
"""
	*** Reco Funcs - Openhealth
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
					'co2': 			'price_list.service_co2',

					'excilite': 			'price_list.service_excilite',					
					'ipl': 			'price_list.service_ipl',
					'ndyag': 		'price_list.service_ndyag',
					'quick': 		'price_list.service_quick',
					'cosmetology': 	'price_list.service_cosmetology',
					'medical': 		'price_list.service_medical',
					'gynecology': 	'price_list.service_gynecology',
					'echography': 	'price_list.service_echography',
					'promotion': 	'price_list.service_promotion',
					'product': 		'price_list.service_product',
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
