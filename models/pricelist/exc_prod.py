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

class ProductTreatmentValueException(Exception):
	pass

# -------------------------------------------------------- Exceptions Treatment ---
#@api.multi
def handle_exceptions_treatment(product, self):
	"""
	Handle Exceptions Treatment
	"""
	print('\n\n')
	print('Handle Exceptions Treatment')

	treatment_arr = exc_vars._treatment_list

	#print(treatment_arr)
	print('Treatment: ' + str(product.pl_treatment))

	# Treatment
	try:
		if product.pl_treatment not in treatment_arr:
			raise ProductTreatmentValueException

	except ProductTreatmentValueException:
		msg = "ERROR: Product Treatment invalid - " + product.name
		print(msg)

		print('Fixing...')

		# Search
		#pl_product = self.env['openhealth.product.pricelist'].search([('name', '=', [product.name]),],)
		pl_product = self.env['openhealth.product.pricelist'].search([('name', '=', [product.name])])
		print(pl_product)
		print(pl_product.name)

		product.pl_treatment = pl_product.treatment

	else:
		print('ok')



# -------------------------------------------------------- Exceptions Family ---
#@api.multi
def handle_exceptions_family(product, self):
	"""
	Handle Exceptions Family
	"""
	print('\n\n')
	print('Handle Exceptions Family')

	family_arr = exc_vars._family_list

	#print(family_arr)
	print('Family: ' + str(product.pl_family))

	# Family
	try:
		if product.pl_family not in family_arr:
			raise ProductFamilyValueException

	except ProductFamilyValueException:
		msg = "ERROR: Product Family invalid - " + product.name
		print(msg)

		print('Fixing...')
		# Search
		#pl_product = self.env['openhealth.product.pricelist'].search([('name', '=', [product.name]),],)
		pl_product = self.env['openhealth.product.pricelist'].search([('name', '=', [product.name])])
		print(pl_product)
		print(pl_product.name)

		product.pl_family = pl_product.family

	else:
		print('ok')



# --------------------------------------------- Handle Exceptions subfamily ----
#@api.multi
def handle_exceptions_subfamily(product, self):
	"""
	Handle Exceptions subfamily
	"""
	print('\n\n')
	print('Handle Exceptions - Subfamily')

	subfamily_arr = exc_vars._subfamily_list
	#print(subfamily_arr)
	#print(self.pl_subfamily)

	# subfamily
	try:
		if product.pl_subfamily not in subfamily_arr:
			raise ProductSubFamilyValueException

	except ProductSubFamilyValueException:
		msg = "ERROR: Product Sub Family invalid - " + product.name
		print(msg)

		print('Fixing...')

		# Search
		pl_product = self.env['openhealth.product.pricelist'].search([('name', '=', [product.name])])
		print(pl_product)
		print(pl_product.name)

		product.pl_subfamily = pl_product.subfamily

	else:
		print('ok')




