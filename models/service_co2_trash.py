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
