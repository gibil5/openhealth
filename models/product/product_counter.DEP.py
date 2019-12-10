# 10 Dec 2019


# ----------------------------------------------------------- Actions - Dep ------------------------------------------------------
	# Increase 
	@api.multi
	#def increase_qty(self, qty):  
	def increase_qty_dep(self, qty):  
		#print
		#print 'Increase Qty'

		self.qty = self.qty + qty 


	# Increase 
	@api.multi
	#def increase_total(self, total):  
	def increase_total_dep(self, total):  
		#print
		#print 'Increase Total'

		self.total = self.total + total 




# ----------------------------------------------------------- Deprecated ? ------------------------------------------------------




	categ = fields.Selection(

			[	
				('a', 		'A'),
				('b', 		'B'),
				('c', 		'C'),
			], 

		)



	# Report Sale 
	#report_sale_a_id = fields.Many2one(
	#	'openhealth.report.sale', 
	#	string='Report Reference', 		
	#	ondelete='cascade', 
	#)

	#report_sale_b_id = fields.Many2one(
	#	'openhealth.report.sale', 
	#	string='Report Reference', 		
	#	ondelete='cascade', 
	#)

	#report_sale_c_id = fields.Many2one(
	#	'openhealth.report.sale', 
	#	string='Report Reference', 		
	#	ondelete='cascade', 
	#)

