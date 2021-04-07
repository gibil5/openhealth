# -*- coding: utf-8 -*-

from __future__ import print_function
from openerp import _
from openerp.exceptions import Warning as UserError

from . import exc_vars

# ----------------------------------------------------------- Exceptions -------------------------
class ProductFamilyValueException(Exception):
    pass

class ProductSubFamilyValueException(Exception):
    pass


# ----------------------------------------------------------- Handle Exceptions -------------------------
#@api.multi
def fix_exceptions(self):
	"""
	Fix Exceptions
	"""
	print()
	print('PROD - Fix Exceptions')

	_dic = {

		# Medical
		'VICTAMINA C ENDOVENOSA':	'vitamin_c_intravenous', 
		'CRIOCIRUGIA':	'cryosurgery',
		'ESCLEROTERAPIA': 'sclerotherapy',
		'PLASMA': 'plasma',
		'BOTOX': 'botox', 
		'REDUX': 'redux',
		'ACIDO HIALURONICO': 'hyaluronic_acid',
		'MESOTERAPIA NCTF': 'mesotherapy',
		'INFILTRACIONES': 'infiltrations', 

		# Cosmetology
		'PUNTA DE DIAMANTES': 'diamond_tip', 
		'CARBOXITERAPIA': 'carboxytherapy', 
		'LASER TRIACTIVE + CARBOXITERAPIA': 'laser_triactive_carboxytherapy',

	}

	# Fix
	if self.pl_treatment in _dic:
		self.pl_subfamily = _dic[self.pl_treatment]



# ----------------------------------------------------------- Handle Exceptions -------------------------
#@api.multi
def handle_exceptions(self):
	"""
	Handle Exceptions
	"""
	print()
	print('PROD - Handle Exceptions')

	self.init_configurator()


	if self.configurator.error_validation_product:
		print('Error validation ACTIVE')

		handle_exceptions_family(self)

		handle_exceptions_subfamily(self)


	else:
		print('Error validation INACTIVE')



# ----------------------------------------------------------- Handle Exceptions Family -------------------------
#@api.multi
def handle_exceptions_family(self):
	"""
	Handle Exceptions Family
	"""
	#print()
	#print('PROD - Handle Exceptions - Family')

	family_arr = exc_vars._family_list
	#print(family_arr)
	#print(self.pl_family)

	# Family
	try:
		if self.pl_family not in family_arr:
			msg = "ERROR: Producto Familia Incorrecta"
			raise ProductFamilyValueException

	except ProductFamilyValueException:
		class_name = type(self).__name__
		obj_name = self.name
		msg =  msg + '\n' + class_name + '\n' + obj_name

		raise UserError(_(msg))



# ----------------------------------------------------------- Handle Exceptions subfamily -------------------------
#@api.multi
def handle_exceptions_subfamily(self):
	"""
	Handle Exceptions subfamily
	"""
	#print()
	#print('PROD - Handle Exceptions - Subfamily')

	subfamily_arr = exc_vars._subfamily_list
	#print(subfamily_arr)
	#print(self.pl_subfamily)

	# subfamily
	try:
		if self.pl_subfamily not in subfamily_arr:
			msg = "ERROR: Producto Sub Familia Incorrecta"
			raise ProductSubFamilyValueException


	except ProductSubFamilyValueException:
		class_name = type(self).__name__
		obj_name = self.name
		msg =  msg + '\n' + class_name + '\n' + obj_name

		raise UserError(_(msg))



