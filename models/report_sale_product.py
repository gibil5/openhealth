# -*- coding: utf-8 -*-
#
# 	ReportSaleProduct 
# 
#

from openerp import models, fields, api
#import datetime
import resap_funcs


class ReportSaleProduct(models.Model):
	
	#_inherit='sale.closing'

	_name = 'openhealth.report.sale.product'
	






# ----------------------------------------------------------- Relational ------------------------------------------------------
	
	# Product Counters 
	product_counter_ids = fields.One2many(
		
			'openhealth.product.counter', 

			'report_sale_product_id', 
			
			#string="Estado de cuenta",
		)





	# Lines
	order_line_ids = fields.One2many(
		
			'openhealth.order.report.nex.line', 

			'report_sale_product_id', 
			
			#string="Estado de cuenta",
		)





# ----------------------------------------------------------- Actions ------------------------------------------------------

	# Update 
	@api.multi
	def update_report(self):  

		print
		print 'Update report'



		# Clean 
		self.order_line_ids.unlink()
		self.product_counter_ids.unlink()




		# Orders 
		#categ_name = 'Cremas'
		#orders,count = resap_funcs.get_orders(self, self.date, categ_name)
		#orders,count = resap_funcs.get_orders(self, self.date)
		orders,count = resap_funcs.get_orders(self, self.name)
		print orders, count






		# Order lines
		for order in orders: 
			print order 
			for line in order.order_line: 
				
				if line.product_id.categ_id.name == 'Cremas': 
					print 'Gotcha'
					print line.product_id.name 

					ret = self.order_line_ids.create({
															'name': line.name,
															'product_id': line.product_id.id,
															'price_unit': line.price_unit,

															'product_uom_qty': line.product_uom_qty, 
															
															'x_date_created': line.create_date,															

															'report_sale_product_id': self.id,
													})

					print ret 
					print 



		# Lines
		total_qty = 0
		total = 0 
		for order_line in self.order_line_ids: 


			name = order_line.product_id.name
			qty = order_line.product_uom_qty


			#total = order_line.price_subtotal 
			subtotal = order_line.price_total 





			total_qty = total_qty + qty
			total = total + subtotal




			prod_ctr = self.env['openhealth.product.counter'].search([
																		('name', '=', name),

																		('report_sale_product_id', '=', self.id),
											],
												#order='x_serial_nr asc',
												limit=1,
											)

			print prod_ctr


			if prod_ctr.name != False: 
				print prod_ctr.name 
				
				prod_ctr.increase_qty(qty)

				prod_ctr.increase_total(subtotal)



			else:

				ret = self.product_counter_ids.create({
															'name': name,
															'qty': qty, 
															'total': subtotal, 

															#'product_id': line.product_id.id,

															'report_sale_product_id': self.id,
													})

				print ret 





		self.total_qty = total_qty
		self.total = total
		print self.total_qty
		print self.total
		print 





# ----------------------------------------------------------- Primitives ------------------------------------------------------


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
