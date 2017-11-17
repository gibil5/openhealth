# -*- coding: utf-8 -*-


from openerp import models, fields, api
#from datetime import datetime

from . import pat_vars


@api.model
def _lang_get(self):
	languages = self.env['res.lang'].search([])
	return [(language.code, language.name) for language in languages]




class Partner(models.Model):
	
	_inherit = 'res.partner'
	#_inherit = ['res.partner', 'base_multi_image.owner']
	#_inherit = ['res.partner', 'oeh.medical.evaluation', 'base_multi_image.owner']
	#_name = 'openhealth.patient'	#The best solution ? So that impact is minimal ?	- Deprecated




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





	# Email 
	email = fields.Char(

			'Email', 
			required=True, 
		)










	# Commons 
	vspace = fields.Char(
			' ', 
			readonly=True
			)



	x_my_company = fields.Boolean(
			'Mi compañía ?', 
		)



	x_firm = fields.Char(
			"Razón social", 	
		)

	x_ruc = fields.Char(
			"RUC", 	
		)

	x_dni = fields.Char(

			"DNI", 	
		)





	phone = fields.Char(
			
			'Teléfono 1', 
			required=True, 
		)
	
	mobile = fields.Char(
			
			'Teléfono 2', 
		)




	#'state_id': fields.many2one("res.country.state", 'State', ondelete='restrict'),
	#'zip': fields.char('Zip', size=24, change_default=True),

	street = fields.Char(

			'Calle', 
			required=True, 
		)

	street2 = fields.Char(

			'Distrito', 
			placeholder="Distrito...", 
			required=True, 
		)

	city = fields.Char(

			'City', 
			required=True, 
		)

	country_id = fields.Many2one(

			'res.country', 
			'Country', 
			ondelete='restrict', 
			required=True, 
		)





	# Street 2 
	street2_sel = fields.Selection(
			selection = pat_vars._street2_list, 
			string = "Distrito", 	
			
			#required=True, 
			required=False, 
		)














	x_quotation_ids = fields.One2many(

			'openhealth.quotation', 		
		
			'partner_id', 
		
			string="Cotizacion"
		)





	#lang = fields.Selection(
		#_lang_get, 
		#'Language',
		#default='es_ES', 
	#),


	lang = fields.Selection(
		_lang_get, 
		'Language',
		default='es_ES', 
		help="If the selected language is loaded in the system, all documents related to this contact will be printed in this language. If not, it will be English."
	)














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


	# Vip 
	x_vip = fields.Boolean(
		string="Vip",
		default=False, 

		compute='_compute_x_vip', 
	)




	@api.multi
	#@api.depends('x_card')
	def _compute_x_vip(self):
		for record in self:
			x_card = record.env['openhealth.card'].search([
															('patient_name','=', record.name),
														],
														#order='appointment_date desc',
														limit=1,)
			if x_card.name != False:
				record.x_vip = True 





# ----------------------------------------------------------- CRUD ------------------------------------------------------


	@api.model
	def create(self,vals):

		print 
		print 'CRUD - Partner - Create'
		print vals
		#print 
	


		# Here 
		key = 'name'
		if key in vals:
			print vals[key]
			#vals[key] = vals[key].split().upper()		# No - Watch out !
			#vals[key] = vals[key].upper()


			#vals[key] = vals[key].strip().upper()
			#" ".join(sentence.split())			

			name = vals[key]
			name = name.strip().upper()
			name = " ".join(name.split())			
			vals[key] = name 

			
			print vals[key]



		# Put your logic here 
		res = super(Partner, self).create(vals)
		# Put your logic here 


		return res

	# CRUD - Create 






# Write 
	@api.multi
	def write(self,vals):

		print 
		print 'CRUD - Partner - Write'
		print 
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


		print self.name 

		print 


		return res
	# CRUD - Write 



# ----------------------------------------------------------- END ------------------------------------------------------
