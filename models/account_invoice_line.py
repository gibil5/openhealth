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

