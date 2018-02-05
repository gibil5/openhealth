# -*- coding: utf-8 -*-

from openerp import models, fields, api




# Progress 
_hap = {
			
			# Treatment 
			'laser_quick':         	'Quick', 
			'laser_co2':          	'Co2', 
			'laser_excilite':       'Exc', 
			'laser_ipl':         	'Ipl', 
			'laser_ndyag':        	'Ndy', 

			'hyaluronic_acid':      'Hial', 
			'criosurgery':         	'Crio', 
			'sclerotherapy':        'Escl', 
			'lepismatic':         	'Lepi', 
			'mesotherapy_nctf':     'Meso', 
			'plasma':         		'Plasma', 
			'botulinum_toxin':      'Botox', 
			'intravenous_vitamin':  'Vita Int', 



			# Zona 
			'areolas': 				'Ariolas', 
			'arms': 				'Brazos', 
			'armpits': 				'Axilas', 

			'back': 				'Espalda', 
			'belly': 				'Vientre', 
			'body_local': 			'Cuerpo', 
			'breast': 				'Pecho', 

			'cheekbones': 			'Pómulos', 

			'face': 				'Rostro', 
			'face_all': 			'Todo Rostro', 
			'face_all_hands': 		'Rostro Man', 
			'face_all_neck': 		'Rostro Cue', 
			'face_local': 			'Rostro', 
			'feet': 				'Pies', 

			'gluteus': 				'Glúteos', 

			'hands': 				'Manos', 

			'legs': 				'Piernas', 

			'neck': 				'Cuello', 
			'neck_hands': 			'Cuello Man', 

			'shoulders': 			'Hombros', 

			'vagina': 				'Vag', 




			# Patho
			'acne_sequels': 		'Acnsec', 
			'cyst': 				'Quis', 
			'keratosis': 			'Quer', 
			'mole': 				'Lun', 
			'rejuvenation': 		'Rejuv', 
			'scar': 				'Cic', 
			'stains': 				'Man', 
			'tatoo': 				'Tat', 
			'wart': 				'Verr', 
			'alopecia': 			'Alo', 
			'psoriasis': 			'Pso', 
			'vitiligo': 			'Viti', 
			'depilation': 			'Depi', 
			'acne_active': 			'Acné act', 
			'rosacea': 				'Ros', 
			'emangiomas': 			'Hem', 
			'ruby_points': 			'P Rubi', 
			'telangiectasia': 		'Tela', 
			'varices': 				'Var', 



			'acne_sequels_1': 		'Acnsec', 
			'acne_sequels_2': 		'Acnsec', 
			'acne_sequels_3': 		'Acnsec', 
			'acne_sequels_4': 		'Acnsec', 
			'acne_sequels_5': 		'Acnsec', 

			'cyst_1': 				'Qui', 
			'cyst_2': 				'Qui', 
			'cyst_3': 				'Qui', 
			'cyst_4': 				'Qui', 
			'cyst_5': 				'Qui', 

			'keratosis_1': 			'Que', 
			'keratosis_2': 			'Que', 
			'keratosis_3': 			'Que', 
			'keratosis_4': 			'Que', 
			'keratosis_5': 			'Que', 

			'mole_1': 				'Lun', 
			'mole_2': 				'Lun', 
			'mole_3': 				'Lun', 
			'mole_4': 				'Lun', 
			'mole_5': 				'Lun', 

			
			'scar_1': 				'Cic', 
			'scar_2': 				'Cic', 
			'scar_3': 				'Cic', 
			'scar_4': 				'Cic', 
			'scar_5': 				'Cic', 


			'stains_1': 				'Manchas', 
			'stains_2': 				'Manchas', 
			'stains_3': 				'Manchas', 
			'stains_4': 				'Manchas', 
			'stains_5': 				'Manchas', 

			'rejuvenation_neck_1': 		'Rejuv', 
			'rejuvenation_neck_2': 		'Rejuv', 
			'rejuvenation_neck_3': 		'Rejuv', 
			'rejuvenation_neck_4': 		'Rejuv', 
			'rejuvenation_neck_5': 		'Rejuv', 

			'rejuvenation_hands_1': 		'Rejuv', 
			'rejuvenation_hands_2': 		'Rejuv', 
			'rejuvenation_hands_3': 		'Rejuv', 
			'rejuvenation_hands_4': 		'Rejuv', 
			'rejuvenation_hands_5': 		'Rejuv', 


			'rejuvenation_face_1': 		'Rejuv', 
			'rejuvenation_face_2': 		'Rejuv', 
			'rejuvenation_face_3': 		'Rejuv', 
			'rejuvenation_face_4': 		'Rejuv', 
			'rejuvenation_face_5': 		'Rejuv', 


			'wart_1': 				'Verr', 
			'wart_2': 				'Verr', 
			'wart_3': 				'Verr', 
			'wart_4': 				'Verr', 
			'wart_5': 				'Verr', 


			'monalisa_touch': 		'Monalisa', 

}



_hac = {

			'acnetopic_200ml': 				'Acnetopic', 

			'anti_red': 					'Antirojeces', 
			
			'aloe_vital': 					'Aloé vital', 
			
			'cream_vitamins': 				'Crema vitaminas', 
			
			'cream_vitamins_aec': 			'Crema vitaminas AEC', 
			
			'dermatopic_lotion_120ml': 		'Dermatopic loción', 
			
			'dermatopic_sulfur_90gr': 		'Dermatopic sulfur', 
			
			'depigmentation_aha': 			'Despigmentante Aha', 
			
			'depigmentation_bfd8': 			'Despigmentante Bfd8', 
			
			'depigmentation_gliko': 		'Despigmentante Glico', 
			
			'depigmentation_hq': 			'Despigmentante Hq', 

			'depigmentation_santa_teresa': 		'Despigmentante Sta Teresa', 
			
			'depigmentation_no_hidroquinone': 	'Despigmentante sin Hidroquinona', 
			


			'hidratopic_lotion_120ml': 			'Hidratopic', 
			
			'kit_post_laser': 					'Kit post láser', 
			
			'mask_astringent_liquid_powder': 	'Máscara astringente liq+polvo', 
			
			'mask_astringent_liquid': 			'Máscara astringente liq', 
			
			'mask_astringent_powder': 			'Máscara astringente polvo', 
			
			'nctf': 							'Nctf', 
			
			'solar_protector': 					'Protector solar', 
			
			'q54': 								'Q54', 
			
			'tretinoina': 						'Tretinoina', 


			'acneclean': 						'Acnéclean', 

			'vip_card': 						'Tarjeta Vip', 



			'notil': 					'Notil', 
			'bepanthen': 				'Bepanthen', 
			'serum': 					'Suero fisiológico', 
			'gause': 					'Gasa de kit', 
			'redoxon': 					'Redoxon', 

			'token': 					'Token', 


			# Proliant 
			'dexpantenol_5ml':			'Dexpantenol 5ml', 
			'fillderma_ultra': 			'Fillderma ultra', 
			'formula_1':				'Fórmula 1', 

}









# Get Ticket Name 
@api.multi
#def get_ticket_name(self, treatment, zone, pathology, family, x_type):
def get_ticket_name(self, treatment, zone, pathology, family, x_type, name_short):


	print 'jx'
	print 'Get Ticket Name'

	#name_ticket = 'jx'
	name_ticket = 'x'



	# Service 
	if x_type == 'service': 

		if family == 'laser': 
			#name_ticket = _hap[treatment] + ' ' + zone + ' ' + pathology 

			if pathology in _hap: 
				name_ticket = _hap[treatment] + ' ' + _hap[zone] + ' ' + _hap[pathology]
			else: 
				name_ticket = _hap[treatment] + ' ' + _hap[zone] + ' ' + pathology 

		else:
			#name_ticket = treatment + ' ' + zone + ' ' + pathology 
			name_ticket = _hap[treatment] + ' ' + zone + ' ' + pathology 



	# Product 
	else: 
		if name_short in _hac: 
			name_ticket = _hac[name_short] 






	return name_ticket





