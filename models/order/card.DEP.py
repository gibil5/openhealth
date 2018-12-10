

	@api.model
	def create(self,vals):
		#print 'jx'
		#print 'CRUD - Card - Create'
		#print 

		#print vals
		#print 
	


		# Put your logic here 
		#res = super(Patient, self).create(vals)
		res = super(Card, self).create(vals)
		# Put your logic here 




		# Partner - Pricelist 
		#pl = self.env['product.pricelist'].search([
		#													('name','=', 'VIP'),
		#											],
													#order='appointment_date desc',
		#											limit=1,)
		#print pl
		#print self.partner_id
		#print self.partner_id.property_product_pricelist
		#self.partner_id.property_product_pricelist = pl

		return res

	# CRUD - Create 