# -*- coding: utf-8 -*-
#
# 	*** Base - DEPRECATED ? 
# 

# Created: 				26 Jun 2017
# Last updated: 	 	Id. 

from openerp import models, fields, api




#------------------------------------------------------------------------
class Base(models.Model):

	#_inherit = 'oeh.medical.evaluation'

	_name =	'openhealth.base'


	#name = fields.Char(
	#		)





	# Dictionaries

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




	# Other 
	_dic = {
				'Male':		'Masculino', 
				'Female':	'Femenino', 

				'none':		'Ninguno', 

				'one':			'I', 
				'two':			'II', 
				'three':		'III', 
				'four':			'IV', 
				'five':			'V', 
				'six':			'VI', 
				'seven':		'VII', 

				'continuous':	'Contínua', 
				'fractional':	'Fraccionado',

				True:			'Si', 
				False:		'No', 

				#'':			'', 
			}






	# Vertical space 
	vspace = fields.Char(
			' ', 
			readonly=True
			)






