

# 22 Jun 2018 

	# Total 
	amount_total_report = fields.Float(
			'Total S/.', 
			default='0', 

			#compute='_compute_amount_total_report', 
		)

	#@api.multi
	#def _compute_amount_total_report(self):
	#	for record in self:		
	#		total = 0 
	#		for line in record.order_line_ids: 
	#			total = total + line.price_subtotal 
	#		record.amount_total_report = total
