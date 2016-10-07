	@api.onchange('co2_hands_stains')
	def _onchange_co2_hands_stains(self):
		if self.co2_hands_stains == True:		
			#self.co2_hands_stains = False
			self.co2_hands_scar = False
			self.co2_hands_wart = False
			self.co2_hands_rejuvenation = False

	@api.onchange('co2_hands_scar')
	def _onchange_co2_hands_scar(self):
		if self.co2_hands_scar == True:	
			self.co2_hands_stains = False
			#self.co2_hands_scar = False
			self.co2_hands_wart = False
			self.co2_hands_rejuvenation = False

	@api.onchange('co2_hands_wart')
	def _onchange_co2_hands_wart(self):
		if self.co2_hands_wart == True:		
			self.co2_hands_stains = False
			self.co2_hands_scar = False
			#self.co2_hands_wart = False
			self.co2_hands_rejuvenation = False

	@api.onchange('co2_hands_rejuvenation')
	def _onchange_co2_hands_rejuvenation(self):
		if self.co2_hands_rejuvenation == True:		
			self.co2_hands_stains = False
			self.co2_hands_scar = False
			self.co2_hands_wart = False
			#self.co2_hands_rejuvenation = False







	# Booleans
	
	co2_hands_stains = fields.Boolean(
			string="Manchas", 
			default=False,	
			#compute='_compute_co2_hands_stains', 
			)
	#@api.depends('co2_hands_scar')
	#def _compute_co2_hands_stains(self):
	#	for record in self:
	#		record.hands_stains=True
	
	
	
			
	co2_hands_scar = fields.Boolean(
			string="Cicatriz", 
			default=False,	
			)
	co2_hands_wart = fields.Boolean(
			string="Verruga", 
			default=False,	
			)
	co2_hands_rejuvenation = fields.Boolean(
			string="Rejuvenecimiento", 
			default=False,	
			)





	# On change 

	# Smart 

	#@api.onchange('co2_hands_stains', 'co2_hands_scar', 'co2_hands_wart', 'co2_hands_rejuvenation')
	#@api.onchange('field1', 'field2')
	
	@api.onchange('co2_hands_stains', 'co2_hands_scar')
	def _onchange_co2_hands(self):
		
		print
		print 'jx'
		print
		
		if self.co2_hands_stains == True:		
			#self.co2_hands_stains = False
			self.co2_hands_scar = False
			self.co2_hands_wart = False
			self.co2_hands_rejuvenation = False

		if self.co2_hands_scar == True:	
			self.co2_hands_stains = False
			#self.co2_hands_scar = False
			self.co2_hands_wart = False
			self.co2_hands_rejuvenation = False

		if self.co2_hands_wart == True:		
			self.co2_hands_stains = False
			self.co2_hands_scar = False
			#self.co2_hands_wart = False
			self.co2_hands_rejuvenation = False

		if self.co2_hands_rejuvenation == True:		
			self.co2_hands_stains = False
			self.co2_hands_scar = False
			self.co2_hands_wart = False
			#self.co2_hands_rejuvenation = False

			



	co2_neck_scar = fields.Boolean(
			string="Cuello Cicatriz", 
			default=False,	
			#compute='_compute_co2_neck', 
			)





			
	@api.depends('co2_hands')
	def _compute_co2_neck(self):
		for record in self:
			record.co2_neck=False
			
			
			
			
			
			
			
	
	@api.multi
	def clear_all(self):
	#def clear_all(self,cr,uid,ids,context=None):
		
		
		self.co2_hands = False
		self.co2_cheekbone = False
		self.co2_neck = False
		self.co2_vagina = False
		self.co2_packages = False

		self.co2_neck_scar = False
		
		print
		print self.co2_hands
		print
		
		#print 'jx: Mark'
		#print context 

		return {}
		
					