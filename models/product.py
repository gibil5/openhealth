# -*- coding: utf-8 -*-
#
# 	Product
# 
# Created: 			    Nov 2016
#

from openerp import models, fields, api
from datetime import datetime
from . import prodvars
from . import prod_funcs
from openerp.exceptions import ValidationError


class Product(models.Model):

	#_name = 'openhealth.service'

	_inherit = 'product.template'

	#_order = 'x_name_short'
	_order = 'name'




	#default_code = fields.related('product_variant_ids', 'default_code', type='char', string='Internal Reference'),	
	#_sql_constraints = [
	#						('ref_unique','unique(default_code)', 'reference must be unique!')
	#					]     







# ----------------------------------------------------------- Constraints ------------------------------------------------------

	#@api.constrains('default_code')
	#def _check_something(self):
	#	for record in self:
	#		if record.default_code == '0':
	#			raise ValidationError("Default code not valid: %s" % record.default_code)

			# count 
	#		if record.default_code != False: 
	#			count = self.env['product.template'].search_count([
	#																('default_code', '=', record.default_code),
	#										])
	#			if count > 1: 
	#				raise ValidationError("Default code already exists: %s" % record.default_code)
		# all records passed the test, don't return anything





# ----------------------------------------------------------- Keys ------------------------------------------------------
	
	x_name_short = fields.Char(
		)
	#_sql_constraints = [
	#						('x_name_short_unique','unique(x_name_short)', 'x_name_short must be unique!')
	#					]     




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

			#required=True, 
			required=False, 
			
			change_default=True, 
			domain="[('type','=','normal')]" ,
			help="Select category for the current product"
		)













	# For Tickets 
	x_name_ticket = fields.Char(		
			default="x", 

			compute='_compute_x_name_ticket', 
		)


	@api.multi
	#@api.depends('state')
	
	def _compute_x_name_ticket(self):
		
		#print 'jx'
		#print 'compute x_name_ticket'

		for record in self:
					
			record.x_name_ticket = prod_funcs.get_ticket_name(self, record.x_treatment, record.x_zone, record.x_pathology, record.x_family, record.type, record.x_name_short)
			
			#print record.x_name_ticket






	# Description - For tickets - Deprecated ? 
	description = fields.Text(
			'Description',
			default="x", 
		)
















# ----------------------------------------------------------- Canonical ------------------------------------------------------

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
			required=False, 
		)


	# Price Vip
	x_price_vip = fields.Float(
			required=False, 
		)


	# Price Vip Return 
	x_price_vip_return = fields.Float(
			required=False, 
		)


	x_level = fields.Selection(
			selection=prodvars._level_list,
			required=False, 
		)	



	x_family = fields.Selection(
			selection=prodvars._family_list,
			required=False, 
		)	


	x_treatment = fields.Selection(
			selection=prodvars._treatment_list,
			required=False, 
		)	

	
	x_zone = fields.Selection(
			selection=prodvars._zone_list,
			required=False, 
		)	

	
	x_pathology = fields.Selection(
			selection=prodvars._pathology_list,
			required=False, 
		)


	x_sessions = fields.Char(
			default="",
			required=False, 
		)


	x_time = fields.Char(
			selection=prodvars._time_list,
			required=False, 
		)






	# Deprecated ? 

	# Partner 
	#product_manager_id = fields.Many2one(
	
	#		'openhealth.product.manager',
			
			#string = "Cliente", 	
			#ondelete='cascade', 			
			#required=True, 
			#required=False, 
	#	)



