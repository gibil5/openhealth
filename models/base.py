# -*- coding: utf-8 -*-
#
# 	*** Base 
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





	# Dictionary 
	_dic = {
				'Male':		'Masculino', 
				'Female':	'Femenino', 

				'none':		'Ninguno', 

				'one':			'I', 
				'two':			'II', 
				'three':			'III', 

				'continuous':	'Contínua', 
				'fractional':	'Fraccionado',

				True:			'Si', 
				False:		'No', 



				'rejuvenation_capilar':			'Rejuvenecimiento capilar', 
				'body_local':					'Localizado cuerpo', 
				#'':			'', 
			}






	# Vertical space 
	vspace = fields.Char(
			' ', 
			readonly=True
			)






