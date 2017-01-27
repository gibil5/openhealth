






	@api.onchange('med_hya')
	def _onchange_med_hya(self):
		
		if self.med_hya != 'none':
			print 
			print 'med_hya'
			print 

			self.med_hya = self.clear_all_med(self.med_hya)
			#self.clear_local()


			#self.family = 'medical'
			self.treatment = 'hyaluronic_acid'

			return {
				'domain': {'service': [
										#('x_family', '=', self.family),
										('x_treatment', '=', self.treatment),
										]},
			}


	@api.onchange('med_scle')
	def _onchange_med_scle(self):
		
		if self.med_scle != 'none':
			print 
			print 'med_scle'
			print 

			self.med_scle = self.clear_all_med(self.med_scle)


			#self.family = 'medical'
			self.treatment = 'sclerotherapy'

			return {
				'domain': {'service': [
										#('x_family', '=', self.family),
										('x_treatment', '=', self.treatment),
										]},
			}






	@api.onchange('med_lep')
	def _onchange_med_lep(self):
		
		if self.med_lep != 'none':
			print 
			print 'med_lep'
			print 

			self.med_lep = self.clear_all_med(self.med_lep)

			#self.family = 'medical'
			self.treatment = 'lepismatic'

			return {
				'domain': {'service': [
										#('x_family', '=', self.family),
										('x_treatment', '=', self.treatment),
										]},
			}

	@api.onchange('med_pla')
	def _onchange_med_pla(self):
		
		if self.med_pla != 'none':
			print 
			print 'med_pla'
			print 

			self.med_pla = self.clear_all_med(self.med_pla)

			#self.family = 'medical'
			self.treatment = 'plasma'

			return {
				'domain': {'service': [
										#('x_family', '=', self.family),
										('x_treatment', '=', self.treatment),
										]},
			}

	@api.onchange('med_bot')
	def _onchange_med_bot(self):
		
		if self.med_bot != 'none':
			print 
			print 'med_bot'
			print 

			self.med_bot = self.clear_all_med(self.med_bot)

			#self.family = 'medical'
			self.treatment = 'botulinum_toxin'

			return {
				'domain': {'service': [
										#('x_family', '=', self.family),
										('x_treatment', '=', self.treatment),
										]},
			}



	@api.onchange('med_int')
	def _onchange_med_int(self):
		
		if self.med_int != 'none':
			print 
			print 'med_int'
			print 


			self.med_int = self.clear_all_med(self.med_int)

			#self.family = 'medical'
			self.treatment = 'intravenous_vitamin'

			return {
				'domain': {'service': [
										#('x_family', '=', self.family),
										('x_treatment', '=', self.treatment),
										]},
			}




