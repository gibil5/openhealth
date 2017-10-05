from openerp import models, fields, api
#from datetime import datetime



class Partner(models.Model):
	
	#_name = 'openhealth.patient'	#The best solution ? So that impact is minimal ?	- Deprecated

	_inherit = 'res.partner'







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

				('manager', 		'Gerente'),
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
	# 






	#property_product_pricelist = fields.Property(
	property_product_pricelist = fields.Many2one(
		#type='many2one', 
		relation='product.pricelist', 
		string="Sale Pricelist - jx", 
		help="This pricelist will be used, instead of the default one, for sales to the current partner", 

		compute='_compute_property_product_pricelist', 
	)




	@api.multi
	#@api.depends('x_card')

	def _compute_property_product_pricelist(self):
		for record in self:

			#x_card = record.env['openhealth.card'].search([
			#												('patient_name','=', record.name),
			#											],
														#order='appointment_date desc',
			#											limit=1,)

			#if x_card.name != False:
			#	record.property_product_pricelist = True 


			#record.property_product_pricelist = 'VIP'
			#record.property_product_pricelist = 'VIP' 
			record.property_product_pricelist = False 
	# 



