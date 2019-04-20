

# 31 March 2017




#	order_line = field_One2many=fields.One2many(
#			'sale.order.line',
#			'consultation',
#			domain = [
						#('order_id', '=', pre_order),
#						('state', '=', 'draft'),
#					],

		#compute='_compute_order_line', 
#	)


	@api.depends('service_co2_ids')
	
	def _compute_order_line(self):

		print 
		print "Compute order line"
		
		consultation_id = self.id

		print self.pre_order
		print self.pre_order.id 

		order_id = self.pre_order.id
		#order_id = self.order.id
		
		
		for record in self:	
			#record.order_line.id = record.order.order_line.id
			
			for se in record.service_co2_ids:
				print se.name 

				ol = record.order_line.create({
											'product_id': se.service.id,
											'name': se.name_short,
											'product_uom': se.service.uom_id.id,


											'consultation': consultation_id,											
											'order_id': order_id,

											#'order_id': consultation_id,											
										})

		print 

