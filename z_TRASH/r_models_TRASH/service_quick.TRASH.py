

# 4 Jan 2018

	#@api.multi
	#def _compute_patient(self):
	#	print 'jx'
	#	print 'compute patient'
	#	for record in self:
	#		record.patient = record.treatment.patient



# 27 Aug 20a8 

# ----------------------------------------------------------- CRUD ------------------------------------------------------

# Create 
	@api.model
	def create(self,vals):

		print 'jx'
		print 'Service Quick - Create - Override'
		print vals
	
		# My logic 		
		#self.nr_hands_i = 7
		#self.nr_body_local_i = 7
		#self.nr_face_local_i = 7
		#vals['nr_hands_i'] = 7
		#vals['nr_hands_i'] = self.patient.x_nr_quick_hands

		# Put your logic here 
		res = super(ServiceQuick, self).create(vals)
		# Put your logic here 

		return res
	# CRUD - Create 
