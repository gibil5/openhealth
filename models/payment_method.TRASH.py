

# 18 nov 2017


			return {
					'type': 'ir.actions.act_window',
					'name': ' New Proof Current', 

					'view_type': 'form',
					'view_mode': 'form',	
					'target': 'current',

					'res_model': model,
					'res_id': proof_id,

					'flags': 	{
									#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
									'form': {'action_buttons': True, }
								},

					'context': {
								'default_payment_method': self.id,
								'default_total': self.total,							
								'default_date_created': self.date_created,
								'default_order': self.order.id,
								'default_name': self.saledoc_code,
								'default_partner': self.partner.id,
								'default_my_firm': self.order.x_my_company.x_firm, 
								'default_my_address': self.order.x_my_company.x_address, 
								'default_my_ruc': self.order.x_my_company.x_ruc, 
								'default_my_phone': self.order.x_my_company.phone, 
							}
					}









# 6 Dec 2017

			#return {
			#		'type': 'ir.actions.act_window',
			#		'name': ' New Proof Current', 

			#		'view_type': 'form',
			#		'view_mode': 'form',	
			#		'target': 'current',

			#		'res_model': model,
			#		'res_id': proof_id,

			#		'flags': 	{
									#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
			#						'form': {'action_buttons': True, }
			#					},

			#		'context': {
			#					'default_name': self.saledoc_code,
			#					'default_payment_method': self.id,
			#					'default_order': self.order.id,
			#					'default_partner': self.partner.id,
			#					'default_total': self.total,		
			#					'default_date_created': self.date_created,
			#				}
			#	}







# 11 Jan 2018

	# Serial Number 
	#serial_nr = fields.Char(
	#		string="Nr de Serie", 
	#	)



	# Prefix 
	#prefix = fields.Char(
	#		string="Prefijo", 
	#	)







# 25 Jan 2018
	# Deprecated 
	#@api.onchange('total')	
	#def _onchange_total(self):
	#	print 'jx'
	#	print 'onchange - Total'







# 26 Jan 2018


			#compute='_compute_ruc', 
			#compute='_compute_dni', 
			#compute='_compute_firm', 

	#@api.multi
	#@api.depends('')
	#def _compute_dni(self):
	#	for record in self:
	#		record.dni = record.partner.x_dni



	#@api.multi
	#@api.depends('')
	#def _compute_firm(self):
	#	for record in self:
	#		record.firm  = record.partner.x_firm

	#@api.multi
	#@api.depends('')
	#def _compute_ruc(self):
	#	for record in self:
	#		record.ruc = record.partner.x_ruc











	# On change Dni
	#@api.onchange('dni')
	#def _onchange_dni(self):
	#	print 'jx'
	#	print 'On change - Dni'

	#	if self.dni != False:
	#		print 'gotcha !'
			#print self.partner 
			#print self.partner.name 
			#print self.partner.x_dni
			#self.partner.x_dni = self.dni
			#print self.partner.x_dni
			#self.firm = self.dni  


#partner_id = self.partner.id 
#return {
#'value': {
#	'partner_id': partner_id,
#	'comment': 'I was changed automatically!',
	#'order_lines': [
	#		(1, 13, {'discount': 30, 'quantity': 10}),
	#		(1, 14, {'discount': 15, 'quantity': 34}),
	#   ]
#	}
#}



	# On change Firm
	@api.onchange('firm')
	def _onchange_firm(self):
		print 'jx'
		print 'On change - Firm'

		if self.firm != False:
			print 'gotcha !'
			self.partner.x_firm = self.firm


	# On change Ruc
	@api.onchange('ruc')
	def _onchange_ruc(self):
		print 'jx'
		print 'On change - Ruc'

		if self.ruc != False:
			print 'gotcha !'
			self.partner.x_ruc = self.ruc



