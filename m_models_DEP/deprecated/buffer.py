			ret = record.x_order_line_ids.create({

												'product_id': line.product_id.id,
												'name': line.name,
												'price_subtotal': line.price_subtotal,

												#'order_id': order_id,										
												#'name': target,
												#'state':'draft',
												#'price_unit': price_unit,
												#'x_price_vip': x_price_vip,
												#'product_uom': product_uom, 

										})

