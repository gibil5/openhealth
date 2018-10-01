# -*- coding: utf-8 -*-
#
# 		gen.py
#
# 		Generates Names and Description, from Short Names. 
# 
# 		Created: 			21 Sep 2018
# 		Last up: 	 		21 Sep 2018
#



#------------------------------------------------ Const ---------------------------------------------------
# All But Med 
_dic_tre = {
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



_dic_zo = {
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


				# Con
				'med': 	'MEDICA', 
				'gyn': 	'GINECOLOGICA', 


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



_dic_time = {
				'5m': 	'5 min', 
				'15m': 	'15 min', 
				'30m': 	'30 min', 

				# Cos 
				'60m': 	'60 min', 

				# Quick
				'45m': 	'45 min', 
}


_dic_ses = {
				'one': 	'1', 
				'six': 	'6', 

				# Med
				'two': 		'2', 
				'three': 	'3', 
				'five': 	'5', 
				'ten': 		'10', 

				# Cos 
				'twelve': 		'12', 
}



#------------------------------------------------ Const - Co2 ---------------------------------------------------
# Ex 
# LASER CO2 FRACCIONAL - Cuello - Rejuvenecimiento Cuello Grado 1
# LASER CO2 FRACCIONAL - Localizado Cuerpo - Acne y Secuelas Grado 1
# LASER CO2 FRACCIONAL - Localizado Rostro - Cicatriz Grado 1
# LASER CO2 FRACCIONAL - Manos - Rejuvenecimiento Manos Grado 1
# LASER CO2 FRACCIONAL - Pomulos - Acne y Secuelas Grado 1

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

_dic_deg = {
				'1': 	'Grado 1', 
				'2': 	'Grado 2', 
				'3': 	'Grado 3', 
				'4': 	'Grado 4', 
				'5': 	'Grado 5', 

				#'n': 	'Touch', 
}



_dic_prod = {
				'acneclean': 			'ACNECLEAN 50 GR', 
				'acnetopic_200ml': 		'ACNETOPIC 200 ML', 
				'aloe_vital': 			'ALOE VITAL', 
				#'acne_topic_wash': 		'ACNETOPIC WASH', 
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

				#'mon': 	'Lunar', 
}


#------------------------------------------------  5 Params - Quick  ---------------------------------------------------
# Get Generated - 5 Params 
def get_generated_quick(short_name):
	#print 
	#print 'Get Generated Quick'

	# Init 
	generated = ''
	
	arr = short_name.split('_')
	
	tre = 		arr[0]
	zone = 		arr[1]
	patho = 	arr[2]


	# Generate 
	if len(arr) > 4: 
		time = 		short_name.split('_')[3]
		ses = 		short_name.split('_')[4]

		#if 	tre in _dic_tre and zone in _dic_zo  and patho in _dic_patho 	and 	time in _dic_time: 
		#if 	tre in _dic_tre and zone in _dic_zo: 
		if 	tre in _dic_tre 	and 	zone in _dic_zo 	and 	patho in _dic_patho: 
			
			#generated = _dic_tre[tre] + ' - ' + _dic_zo[zone] + ' - ' 
			#generated = _dic_tre[tre] + ' - ' + _dic_zo[zone] + ' - ' + _dic_patho[patho]
			generated = _dic_tre[tre] + ' - ' + _dic_zo[zone] + ' - ' + _dic_patho[patho] + ' - ' + _dic_time[time] + ' - ' + _dic_ses[ses] 

			#print generated


	return generated



#------------------------------------------------  Products - 1 Param ---------------------------------------------------
# Get Generated - 2 Params 
def get_generated_prod(short_name):
	#print 
	#print 'Get Generated Prod'

	generated = ''

	prod = 		short_name



	if 	prod in _dic_prod: 

			generated = _dic_prod[prod] 

			#print generated

	return generated








#------------------------------------------------  Consultations - 2 Params ---------------------------------------------------
# Get Generated - 2 Params 
def get_generated_con(short_name):
	#print 
	#print 'Get Generated Con'

	generated = ''

	tre = 		short_name.split('_')[0]
	zone = 		short_name.split('_')[1]


	if 	tre in _dic_tre and zone in _dic_zo: 

			generated = _dic_tre[tre] + ' ' + _dic_zo[zone] 

	return generated




#------------------------------------------------ Co2 - 3 Params ---------------------------------------------------
# Get Generated - 3 Params 
def get_generated_co2(short_name):
	#print 
	#print 'Get Generated Co2'

	generated = ''

	tre = 		short_name.split('_')[0]
	zone = 		short_name.split('_')[1]
	patho = 	short_name.split('_')[2][:2]
	deg = 		short_name.split('_')[2][-1:]
	third = 	short_name.split('_')[2]


	# Prints 
	#print tre 
	#print zone 
	#print patho 
	#print deg 
	#print third 


	# All but MT 
	if third != 'mon': 	
		if 	tre in _dic_tre 	and 	zone in _dic_zo 	and 	patho in _dic_patho_co2 	and 	deg in _dic_deg:
				generated = _dic_tre[tre] + ' - ' + _dic_zo[zone] + ' - ' + _dic_patho_co2[patho] + ' ' + _dic_deg[deg]

	# Only Monalisa Touch
	else: 
		generated = _dic_tre[tre] + ' - ' + _dic_zo[zone] + ' - ' + _dic_patho_co2[third]


	return generated




#------------------------------------------------  Med - 4 Params ---------------------------------------------------
# Get Generated - 4 Params 
def get_generated_med(short_name):
	#print 
	#print 'Get Generated Med'

	generated = ''

	arr = short_name.split('_')

	# Prints 
	#print short_name
	#print arr 


	# Generate 
	if len(arr) > 2: 
		tre = 		arr[0]
		zone = 		arr[1]
		patho = 	arr[2]

		# Prints 
		#print tre 
		#print zone 
		#print patho 


		# Generate 
		# Intravenous Vitamin
		if 	tre in ['ivc']: 
			generated = _dic_tre_med[tre] 

		# Infiltrations 
		elif tre in ['inf']: 
			generated = _dic_tre_med[tre] + ' - ' + _dic_patho[patho] 

		elif tre in _dic_tre_med and zone in _dic_zo and patho in _dic_patho: 

			if len(arr) > 3: 
				ses = 		arr[3]
				generated = _dic_tre_med[tre] + ' - ' + _dic_zo[zone] + ' - ' + _dic_patho[patho] + ' - ' + _dic_ses[ses]

	return generated





#------------------------------------------------  5 Params - Exc, Ipl, Ndyag, Cosmeto  ---------------------------------------------------
# Get Generated - 5 Params 
def get_generated_exc(short_name):
	#print 
	#print 'Get Generated Laser'

	# Init 
	generated = ''
	arr = short_name.split('_')
	tre = 		short_name.split('_')[0]
	zone = 		short_name.split('_')[1]
	patho = 	short_name.split('_')[2]

	# Prints 
	#print short_name
	#print arr 
	#print tre 
	#print zone 
	#print patho 


	# Generate 
	if len(arr) > 4: 
		time = 		short_name.split('_')[3]
		ses = 		short_name.split('_')[4]
		
		#print time 
		#print ses 
	
		#if 	tre in _dic_tre 	and 	zone in _dic_zo  	and 	patho in _dic_patho 	and 	time in _dic_time  	and ses in _dic_ses[ses]:
		if 	tre in _dic_tre and zone in _dic_zo  and patho in _dic_patho 	and 	time in _dic_time: 
				generated = _dic_tre[tre] + ' - ' + _dic_zo[zone] + ' - ' + _dic_patho[patho] + ' - ' + _dic_time[time] + ' - ' + _dic_ses[ses] 



	# Prints 
	#if tre in ['exc']: 
	#if True: 
	#	print 
	#	print 'Get Generated Exc'
	#	print tre + '.'
	#	print zone + '.'
	#	print patho + '.'
	#	print time + '.' 
	#	print ses + '.'
	#	print generated + '.'
	#	print 
	
	return generated


