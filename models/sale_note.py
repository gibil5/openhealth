# -*- coding: utf-8 -*-
#
# 	sale_note 
# 
#

from openerp import models, fields, api



class SaleNote(models.Model):
	
	_name = 'openhealth.sale_note'

	#_inherit='openhealth.sale_document'
	_inherit='openhealth.sale_proof'




	name = fields.Char(
			string="Nota #", 
			required=True, 
			compute='_compute_name', 
			)

	#@api.depends()
	@api.multi

	def _compute_name(self):
		for record in self:
			record.name = 'NO-' + str(record.id) 
