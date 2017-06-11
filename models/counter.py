# -*- coding: utf-8 -*-
#
# 	counter
# 
#

from openerp import models, fields, api

import ord_vars


class counter(models.Model):
	
	_name = 'openhealth.counter'


	name = fields.Char(
			default='receipt', 
		)


	value = fields.Integer(
			default=1, 
		)

	@api.multi 
	def increase(self):
		self.value = self.value + 1


	@api.multi 
	def reset(self):
		self.value = 1

