

# 8 May 2018



# ----------------------------------------------------------- CRUD ------------------------------------------------------

	@api.model
	def create(self,vals):
		
		consultation_id = self.id
		appointment_id = vals['appointment']

		#print 
		#print 'jx'
		#print 'Create Consultation - Override - CRUD'
		#print 
		#print vals
		#print 
		#print 'consultation_id: ', consultation_id
		#print 'appointment_id: ', appointment_id
		#print 


		# Return 
		res = super(Consultation, self).create(vals)

		return res
	# create - CRUD 

