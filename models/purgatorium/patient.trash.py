


	#_name = 'openhealth.patient'		#The best solution ? So that impact is minimal ?	- Deprecated

	#_inherit = ['oeh.medical.patient', 'openhealth.base']
	#_inherits = ['oeh.medical.patient', 'openhealth.base']






# 25 Augu 2017

	# Dictionary 
	#_dic = {
	#			'Male':		'Masculino', 
	#			'Female':	'Femenino', 
	#			'none':		'Ninguno', 
	#			'':			'', 
	#		}

	#x_sex_name = fields.Char(
	#		'Sexo', 
	#		required=True, 
	#		compute='_compute_x_sex_name', 
	#	)

	#@api.multi
	#def _compute_x_sex_name(self):
	#	for record in self:
	#		record.x_sex_name = record._dic[record.sex] 



