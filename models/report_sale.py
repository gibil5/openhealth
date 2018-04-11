# -*- coding: utf-8 -*-
#
# 	Repor tSale
# 

from openerp import models, fields, api
import resap_funcs


class ReportSale(models.Model):
	
	_inherit = 'openhealth.report'

	_name = 'openhealth.report.sale'


	

# ----------------------------------------------------------- Relational ------------------------------------------------------
	# Order Lines
	order_line_ids = fields.One2many(
		
			'openhealth.report.order_line', 

			'report_sale_id', 
			
			#string="Estado de cuenta",
		)






# ----------------------------------------------------------- Filters ------------------------------------------------------

	categ = fields.Selection(

			[	
				('Cremas', 				'Cremas'),
				('Consultas', 			'Consultas'),
				('Procedimientos', 		'Procedimientos'),
			], 

		)




# ----------------------------------------------------------- Create Lines ------------------------------------------------------


	# Filter Lines 
	@api.multi
	def filter_lines_categ(self, orders):  

		lines = []

		for order in orders: 

			for line in order.order_line: 

				if line.product_id.categ_id.name == self.categ: 

					#lines = lines + line  
					lines.append(line)


		return lines 





	# Create Lines 
	@api.multi
	#def create_lines(self, orders):  
	def create_lines(self, lines):  

		total_qty = 0
		total = 0 

		#for order in orders: 

		#for line in order.order_line: 
		for line in lines: 


			#name = line.product_id.name
			qty = line.product_uom_qty
			subtotal = line.price_total 

			total_qty = total_qty + qty
			total = total + subtotal
			


			#if line.product_id.categ_id.name == 'Cremas': 

			ret = self.order_line_ids.create({
														'name': line.name,
														'product_id': line.product_id.id,
														'price_unit': line.price_unit,
														'product_uom_qty': line.product_uom_qty, 
														'x_date_created': line.create_date,															
														'report_sale_id': self.id,
												})


		self.total_qty = total_qty
		self.total = total




# ----------------------------------------------------------- Actions ------------------------------------------------------

	# Update 
	@api.multi
	def update_report(self):  

		print
		print 'Update report'



		# Clean 
		self.order_line_ids.unlink()
		#self.product_counter_ids.unlink()



		# Orders 
		orders,count = resap_funcs.get_orders_filter(self, self.date_begin, self.date_end)
		print orders, count
		print 






		# Filter 
		lines = self.filter_lines_categ(orders)



		# Create
		#self.create_lines(orders)
		self.create_lines(lines)







