# -*- coding: utf-8 -*-



# State 
_state_list = [
				('pre_scheduled',	 		'No confirmado'),
				('Scheduled', 				'Confirmado'),
				#('pre_scheduled_control', 	'Pre-cita'),
				('pre_scheduled_control', 	'Sin Hora (Control)'),

				('pre_scheduled_session', 	'Sin Hora (Sesion)'),



				#('event', 					'Evento'),
				#('invoiced', 				'Facturado'),
				#('error', 					'Error'),
				#('completed', 				'Completo'),

				# Oe Health 
				#('Scheduled', 'Scheduled'),
				#('Completed', 'Completed'),
				#('Invoiced', 'Invoiced'),
]






# Type 
_type_list = [
        			('consultation', 'Consulta'),
        			('procedure', 	'Procedimiento'),
        			('event', 		'Evento'),
        			('session', 	'Sesión'),
        			('control', 	'Control'),
        			
        			#('cosmetology', 'Cosmiatría'),
]



# SubType 
_h_subtype = {
					# Other 
					'other':		'Otr',


					# Consultation 
					'consultation':		'',

					# Laser 
					'laser_quick':		'Qui', 
					'laser_co2':		'Co2 ', 
					'laser_excilite':	'Exc', 
					'laser_m22':		'M22', 
					'laser_ipl':		'Ipl', 
					'laser_ndyag':		'Ndy', 


					# Medical 
					'criosurgery': 			'Cri', 					
					'botulinum_toxin': 		'Bot', 
					'hyaluronic_acid': 			'Hia', 
					'hyaluronic_acid_repair': 	'Hiar', 
					'intravenous_vitamin': 	'Vit', 
					'lepismatic': 			'Lep', 
					'mesotherapy_nctf': 	'Mes', 
					'plasma': 				'Pla', 
					'sclerotherapy': 		'Esc', 

					'infiltration_keloid': 	'Infq', 
					'infiltration_scar': 	'Infc', 


					# Cosmetology
					#'laser_triactive':		'Tri', 
					#'chamber_reduction':	'Cam',
					#'carboxy_diamond':		'Car',
					'carboxytherapy':		'Carbo', 
					'diamond_tip':				'Punta', 
					'triactive_carboxytherapy':				'Trca', 
					'triactive_carboxytherapy_reductionchamber':	'Trcare', 


					#'medical': 			'TM', 					
					False: 				'x', 					
}


# Subtype
#_machines_list = [
_subtype_list = [
					# Consultation 
					#('consultation','consultation'), 
					('consultation','Consulta'), 


					# Laser 
					#('laser_co2_1',	'Co2 1'), 
					#('laser_co2_2',	'Co2 2'), 
					#('laser_co2_3',	'Co2 3'), 
					('laser_quick',		'Quick'), 
					('laser_co2',		'Co2 '), 
					('laser_excilite',	'Excilite'), 
					('laser_m22',		'M22'), 

					('laser_ipl',		'Ipl'), 
					('laser_ndyag',		'Ndyag'), 



					# Medical 
					('criosurgery', 			'Criocirugía'), 					
					('botulinum_toxin', 		'Toxina botulínica'), 
					('hyaluronic_acid', 		'Acido hialurónico'), 
					('hyaluronic_acid_repair', 	'Acido hialurónico - Repair'), 
					('intravenous_vitamin', 	'Vitamina intravenosa'), 
					('lepismatic', 				'Lepismático'), 
					('mesotherapy_nctf', 		'Mesoterapia NCTF'), 
					('plasma', 					'Plasma'), 
					('sclerotherapy', 			'Escleroterapia'), 

					('infiltration_keloid', 	'Infiltracion Queloide'), 
					('infiltration_scar', 		'Infiltracion Cicatriz'), 



					# Cosmetology
					#('laser_triactive',			'Triactivo'), 
					#('chamber_reduction',		'Cámara de reducción'), 
					#('carboxy_diamond',			'Carboxiterapia - Punta de Diamante'), 
					('carboxytherapy',			'Carboxiterapia'), 
					('diamond_tip',				'Punta de Diamante'), 
					('triactive_carboxytherapy',					'Triactivo Carboxiterapia'), 
					('triactive_carboxytherapy_reductionchamber',	'Triactivo Carboxiterapia Camara Reduccion'), 




					#('none','Ninguna'), 		
					#('medical',					'Tratamiento Medico'), 		
					('other',					'Otro'), 		


]















_type_cal_dic = {
        			#'consultation': 	'C',
        			#'procedure': 		'P',
        			#'session': 			'S',        			
        			#'control': 			'Ctl',

        			'consultation': 	'Con',
        			'procedure': 		'Pro',
        			#'event': 			'EVENTO',
        			'event': 			'Eve',
        			'control': 			'Ctl',
        			'session': 			'Ses',        			


        			#'Consulta': 		'C',
        			#'Procedimiento': 	'P',
        			#'Sesion': 			'S',
        			#'Control': 			'Ctl',
}


_type_cal_list = [
        			#('S', 	'S'),
        			('Ses', 	'Ses'),

        			#('C', 	'C'),
        			#('P', 	'P'),
        			#('Ctl', 'Ctl'),

        			
        			('Con', 	'Con'),
        			('Pro', 	'Pro'),
        			('Ctl', 	'Ctl'),

        			#('EVENTO', 'EVENTO'),
        			('Eve', 	'Eve'),


        			#('consultation', 'C'),
        			#('procedure', 'P'),
        			#('session', 'S'),
        			#('control', 'X'),
]



_hash_state = {
						#'Scheduled':				'1',
						#'pre_scheduled':			'2',
						#'pre_scheduled_control':	'3',
						#'event':					'11',

						#'Scheduled':				'Conf',
						'Scheduled':				'C',
						#'pre_scheduled':			'NConf',
						'pre_scheduled':			'N',
						'event':					'11',
						
						'pre_scheduled_control':	'3',
						#'pre_scheduled_session':	'4',
						'pre_scheduled_session':	'3',
						

						#'error':					'55',
						#'invoiced':				'10',
						#False:				'', 
						#'completed':				'20',
}





_hash_colors_x_type = {

			'Procedimiento': 1,
			'procedure': 1,
			'Consulta': 2,
			'consultation': 2,
			'procedure_pre_scheduled': 3,
			'Sesion': 4,
			'session': 4,
			'Control': 5,
			'control': 5,
			
}


_duration_list = [
        			('0.25', 	'15 min'),
        			('0.5', 	'30 min'),

					#('0.75', 	'45 min'),
        			#('1.0', 	'60 min'),
        			#('2.0', 	'120 min'),
]











# Hash 
_hash_doctor_code = {
							#'Dra. Acosta':		'Dra. A',
							#'Dr. Canales':		'Dr. Ca',
							#'Dr. Chavarri':	'Dr. Ch',
							#'Dr. Gonzales':	'Dr. Go',
							#'Dr. Escudero':	'Dr. Es',
							#'Dr. Alarcon':		'Dr. Al',
							#'Dr. Vasquez':		'Dr. Va',

							#'Dra. Acosta':		'AC',
							#'Dr. Alarcón':		'AL',



							# Physicians 
							'Dr. Canales':		'CA',
							'Dr. Chavarri':		'CH',
							'Dr. Gonzales':		'GO',
							'Dr. Escudero':		'ES',
							'Dr. Vasquez':		'VA',
							'Dr. Alarcon':		'AL',
							'Dr. Mendez':		'ME',
							'Dr. Monteverde':	'MO',


							'Dr. Loaiza':		'LO',
							'Dr. Castillo':		'CS',
							'Dr. Abriojo':		'AB',




							# Lasers  
							'laser_co2_1':		'Co2_1',
							'laser_co2_2':		'Co2_2',
							'laser_co2_3':		'Co2_3',
							'laser_excilite':	'Exc',
							'laser_m22':		'M22',

							# Cosmetology 
							'Eulalia':		'EU',
							'Eulalia 2':	'EU2',
							'Eulalia 3':	'EU3',							



							'Dr. Medico':		'CH',

							False:				'', 
		}



# Profile
_profile_list = [

		('normal','Normal'), 
		('anxious','Ansioso'), 
		('psychiatric','Psiquiátrico'), 
		('plaintif','Quejoso'), 
		('depressed','Deprimido'), 
		('histroinic','Histriónico'), 
		('other','Otro'), 
		
		#('',''), 
]




# Machines
_machines_cos_list = [

		('laser_triactive','Triactivo'), 
		('chamber_reduction','Cámara de reducción'), 
		('carboxy_diamond','Carboxiterapia - Punta de Diamante'), 

		#('none','Ninguna'), 		
]






# Targets
#_target_list = [
#		('doctor','Doctor'), 
#		('therapist','Cosmeatra'), 
		#('machine','Machine'), 
#]

