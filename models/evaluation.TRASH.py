

# 3 Jan 2018


	#name = fields.Char(
	#		)





	# Commons
	#vspace = fields.Char(
	#		' ', 
	#		readonly=True
	#		)

	#_dic = {
	#			'Male':		'Masculino', 
	#			'Female':	'Femenino', 
	#			'none':		'Ninguno', 
	#			'one':			'I', 
	#			'two':			'II', 
	#			'three':			'III', 
	#			'continuous':	'Continua', 
	#			'fractional':	'Fraccionado',
	#			True:			'Si', 
	#			False:		'No', 
	#			'rejuvenation_capilar':			'Rejuvenecimiento capilar', 
	#			'body_local':					'Localizado cuerpo', 
	#			'':			'', 
	#		}





	#patient_id = fields.Integer(
	#		default=3025, 
	#)






	#therapist = fields.Many2one(
	#		'openhealth.therapist',

			#string = "Terapeuta", 	
	#		string = "Cosmeatra", 	

			#required=True, 
	#		required=False, 
	#		)





# 9 May 2018


	# Evaluation Nr
	evaluation_nr = fields.Integer(
			string="Evaluation #", 
			default=1, 

			required=True, 
			#compute='_compute_evaluation_nr', 
			)

	#@api.multi
	#@api.depends('state')
	#def _compute_evaluation_nr(self):
	#	for record in self:
	#		nr = 1
	#		record.evaluation_nr = nr  

