# -*- coding: utf-8 -*-
#
# 	ReportSaleProduct 
# 
from openerp import models, fields, api
from . import mgt_funcs

class ReportSaleProduct(models.Model):
	
	_name = 'openhealth.report.sale.product'
	


# ----------------------------------------------------------- Test ------------------------------------------------------

	test_target = fields.Boolean(
			string="Test Target", 
		)



# ----------------------------------------------------------- Primitives ------------------------------------------------------
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



# ----------------------------------------------------------- Relational ------------------------------------------------------	
	# Item Counter
	item_counter_ids = fields.One2many(
			'openhealth.item.counter', 
			'report_sale_product_id', 
			#string="Estado de cuenta",
		)


	# Order Lines
	order_line_ids = fields.One2many(
			'openhealth.report.order_line', 
			'report_sale_product_id', 
			#string="Estado de cuenta",
		)



# ----------------------------------------------------------- Create Lines ------------------------------------------------------

	# Create Lines 
	def create_lines(self, orders):  
		for order in orders: 
			for line in order.order_line: 
				if line.product_id.categ_id.name == 'Cremas': 
					
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
		#print
		#print 'Report Sale Product - Update'


		# Clean 
		self.order_line_ids.unlink()
		self.item_counter_ids.unlink()



		# Orders 
		#orders,count = acc_funcs.get_orders_filter(self, self.name, self.name)				# Sales and Cancelled
		orders,count = mgt_funcs.get_orders_filter_fast(self, self.name, self.name)			# Only Sales



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
