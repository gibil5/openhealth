# -*- coding: utf-8 -*-
#
# 	Account Line Contasis
# 
# Created: 				19 April 2018
#
#

from openerp import models, fields, api

import datetime

#import resap_funcs



class AccountLineContasis(models.Model):
	
	_name = 'openhealth.account.line.contasis'

	_inherit='openhealth.account.line'

	_order = 'date_time asc'



