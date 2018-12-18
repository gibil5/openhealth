# -*- coding: utf-8 -*-



# PRODUCTS
#--------------------------------------------------------------------------------------------------

_dic_prod = {
				#'dexpantenol_5ml': 		'AMP. DEXPANTENOL 5 ML',
				'dexpantenol_5ml': 		'DEXPANTENOL 5 ML',
				

				# New
				'product_1': 				'Producto 1',
				'claridermil': 				'CLARIDERMIL',
				'vitamin_k': 				'VITAMINA K',
				'vitamin_c_serum': 			'VITAMINA C SERUM',



				'acneclean': 			'ACNECLEAN 50 GR',
				'acnetopic_200ml': 		'ACNETOPIC 200 ML',
				'aloe_vital': 			'ALOE VITAL',
				#'acne_topic_wash': 	'ACNETOPIC WASH',
				'acnetopic_wash': 		'ACNETOPIC WASH',
				'anti_red': 			'ANTIRROJECES', 
				'bepanthen': 			'BEPANTHEN', 
				
				'cream_vitamins': 			'CREMA CON VITAMINAS', 
				'cream_vitamins_aec': 		'CREMA CON VITAMINAS A, E, C', 
				'dermatopic_lotion_120ml': 	'DERMATOPIC LOCION 120 ML', 
				'dermatopic_sulfur_90gr': 	'DERMATOPIC SULFUR 90 GR', 

				'depigmentation_aha': 				'DESPIGMENTANTE AHA', 
				'depigmentation_bfd8': 				'DESPIGMENTANTE BF-D8', 
				'depigmentation_gliko': 			'DESPIGMENTANTE GLI-KO', 
				'depigmentation_hq': 				'DESPIGMENTANTE HQ', 
				'depigmentation_santa_teresa': 		'DESPIGMENTANTE SANTA TERESA', 
				'depigmentation_no_hidroquinone': 	'DESPIGMENTANTE SIN HIDROQUINONA', 

				'gause': 							'GASA DE KIT',
				'hidratopic_lotion_120ml': 			'HIDRATOPIC LOCION 120 ML',
				'kit_post_laser': 					'KIT POST LASER',
				'mask_astringent_liquid_powder': 	'MASCARA ASTRINGENTE (LIQUIDO + POLVO)',
				'mask_astringent_liquid': 			'MASCARA ASTRINGENTE LIQUIDO',
				'mask_astringent_powder': 			'MASCARA ASTRINGENTE POLVO',

				'nctf': 		'NCTF', 
				'notil': 		'NOTIL', 
				'other': 		'OTROS', 

				'solar_protector': 	'PROTECTOR SOLAR',
				'q54': 				'Q54',
				'redoxon': 			'REDOXON',
				'serum': 			'SUERO FISIOLOGICO',
				'vip_card': 		'TARJETA VIP',
				'tretinoina': 		'TRETINOINA',

				'dermobalance_180gr': 		'DERMOBALANCE 180 GR',
				'dexpanthenol_5ml': 		'DEXPANTENOL 5 ML',
				'fillderma_ultra_1ml': 		'FILLDERMA ULTRA 1 ML',
				'formula_1': 				'FORMULA 1',
}





# TREATMENTS
#--------------------------------------------------------------------------------------------------

# All But Med 
_dic_tre = {
				# Consultations 
				'con': 	'CONSULTA', 

				# Lasers 
				'co2': 	'LASER CO2 FRACCIONAL',
				'exc': 	'LASER EXCILITE',
				'ipl': 	'LASER M22 IPL',
				'ndy': 	'LASER M22 ND YAG',
				'qui': 	'QUICKLASER',

				# Cosmeto 
				'car': 	'CARBOXITERAPIA',
				'tcr': 	'LASER TRIACTIVE + CARBOXITERAPIA + CAMARA DE REDUCCION',
				'tca': 	'LASER TRIACTIVE + CARBOXITERAPIA',
				'dit': 	'PUNTA DE DIAMANTES',
}


# Medical 
_dic_tre_med = {
				'hac': 	'ACIDO HIALURONICO',
				'cri': 	'CRIOCIRUGIA',
				'scl': 	'ESCLEROTERAPIA',
				'lep': 	'LEPISMATICO (resorcina)',
				'men': 	'MESOTERAPIA NCTF',
				'pla': 	'PLASMA',
				'bot': 	'TOXINA BOTULINICA',
				'ivc': 	'VITAMINA C ENDOVENOSA',
				'inf': 	'INFILTRACIONES',
				#'infiltration': 	'INFILTRACIONES', 
}



# ZONES
#--------------------------------------------------------------------------------------------------

_dic_zo = {
				# Con
				'med': 	'MEDICA', 
				'gyn': 	'GINECOLOGICA', 


				# Exc
				'nec': 	'Cuello', 
				'bol': 	'Localizado Cuerpo', 
				'fal': 	'Localizado Rostro', 
				'faa': 	'Todo Rostro', 
				'han': 	'Manos', 
				'che': 	'Pomulos', 
				'vag': 	'Vagina', 


				# Ipl
				'bel': 	'Abdomen', 
				'are': 	'Ariolas', 
				'arp': 	'Axilas', 
				'arm': 	'Brazos', 
				'bac': 	'Espalda', 
				'glu': 	'Gluteos', 
				'sho': 	'Hombros', 
				'bre': 	'Pecho', 
				'leg': 	'Piernas', 
				'fee': 	'Pies', 
				'fac': 	'Rostro', 




				# Med
				'hea': 	'Cabeza', 
				'1hy': 	'1 Jeringa', 
				'1zo': 	'1 Zona', 

				# Cosmeto
				'bod': 	'Cuerpo', 
				#'fac': 	'1 Jeringa', 
				'boa': 	'Todo Cuerpo', 
				'fdn': 	'Rostro, Papada y Cuello', 


				# Quick
				'nec-han': 	'Cuello + Manos',
				'faa-han': 	'Todo Rostro + Manos',
				'faa-nec': 	'Todo Rostro + Cuello',
}



# PATHOLOGIES
#--------------------------------------------------------------------------------------------------

_dic_patho = {
				# Exc
				'alo': 	'Alopecias', 
				'pso': 	'Psoriasis', 
				'vit': 	'Vitiligo', 
				
				# Ipl
				'dep': 	'Depilacion', 
				'ros': 	'Rosacea', 
				'aca': 	'Acne Activo', 
				'sta': 	'Manchas', 
				'rfa': 	'Rejuvenecimiento Facial', 

				# Ndyag
				'ema': 	'Hemangiomas', 
				'rub': 	'Puntos Rubi', 
				'tel': 	'Telangectacias', 
				'var': 	'Varices', 


				# Med
				#'scar': 	'Cicatriz', 
				#'keloid': 	'Queloide', 
				'sca': 		'Cicatriz', 
				'kel': 		'Queloide', 
				'rfr': 		'Rejuvenecimiento Facial REPAIR', 
				'rec': 		'Rejuvenecimiento Capilar', 
				'acn': 		'Acne', 


				# Cosmeto
				'rwm': 	'Reduccion de peso y medidas', 
				'dfc': 	'Limpieza facial profunda', 
				#'rfa': 	'Rejuvenecimiento Facial', 
				'rea': 	'Reafirmacion', 


				# Quick
				'rej': 	'Rejuvenecimiento', 
				'acs': 	'Acne y Secuelas', 
				'ker': 	'Queratosis', 
				'cys': 	'Quiste', 
				'tat': 	'Tatuaje', 
				'war': 	'Verruga', 
				'mol': 	'Lunar', 

}


# PATHO CO2
_dic_patho_co2 = {
				'rn': 	'Rejuvenecimiento Cuello', 
				'as': 	'Acne y Secuelas', 
				'sc': 	'Cicatriz', 
				'mo': 	'Lunar', 
				'st': 	'Manchas', 
				'ke': 	'Queratosis', 
				'cy': 	'Quiste', 
				'wa': 	'Verruga', 
				'rf': 	'Rejuvenecimiento Facial', 
				'rh': 	'Rejuvenecimiento Manos', 
				'mon': 	'Monalisa Touch', 
}




# TIME
#--------------------------------------------------------------------------------------------------
_dic_time = {
				'5m': 	'5 min',
				'15m': 	'15 min',
				'30m': 	'30 min',
				'45m': 	'45 min',
				'60m': 	'60 min',
}



# SESSIONS
#--------------------------------------------------------------------------------------------------
_dic_ses = {
				'one': 		'1',
				'two': 		'2',
				'three': 	'3',
				'five': 	'5',
				'six': 		'6',
				'ten': 		'10',
				'twelve': 	'12',
}



# LEVELS
#--------------------------------------------------------------------------------------------------
_dic_deg = {
				'1': 	'Grado 1',
				'2': 	'Grado 2',
				'3': 	'Grado 3',
				'4': 	'Grado 4',
				'5': 	'Grado 5',
}

