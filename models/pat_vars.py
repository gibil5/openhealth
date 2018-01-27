# -*- coding: utf-8 -*-







# Zone 
_zo_dic = {

				#'body_local':					'Localizado cuerpo', 

				# Begin
				'areolas':		'Areolas', 
				'armpits':		'Axilas', 
				'arms':			'Brazos', 
				'back':			'Espalda', 
				'belly':		'Abdomen', 
				'body_local':	'Localizado cuerpo', 
				'breast':		'Pecho', 
				'cheekbones':	'Pómulos', 
				'face':			'Rostro',
				'face_all':		'Todo Rostro', 
				'face_hands':	'Rostro-Manos', 
				'face_local':	'Localizado Rostro', 
				'face_neck':	'Rostro-Cuello', 
				'face_neck_hands':	'Rostro-Cuello-Manos',   
				'feet':			'Pies', 
				'gluteus':		'Glúteos', 
				'hands':		'Manos', 
				'head':			'Cabeza', 
				'legs':			'Piernas', 
				'neck':			'Cuello', 
				'package':		'Paquete', 
				'shoulders':	'Hombros', 
				'vagina':		'Vagina', 
				# End 

		}




# Chief complaint 
_cc_dic = {

				#'scar':							'Cicatriz', 
				#'rejuvenation_capilar':			'Rejuvenecimiento capilar', 

				# Begin
				'acne_active':	'Acné Activo',
				'acne_sequels':	'Acné y Secuelas',
				'alopecia':		'Alopecias',
				'scar':			'Cicatriz',
				'depilation':	'Depilación',
				'emangiomas':	'Hemangiomas',
				'mole':			'Lunar',
				'stains':		'Manchas',
				'monalisa_touch':'Monalisa Touch',
				'polyp':		'Pólipo',
				'psoriasis':	'Psoriasis',
				'ruby_point':	'Punto rubí',
				'keratosis':	'Queratosis',
				'cyst':			'Quiste',
				'rejuvenation_capilar':			'Rejuvenecimiento Capilar',	# Medical 
				'rejuvenation_facial':			'Rejuvenecimiento Facial',
				'rejuvenation_hands':			'Rejuvenecimiento en manos',
				'rejuvenation_neck':			'Rejuvenecimiento en cuello',
				'rejuvenation_face_neck':		'Rejuvenecimiento Facial + Rejuvenecimiento en Cuello',
				'rejuvenation_face_hands':		'Rejuvenecimiento Facial + Rejuvenecimiento en Manos',
				'rejuvenation_face_neck_hands':	'Rejuvenecimiento Facial + Rejuvenecimiento en Cuello + Rejuvenecimiento en Manos',
				'rosacea':			'Rosácea',
				'telangiectasia':	'Telangectacias',
				'varices':			'Varices',
				'wart':				'Verruga',
				'vitiligo':			'Vitiligo',
				# End 		

		}













_sex_type_list = [

			('Male', 'Masculino'),
			('Female', 'Femenino'),

			]







_dic_sex = {
				'Male':	'Masculino', 
				'Female':	'Femenino', 

				#'male':	'Masculino', 
				#'female':	'Femenino', 
			}


_state_list = [
        			#(False, 	'Incompleto'),

					#('incomplete', 	'Ficha incompleta'),
					('incomplete', 	'FICHA INCOMPLETA'),

        			('active', 	'Activo'),

        		]

_education_level_type = [
			('first', 'Primaria'),
			('second', 'Secundaria'),
			('technical', 'Instituto'),
			('university', 'Universidad'),
			('masterphd', 'Posgrado'),
			]

_FAMILY_RELATION = [
			
			('none', 'Ninguno'),

			('Father', 'Padre'),
			('Mother', 'Madre'),
			('Brother', 'Hermano'),
			('Grand Father', 'Abuelo'),
			('Friend', 'Amigo'),
			('Husband', 'Esposo'),
			('Other', 'Otro'),
			#('Sister', 'Hermana'),
			#('Wife', 'Esposa'),
			#('Grand Mother', 'Abuela'),
			#('Aunt', 'Tía'),
			#('Uncle', 'Tío'),
			#('Nephew', 'Sobrino'),
			#('Niece', 'Sobrina'),
			#('Cousin', 'Primo'),
			#('Relative', 'Pariente'),
			]





_first_contact_list = [
		('none','Ninguno'), 
		('recommendation','Recomendación'), 
		('tv','Tv'), 
		('radio','Radio'), 
		('internet','Internet'), 
		('website','Sitio web'), 
		('mail_campaign','Campaña de mail'), 
		]




_street2_list = [

	(1,'Lima'),

	(2,'Ancón'),
	(3,'Ate'),
	(4,'Barranco'),
	(5,'Breña'),
	(6,'Carabayllo'),

	(40,'Cieneguilla'),

	(7,'Comas'),
	(8,'Chaclacayo'),
	(9,'Chorrillos'),
	(10,'El Agustino'),

	(28,'Independencia'),

	(11,'Jesús María'),
	(12,'La Molina'),
	(13,'La Victoria'),
	(14,'Lince'),

	(39,'Los Olivos'),
	
	(15,'Lurigancho'),
	(16,'Lurín'),
	(17,'Magdalena del Mar'),
	(18,'Miraflores'),
	(19,'Pachacamac'),
	(20,'Pucusana'),

	(21,'Pueblo Libre'),
	(22,'Puente Piedra'),
	(23,'Punta Negra'),
	(24,'Punta Hermosa'),
	(25,'Rímac'),

	(43,'Santa Anita'),

	(26,'San Bartolo'),

	(41,'San Borja'),

	(27,'San Isidro'),

	
	(29,'San Juan de Miraflores'),
	(30,'San Luis'),

	(31,'San Martín de Porres'),
	(32,'San Miguel'),
	(33,'Santiago de Surco'),
	(34,'Surquillo'),
	(36,'San Juan de Lurigancho'),
	(37,'Santa María del Mar'),
	(38,'Santa Rosa'),



	(42,'Villa El Salvador'),
	(35,'Villa María del Triunfo'),

]


zip_dic_inv =  {
		
		1:	'Lima',
		2:	'Ancón',
		3:	'Ate',
		4:	'Barranco',
		5:	'Breña',
		6:	'Carabayllo',
		7:	'Comas',
		8:	'Chaclacayo',
		9:	'Chorrillos',
		10:	'El Agustino',
		
		11:	'Jesús María',
		12:	'La Molina',
		13:	'La Victoria',
		14:	'Lince',
		15:	'Lurigancho',
		16:	'Lurín',
		17:	'Magdalena del Mar',
		18:	'Miraflores',
		19:	'Pachacamac',
		20:	'Pucusana',
		
		21:	'Pueblo Libre',
		22:	'Puente Piedra',
		23:	'Punta Negra',
		24:	'Punta Hermosa',
		25:	'Rímac',
		26:	'San Bartolo',
		27:	'San Isidro',
		28:	'Independencia',
		29:	'San Juan de Miraflores',
		30:	'San Luis',
		
		31:	'San Martín de Porres',
		32:	'San Miguel',
		33:	'Santiago de Surco',
		34:	'Surquillo',
		35:	'Villa María del Triunfo',
		36:	'San Juan de Lurigancho',
		37:	'Santa María del Mar',
		38:	'Santa Rosa',
		39:	'Los Olivos',
		40:	'Cieneguilla',
		
		41:	'San Borja',
		42:	'Villa El Salvador',
		43:	'Santa Anita',

		False: '',
		
		}










_street2_list_old = [

			('Lima','Lima'),
			('Ancón','Ancón'),
			('Ate','Ate'),
			('Barranco','Barranco'),
			('Breña','Breña'),
			('Carabayllo','Carabayllo'),
			('Comas','Comas'),
			('Chaclacayo','Chaclacayo'),
			('Chorrillos','Chorrillos'),
			('El Agustino','El Agustino'),
			
			('Jesús María','11'),
			('La Molina','12'),
			('La Victoria','13'),
			('Lince','14'),
			('Lurigancho','15'),
			('Lurín','16'),
			('Magdalena del Mar','17'),
			('Miraflores','18'),
			('Pachacamac','19'),
			('Pucusana','20'),
			
			('Pueblo Libre','21'),
			('Puente Piedra','22'),
			('Punta Negra','23'),
			('Punta Hermosa','24'),
			('Rímac','25'),
			('San Bartolo','26'),
			('San Isidro','27'),
			('Independencia','28'),
			('San Juan de Miraflores','29'),
			('San Luis','30'),
			
			('San Martín de Porres','31'),
			('San Miguel','32'),
			('Santiago de Surco','33'),
			('Surquillo','34'),
			('Villa María del Triunfo','35'),
			('San Juan de Lurigancho','36'),
			('Santa María del Mar','37'),
			('Santa Rosa','38'),
			('Los Olivos','39'),
			('Cieneguilla','40'),
			
			('San Borja','41'),
			
			('Villa El Salvador','42'),
			('Santa Anita','43'),
			]







_city_list = [
			('lima','Lima'),
			('abancay','Abancay'),
			('arequipa','Arequipa'),
			('ayacucho','Ayacucho'),
			('cajamarca','Cajamarca'),
			('callao','Callao'),
			('cerro_de_pasco','Cerro de Pasco'), 
			('chachapoyas','Chachapoyas'),
			('chiclayo','Chiclayo'),
			('cuzco','Cuzco'),
			('huacho','Huacho'),
			('huancavelica','Huancavelica'),
			('huancayo','Huancayo'),
			#('huanuco','Huánuco'),
			('huanuco','Huanuco'),
			('huaraz','Huaraz'),
			('ica','Ica'),
			('iquitos','Iquitos'),
			('moquegua','Moquegua'),
			('moyobamba','Moyobamba'),
			('piura','Piura'),
			('pucallpa','Pucallpa'),
			('puerto_maldonado','Puerto Maldonado'), 
			('puno','Puno'),
			('tacna','Tacna'),
			('trujillo','Trujillo'),
			('tumbes','Tumbes'),

			('',''),
		]




zip_dic =  {
		
		'Lima':			1,
		'Ancón':		2,
		'Ate':			3,
		'Barranco':		4,
		'Breña':		5,
		'Carabayllo':	6,
		'Comas':		7,
		'Chaclacayo':	8,
		'Chorrillos':	9,
		'El Agustino':	10,
		'Jesús María':	11,
		'La Molina':	12,
		'La Victoria':	13,
		'Lince':		14,
		'Lurigancho':	15,
		'Lurín':		16,
		'Magdalena del Mar':	17,
		'Miraflores':	18,
		'Pachacamac':	19,
		'Pucusana':		20,
		'Pueblo Libre':	21,
		'Puente Piedra':22,
		'Punta Negra':	23,
		'Punta Hermosa':24,
		'Rímac':		25,
		'San Bartolo':	26,
		'San Isidro':	27,
		'Independencia':	28,
		'San Juan de Miraflores':	29,
		'San Luis':	30,
		'San Martín de Porres':	31,
		'San Miguel':	32,
		'Santiago de Surco':	33,
		'Surquillo':	34,
		'Villa María del Triunfo':	35,
		'San Juan de Lurigancho':	36,
		'Santa María del Mar':	37,
		'Santa Rosa':	38,
		'Los Olivos':	39,
		'Cieneguilla':	40,
		'San Borja':	41,
		'Villa El Salvador':	42,
		'Santa Anita':	43,
		
		}




zip_list = [

			('Lima','1'),
			('Ancón','2'),
			('Ate','3'),
			('Barranco','4'),
			('Breña','5'),
			('Carabayllo','6'),
			('Comas','7'),
			('Chaclacayo','8'),
			('Chorrillos','9'),
			('El Agustino','10'),
			('Jesús María','11'),
			('La Molina','12'),
			('La Victoria','13'),
			('Lince','14'),
			('Lurigancho','15'),
			('Lurín','16'),
			('Magdalena del Mar','17'),
			('Miraflores','18'),
			('Pachacamac','19'),
			('Pucusana','20'),
			('Pueblo Libre','21'),
			('Puente Piedra','22'),
			('Punta Negra','23'),
			('Punta Hermosa','24'),
			('Rímac','25'),
			('San Bartolo','26'),
			('San Isidro','27'),
			('Independencia','28'),
			('San Juan de Miraflores','29'),
			('San Luis','30'),
			('San Martín de Porres','31'),
			('San Miguel','32'),
			('Santiago de Surco','33'),
			('Surquillo','34'),
			('Villa María del Triunfo','35'),
			('San Juan de Lurigancho','36'),
			('Santa María del Mar','37'),
			('Santa Rosa','38'),
			('Los Olivos','39'),
			('Cieneguilla','40'),
			
			('San Borja','41'),
			
			('Villa El Salvador','42'),
			('Santa Anita','43'),
			]


