# -*- coding: utf-8 -*-
"""
	Pat funcs
"""
import datetime

#--------------------------------------------------------------- compute age ---
#def compute_age_from_dates(patient_dob, patient_deceased, patient_dod):
def compute_age_from_dates(patient_dob, patient_deceased=False, patient_dod=''):
	"""
	Computes age
	"""
	now = datetime.datetime.now()

	if patient_dob:
	    dob = datetime.datetime.strptime(patient_dob, '%Y-%m-%d')

	    if patient_deceased:
	        dod = datetime.datetime.strptime(patient_dod, '%Y-%m-%d')
	        delta = dod - dob
	        deceased = " (deceased)"
	        years_months_days = str(delta.days // 365)+" years "+ str(delta.days%365)+" days" + deceased
	    else:
	        delta = now - dob
	        years_months_days = str(delta.days // 365)+" years "+ str(delta.days%365)+" days"

	else:
	    years_months_days = "No DoB !"

	return years_months_days


#------------------------------------------------ Patient - Test content --------------------------
# Name
#def test_for_one_last_name(self, last_name):
def test_for_one_last_name(last_name):
	"""
	Test for one last name
	"""
	if last_name != False:
		nr_words = len(last_name.split())
		if nr_words == 1:
			return {
					'warning': {
						'title': "Error: Introduzca los dos Apellidos.",
						'message': last_name,
					}}
		else:
			return 0
# test_for_one_name

#------------------------------------------------ Patient - Unidecode -----------------------------
def remove_whitespaces(foox):
	"""
	Remove extra white spaces
	"""
	#print
	#print 'Remove Whitespaces'
	return " ".join(foox.split())
