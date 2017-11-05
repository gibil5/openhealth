# -*- coding: utf-8 -*-


from openerp import models, fields, api





class Quotation(models.Model):
	
	#_inherit = 'res.partner'
	_name = 'openhealth.quotation'	



	# Commons 
	vspace = fields.Char(
			' ', 
			readonly=True
			)





	name = fields.Char(
		'Cotización'
	)




	# Partner 
	partner_id = fields.Many2one(

			'res.partner',
		
			#string = "Cliente", 	
		)

