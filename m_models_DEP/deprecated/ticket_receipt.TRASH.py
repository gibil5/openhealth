

# 6 Feb 2018




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

