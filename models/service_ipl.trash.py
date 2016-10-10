	#rosacea = fields.Selection(
	#		selection = ipl._rosacea_list, 
	#		string="Rosácea", 
	#		default='',	
	#		)
			
	#stains = fields.Selection(
	#		selection = ipl._stains_list, 
	#		string="Manchas", 
	#		default='',	
	#		)


	#@api.onchange('rosacea')
	#def _onchange_rosacea(self):
	
	#	if self.rosacea != 'none':	
	#		self.rosacea = self.clear_all(self.rosacea)

	#		self.zone = self.rosacea
	#		self.pathology = 'rosacea'
			
	#		return {
	#			'domain': {'service': [('x_treatment', '=', 'laser_ipl'),('x_zone', '=', self.zone),('x_pathology', '=', self.pathology)]},
	#		}
			
			
	#@api.onchange('stains')
	#def _onchange_stains(self):
	
	#	if self.stains != 'none':	
	#		self.stains = self.clear_all(self.stains)

	#		self.zone = self.stains
	#		self.pathology = 'alopecia'
			
	#		return {
	#			'domain': {'service': [('x_treatment', '=', 'laser_ipl'),('x_zone', '=', self.zone),('x_pathology', '=', self.pathology)]},
	#		}
	
	
	
	#@api.onchange('time_pat')
	#def _onchange_time_pat(self):
	
		
	#	if self.time_pat != 'none':	
			#self.time_pat = self.clear_all(self.time_pat)

	#		self.time = self.time_pat
			
	#		return {
	#			'domain': {'service': [('x_treatment', '=', 'laser_ipl'),('x_zone', '=', self.zone),('x_pathology', '=', self.pathology),('x_time', '=', self.time)]},
	#		}
	
	
	
	
	
	@api.onchange('time_1')
	def _onchange_time_1(self):
	
		if self.time_1 != 'none':	
			#self.time_1 = self.clear_all(self.time_1)

			self.time = self.time_1
			
			return {
				'domain': {'service': [('x_treatment', '=', self.laser),('x_zone', '=', self.zone),('x_pathology', '=', self.pathology),('x_time', '=', self.time)]},
			}

			
			
	@api.onchange('time_2')
	def _onchange_time_2(self):
	
		if self.time_2 != 'none':	
			#self.time_2 = self.clear_all(self.time_2)

			self.time = self.time_2
			
			return {
				'domain': {'service': [('x_treatment', '=', self.laser),('x_zone', '=', self.zone),('x_pathology', '=', self.pathology),('x_time', '=', self.time)]},
			}
			
			
	@api.onchange('time_3')
	def _onchange_time_3(self):
	
		if self.time_3 != 'none':	
			#self.time_3 = self.clear_all(self.time_3)

			self.time = self.time_3
			
			return {
				'domain': {'service': [('x_treatment', '=', self.laser),('x_zone', '=', self.zone),('x_pathology', '=', self.pathology),('x_time', '=', self.time)]},
			}
			
	
	
	
	
	client_type_2 = fields.Selection(
			selection = ipl._ctype_list, 
			string="Tipo de cliente", 
			default='none',	
			)
	client_type_3 = fields.Selection(
			selection = ipl._ctype_list, 
			string="Tipo de cliente", 
			default='none',	
			)
			
			
	@api.onchange('client_type_2')
	def _onchange_client_type_2(self):
	
		if self.client_type_2 != 'none':	
			#self.client_type_2 = self.clear_all(self.client_type_2)

			self.client_type = self.client_type_2
			
			return {
				'domain': {'service': [('x_treatment', '=', self.laser),('x_zone', '=', self.zone),('x_pathology', '=', self.pathology),('x_time', '=', self.time),('x_client_type', '=', self.client_type) ]},
			}
	
	@api.onchange('client_type_3')
	def _onchange_client_type_3(self):
	
		if self.client_type_3 != 'none':	
			#self.client_type_3 = self.clear_all(self.client_type_3)

			self.client_type = self.client_type_3
			
			return {
				'domain': {'service': [('x_treatment', '=', self.laser),('x_zone', '=', self.zone),('x_pathology', '=', self.pathology),('x_time', '=', self.time),('x_client_type', '=', self.client_type) ]},
			}
	
	
	
	