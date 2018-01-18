# -*- coding: utf-8 -*-


from openerp import models, fields, api




class AccountInvoiceLine(models.Model):
	_inherit = "account.invoice.line"
	_description = "Invoice Line"
	_order = "invoice_id,sequence,id"




	quantity = fields.Float(
			string='Quantity', 


			#digits=dp.get_precision('Product Unit of Measure'),
			digits=(16, 0), 


			required=True, 
			default=1, 
		)



	#@api.multi
	#def _get_analytic_line(self):
	#	ref = self.invoice_id.number
	#	return {
	#		'name': self.name,
	#		'date': self.invoice_id.date_invoice,
	#		'account_id': self.account_analytic_id.id,
	#		'unit_amount': self.quantity,
	#		'amount': self.price_subtotal_signed,
	#		'product_id': self.product_id.id,
	#		'product_uom_id': self.uom_id.id,
	#		'general_account_id': self.account_id.id,
	#		'ref': ref,
	#	}


