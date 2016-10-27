# -*- coding: utf-8 -*-
#
# 	Order 
# 
#


from openerp import models, fields, api


class sale_order(models.Model):
	

	#_name = 'openhealth.order'
	_inherit='sale.order'
	





	state = fields.Selection(
			#selection = _state_list, 
			#string='Status', 			
			
			#readonly=True, 
			readonly=False, 

	#		default='draft'

			#copy=False, 
			#index=True, 
			#track_visibility='onchange', 
			)




	
	vspace = fields.Char(
			' ', 
			readonly=True
			)
	
	
	order_line = field_One2many=fields.One2many('sale.order.line',
		'order_id',
		#string='Order',
		)




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



	# Update Lines 
	@api.multi 
	def update_order_lines(self):

		

		#if self.state == 'draft':
		if self.state == 'draft'  and  self.nr_lines == 0:
			print 
			print 'update_order_lines'
			print 

			#ret = self.remove_order_lines()
			ret = self.x_create_order_lines()
			#print ret  


#jx
			print 'copy'

			ret = self.copy({
				
							#'state':'sale',
							'state':'sent',
				})

			
			print ret 




	



	# Remove 
	@api.multi 
	def remove_order_lines(self):
		ret = self.order_line.unlink()
		return ret 



	# Create 
	@api.multi 
	def x_create_order_lines(self):
		print 
		print 'Create order lines'
		
		
		order_id = self.id


		print 'co2'
		for se in self.consultation.service_co2_ids:
			#print se 

			#print se.service.id
			#print order_id
			#print se.name_short

			ol = self.order_line.create({
										'product_id': se.service.id,
										'order_id': order_id,
										'name': se.name_short,
									})
			

		print 'excilite'
		for se in self.consultation.service_excilite_ids:
			#print se 

			ol = self.order_line.create({
										'product_id': se.service.id,
										'order_id': order_id,
										'name': se.name_short,
									})

		
		print 'ipl'
		for se in self.consultation.service_ipl_ids:
			#print se 

			ol = self.order_line.create({
										'product_id': se.service.id,
										'order_id': order_id,
										'name': se.name_short,
									})

		print 'ndyag'
		for se in self.consultation.service_ndyag_ids:
			#print se 

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


	order_id=fields.Many2one(

		'sale.order',
		#'openhealth.order',

		string='Order',
		)


	consultation = fields.Many2one('openhealth.consultation',
			ondelete='cascade', 
	)

	procedure_created = fields.Boolean(
		default=False,
	)


	#x_mark = fields.Char(
	#	default='mark',
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