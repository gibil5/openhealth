# -*- coding: utf-8 -*-



_co2_mode_emission_list = [

		('continuous','Continua'), 
		('fractional','Fraccionado'), 
		
		#('',''), 
]



_co2_mode_exposure_list = [

		#('one','uno'), 
		#('two','dos'), 
		
		('continuous',	'Continuo'), 
		('repete',		'Repetir'), 

		#('',''), 
]






def test_for_zero(self, token):
	#print 'test_for_zero'
	#print token 

	#if token and (not token.isdigit()):
	#if token and token == 0.0:
	if token == 0.0:
		#print 'Error'
		#return {
		#		'warning': {
		#			'title': 	"Error: Valor Nulo.",
		#			'message': 	token,
		#		}}
		return {'value':{},'warning':{'title':'warning','message':'Valor nulo'}}

	else:
		return 0
# test_for_digits


