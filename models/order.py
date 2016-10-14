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
		string='Order',
		)



	consultation = fields.Many2one('openhealth.consultation',
			ondelete='cascade', 
	)
	
	
	#products = fields.One2many(
	#products = fields.Many2one(
	#		'product.template',
	#		)
			
			
	
	
	x_nex = fields.Char(
		default='nex',
	)
	
	
	
	
	# Button
	@api.multi 
	def x_create_order_lines(self):
		print 
		print 'Mark'
		
		order_id = self.id


		#prod_array = [3480, 3527, 3510]		
		#for prod_id in prod_array:

		for service_laser in self.consultation.service_co2_ids:
			prod_id = service_laser.service.id			
			ol = self.order_line.create({
										'product_id': prod_id,
										'order_id': order_id,
										'name': '',
										#'product_uom' : what.product_id.uom_id.id
									})
			
		for service_laser in self.consultation.service_excilite_ids:
			prod_id = service_laser.service.id			
			ol = self.order_line.create({
										'product_id': prod_id,
										'order_id': order_id,
										'name': '',
										#'product_uom' : what.product_id.uom_id.id
										
									})

		for service_laser in self.consultation.service_ipl_ids:
			prod_id = service_laser.service.id			
			ol = self.order_line.create({
										'product_id': prod_id,
										'order_id': order_id,
										'name': '',
										#'product_uom' : what.product_id.uom_id.id

									})

		for service_laser in self.consultation.service_ndyag_ids:
			prod_id = service_laser.service.id			
			ol = self.order_line.create({
										'product_id': prod_id,
										'order_id': order_id,
										'name': '',
										#'product_uom' : what.product_id.uom_id.id
									})


		print

	
	
#sale_order()


class sale_order_line(models.Model):

	_inherit='sale.order.line'

	order_id=fields.Many2one('sale.order',
		string='Order',
		)

	
	
	x_mark = fields.Char(
		default='mark',
	)

	consultation = fields.Many2one('openhealth.consultation',
			ondelete='cascade', 
	)


	#product_id = fields.Many2one(
	#	'product.product',
	#	'order_line',
	#	domain = [
	#				('type', '=', 'service'),
	#				('x_treatment', '=', 'laser_co2'),
	#			],

	#	)







#sale_order_line()