# Part of Odoo. See LICENSE file for full copyright and licensing details.

import time

from openerp import api, fields, models, _
import openerp.addons.decimal_precision as dp
from openerp.exceptions import UserError

class SaleAdvancePaymentInv(models.TransientModel):

	#_name = "sale.advance.payment.inv"

	_inherit='sale.advance.payment.inv'

	_description = "Sales Advance Payment Invoice"




	@api.multi
	def create_invoices(self):

		#jx
		print
		print 'jx - Sales Advance Payment Invoice - Local - Gotcha !'
		print




	@api.multi
	def _create_invoice(self, order, so_line, amount):
		print 'jx - _create_invoice !'



	def _prepare_deposit_product(self):
		print 'jx - _prepare_deposit_product !'

