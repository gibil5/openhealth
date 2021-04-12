"""
    Pricelist container 
    Deprecated funcs 
"""






# --------------------------------------------- Create or update Products Templates - Button ---
	@api.multi
	def create_product_templates(self):
		"""
		Pricelist 2019
		Creates Product Templates 
		Uses Pricelist Products
		Avoids Product Duplication
		"""
		print('\n\n')
		print('Create Products 2019')

		# Search all Pricelist products
		products = self.env['openhealth.product.pricelist'].search([],)

		# Count all
		count = self.env['openhealth.product.pricelist'].search_count([],)

		# Loop 
		for pro in products:
			print('\n')
			print(pro)
			print(pro.name)  		# Generates Encode Error

			# Count PTs 
			count = self.env['product.template'].search_count([
																('name', '=', pro.name),
																('pl_price_list', '=', '2019'),
														])
			#print(count)

			# Avoids PT Duplication
			if count == 0:

				# Create 
				print('CREATE !')
				product_template = self.env['product.template'].create({
																			'name': 			pro.name,
																			'sale_ok': 			True,
																			'purchase_ok': 		False,
																			'pl_price_list': 	'2019',
																			'pl_time_stamp': 	pro.time_stamp,
																			'type': 			pro.x_type,
																			'pl_name_short': 	pro.name_short,
																			'pl_prefix': 		pro.prefix,
																			'pl_idx': 			pro.idx,
																			'pl_idx_int': 		pro.idx_int,
																			'pl_family': 		pro.family,
																			'pl_subfamily':		pro.subfamily,
																			'pl_treatment': 	pro.treatment,
																			'pl_zone': 			pro.zone,
																			'pl_pathology': 	pro.pathology,
																			'pl_level': 		pro.level,
																			'pl_sessions': 		pro.sessions,
																			'pl_time': 			pro.time,
																			'list_price': 				pro.price,
																			'pl_price_vip': 			pro.price_vip,
																			'pl_price_company': 		pro.price_company,
																			'pl_price_session': 		pro.price_session,
																			'pl_price_session_next': 	pro.price_session_next,
																			'pl_price_max': 			pro.price_max,

																			# Only Prods
																			'pl_manufacturer': 			pro.manufacturer,
																			'pl_brand': 				pro.brand,
				})
				print(product_template)

			else:
				print('WRITE !!!')

				# Search
				product_template = self.env['product.template'].search([
																		('name', '=', pro.name),
																		('pl_price_list', '=', '2019'),
																	])
				print(product_template)

				# Write 
				product_template.write({
																			'name': 			pro.name,
																			'sale_ok': 			True,
																			'purchase_ok': 		False,
																			'pl_price_list': 	'2019',
																			'pl_time_stamp': 	pro.time_stamp,
																			'type': 			pro.x_type,
																			'pl_name_short': 	pro.name_short,
																			'pl_prefix': 		pro.prefix,
																			'pl_idx': 			pro.idx,
																			'pl_idx_int': 		pro.idx_int,
																			'pl_family': 		pro.family,
																			'pl_subfamily':		pro.subfamily,
																			'pl_treatment': 	pro.treatment,
																			'pl_zone': 			pro.zone,
																			'pl_pathology': 	pro.pathology,
																			'pl_level': 		pro.level,
																			'pl_sessions': 		pro.sessions,
																			'pl_time': 			pro.time,
																			'list_price': 				pro.price,
																			'pl_price_vip': 			pro.price_vip,
																			'pl_price_company': 		pro.price_company,
																			'pl_price_session': 		pro.price_session,
																			'pl_price_session_next': 	pro.price_session_next,
																			'pl_price_max': 			pro.price_max,

																			# Only Prods
																			'pl_manufacturer': 			pro.manufacturer,
																			'pl_brand': 				pro.brand,
																			})
				#print(product_template)

		print('Created end !')

	# create_products_2019




class ProductSubFamilyValueException(Exception):
	pass

# --------------------------------------------- Handle Exceptions subfamily ----
#@api.multi
def handle_exceptions_subfamily(self):
	"""
	Handle Exceptions subfamily
	"""
	#print()
	#print('PROD - Handle Exceptions - Subfamily')

	subfamily_arr = exc_vars._subfamily_list
	#print(subfamily_arr)
	#print(self.pl_subfamily)

	# subfamily
	try:
		if self.pl_subfamily not in subfamily_arr:
			msg = "ERROR: Producto Sub Familia Incorrecta"
			raise ProductSubFamilyValueException

	except ProductSubFamilyValueException:
		class_name = type(self).__name__
		obj_name = self.name
		msg =  msg + '\n' + class_name + '\n' + obj_name
		raise UserError(_(msg))


# ----------------------------------------------------------- Handle Exceptions -------------------------
#@api.multi
#def fix_exceptions(self):
def fix_exceptions_dep(self):
	"""
	Fix Exceptions
	"""
	print()
	print('PROD - Fix Exceptions')

	_dic = {

	# Medical
	'VICTAMINA C ENDOVENOSA':	'vitamin_c_intravenous', 
	'CRIOCIRUGIA':	'cryosurgery',
	'ESCLEROTERAPIA': 'sclerotherapy',
	'PLASMA': 'plasma',
	'BOTOX': 'botox', 
	'REDUX': 'redux',
	'ACIDO HIALURONICO': 'hyaluronic_acid',
	'MESOTERAPIA NCTF': 'mesotherapy',
	'INFILTRACIONES': 'infiltrations', 

	# Cosmetology
	'PUNTA DE DIAMANTES': 'diamond_tip', 
	'CARBOXITERAPIA': 'carboxytherapy', 
	'LASER TRIACTIVE + CARBOXITERAPIA': 'laser_triactive_carboxytherapy',

	}

	# Fix
	if self.pl_treatment in _dic:
		self.pl_subfamily = _dic[self.pl_treatment]




# ----------------------------------------------------------- Handle Exceptions -------------------------
#@api.multi
def handle_exceptions(self):
	"""
	Handle Exceptions
	"""
	#print()
	#print('Handle Exceptions')

	handle_exceptions_family(self)
	#handle_exceptions_subfamily(self)
