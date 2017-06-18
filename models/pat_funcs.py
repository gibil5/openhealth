# -*- coding: utf-8 -*-
#
# 	*** Pat Funcs
# 
# Created: 				  1 Nov 2016
# Last updated: 	 	 21 Jan 2017

from openerp import models, fields, api

import unicodedata


#------------------------------------------------ Unidecode ---------------------------------------------------
def strip_accents(s):
   return ''.join(c for c in unicodedata.normalize('NFD', s)
                  if unicodedata.category(c) != 'Mn')

# strip_accents


#------------------------------------------------ Tests ---------------------------------------------------

def test_name(self, token):
	if token != False:
		nr_words = len(token.split())
		if nr_words == 1:
			return {
					'warning': {
						'title': "Error: Introduzca los dos Apellidos.",
						'message': token,
					}}
		else:
			return 0
# test_name



def test_for_digits(self, token):
	if token and (not token.isdigit()):
		return {
				'warning': {
					'title': "Error: Debe ser número.",
					'message': token,
				}}
	else:
		return 0
# test_for_digits



def test_for_length(self, token, length):
	if token and (len(str(token))!= length):
		return {
				'warning': {
					'title': "Error: Debe tener " + str(length) + " caracteres.",
					'message': token,
				}}
	else:
		return 0
# test_for_length


