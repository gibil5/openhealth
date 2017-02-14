# -*- coding: utf-8 -*-
#
# 	ticket_invoice 
# 
#

from openerp import models, fields, api



class TicketInvoice(models.Model):
	
	_name = 'openhealth.ticket_invoice'

	_inherit='openhealth.sale_document'



	name = fields.Char(
			string="Ticket Factura #", 
			required=True, 
			compute='_compute_name', 
			)

	#@api.depends()
	@api.multi

	def _compute_name(self):
		for record in self:
			record.name = 'TF-' + str(record.id) 
