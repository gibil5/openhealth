# -*- coding: utf-8 -*-


#from openerp import models, fields, api
#import time_funcs
#from datetime import datetime,tzinfo,timedelta








# Test

def test_name(self, token):
		
	print 
	print 'on change name'
	print 


	if token != False:

		nr_words = len(token.split())


		if nr_words == 1:
			return {
					'warning': {
						'title': "Error: Apellido incompleto: ",
						'message': token,
					}}




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

