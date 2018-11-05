# 5 Nov 2018


# ----------------------------------------------------------- Test - Fields ------------------------------------------------------

	#x_test = fields.Boolean(
	#		'Test', 
	#	)

	#x_test_case = fields.Char(
	#		'Test Case', 
	#	)






# 11 Sep 2018 

# ----------------------------------------------------------- Print - Deprecated ------------------------------------------------------

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







# 23 Aug 2018 

# ----------------------------------------------------------- Function ------------------------------------------------------
	# Function 
	function = fields.Selection(

			[	
				('reception', 	'Plataforma'),
				('cash', 		'Caja'),
				('assistant', 	'Asistente Medico'),
				('physician', 	'Medico'),
				('inventory', 	'Almacen'),
				('hc', 			'Personal'),
				('marketing', 	'Marketing'),
				('accounting', 	'Contabilidad'),
				('manager', 	'Gerente'),
				('lawyer', 		'Abogado'),
			], 
		)


# ----------------------------------------------------------- Pricelist ------------------------------------------------------

	# PPL 
	@api.multi
	def action_ppl_public(self):  

		print 'jx'
		print 'PPL Public'


		pricelist_name = 'Public Pricelist'


		# Pricelist 
		pricelist = self.env['product.pricelist'].search([
																	('name','=', pricelist_name),
															],
														#order='appointment_date desc',
														limit=1,)

		self.property_product_pricelist = pricelist




	# PPL 
	@api.multi
	def action_ppl_vip(self):  

		pricelist_name = 'VIP'


		# Pricelist 
		pricelist = self.env['product.pricelist'].search([
																	('name','=', pricelist_name),
															],
														#order='appointment_date desc',
														limit=1,)

		self.property_product_pricelist = pricelist





# ----------------------------------------------------------- Code ------------------------------------------------------
	
	x_id_code = fields.Char(
			'Nr Historia Médica',
			size=256, 
			readonly=False, 
		)

# ----------------------------------------------------------- QC ------------------------------------------------------

	x_completeness = fields.Integer(
			string="Completeness", 
		)


# ----------------------------------------------------------- Lang ------------------------------------------------------
	
	# Lang 
	@api.model
	def _lang_get(self):
		languages = self.env['res.lang'].search([])
		return [(language.code, language.name) for language in languages]


	lang = fields.Selection(
			_lang_get, 
			'Language',
			help="", 
		)



	#'state_id': fields.many2one("res.country.state", 'State', ondelete='restrict'),
	#'zip': fields.char('Zip', size=24, change_default=True),



	#lang = fields.Selection(
	#	_lang_get, 
	#	'Language',
	#	default='es_ES', 
	#	help="If the selected language is loaded in the system, all documents related to this contact will be printed in this language. If not, it will be English."
	#)



# ----------------------------------------------------------- Pricelist ------------------------------------------------------
	# Pricelist 
	#property_product_pricelist = fields.Many2one(
	#		'product.pricelist',
	#		'Sale Pricelist - jx',
	#		#compute='_compute_ppl', 
	#	)

	#@api.multi
	#@api.depends('x_card')
	#def _compute_ppl(self):
	#	print 'jx'
	#	print 'Compute PPL'
	#	for record in self:
	#		record.property_product_pricelist = False






# ----------------------------------------------------------- Vip ------------------------------------------------------
	@api.multi
	#@api.depends('x_card')
	def _compute_x_vip(self):

			# Pricelist 
			#pricelist = self.env['product.pricelist'].search([
			#															('name','=', pricelist_name),
			#													],
															#order='appointment_date desc',
			#												limit=1,)
			#print pricelist
			#print record.property_product_pricelist
			#record.property_product_pricelist = pricelist
			#print record.property_product_pricelist




# ----------------------------------------------------------- Autofill ------------------------------------------------------
	# Autofill 
	x_autofill = fields.Boolean(
		string="Autofill",
		default=False, 
	)

	@api.onchange('x_autofill')
	def _onchange_x_autofill(self):
		if self.x_autofill == True:
			self.street = 'x'
			self.street2 = 'x'
			self.city = 'x'
			self.country_id = 175
			self.x_dni = 'x'
			self.email = 'x'
			self.phone = 'x'
			for invoice in self.invoice_ids:
				invoice.state = 'draft'



# ----------------------------------------------------------- Remove ------------------------------------------------------
	# Removem
	@api.multi
	def remove_myself(self):  
		self.sale_order_ids.unlink()
		self.invoice_ids.unlink()		
		self.unlink()



# ----------------------------------------------------------- CRUD ------------------------------------------------------

	# Create 
	@api.model
	def create(self,vals):

		print 
		print 'CRUD - Partner - Create'
		#print vals
		#print 
	


		# Here 
		key = 'name'
		if key in vals:


		# Compact Name
		#print vals[key]
		name = vals[key]
		name = name.strip().upper()
		name = " ".join(name.split())			
		vals[key] = name 
		#print vals[key]



		# Put your logic here 
		res = super(Partner, self).create(vals)
		# Put your logic here 



		# Create Patient
		#print 'Create Patient'
		#print name  
		#print res 
		#name = res.name 
		#print name  
		#patient = self.env['oeh.medical.patient'].create({
		#													'name': name, 
		#	})
		#print patient
		#print patient.name 

		return res

	# CRUD - Create 



# Write 
	@api.multi
	def write(self,vals):

		#print 
		#print 'CRUD - Partner - Write'
		#print 
		#print vals
		#print 
		#print 



		#if vals['name'] != False: 
		#	vals['name'] = vals['name'].strip().upper()
		#	print vals['name']


		#Write your logic here
		res = super(Partner, self).write(vals)
		#Write your logic here


		#print self.name 
		#name = self.name
		#self.name = self.name.upper()
		#self.name = name.upper()


		#print self.name 
		#print 

		return res
	# CRUD - Write 


