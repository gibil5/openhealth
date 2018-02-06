# -*- coding: utf-8 -*-
#
# 	ticket_invoice 
# 
#

from openerp import models, fields, api

class TicketInvoice(models.Model):
	
	_inherit='openhealth.sale_proof'

	_name = 'openhealth.ticket_invoice'




# ----------------------------------------------------------- Defaults ------------------------------------------------------

	@api.model
	def _get_default_serial_nr(self):

		print 'jx'
		print 'Get Default Serial Number'


		name = 'ticket_invoice'


		#counter = self.env['openhealth.counter'].search([('name', '=', serial_nr)])
 		counter = self.env['openhealth.counter'].search([
																('name', '=', name), 
															],
																#order='write_date desc',
																limit=1,
															)

 		#print counter 
 		
		default_serial_nr = '13'


		if counter.total != False: 
			default_serial_nr = counter.total
			counter.increase()



		#print default_serial_nr
		
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





	# ----------------------------------------------------------- CRUD ------------------------------------------------------

 	# Create 
	@api.model
	def create(self,vals):

		#print 
		#print 'Create Ticket Invoice'
		#print 
		#print vals
		#print 
	


		# Counter - Deprecated
		#counter = self.env['openhealth.counter'].search([('name', '=', 'ticket_invoice')])		
		#vals['serial_nr'] = counter.total
		#counter.increase()



		#Write your logic here
		res = super(TicketInvoice, self).create(vals)
		#Write your logic here

		return res

		