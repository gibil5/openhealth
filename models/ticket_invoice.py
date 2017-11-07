# -*- coding: utf-8 -*-
#
# 	ticket_invoice 
# 
#
from openerp import models, fields, api

class TicketInvoice(models.Model):
	
	_name = 'openhealth.ticket_invoice'

	_inherit='openhealth.sale_proof'



	name = fields.Char(
			string="Ticket Factura #", 
		)


	family = fields.Selection(
			default='ticket_invoice', 
		)



	# ----------------------------------------------------------- CRUD ------------------------------------------------------

 	# Create 
	@api.model
	def create(self,vals):

		#print 
		#print 'Create Override'
		#print 
		#print vals
		#print 
	
		counter = self.env['openhealth.counter'].search([('name', '=', 'ticket_invoice')])		
		counter.increase()


		#Write your logic here
		res = super(TicketInvoice, self).create(vals)
		#Write your logic here

		return res

		