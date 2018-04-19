# -*- coding: utf-8 -*-
#
# 	Account Line
# 
# Created: 				18 April 2018
#
#

from openerp import models, fields, api

import datetime

#import resap_funcs



class AccountLine(models.Model):
	
	#_inherit='sale.closing'

	_name = 'openhealth.account.line'
	
	_order = 'serial_nr asc'



# ----------------------------------------------------------- Relational ------------------------------------------------------

	account_id = fields.Many2one(

			'openhealth.account.contasis'

		)





# ----------------------------------------------------------- Primitives ------------------------------------------------------

	serial_nr = fields.Char()

	date = fields.Date()

	patient = fields.Many2one(
			'oeh.medical.patient'
		)

	amount = fields.Float()









