# -*- coding: utf-8 -*-
#
# 	Order 
# 

from openerp import models, fields, api




class sale_order(models.Model):
	
	_inherit='sale.order'
	
	
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
			
			
			
