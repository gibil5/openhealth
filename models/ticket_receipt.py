# -*- coding: utf-8 -*-
#
# 	ticket_receipt 
# 
#
from openerp import models, fields, api

class TicketReceipt(models.Model):
	
	_name = 'openhealth.ticket_receipt'

	_inherit='openhealth.sale_proof'



	name = fields.Char(
			string="Ticket Boleta #", 
		)


	family = fields.Selection(
			default='ticket_receipt', 
		)



	# ----------------------------------------------------------- CRUD ------------------------------------------------------

 	# Create 
	@api.model
	def create(self,vals):

		#print 'jx'
		#print 'Create Ticket Receipt'
		#print 
		#print vals
		#print 
	


		counter = self.env['openhealth.counter'].search([('name', '=', 'ticket_receipt')])	

		vals['serial_nr'] = counter.total

		counter.increase()



		#Write your logic here
		res = super(TicketReceipt, self).create(vals)
		#Write your logic here


		return res

