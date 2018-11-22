

# ----------------------------------------------------------- Static ------------------------------------------------------

	i = 0 

	# Increase Static
	@api.multi 
	def increase_static(self):
		
		print 
		print 'Increase Static'

		Counter.i = Counter.i + 1

		self.value_static = Counter.i 

		print Counter.i
		print 

		#self.value = self.value + 1
		#self.date_modified = fields.datetime.now()


# ----------------------------------------------------------- Pre ------------------------------------------------------

	# Value 
	value_static = fields.Integer(
			string="Valor Estático", 
			default=1, 
		)


	#@api.onchange('Counter.i')
	#def _onchange_Counter_i(self):
	#	print 
	#	print 'jx'
	#	print 
