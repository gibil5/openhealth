# -*- coding: utf-8 -*-
#
# 	*** Product
# 
# Created: 			    Nov 2016
# Last updated: 	 19 Feb 2017

from openerp import models, fields, api

from datetime import datetime
from . import prodvars
from . import prod_funcs


class Product(models.Model):

	#_name = 'openhealth.service'

	_inherit = 'product.template'

	_order = 'x_name_short'

	#_order = 'name'







# ----------------------------------------------------------- Actions ------------------------------------------------------

	# Update 
	@api.multi 
	def update_level(self):

		#print 'jx'
		#print 'Update Product'

		self.x_level = self.x_pathology[-1]

		#print self.x_level




# ----------------------------------------------------------- Primitives ------------------------------------------------------


	categ_id = fields.Many2one(
			'product.category',
			'Internal Category', 
			required=True, 
			change_default=True, 
			domain="[('type','=','normal')]" ,
			help="Select category for the current product"
		)



	# Partner 
	product_manager_id = fields.Many2one(
	
			'openhealth.product.manager',
			
			#string = "Cliente", 	
			#ondelete='cascade', 			
			#required=True, 
			#required=False, 
		)










	# For Tickets 
	x_name_ticket = fields.Char(

			#'x_name_ticket',
		
			default="x", 


			compute='_compute_x_name_ticket', 
		)


	@api.multi
	#@api.depends('state')
	
	def _compute_x_name_ticket(self):
		
		print 'jx'
		print 'compute x_name_ticket'

		for record in self:
		
			print 'jx'
			print record.x_name_ticket
			


			#record.x_name_ticket = record.x_name_short
			#record.x_name_ticket = prod_funcs.get_ticket_name(self, record.x_treatment, record.x_zone, record.x_pathology, record.x_family)
			#record.x_name_ticket = prod_funcs.get_ticket_name(self, record.x_treatment, record.x_zone, record.x_pathology, record.x_family, record.type)
			record.x_name_ticket = prod_funcs.get_ticket_name(self, record.x_treatment, record.x_zone, record.x_pathology, record.x_family, record.type, record.x_name_short)
			

			print record.x_name_ticket









	# Description - For Tickets 
	description = fields.Text(

			'Description',
		
			default="x", 

			#translate=True,
			#help="A precise description of the Product, used only for internal information purposes."

			#compute='_compute_description', 
		)


	#@api.multi
	#@api.depends('state')
	#def _compute_description(self):
	#	print 'jx'
	#	print 'compute description'
	#	for record in self:
	#		print 'jx'
	#		print record.description
	#		record.description = record.x_name_short
	#		print record.description







	# Price Vip
	x_price_vip = fields.Float(
		)



	# Price Vip Return 
	x_price_vip_return = fields.Float(
		)



	# Unit of measure 
	uom = fields.Many2one(
			'product.uom',
			required=False, 
		)


	# Origin
	x_origin = fields.Selection(
		[
			('legacy', 'Legacy'),
			('test', 'Test'), 
			('production', 'Production'),
		],
	)




	# Only Products 
	x_brand = fields.Char(
			string="Marca", 
		)







# ----------------------------------------------------------- Canonical ------------------------------------------------------

	x_level = fields.Selection(
			selection=prodvars._level_list,
		)	



	x_family = fields.Selection(
			selection=prodvars._family_list,
		)	


	x_treatment = fields.Selection(
			selection=prodvars._treatment_list,
		)	

	
	x_zone = fields.Selection(
			selection=prodvars._zone_list,
		)	

	
	x_pathology = fields.Selection(
			selection=prodvars._pathology_list,
		)


	x_sessions = fields.Char(
			default="",
		)


	x_time = fields.Char(
			selection=prodvars._time_list,
		)





	x_name_short = fields.Char(
		)







	# Before 
	x_date_updated = fields.Date(
			)


	x_date_created = fields.Date(

			)




