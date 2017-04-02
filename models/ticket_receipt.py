# -*- coding: utf-8 -*-
#
# 	ticket_receipt 
# 
#

from openerp import models, fields, api



class TicketReceipt(models.Model):
	
	_name = 'openhealth.ticket_receipt'

	#_inherit='openhealth.sale_document'
	_inherit='openhealth.sale_proof'




	name = fields.Char(
			string="Ticket Boleta #", 
			required=True, 
			compute='_compute_name', 
			)

	#@api.depends()
	@api.multi

	def _compute_name(self):
		for record in self:
			record.name = 'TB-' + str(record.id) 
