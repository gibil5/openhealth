# -*- coding: utf-8 -*-
#
# 		*** Jr Funcs
# 
# Created: 				 1 Nov 2016
# Last updated: 	 	 3 Jul 2018 
#

from openerp import models, fields, api



#------------------------------------------------ Appointment ---------------------------------------------------

# Update Apps 
@api.multi
def update_appointment_go(self, appointment_id, owner_id, x_type):


	# Get all Apps 	
	rec_set = self.env['oeh.medical.appointment'].browse([
															appointment_id
														])
	#print rec_set


	# By type 
	if x_type == 'consultation':
		ret = rec_set.write({
								'consultation': owner_id,
							})

	elif x_type == 'procedure':
		ret = rec_set.write({
								'procedure': owner_id,
								#'state': 'Scheduled',
							})

	elif x_type == 'session':
		ret = rec_set.write({
								'session': owner_id,
							})

	elif x_type == 'control':
		ret = rec_set.write({
								'control': owner_id,
							})
	#else:
	#	tra = 1
		#print 
		#print 'This should not happen !!!'
		#print 


	#print ret 
	return ret

# update_appointment_go




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

