# -*- coding: utf-8 -*-

#from openerp import models, fields, api


#------------------------------------------------ Patient - Test content --------------------------
# Name
def test_for_one_last_name(self, last_name):
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
