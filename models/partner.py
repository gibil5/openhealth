# -*- coding: utf-8 -*-


from openerp import models, fields, api
#from datetime import datetime



@api.model
def _lang_get(self):
	languages = self.env['res.lang'].search([])
	return [(language.code, language.name) for language in languages]



class Partner(models.Model):
	

	_inherit = 'res.partner'
	#_inherit = ['res.partner', 'base_multi_image.owner']
	#_inherit = ['res.partner', 'oeh.medical.evaluation', 'base_multi_image.owner']


	#_name = 'openhealth.patient'	#The best solution ? So that impact is minimal ?	- Deprecated





	# Commons 
	vspace = fields.Char(
			' ', 
			readonly=True
			)


	x_firm = fields.Char(
		"Razon social", 	
		)

	x_ruc = fields.Char(
		"Ruc", 	
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




# ----------------------------------------------------------- END ------------------------------------------------------



