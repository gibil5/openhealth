# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------------------------------------------------------#
#  																															  	#
# ----------------------------------------------------------- Order line -------------------------------------------------------#
#																																#
# ------------------------------------------------------------------------------------------------------------------------------#


from openerp import models, fields, api

import math
import jxvars



class sale_order_line(models.Model):

	#_name = 'openhealth.order_line'
	_inherit='sale.order.line'


	#_inherit='sale.order.line, openhealth.line'
	#_inherit=['sale.order.line','openhealth.line']




	order_id=fields.Many2one(
		'sale.order',
		string='Order',
		)




# Line 

#class line(models.Model):
	#_name = 'openhealth.line'


	consultation = fields.Many2one('openhealth.consultation',
			ondelete='cascade', 
		)

	procedure_created = fields.Boolean(
			default=False,
		)




	_state_list = [
        			('pre-draft', 'Pre-Quotation'),

        			('draft', 'Quotation'),
        			('sent', 'Quotation Sent'),
        			('sale', 'Sale Order'),
        			('done', 'Done'),
        			('cancel', 'Cancelled'),
        		]

	state = fields.Selection(
				selection = _state_list, 
				
				string="State",

				)







	x_price_vip = fields.Float(
			string="Price Vip",
		)

	x_price_vip_wigv = fields.Float(
			string="Precio Vip",

			compute="_compute_x_price_vip_wigv",
		)

	#@api.multi
	@api.depends('x_price_vip')
	
	def _compute_x_price_vip_wigv(self):
		for record in self:

			if record.x_price_vip == 0.0:
				#record.x_price_vip = record.x_price
				price_vip = record.x_price
			else:
				price_vip = record.x_price_vip


			#record.x_price_vip_wigv = math.ceil(record.x_price_vip * 1.18)
			record.x_price_vip_wigv = math.ceil(price_vip * 1.18)




	x_price = fields.Float(
			string="Price Std",
		)

	x_price_wigv = fields.Float(
			string="Precio",

			compute="_compute_x_price_wigv",
		)


	#@api.multi
	@api.depends('x_price')
	
	def _compute_x_price_wigv(self):
		for record in self:
			record.x_price_wigv = math.ceil(record.x_price * 1.18)







	price_total = fields.Float(
			
			string="Total",

			#compute="_compute_price_total",
		)

	#@api.multi
	#@api.depends('x_price')	
	#def _compute_price_total(self):
	#	for record in self:
	#		record.x_price_wigv = math.ceil(record.x_price * 1.18)



	#@api.onchange('price_total')
	
	#def _onchange_price_total(self):
	#	print 
	#	print 'on change price total'
	#	print self.price_total

	#	self.price_total = math.ceil(self.price_total)

	#	print self.price_total
	#	print 





	_x_type_list = [
						('service','Servicio'), 
						('consu','Producto'), 
					]


	x_type = fields.Selection(
			selection = _x_type_list, 

			string="Tipo",			
			compute='_compute_x_type', 			
			)
	
	#@api.multi
	@api.depends('product_id')

	def _compute_x_type(self):
		for record in self:
			record.x_type = record.product_id.type


#sale_order_line()
