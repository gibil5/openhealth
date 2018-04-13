


		ret = self.filter_a.create({

										'name': 'filter_a',
										'date_begin': self.date_begin, 
										'date_end': self.date_end, 
										
										'categ': self.categ_a, 

										'report_sale_id': self.id 
			})

		ret = self.filter_b.create({

										'name': 'filter_b',
										'date_begin': self.date_begin, 
										'date_end': self.date_end, 
										
										'categ': self.categ_b, 

										'report_sale_id': self.id 
			})



		item_counter_a = self.filter_a.item_counter 
		item_counter_b = self.filter_b.item_counter 

		item_counter_c = item_counter_b - item_counter_a  

