# -*- coding: utf-8 -*-
#
# 	ticket_invoice 
# 
from openerp import models, fields, api

class TicketInvoice(models.Model):
	
	_name = 'openhealth.ticket_invoice'

	_inherit='openhealth.sale_proof'



	# ----------------------------------------------------------- Defaults ------------------------------------------------------
	@api.model
	def _get_default_serial_nr(self):

		print 'jx'
		print 'Get Default Serial Number - Ticket Invoice'

		name = 'ticket_invoice'
 		counter = self.env['openhealth.counter'].search([
																('name', '=', name), 
															],
																#order='write_date desc',
																limit=1,
															)
		default_serial_nr = '13'

		if counter.total != False: 
			default_serial_nr = counter.total
			counter.increase()

		return default_serial_nr


	# ----------------------------------------------------------- Primitives ------------------------------------------------------

	# Serial Number 
	serial_nr = fields.Char(	
			default=_get_default_serial_nr, 
		)


	
	name = fields.Char(
			string="Ticket Factura #", 
		)


	family = fields.Selection(
			default='ticket_invoice', 
		)


