

						# Create 
						pl_ol = pl.order_line.create({
														'name': ol.name, 
														'product_id': ol.product_id.id, 
														'x_date_created': ol.create_date, 


														#'order_id': ol.order_id.id, 
														#'price_subtotal': ol.price_subtotal, 
														#'product_uom_qty': ol.product_uom_qty, 
														#'price_unit': ol.price_unit, 


														'patient_line_id': pl.id, 
							})
