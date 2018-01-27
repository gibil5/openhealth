# -*- coding: utf-8 -*-
#
# 	Zone 
# 
# Created: 				26 Jan 2018
# Last updated: 	 	id.

from openerp import models, fields, api



class Zone(models.Model):

	_name = 'openhealth.zone'



	name = fields.Char(
			string="Nombre", 
		)

	name_short = fields.Char(
			#string="Nombre corto", 
		)


