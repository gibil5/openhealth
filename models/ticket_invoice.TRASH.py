

# 6 Feb 2018



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
