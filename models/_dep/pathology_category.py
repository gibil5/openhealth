# -*- coding: utf-8 -*-
#
# 	Pathology Category
# 
# Created: 				26 Dec 2016
# Last updated: 	 	id.

from openerp import models, fields, api



class PathologyCategory(models.Model):

	#_inherit = 'openhealth.base', 

	_name = 'openhealth.pathology_category'



	# Name 
	name = fields.Char(
		)
