# -*- coding: utf-8 -*-
#
# 		lib_coeffs.py
# 
# 		Created: 			15 Apr 2019
# 		Last up: 	 		15 Apr 2019
#


#------------------------------------------------ Get Coeff -------------------
# Get Coeff
def get_coeff(state):
	"""
	Used by Electronic Order (electronic.electronic_order)
	Coeff is a function of the state (Credit note or not)
	"""
	#print()
	#print('Get Coeff')

	if state in ['credit_note']:
		coeff = -1

	else:
		coeff = 1

	#print(coeff)
	return coeff