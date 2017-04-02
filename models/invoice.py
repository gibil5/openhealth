# -*- coding: utf-8 -*-
#
# 	Invoice 
# 
#

from openerp import models, fields, api


class Invoice(models.Model):
	
	_name = 'openhealth.invoice'

	#_inherit='openhealth.sale_document'
	_inherit='openhealth.sale_proof'




	name = fields.Char(

			string="Factura #", 

			required=True, 

			compute='_compute_name', 
			)


	#@api.depends('',)
	@api.multi

	def _compute_name(self):
		for record in self:
			record.name = 'FA-' + str(record.id) 






	#ruc = fields.Char(
	#		string="RUC", 					
	#		required=True, 
	#	)

