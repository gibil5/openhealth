# -*- coding: utf-8 -*-



# Test

def test_for_digits(self, token):
		
	print 
	print 'test for digits'
	print 

	if token and (not token.isdigit()):
		return {
				'warning': {
					'title': "Error: Debe ser número.",
					'message': token,
				}}
	else:
		return 0



def test_for_length(self, token, length):
		
	print 
	print 'test for length'
	print 


	#if token and (not token.isdigit()):
	#	return {
	#			'warning': {
	#				'title': "Error: No es número",
	#				'message': token,
	#			}}

	if token and (len(str(token))!= length):
		return {
				'warning': {
					'title': "Error: Debe tener " + str(length) + " caracteres.",
					'message': token,
				}}
	else:
		return 0

