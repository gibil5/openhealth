# -*- coding: utf-8 -*-
#
# 	*** Product Manager 
# 
# Created: 			    Feb 2018
# Last updated: 	 	Id.

from openerp import models, fields, api



class ProductManager(models.Model):


	_name = 'openhealth.product.manager'

	#_order = 'x_name_short'
	#_order = 'name'




# ----------------------------------------------------------- Actions ------------------------------------------------------

	# Update 
	@api.multi 
	def update_products(self):

		print
		print 'jx'
		print 'Update Products'

		#prods = self.env['product.template'].search(
		#	)

		products = self.env['product.template'].search([
																
																#('x_treatment', '=', self.treatment),
																('x_treatment', '=', 'laser_co2'),
																('x_origin', '=', False),
													
													],
													#order='date desc',
													#limit=1,
												)

		#print products


		for product in products: 
			print product.x_name_ticket 
			print product.x_pathology 


			if product.x_pathology != 'monalisa_touch': 
				product.update_level()


			print product.x_level 
			print 


		print



# ----------------------------------------------------------- Primitives ------------------------------------------------------

	name = fields.Char(
		)


	# Treatment 
	treatment = fields.Selection(
			selection=[
							('laser_quick',		'Quick'), 
							('laser_co2',		'Co2'), 
							('laser_excilite',	'Excilite'), 
							('laser_ipl',		'IPL'), 
							('laser_ndyag',		'NDYAG'), 
				],
			string='Tratamiento', 
		)


	#product_ids = fields.One2many(
	#		'product.template', 
	#		'product_manager_id', 
	#		string="Presupuestos",
	#	)





