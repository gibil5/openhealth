# -*- coding: utf-8 -*-
#
# 	Advertisement 
# 
#

from openerp import models, fields, api



class advertisement(models.Model):
	
	_name = 'openhealth.advertisement'

	_inherit='openhealth.sale_document'



	name = fields.Char(
			string="Canje #", 
			required=True, 
			compute='_compute_name', 
			)

	#@api.depends()
	@api.multi

	def _compute_name(self):
		for record in self:
			record.name = 'CA-' + str(record.id) 
