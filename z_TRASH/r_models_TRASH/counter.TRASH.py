



# 5 Apr 2018

# ----------------------------------------------------------- Computes ------------------------------------------------------

	# Total 
	total = fields.Char(
			string="Total", 
		
			#compute='_compute_total', 
		)

	#@api.multi
	#@api.depends()
	#def _compute_total(self):		
	#	for record in self:
	#		if record.prefix != False:
	#			if record.separator != False: 
	#				record.total = record.prefix  +  record.separator  +  str(record.value).zfill(record.padding)
	#			else:
	#				record.total = record.prefix  +  str(record.value).zfill(record.padding)






# 15 Jun 2018


#class counter(models.Model):




	#@api.onchange('value')
	#def _onchange_value(self):

	#	print 
	#	print 'On Change Value - Counter'
	#	print 

		# Date 
	#	self.date_modified = fields.datetime.now()

		# Total 
	#	name = count_funcs.get_name(self, self.prefix, self.separator, self.padding, self.value)		
	#	self.total = name



	# Total 
	#total = fields.Char(
	#		string="Total", 		
	#	)




	# Decrease
	#@api.multi 
	#def decrease(self):
	#	self.value = self.value - 1
	#	self.date_modified = fields.datetime.now()


	# Reset
	#@api.multi 
	#def reset(self):
	#	self.value = 1
	#	self.date_modified = fields.datetime.now()




	# Increase
	@api.multi 
	def increase(self):

		self.value = self.value + 1
		
		self.date_modified = fields.datetime.now()

		# Total 
		#self.total = count_funcs.get_name(self, self.prefix, self.separator, self.padding, self.value)		





