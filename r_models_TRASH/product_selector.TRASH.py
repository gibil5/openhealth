

# 29 Jan 2018

	# Zone 
	#zone = fields.Selection(
	#		selection=prodvars._zone_list,
			#selection=[
			#				('laser_quick',		'Quick'), 
			#	],


# 28 Aug 2018 

	# Reset 
	@api.multi
	def reset(self):  
		#print 
		#print 'Reset'

 		# Reset 
 		self.default_code = ''
 		self.product_id = False
 		self.price_manual_flag = False
 		self.price_manual = 0
		self.family = False
	 	self.treatment = False
		self.zone = False
	 	self.family = False
