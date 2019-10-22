# 16 Oct 2019
# Done by PL



# ----------------------------------------------------------- Create Lines - DEP ------------------------------------------------------

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

