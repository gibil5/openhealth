

# 6 Oct 2017




# Extremely Dangerous !!!
# Do not do this. 


	#property_product_pricelist = fields.Many2one(
	#	relation='product.pricelist', 
	#	string="Sale Pricelist", 
	#	help="This pricelist will be used, instead of the default one, for sales to the current partner", 
		#compute='_compute_property_product_pricelist', 
	#)


#	@api.multi
	#@api.depends('x_card')

#	def _compute_property_product_pricelist(self):
#		for record in self:
			#x_card = record.env['openhealth.card'].search([
			#												('patient_name','=', record.name),
			#											],
														#order='appointment_date desc',
			#											limit=1,)

			#if x_card.name != False:
			#	record.property_product_pricelist = True 
			#record.property_product_pricelist = 'VIP'
			#record.property_product_pricelist = 'VIP' 
#			record.property_product_pricelist = False 
# 







	property_product_pricelist = fields.Many2one(
		relation='product.pricelist', 
		string="Sale Pricelist", 
		#help="This pricelist will be used, instead of the default one, for sales to the current partner", 
		
		compute='_compute_property_product_pricelist', 
	)


	@api.multi
	#@api.depends('x_card')

	def _compute_property_product_pricelist(self):

		print 'jx'
		print 'compute pl'

		for record in self:

			x_card = record.env['openhealth.card'].search([
															('patient_name','=', record.name),
														],
														#order='appointment_date desc',
														limit=1,)

			print x_card


			if x_card.name != False:

				pl = record.env['product.pricelist'].search([
																('name','=', 'VIP'),
															],
															#order='appointment_date desc',
															limit=1,)
				record.property_product_pricelist = pl

				print pl  






# 17 Oct 2017

	@api.multi
	def process_name(self, name):  
		arr = name.split(' ')
		second = arr[0] + ' ' + arr[1]
		first = arr[2]
		if len(arr) > 3:
			first = first + ' ' + arr[3]
		second = second.upper()
		first = first.title()
		full = second + ' ' + first
		return full  



# ----------------------------------------------------------- CRUD ------------------------------------------------------

	@api.model
	def create(self,vals):

		print 
		#print 'jx: begin'
		print 'jx'
		print 'Partner - Create - Override'
		print 
		#print vals
		print vals['name']

		#print 'name: ', self.name 
	


		vals['name'] = self.process_name(vals['name'])
		print vals['name']



		# Put your logic here 
		res = super(Partner, self).create(vals)
		# Put your logic here 


		#print 'name: ', self.name 
		print 


		return res

	# CRUD - Create 








# 10 Jan 2018

	#_inherit = ['res.partner', 'base_multi_image.owner']
	#_inherit = ['res.partner', 'oeh.medical.evaluation', 'base_multi_image.owner']
	#_name = 'openhealth.patient'	#The best solution ? So that impact is minimal ?	- Deprecated





# 29 Jan 2018


			#vals[key] = vals[key].split().upper()		# No - Watch out !
			#vals[key] = vals[key].upper()
			#vals[key] = vals[key].strip().upper()
			#" ".join(sentence.split())			




#@api.model
#def _lang_get(self):
#	languages = self.env['res.lang'].search([])
#	return [(language.code, language.name) for language in languages]







# 8 Mar 2018

# ----------------------------------------------------------- Defaults ------------------------------------------------------
	#@api.model
	#def _get_default_team(self):
		#default_team_id = self.env['crm.team']._get_default_team_id()
		#return self.env['crm.team'].browse(default_team_id)

	#@api.model
	#def _get_default_id_code(self):
	#	default_id_code = '55'
	#	return default_id_code




	









# 7 April 2018

	#x_country_name = fields.Char(
	#		readonly=False, 	
			#compute='_compute_x_country_name', 
	#	)


	#@api.multi
	#@api.depends('country_id')
	#def _compute_x_country_name(self):
	#	print 'jx'
	#	print 'Compute Country Name'
	#	for record in self:
	#		record.x_country_name = record.country_id.name 
	#		print record.x_country_name







	#x_country_name = fields.Char(
	#		'Pais', 
	#		required=True, 			
	#		compute='_compute_x_country_name', 
	#	)

	#@api.multi
	#@api.depends('country_id')

	#def _compute_x_country_name(self):
	#	for record in self:
	#		record.x_country_name = 'Peru'






	#@api.multi
	#@api.depends('')
	#def _compute_x_country_name(self):
	#	for record in self:
	#		#cid = record.country_id.id
	#		cid = 175
	#		country = self.env['res.country'].search([
	#													('id', '=', cid),					
	#											],
													#order='write_date desc',
	#												limit=1,
	#											)
	#		record.x_country_name = country.name 








# Geographical 

	#street2 = fields.Char(
	#		'Distrito', 
	#		placeholder="Distrito...", 		
			#required=True, 
	#		required=False, 
	#	)


	#@api.onchange('country_id')
	#def _onchange_country_id(self):
	#	print 
	#	print 'jx'
	#	print 'On change Country id'
	#	print self.country_id
	#	print self.country_id.name 
		#self.x_country_name = self.country_id.name 



	#city = fields.Char(
	#		'City', 
	#		required=False, 
	#	)


	#street = fields.Char(
	#		'Calle', 
	#		required=False, 
	#	)


	#zip = fields.Integer(
	#		string = 'Código',  
	#		required=False, 			
	#	)





# 17 Aug 2018 

	#x_quotation_ids = fields.One2many(
	#		'openhealth.quotation', 		
	#		'partner_id', 
	#		string="Cotizacion"
	#	)


