# -*- coding: utf-8 -*-
#
# 	*** Pat Funcs
# 

# Created: 				  1 Nov 2016
# Last updated: 	 	 21 Jan 2017



from openerp import models, fields, api
#import time_funcs
#from datetime import datetime,tzinfo,timedelta





#------------------------------------------------ Unidecode ---------------------------------------------------

import unicodedata
def strip_accents(s):
   return ''.join(c for c in unicodedata.normalize('NFD', s)
                  if unicodedata.category(c) != 'Mn')





#------------------------------------------------ Appointment ---------------------------------------------------

@api.multi

def update_appointment_go(self, appointment_id, owner_id, x_type):


		rec_set = self.env['oeh.medical.appointment'].browse([
																appointment_id																
															])
		print rec_set




		if x_type == 'consultation':
			ret = rec_set.write({
									'consultation': owner_id,
								})
			#print appointment.consultation
			#print appointment.consultation.id




		elif x_type == 'procedure':
			ret = rec_set.write({
									'procedure': owner_id,
									'state': 'Scheduled',

								})
			#print appointment.procedure
			#print appointment.procedure.id




		elif x_type == 'session':
			ret = rec_set.write({
									'session': owner_id,
								})
			#print appointment.session
			#print appointment.session.id



		elif x_type == 'control':
			ret = rec_set.write({
									'control': owner_id,
								})
			#print appointment.control
			#print appointment.control.id


		else:
			print 
			print 'This should not happen !!!'
			print 



		print ret 



		return ret





#------------------------------------------------ Test ---------------------------------------------------


def test_name(self, token):
		
	#print 
	#print 'on change name'
	#print 


	if token != False:

		nr_words = len(token.split())


		if nr_words == 1:
			return {
					'warning': {
						'title': "Error: Apellido incompleto: ",
						'message': token,
					}}




def test_for_digits(self, token):
		
	#print 
	#print 'test for digits'
	#print 

	if token and (not token.isdigit()):
		return {
				'warning': {
					'title': "Error: Debe ser número.",
					'message': token,
				}}
	else:
		return 0



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



