# -*- coding: utf-8 -*-
#
# 		*** Jr Funcs
# 
# Created: 				  1 Nov 2016
# Last updated: 	 	 20 Jul 2018 
#

from openerp import models, fields, api




#------------------------------------------------ Tests ---------------------------------------------------

# Must have double sur name
def test_name(self, token):
		
	#print 
	#print 'Test name'
	#print 

	if token != False:
		nr_words = len(token.split())
		if nr_words == 1:
			return {
					'warning': {
						'title': "Error: Apellido incompleto: ",
						'message': token,
					}}
# test_name



# For Digits 
def test_for_digits(self, token):
		
	#print 
	#print Test for digits'
	#print 

	if token and (not token.isdigit()):
		return {
				'warning': {
					'title': "Error: Debe ser número.",
					'message': token,
				}}
	else:
		return 0
# test_for_digits



# For Length 
def test_for_length(self, token, length):
		
	#print 
	#print 'test for length'
	#print 

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
# test_for_length

