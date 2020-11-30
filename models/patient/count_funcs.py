# -*- coding: utf-8 -*-
"""
	Count funcs
	Created: 			29 nov 2020
	Last up: 			29 nov 2020
"""
# ----------------------------------------------------------- Count Funcs ------
#def get_name(self, prefix, separator, padding, value):
def get_name(prefix, separator, padding, value):
	"""
	Get name - used by patient
	"""
	if separator != False:
		name = prefix  +  separator  +  str(value).zfill(padding)
	else:
		name = prefix  +  str(value).zfill(padding)
	return name
