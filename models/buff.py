


			
			self.inventory_line.create({

													'product_id': stock_min_funcs.get_product_id(self, line.code),

													'code': line.code,
															
													'description': line.description,

													'qty': line.qty,

													'units': line.units,

													#'state': 'done', 
													'state': line.state, 

													'inventory_id': self.id,
				})

