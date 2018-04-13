# -*- coding: utf-8 -*-
#
# 	ReportSaleProduct 
# 

from openerp import models, fields, api
import resap_funcs


class ReportSaleProduct(models.Model):
	
	#_inherit = 'openhealth.report'
	_inherit = 'openhealth.report.sale'

	_name = 'openhealth.report.sale.product'
	







# ----------------------------------------------------------- Relational ------------------------------------------------------
	
	# Item Counter
	item_counter_ids = fields.One2many(
		
			#'openhealth.product.counter', 
			'openhealth.item.counter', 

			'report_sale_product_id', 
			
			#string="Estado de cuenta",
		)





	# Order Lines
	order_line_ids = fields.One2many(
		
			#'openhealth.order.report.nex.line', 
			'openhealth.report.order_line', 

			'report_sale_product_id', 
			
			#string="Estado de cuenta",
		)












# ----------------------------------------------------------- Create Lines ------------------------------------------------------

	# Create Lines 
	@api.multi
	def create_lines(self, orders):  

		for order in orders: 

			for line in order.order_line: 
				
				if line.product_id.categ_id.name == 'Cremas': 


					ret = self.order_line_ids.create({
															'name': line.name,

															'product_id': line.product_id.id,
															

															'patient': order.patient.id,


															'price_unit': line.price_unit,

															'product_uom_qty': line.product_uom_qty, 
															
															'x_date_created': line.create_date,															

															'report_sale_product_id': self.id,
													})





# ----------------------------------------------------------- Actions ------------------------------------------------------

	# Update 
	@api.multi
	def update_report(self):  

		print
		print 'Update report'



		# Clean 
		self.order_line_ids.unlink()
		self.item_counter_ids.unlink()




		# Orders 
		orders,count = resap_funcs.get_orders(self, self.name)
		print orders, count
		print 





		# Order lines
		self.create_lines(orders)







		# Item Counter 
		total_qty = 0
		total = 0 
		for order_line in self.order_line_ids: 

			name = order_line.product_id.name
			qty = order_line.product_uom_qty
			subtotal = order_line.price_total 
			total_qty = total_qty + qty
			total = total + subtotal



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





		self.total_qty = total_qty
		self.total = total
		#print 






# ----------------------------------------------------------- Primitives ------------------------------------------------------



	name = fields.Date(
			string="Fecha", 
			default = fields.Date.today, 
			#readonly=True,
			required=True, 
		)








