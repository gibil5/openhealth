# -*- coding: utf-8 -*-
#
# 	Order 
# 
#


from openerp import models, fields, api

import math


class sale_order(models.Model):
	

	#_name = 'openhealth.order'
	_inherit='sale.order'
	




	x_vip = fields.Boolean(
			'Vip', 
			#readonly=True
			)




	_state_list = [
        			#('pre-draft', 'Pre-Quotation'),

        			#('draft', 'Quotation'),
        			#('sent', 'Quotation Sent'),
        			#('sale', 'Sale Order'),
        			#('done', 'Done'),
        			#('cancel', 'Cancelled'),


        			('pre-draft', 	'Presupuesto'),

        			('draft', 		'Presupuesto'),
        			
        			('sent', 		'Presupuesto enviado'),
        			('sale', 		'Facturado'),
        			('done', 		'Completo'),
        			('cancel', 		'Cancelado'),
        		]


	state = fields.Selection(
			selection = _state_list, 


			#string='Status', 			
			string='Estado',	
			
			#readonly=True, 
			readonly=False, 

			#default='draft'

			#copy=False, 
			#index=True, 
			#track_visibility='onchange', 
			)



	vspace = fields.Char(
			' ', 
			readonly=True
			)
	
	
	order_line = field_One2many=fields.One2many(
		'sale.order.line',
		'order_id',

		#string='Order',
		#compute="_compute_order_line",
		)


	#@api.multi
	#@api.depends('x_vip')
	
	#def _compute_order_line(self):
	#	for record in self:
	#		print 'compute_order_line'
	#		print record.x_vip 
	#		ret = record.update_order_lines()
	#		print ret 





	# Indexes 
	consultation = fields.Many2one('openhealth.consultation',
		string="Consulta",
		ondelete='cascade', 
	)


	treatment = fields.Many2one('openextension.treatment',
		ondelete='cascade', 
	)



	
	patient = fields.Many2one(
			'oeh.medical.patient',
	)
	
	
	
	x_state = fields.Char(
		default='a',
	)
	

	#x_copy_created = fields.Boolean(
	#	default=False,
	#)

		

	
	
	
	
	
	
	# Nr lines 
	nr_lines = fields.Integer(
			
			default=0,

			string='Nr líneas',
			
			compute='_compute_nr_lines', 
			#required=True, 
			)

	@api.multi
	#@api.depends('order_line')
	
	def _compute_nr_lines(self):
		for record in self:
			#record.name = 'SE00' + str(record.id) 
			#record.nr_lines = 0
			
			ctr = 0
			for l in record.order_line:
				ctr = ctr + 1
			record.nr_lines = ctr 
			
	
	
	
	
	
	# Order lines 

	@api.multi 
	def clean_order_lines(self):
		
		if self.state == 'draft':
			ret = self.remove_order_lines()







	# On change - Vip 

	#@api.onchange('x_vip')
	
	#def _onchange_x_vip(self):
		#print 'onchange'

		#name = self.name 		
		#order_id = self.env['sale.order'].search([('name', 'like', name)]).id

		#print self.id
		#print self.name
		#print order_id 

		#ret = self.update_order_lines(order_id)
		#print ret 

		#print 




	# Update Lines 
	@api.multi 
	def update_order_lines(self):

		print 
		print 'update_order_lines'

		#ret = self.remove_order_lines()

		ret = self.x_create_order_lines()

		return 1



	# Remove 
	@api.multi 
	def remove_order_lines(self):
		ret = self.order_line.unlink()
		return ret 





	# Create Line 

	@api.multi 
	def create_line(self, order_id, se):
		print 'create line'

		product_id = se.service.id
		name = se.name_short


		# Consultation 
		consultation = self.consultation
		print consultation 
		print consultation.id



		x_price_vip = se.service.x_price_vip
		x_price = se.service.list_price

		#if self.x_vip and se.service.x_price_vip != 0.0:
		if self.x_vip and x_price_vip != 0.0:
			#price_unit = se.service.x_price_vip
			price_unit = x_price_vip
		else:
			#price_unit = se.service.list_price
			price_unit = x_price


		#print product_id
		#print order_id
		#print name
		#print price_unit
		#print se.service.uom_id.id
		#print 



		if self.nr_lines == 0:
			print 'create new'

			ol = self.order_line.create({

										'product_id': product_id,
										
										'order_id': order_id,

										
										'consultation':consultation.id,
										'state':'pre-draft',


										'name': name,

										'price_unit': price_unit,

										'x_price_vip': x_price_vip,
										
										'x_price': x_price,

										'product_uom': se.service.uom_id.id, 
									})

		else:
			print 'update existing'

			order_line_id = self.env['sale.order.line'].search([
																('order_id', 'like', order_id),
																('name', 'like', name),
																]).id
			print order_line_id


			rec_set = self.env['sale.order.line'].browse([
															order_line_id																
														])
			print rec_set 

			#ol = self.order_line.create({
			#ol = self.order_line.write(1, order_line_id, 
			
			ol = rec_set.write({
									#'product_id': product_id,
									#'order_id': order_id,
									#'name': name,
									'price_unit': price_unit,
									#'product_uom': se.service.uom_id.id, 
								})


		return 1




	# Create 
	@api.multi 
	def x_create_order_lines(self):
		print 
		print 'Create order lines'
		
		
		order_id = self.id


		print 
		print 'co2'
		for se in self.consultation.service_co2_ids:
			print se 
			
			ret = self.create_line(order_id, se)



		print 
		print 'excilite'
		for se in self.consultation.service_excilite_ids:
			print se 

			ret = self.create_line(order_id, se)


		
		print 
		print 'ipl'
		for se in self.consultation.service_ipl_ids:
			print se 

			ret = self.create_line(order_id, se)



		print 
		print 'ndyag'
		for se in self.consultation.service_ndyag_ids:
			print se 

			ret = self.create_line(order_id, se)



		print 
		print 'medical'
		for se in self.consultation.service_medical_ids:
			print se 
			#print se.service.id
			#print order_id
			#print se.name_short

			ret = self.create_line(order_id, se)



		print 'out'

		return self.nr_lines

	



	# Total 
	x_price_total = fields.Float(
			string="Total",
			default=5.0,

			compute="_compute_x_price_total",
		)

	x_price_vip_total = fields.Float(
			string="Total Vip",
			default=3.0,

			compute="_compute_x_price_vip_total",
		)

	

	@api.multi
	#@api.depends('x_price')
	
	def _compute_x_price_total(self):
		for record in self:			
			total = 0 

			for line in record.order_line:
				#total = total + line.price_total 
				total = total + line.x_price_wigv 

			record.x_price_total = total 



	@api.multi
	#@api.depends('x_price_vip')
	
	def _compute_x_price_vip_total(self):
		for record in self:			
			total = 0 

			for line in record.order_line:
				total = total + line.x_price_vip_wigv

			record.x_price_vip_total = total 


#sale_order()








# Order line 

class sale_order_line(models.Model):

	#_name = 'openhealth.order_line'
	_inherit='sale.order.line'


	#_inherit='sale.order.line, openhealth.line'
	#_inherit=['sale.order.line','openhealth.line']




	order_id=fields.Many2one(
		'sale.order',
		string='Order',
		)


#sale_order_line()






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






