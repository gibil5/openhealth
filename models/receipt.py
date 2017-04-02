# -*- coding: utf-8 -*-
#
# 	Receipt 
# 
#

from openerp import models, fields, api



class Receipt(models.Model):
	
	_name = 'openhealth.receipt'

	#_inherit='openhealth.sale_document'
	_inherit='openhealth.sale_proof'




	name = fields.Char(
			string="Boleta #", 
			required=True, 
			compute='_compute_name', 
			)

	#@api.depends()
	@api.multi

	def _compute_name(self):
		for record in self:
			record.name = 'BO-' + str(record.id) 


