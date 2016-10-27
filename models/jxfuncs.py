# -*- coding: utf-8 -*-



# Test

def test_for_digits(self, token):
		
	print 
	print 'on change'
	print 

	if token and (not token.isdigit()):
	#if  (not token.isdigit()):
		return {
				'warning': {
					'title': "Error: No es número",
					'message': token,
				}}
			
