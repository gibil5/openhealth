# -*- coding: utf-8 -*-

# Deprecated 

from openerp import models, fields, api
import datetime




# ----------------------------------------------------------- Funcs ------------------------------------------------------

@api.multi
def get_name(self, prefix, separator, padding, value):

	print 
	print 'Get Name'
	print

	
	print prefix, padding, value 



	if separator != False: 
		name = prefix  +  separator  +  str(value).zfill(padding)

	else:
		name = prefix  +  str(value).zfill(padding)

	return name