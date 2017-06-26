# -*- coding: utf-8 -*-
#
# 	Test 
# 

from openerp import models, fields, api




class test(models.Model):
	
	#_inherit='sale.order'
	#_inherit='openhealth.base'
	#_inherit=['openhealth.base', 'sale.order']
	_inherit = ['openhealth.base', 'oeh.medical.evaluation']
	
	_name = 'openhealth.test'



	
	# Name 
	name = fields.Char(
			default='SE',
			string='Test #',
			compute='_compute_name', 
			required=True, 
			)

	@api.multi
	def _compute_name(self):
		for record in self:
			record.name = 'SE00' + str(record.id)
			