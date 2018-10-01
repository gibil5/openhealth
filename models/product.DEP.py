

# 17 Sep 2018 



# ----------------------------------------------------------- Constraints - Name Short ------------------------------------------------------
	#_sql_constraints = [
	#						('x_name_short_unique','unique(x_name_short)', 'x_name_short must be unique!')
	#					]     





# ----------------------------------------------------------- Constraints - Default Code - Method 1 ------------------------------------------------------
	#default_code = fields.related('product_variant_ids', 'default_code', type='char', string='Internal Reference'),	
	
	#_sql_constraints = [
	#						('ref_unique','unique(default_code)', 'reference must be unique!')
	#					]     



# ----------------------------------------------------------- Constraints - Default Code - Method 2 ------------------------------------------------------
	#@api.constrains('default_code')
	#def _check_something(self):

	#	for record in self:
	
	#		if record.default_code == '0':
	#			raise ValidationError("Default code not valid: %s" % record.default_code)

			# count 
	#		if record.default_code != False: 
	#			count = self.env['product.template'].search_count([
	#																('default_code', '=', record.default_code),
	#										])
	#			if count > 1: 
	#				raise ValidationError("Default code already exists: %s" % record.default_code)
		# all records passed the test, don't return anything










# ----------------------------------------------------------- Partner ------------------------------------------------------
	# Deprecated ? 

	# Partner 
	#product_manager_id = fields.Many2one(
	
	#		'openhealth.product.manager',
			
			#string = "Cliente", 	
			#ondelete='cascade', 			
			#required=True, 
			#required=False, 
	#	)



# ----------------------------------------------------------- Deprecated ? ------------------------------------------------------
	# Description - For tickets - Deprecated ? 
	#description = fields.Text(
	#		'Description',
	#		default="x", 
	#	)
