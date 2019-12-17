# -*- coding: utf-8 -*-
#
# 	Test - Dep
# 

from openerp import models, fields, api



class TestTool(models.Model):
	
	#_inherit='sale.order'
	#_inherit='openhealth.base'
	#_inherit=['openhealth.base', 'sale.order']
	#_inherit = ['openhealth.base', 'oeh.medical.evaluation']
	
	_name = 'openhealth.test'


	# Name 
	name = fields.Char(
			default='SE',
			string='Test #',
			required=True, 

			#compute='_compute_name', 
		)

	#@api.multi
	#def _compute_name(self):
	#	for record in self:
	#		record.name = 'SE00' + str(record.id)
			