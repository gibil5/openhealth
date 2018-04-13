# -*- coding: utf-8 -*-
#
# 	Report Sale
# 

from openerp import models, fields, api

import resap_funcs



class ReportSale(models.Model):
	
	_inherit = 'openhealth.report'

	_name = 'openhealth.report.sale'



	

# ----------------------------------------------------------- Filters ------------------------------------------------------

	# Categs
	categ_a = fields.Selection(
			[	
				('Cremas', 				'Productos'),
				('Consulta', 			'Consultas'),
				('Procedimiento', 		'Procedimientos'),
				('Cosmeatria', 			'Cosmeatria'),
			], 
			string="Categ A", 
		)

	categ_b = fields.Selection(

			[	
				('Cremas', 				'Productos'),
				('Consulta', 			'Consultas'),
				('Procedimiento', 		'Procedimientos'),
				('Cosmeatria', 			'Cosmeatria'),
			], 

			string="Categ B", 
		)





	# Doctor
	doctor = fields.Many2one(

			'oeh.medical.physician',

			domain = [
						('x_therapist', '=', False),
					],
		)





# ----------------------------------------------------------- Relational ------------------------------------------------------
	# Order Lines
	#order_line_ids = fields.One2many(
	order_line_a_ids = fields.One2many(
		
			'openhealth.report.order_line', 

			'report_sale_a_id', 
			
			#string="Estado de cuenta",
		)



	order_line_b_ids = fields.One2many(
		
			'openhealth.report.order_line', 

			'report_sale_b_id', 
			
			#string="Estado de cuenta",
		)







	# Item Counter
	item_counter_a_ids = fields.One2many(
		
			'openhealth.item.counter', 

			'report_sale_a_id', 
			
			#string="Estado de cuenta",
		)



	item_counter_b_ids = fields.One2many(
		
			'openhealth.item.counter', 

			'report_sale_b_id', 
			
			#string="Estado de cuenta",
		)



	item_counter_c_ids = fields.One2many(
		
			'openhealth.item.counter', 

			'report_sale_c_id', 
			
			#string="Estado de cuenta",
		)









# ----------------------------------------------------------- Create Lines ------------------------------------------------------


	# Item Counter 
	@api.multi
	#def count_items(self):  
	#def count_items(self, order_line_ids, item_counter_ids):  
	def count_items(self, order_line_ids, item_counter_ids, report_sale_id, categ):  


		#for order_line in self.order_line_ids: 
		for order_line in order_line_ids: 


			name = order_line.patient.name
			qty = 1 
			subtotal = order_line.price_total 




			prod_ctr = self.env['openhealth.item.counter'].search([
																		('name', '=', name),
																		(report_sale_id, '=', self.id),
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
				#ret = self.item_counter_ids.create({
				ret = item_counter_ids.create({
															'name': name,
															'qty': qty, 
															'total': subtotal, 

															'categ': categ, 

															report_sale_id: self.id,
													})
				#print ret 









	# Filter Lines - Categ
	@api.multi
	def filter_lines_categ(self, orders, categ):  

		
		lines = []


		# Categ 
		for order in orders: 
			for line in order.order_line: 
				if categ == False: 
					lines.append(line)
				elif categ == 'Procedimiento': 
					if line.product_id.categ_id.name in ['Quick Laser', 'Laser Co2', 'Laser Excilite', 'Laser M22', 'Medical']: 
						lines.append(line)
				else: 
					if line.product_id.categ_id.name == categ: 
						lines.append(line)



		return lines 





	# Filter Lines - Doctor
	@api.multi
	def filter_lines_doctor(self, lines, doctor):  


		for line in lines: 


			if doctor == False: 
				lines.append(line)

			else: 
				if line.doctor.name == doctor: 
					lines.append(line)


		return lines 











	# Create Lines 
	@api.multi
	#def create_lines_a(self, lines):  
	#def create_lines(self, lines, order_line_ids):  
	def create_lines(self, lines, order_line_ids, report_sale_id):  

		total_qty = 0
		total = 0 

		for line in lines: 

			qty = line.product_uom_qty
			subtotal = line.price_total 

			total_qty = total_qty + qty
			total = total + subtotal
			

			#ret = self.order_line_a_ids.create({
			ret = order_line_ids.create({
														'name': line.name,

														'product_id': line.product_id.id,
														'patient': line.order_id.patient.id,

														'doctor': line.order_id.x_doctor.id,

														'price_unit': line.price_unit,
														'product_uom_qty': line.product_uom_qty, 

														#'x_date_created': line.create_date,	
														'x_date_created': line.order_id.date_order,	

														#'report_sale_id': self.id,
														report_sale_id: self.id,
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
		#self.order_line_ids.unlink()
		#self.item_counter_ids.unlink()

		self.order_line_a_ids.unlink()
		self.item_counter_a_ids.unlink()

		self.order_line_b_ids.unlink()
		self.item_counter_b_ids.unlink()


		#self.order_line_c_ids.unlink()
		self.item_counter_c_ids.unlink()




# Get Orders 
		orders,count = resap_funcs.get_orders_filter(self, self.date_begin, self.date_end)





# Filter 
		lines_a = self.filter_lines_categ(orders, self.categ_a)
		lines_b = self.filter_lines_categ(orders, self.categ_b)


		#lines_a = self.filter_lines_doctor(lines_a, self.doctor)







# Create  

		# Create Lines - A
		#self.create_lines(lines_a, self.order_line_a_ids)

		report_sale_id = 'report_sale_a_id'
		self.create_lines(lines_a, self.order_line_a_ids, report_sale_id)

		report_sale_id = 'report_sale_b_id'
		self.create_lines(lines_b, self.order_line_b_ids, report_sale_id)




		# Count Items - A
		#self.count_items()

		report_sale_id = 'report_sale_a_id'
		categ = 'a'
		self.count_items(self.order_line_a_ids, self.item_counter_a_ids, report_sale_id, categ)

		report_sale_id = 'report_sale_b_id'
		categ = 'b'
		self.count_items(self.order_line_b_ids, self.item_counter_b_ids, report_sale_id, categ)  




		# Final Result !
		#self.item_counter_c_ids = self.item_counter_a_ids - self.item_counter_b_ids


		for item_counter in self.item_counter_a_ids: 

			name = item_counter.name
			qty = item_counter.qty
			total = item_counter.total

			count = self.env['openhealth.item.counter'].search_count([
																			('name', '=', name),

																			('report_sale_b_id', '=', self.id),
																	],
																		#order='x_serial_nr asc',
																		#limit=1,
																	)

			if count == 0: 
				print 'Gotcha !'
				print item_counter
				print item_counter.name 

				categ = 'c'
				
				ret = self.item_counter_c_ids .create({
															'name': name,
															'qty': qty, 
															'total': total, 
															'categ': categ, 
															'report_sale_c_id': self.id,
													})
				print ret 






