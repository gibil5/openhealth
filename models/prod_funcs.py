# -*- coding: utf-8 -*-

from openerp import models, fields, api



# Family, Treatment, Zone, Pathology 
_hap = {
			'other':         	'Otros', 


			'infiltration': 		'Infiltración', 
			
			'infiltration_scar': 	'Infiltración Cicatriz', 
			'infiltration_keloid': 	'Infiltración Queloide', 



			'x': 'x', 
			'laser_m22': 			'M22', 

			
			# Treatment 
			#'consultation':          'Consulta', 

			'laser_quick':         	'Quick', 
			'laser_co2':          	'Co2', 
			'laser_excilite':       'Exc', 
			'laser_ipl':         	'Ipl', 
			'laser_ndyag':        	'Ndy', 



			# Medical 

			'criosurgery':         	'Criocirugía', 
			'plasma':         		'Plasma', 
			'botulinum_toxin':      'Toxina Botulínica', 
			'hyaluronic_acid':      'Acido Hialurónico', 
			'sclerotherapy':        'Escleroterapia', 
			'lepismatic':         	'Lepismático', 
			'mesotherapy_nctf':     'Mesoterapia nctf', 
			'intravenous_vitamin':  'Vit C Endovenosa', 




			# Cosmetology 
			'carboxytherapy':       'Carboxiterapia', 
			'diamond_tip':			'Punta Diamante', 
			'triactive_carboxytherapy': 					'Triac + Carbo', 
			'triactive_carboxytherapy_reductionchamber': 	'Triac + Carbo + CR', 




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



# Products 
_hac = {
			'other': 				'Otros', 


			'kenacort': 			'Kenacort', 
			'acne_topic_wash': 		'Acnetopic Wash', 
			'generic_product': 		'Producto genérico', 
			'generic_service': 		'Servicio genérico', 
			'con_med': 				'Consulta Médica', 
			'con_gyn': 				'Consulta Ginecológica', 
			'con_med_zero': 		'Consulta Médica - Costo Zero', 



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
def get_ticket_name(self, treatment, zone, pathology, family, x_type, name_short):

	#print
	#print 'Get Ticket Name'
	#print x_type, name_short, family, treatment, zone, pathology
	#print 



	if family == False: 
		family = 'x'

	if treatment == False: 
		treatment = 'x'

	if zone == False: 
		zone = 'x'

	if pathology == False: 
		pathology = 'x'



	name_ticket = 'x'


	# Service 
	if x_type == 'service': 

		if family == 'laser': 
			#name_ticket = _hap[treatment] + ' ' + zone + ' ' + pathology 

			if pathology in _hap: 
				name_ticket = _hap[treatment] + ' ' + _hap[zone] + ' ' + _hap[pathology]
			else: 
				name_ticket = _hap[treatment] + ' ' + _hap[zone] + ' ' + pathology 


		elif family == 'consultation': 
			if name_short in _hac: 
				name_ticket = _hac[name_short] 

		else: 
			if treatment in _hap: 
				name_ticket = _hap[treatment] 






	# Product 
	else: 
		if name_short in _hac: 
			name_ticket = _hac[name_short] 





	#print name_ticket
	#print 

	return name_ticket



