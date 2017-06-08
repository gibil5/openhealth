# -*- coding: utf-8 -*-
#
# 	Sale proof 
# 
#

from openerp import models, fields, api


class SaleProof(models.Model):
	
	_name = 'openhealth.sale_proof'



	# Date created 
	date_created = fields.Datetime(
			string="Fecha", 
			#readonly=True,
			required=True, 
			)





	# Open Order
	@api.multi 
	def open_order(self):
		print 
		print 'Open order'

		ret = self.order.open_myself()

		return ret 
	# open_order



	# Open Payment Method
	@api.multi 
	def open_pm(self):
		print 
		print 'Open Payment method'

		ret = self.payment_method.open_myself()

		return ret 
	# open_order







	payment_method = fields.Many2one('openhealth.payment_method',
			ondelete='cascade', 
			string="Payment method",
			)




	sale_document = fields.Many2one('openhealth.sale_document',
			ondelete='cascade', 
			string="Sale document",
			)


	order = fields.Many2one(
			'sale.order',

			string="Presupuesto",
			
			ondelete='cascade', 
			
			required=True, 
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


