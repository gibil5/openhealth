

# 6 Feb 2018


	# ----------------------------------------------------------- CRUD ------------------------------------------------------

 	# Create 
	@api.model
	def create(self,vals):

		#print 
		#print 'Create Override'
		#print 
		#print vals
		#print 
	

		# Counter - Deprecated 
		#counter = self.env['openhealth.counter'].search([('name', '=', 'advertisement')])		
		#vals['serial_nr'] = counter.total
		#counter.increase()



		#Write your logic here
		res = super(Advertisement, self).create(vals)
		#Write your logic here

		return res

