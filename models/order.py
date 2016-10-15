# -*- coding: utf-8 -*-
#
# 	Order 
# 

#from openerp import fields,models
from openerp import models, fields, api


class sale_order(models.Model):
	
	_inherit='sale.order'
	
    
	order_line = field_One2many=fields.One2many('sale.order.line',
		'order_id',
		#string='Order',
		)



	consultation = fields.Many2one('openhealth.consultation',
		ondelete='cascade', 
	)
	
	
	#products = fields.One2many(
	#products = fields.Many2one(
	#		'product.template',
	#		)
			
	#x_nex = fields.Char(
	#	default='nex',
	#)
	
	
	
	
	# Nr lines 
	nr_lines = fields.Integer(
			default=0,
			string='Nr líneas',
			
			compute='_compute_nr_lines', 
			#required=True, 
			)

	#@api.multi
	@api.depends('order_line')
	
	def _compute_nr_lines(self):
		for record in self:
			#record.name = 'SE00' + str(record.id) 
			#record.nr_lines = 0
			
			ctr = 0
			for l in record.order_line:
				ctr = ctr + 1
			record.nr_lines = ctr 
			
	
	
	
	
	
	# Methods
	
	@api.multi 
	def remove_order_lines(self):
		ret = self.order_line.unlink()
		return ret 
		
	
	@api.multi 
	def x_create_order_lines(self):
		print 
		print 'Create order lines'
		
		order_id = self.id

		for se in self.consultation.service_co2_ids:
			
			ol = self.order_line.create({
										'product_id': se.service.id,
										'order_id': order_id,
										'name': se.name_short,
									})
			
		for se in self.consultation.service_excilite_ids:

			ol = self.order_line.create({
										'product_id': se.service.id,
										'order_id': order_id,
										'name': se.name_short,
									})

		for se in self.consultation.service_ipl_ids:

			ol = self.order_line.create({
										'product_id': se.service.id,
										'order_id': order_id,
										'name': se.name_short,
									})

		for se in self.consultation.service_ndyag_ids:

			ol = self.order_line.create({
										'product_id': se.service.id,
										'order_id': order_id,
										'name': se.name_short,
									})


		print

		return self.nr_lines

	
	
#sale_order()


class sale_order_line(models.Model):

	_inherit='sale.order.line'

	order_id=fields.Many2one('sale.order',
		string='Order',
		)

	
	#x_mark = fields.Char(
	#	default='mark',
	#)

	#consultation = fields.Many2one('openhealth.consultation',
	#		ondelete='cascade', 
	#)


	#product_id = fields.Many2one(
	#	'product.product',
	#	'order_line',
	#	domain = [
	#				('type', '=', 'service'),
	#				('x_treatment', '=', 'laser_co2'),
	#			],

	#	)

#sale_order_line()