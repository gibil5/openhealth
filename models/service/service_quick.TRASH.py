
# ----------------------------------------------------------- Dep ------------------------------

	# Pathology
	#nex_pathology = fields.Many2one(
	#		'openhealth.pathology',
	#		string="Nex Pathology", 
	#		domain = [
	#					('treatment', '=', 'laser_quick'),
	#				],
	#	)

	# Zone 
	#nex_zone = fields.Many2one(
	#		'openhealth.nexzone',
	#		string="Nex Zone", 
	#		domain = [
	#					('treatment', '=', 'laser_quick'),
	#				],
	#	)




# ----------------------------------------------------------- On Changes - Dep ------------------------------------------------------

	# Service
	@api.onchange('service')
	def _onchange_service(self):
		pass

	@api.onchange('nex_zone')
	def _onchange_nex_zone(self):
		if self.nex_zone != False:	
			self.zone = self.nex_zone.name_short
			return {
						'domain': {		
									'service': 	[
													('x_treatment', '=', 'laser_quick'),
													('x_zone', '=', self.zone),
												], 
									'nex_pathology': [
														(self.nex_zone.name_short, '=', True),
													], 
									},
					}

	@api.onchange('nex_pathology')
	def _onchange_nex_pathology(self):
		if self.nex_pathology != False:	
			self.pathology = self.nex_pathology.name_short
			return {
						'domain': {'service': [
												('x_treatment', '=', 'laser_quick'),
												('x_pathology', '=', self.pathology),
												('x_zone', '=', self.zone)			
										]},
			}



# ----------------------------------------------------------- Test ------------------------------------------------------

	# Test
	def test_computes(self):
		super(ServiceQuick, self).test_computes()

	def test_actions(self):
		super(ServiceQuick, self).test_actions()






# ----------------------------------------------------------- Computes ------------------------------------------------------
	
	# Comeback 
	comeback = fields.Boolean(
			string='Regreso', 
			
			compute='_compute_comeback', 
		)
	@api.multi
	def _compute_comeback(self):
		for record in self:
			zone = record.zone			
			nr = record.get_nr_zones(zone)
			if nr > 0:
				comeback = True
			else:
				comeback = False
			record.comeback = comeback




	# Price Vip Return
	price_vip_return = fields.Float(
			string='Precio Vip Return', 

			compute='_compute_price_vip_return', 
		) 
	#@api.multi
	@api.depends('service')
	def _compute_price_vip_return(self):
		for record in self:
			record.price_vip_return= (record.service.x_price_vip_return)




	
	# Price Applied
	price_applied = fields.Float(
			string='Precio Aplicado', 

			compute='_compute_price_applied', 
		) 

	#@api.multi
	@api.depends('service')
	def _compute_price_applied(self):
		for record in self:
			
			if record.patient.x_vip: 

				if record.comeback 		and 	record.service.x_price_vip_return != 0: 	# Return 
					record.price_applied = record.service.x_price_vip_return
				else:
					#record.price_applied = record.service.x_price_vip
					record.price_applied = -1 								# Std and Vip 
			
			else:
				#record.price_applied = record.service.list_price		# Std 
				record.price_applied = -1 								# Std and Vip 

