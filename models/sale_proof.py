# -*- coding: utf-8 -*-
#
# 	Sale proof 
# 
#

from openerp import models, fields, api


class SaleProof(models.Model):
	
	_name = 'openhealth.sale_proof'





	# Open Order
	@api.multi 
	def open_order(self):

		print 
		print 'Open order'


		ret = self.order.open_myself()

		return ret 
	# open_order






	sale_document = fields.Many2one('openhealth.sale_document',
			ondelete='cascade', 
			string="Sale document",
			)


	order = fields.Many2one(
			'sale.order',
			string="Presupuesto",
			ondelete='cascade', 
			#required=True, 
		)





	name = fields.Char(
			#compute='_compute_name', 			
		)
	#def _compute_code(self):
	#	for record in self:
	#		record.name = record.id




	vspace = fields.Char(
			' ', 
			readonly=True
			)

	partner = fields.Many2one(
			'res.partner',
			string = "Cliente", 			
			required=True, 
		)

	total = fields.Float(
			string = 'Total', 
		)


	ruc = fields.Char(
			string="RUC", 	
			#required=True, 
		)


