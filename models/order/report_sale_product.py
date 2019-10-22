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

	# Mangement - For Testing
	management_id = fields.Many2one(
			'openhealth.management',
		)


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
			string="Fecha Final", 
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

	total_qty = fields.Integer(
			string="Cantidad", 
		)

	total = fields.Float(
			string="Total", 
		)

	vspace = fields.Char(
			' ', 
			readonly=True
		)



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


		# Get Orders 
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
