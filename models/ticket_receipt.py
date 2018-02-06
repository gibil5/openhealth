# -*- coding: utf-8 -*-
#
# 	ticket_receipt 
# 
from openerp import models, fields, api

class TicketReceipt(models.Model):
	
	_name = 'openhealth.ticket_receipt'

	_inherit='openhealth.sale_proof'



	# ----------------------------------------------------------- Defaults ------------------------------------------------------
	@api.model
	def _get_default_serial_nr(self):

		print 'jx'
		print 'Get Default Serial Number - Ticket Receipt'

		name = 'ticket_receipt'
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
	



		# Counter - Deprecated 
		#counter = self.env['openhealth.counter'].search([('name', '=', 'ticket_receipt')])	
		#vals['serial_nr'] = counter.total
		#counter.increase()



		#Write your logic here
		res = super(TicketReceipt, self).create(vals)
		#Write your logic here


		return res

