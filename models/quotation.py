# -*- coding: utf-8 -*-


from openerp import models, fields, api





class Quotation(models.Model):


	_name = 'openhealth.quotation'	

	#_inherit = 'res.partner'
	#_inherit = ['base_multi_image.owner']	
	_inherit = 'base_multi_image.owner'




	# Commons 
	vspace = fields.Char(
			' ', 
			readonly=True, 
			)





	#image_ids = fields.One2many(
	#		'openhealth.image', 
	#		'control', 
	#		string = "Fotos", 
	#	)








	name = fields.Char(
			'Nombre', 
			required=True, 
		)


	date = fields.Datetime(
			'Fecha',
			required=True, 
		)




	# Partner 
	partner_id = fields.Many2one(

			'res.partner',
		
			#string = "Cliente", 	
		)

