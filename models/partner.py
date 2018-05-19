# -*- coding: utf-8 -*-
#
#
# 		*** RES PARTNER 
# 
# Created: 				26 Aug 2016
# Last updated: 	 	25 Aug 2017
#
from openerp import models, fields, api
from . import pat_vars
from . import pat_funcs

class Partner(models.Model):
	
	_inherit = 'res.partner'

	_order = 'write_date desc'





# ----------------------------------------------------------- Deprecated ------------------------------------------------------
	#x_quotation_ids = fields.One2many(
	#		'openhealth.quotation', 		
	#		'partner_id', 
	#		string="Cotizacion"
	#	)





# ----------------------------------------------------------- Indexed ------------------------------------------------------
	x_dni = fields.Char(
			"DNI", 	
			index=True, 
			required=False, 
		)
	
	name = fields.Char(
			'Name', 
			select=True,
			index=True, 
		)







# ----------------------------------------------------------- QC ------------------------------------------------------

	x_completeness = fields.Integer(
			string="Completeness", 
		)





# ----------------------------------------------------------- Code ------------------------------------------------------
	
	x_id_code = fields.Char(
			
			#'Patient ID',
			'Nr Historia Médica',
			size=256, 


			#default='55', 
			#default=_get_default_team
			#default=_get_default_id_code, 


			#help='Patient Identifier provided by the Health Center',

			#readonly=True, 
			readonly=False, 
		)





# ----------------------------------------------------------- My Company ------------------------------------------------------


	# Series 
	x_series = fields.Char(
			string='Serie', 
		)



	# Autorization 
	x_authorization = fields.Char(
			string='Autorización', 
		)




	# Warning Sales
	x_warning = fields.Text(
			'Condiciones de Venta', 
		)



	# Warning Purchase 
	x_warning_purchase = fields.Text(
			'Condiciones de Compra', 
		)





# ----------------------------------------------------------- Lang ------------------------------------------------------
	@api.model
	def _lang_get(self):
		languages = self.env['res.lang'].search([])
		return [(language.code, language.name) for language in languages]


	lang = fields.Selection(
			_lang_get, 
			'Language',
			help="", 
		)



# ----------------------------------------------------------- Hard wired ------------------------------------------------------


	# READY 
	phone = fields.Char(
			#'Teléfono 1', 
			'Fijo', 
			#required=True, 
			required=False, 
		)
	
	mobile = fields.Char(
			'Celular', 
		)





	x_firm = fields.Char(
			"Razón social", 	
		)


	x_ruc = fields.Char(
			"RUC", 	
		)



	email = fields.Char(

			string = 'Email',  
			placeholder = '',
			
			#required=True, 
			required=False, 
		)






	# Address
	
	country_id = fields.Many2one(
			'res.country', 
			string = 'País', 
			
			default = 175,	# Peru

			#ondelete='restrict', 			

			required=True, 
		)



	city = fields.Selection(
			selection = pat_vars._city_list, 
			string = 'Departamento',  
			
			default = 'lima', 

			#required=True, 
			required=False, 
		)



	# For patient short card
	city_char = fields.Char(
		
			compute='_compute_city_char', 
		)
	#@api.multi
	@api.depends('city')
	def _compute_city_char(self):
		for record in self:
			record.city_char = record.city








	street2 = fields.Char(
			string = "Distrito 2", 	
			
			#required=True, 
			required=False, 
		)



	street2_sel = fields.Selection(
			selection = pat_vars._street2_list, 
			string = "Distrito", 	
			
			#required=True, 
			required=False, 
		)






	street = fields.Char(
			string = "Dirección", 	

			required=False, 
		)




	zip = fields.Char(
			#'Zip', 
			string = 'Código',  
			size=24, 
			#change_default=True, 
			required=False, 
		)







	# Only for foreign addresses

	x_foreign = fields.Boolean(
			string="Dirección en el extranjero", 
		)

	@api.onchange('x_foreign')
	def _onchange_x_foreign(self):

		print 'jx'
		print 'On change foreign'
		
		if self.x_foreign:
			#self.city = False
			self.city = ""



	x_address_foreign = fields.Text(
			string=".", 
		)









# ----------------------------------------------------------- DNI RUC ------------------------------------------------------



	# Test and validate
	@api.onchange('x_dni')
	def _onchange_x_dni(self):
		ret = pat_funcs.test_for_digits(self, self.x_dni)
		if ret != 0: 
			return ret
		ret = pat_funcs.test_for_length(self, self.x_dni, 8)
		if ret != 0: 
			return ret






	# Test and validate
	@api.onchange('x_ruc')
	def _onchange_x_ruc(self):
		ret = pat_funcs.test_for_digits(self, self.x_ruc)
		if ret != 0: 
			return ret
		
		ret = pat_funcs.test_for_length(self, self.x_ruc, 11)
		if ret != 0: 
			return ret









# ----------------------------------------------------------- On Changes ------------------------------------------------------
	# Name 
	@api.onchange('name')
	def _onchange_name(self):
		print 'jx'
		print 'Change name'
		
		if self.name != False: 
			print self.name
			
			#self.name = self.name.strip().upper()
			name = self.name
			name = name.strip().upper()
			name = " ".join(name.split())			
			self.name = name 

			print self.name
			print 























	# Address
	x_address = fields.Char(

			"Dirección",
			compute='_compute_x_address', 
		)

	@api.multi
	#@api.depends('')
	def _compute_x_address(self):
		for record in self:

			#com = record.order.x_my_company
			if record.street != False and record.street2 != False and record.city != False:


				#record.x_address = record.street + ' - ' + record.street2 + ' - ' + record.city
				#record.x_address = record.street.title() + ' - ' + record.street2.title() + ' - ' + record.city.title()
				record.x_address = record.street.title() + ' ' + record.street2.title() + ' - ' + record.city.title()




























	# Commons 
	vspace = fields.Char(
			' ', 
			readonly=True
			)



	x_my_company = fields.Boolean(
			'Mi compañía ?', 
		)


























	#'state_id': fields.many2one("res.country.state", 'State', ondelete='restrict'),
	#'zip': fields.char('Zip', size=24, change_default=True),















	#lang = fields.Selection(
	#	_lang_get, 
	#	'Language',
	#	default='es_ES', 
	#	help="If the selected language is loaded in the system, all documents related to this contact will be printed in this language. If not, it will be English."
	#)














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







	# Vip 
	x_vip = fields.Boolean(
		string="VIP",
		default=False, 

		compute='_compute_x_vip', 
	)


	@api.multi
	#@api.depends('x_card')
	def _compute_x_vip(self):

		#print 'jx'
		#print 'Compute Partner x Vip'

		for record in self:

			x_card = record.env['openhealth.card'].search([
															('patient_name','=', record.name),
														],
														#order='appointment_date desc',
														limit=1,)
			
			if x_card.name != False:
				record.x_vip = True 
				#pricelist_name = 'VIP'

				record.action_ppl_vip()

			else:
				record.x_vip = False 
				#pricelist_name = 'Public Pricelist'
				
				record.action_ppl_public()



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








# ----------------------------------------------------------- Actions ------------------------------------------------------


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









	# Removem
	@api.multi
	def remove_myself(self):  
		
		#self.street = 'a'
		#self.x_dni = 'a'
		#self.email = 'a'
		#self.phone = 'a'


		self.sale_order_ids.unlink()

		self.invoice_ids.unlink()



		#self.purchase_order_count = 0 

		
		self.unlink()






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

