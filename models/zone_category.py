# -*- coding: utf-8 -*-
#
# 	Zone 
# 
# Created: 				26 Dec 2016
# Last updated: 	 	id.

from openerp import models, fields, api



class ZoneCategory(models.Model):

	#_inherit = 'openhealth.base', 

	_name = 'openhealth.zone_category'



	# Name 
	name = fields.Char(
		)
