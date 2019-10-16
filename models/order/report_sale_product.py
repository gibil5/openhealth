# -*- coding: utf-8 -*-
"""
		ReportSaleProduct

 		Created: 			    Nov 2016
		Last up: 	 		 16 Oct 2019
"""

from __future__ import print_function
from openerp import models, fields, api
from openerp.addons.openhealth.models.management import mgt_funcs

class ReportSaleProduct(models.Model):
	"""
	Used as: Venta de Productos por Fecha
	"""
	
	_name = 'openhealth.report.sale.product'
	

# ----------------------------------------------------------- Dep - Test ------------------------------------------------------
	#test_target = fields.Boolean(
	#		string="Test Target", 
	#	)



# ----------------------------------------------------------- Relational ------------------------------------------------------	
	# Order Lines
	order_line_ids = fields.One2many(
			'openhealth.report.order_line', 
			'report_sale_product_id', 
			#string="Estado de cuenta",
		)

	# Item Counter
	item_counter_ids = fields.One2many(
			'openhealth.item.counter', 
			'report_sale_product_id', 
			#string="Estado de cuenta",
		)


# ----------------------------------------------------------- Primitives ------------------------------------------------------

	# Dates
	date_begin = fields.Date(
			string="Fecha Inicio", 
		)

	date_end = fields.Date(
			string="Fecha Fin", 
		)

	several_dates = fields.Boolean(
			'Varias Fechas',
			default=False,
		)



	# Name 
	name = fields.Date(
			string="Fecha", 
			default = fields.Date.today, 
			#readonly=True,
			required=True, 
		)

	vspace = fields.Char(
			' ', 
			readonly=True
		)

	total_qty = fields.Integer(
			string="Cantidad", 
		)

	total = fields.Float(
			string="Total", 
		)






# ----------------------------------------------------------- Create Lines ------------------------------------------------------

	# Create Lines 
	def create_lines(self, orders):  
		#print()
		#print('Create Lines')

		# Loop
		for order in orders: 

			for line in order.order_line: 

				if line.product_id.categ_id.name == 'Cremas':
					
					#print('Create !')

					# Create Order Line 
					ret = self.order_line_ids.create({
															'name': line.name,
															'product_id': line.product_id.id,
															'patient': order.patient.id,
															'price_unit': line.price_unit,
															'product_uom_qty': line.product_uom_qty, 
															'x_date_created': line.create_date,															

															'state': order.state,

															'report_sale_product_id': self.id,
													})



# ----------------------------------------------------------- Actions ------------------------------------------------------

	# Update 
	@api.multi
	def update(self):  
		print()
		print('Report Sale Product - Update')

		# Clean 
		self.order_line_ids.unlink()
		self.item_counter_ids.unlink()


		# Init
		self.date_begin = self.name


		# Orders 
		#orders,count = acc_funcs.get_orders_filter(self, self.name, self.name)				# Sales and Cancelled
		#orders,count = mgt_funcs.get_orders_filter_fast(self, self.name, self.name)			# Only Sales


		if not self.several_dates:
			orders, count = mgt_funcs.get_orders_filter_fast(self, self.date_begin, self.date_begin)

		else:
			orders, count = mgt_funcs.get_orders_filter_fast(self, self.date_begin, self.date_end)



		print(orders)
		print(count)


		# Order lines
		self.create_lines(orders)




		# Item Counter 
		total_qty = 0
		total = 0 
		for order_line in self.order_line_ids: 

			# Init 
			name = order_line.product_id.name
			qty = order_line.product_uom_qty
			subtotal = order_line.price_total 
			total_qty = total_qty + qty
			total = total + subtotal

			#print(name)
			#print(qty)
			#print(subtotal)
			#print()


			# Search 
			prod_ctr = self.env['openhealth.item.counter'].search([
																		('name', '=', name),
																		('report_sale_product_id', '=', self.id),
																	],
																	#order='x_serial_nr asc',
																	limit=1,
																)
			#print prod_ctr


			# Create or update 
			if prod_ctr.name != False: 				
				prod_ctr.increase_qty(qty)
				prod_ctr.increase_total(subtotal)
			else:		# Create 
				ret = self.item_counter_ids.create({
															'name': name,
															'qty': qty, 
															'total': subtotal, 
															'report_sale_product_id': self.id,
													})
				#print ret 


		# Update Descriptors 
		self.total_qty = total_qty
		self.total = total
		#print 

	# update
