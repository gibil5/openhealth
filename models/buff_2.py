

	# Quick Laser 
	elif product.x_treatment == 'laser_quick': 	
		
		#print 'Quick Laser Price'
		
		price_quick = price_applied

		ol = self.order_line.create({
										'name': 		product.name, 
										'product_id': product.id,
										'order_id': order_id,
										'price_unit': price_quick,
										reco_field: reco_id, 
									})


