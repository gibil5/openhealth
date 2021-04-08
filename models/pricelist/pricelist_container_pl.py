# -*- coding: utf-8 -*-
"""
	Pricelist Container

	Created: 	23 Apr 2019
	Prev: 		10 Aug 2019
	Last: 		 8 apr 2021
"""
from __future__ import print_function
import pandas
from openerp import models, fields, api
from . import px_vars, exc_prod, pl_funcs

# ----------------------------------------------------------- Exceptions -------------------------
#class ProductFamilyValueException(Exception):
#	pass

class PricelistContainer(models.Model):
	"""
	Pricelist Container 2019
	Creates, updates and manages Products
	Uses PL Products
	"""
	_description = 'container'

	_inherit = 'openhealth.container.pricelist'


# ------------------------------------------------------ Methods --------------------------------------------------

# -------------------------------------------------------- Load CSV - Button ---
	@api.multi
	def load_csv(self):
		"""
		Load CSV file
		That has been created with Excel by the customer
		"""
		print()
		print('*** Load Csv')

		# Clean
		self.clear()

		_file_name_list = []

		# Init
		_list_all = [
						'PRODS.csv',

						'CONSULTATIONS.csv',

						'CO2.csv',
						'EXCILITE.csv',
						'M22.csv',
						'QUICK.csv',

						'MEDICAL.csv',
						'COSMETO.csv',

						'GINECO.csv',
						'PROMOS.csv',
						'ECO.csv',
		]

		_list_dic = {
						'product':		'PRODS.csv',

						'consultation': 'CONSULTATIONS.csv',

						'co2': 			'CO2.csv',
						'excilite':		'EXCILITE.csv',
						'm22':			'M22.csv',
						'quick':		'QUICK.csv',

						'medical':		'MEDICAL.csv',
						'cosmetology':	'COSMETO.csv',

						'gynecology':	'GINECO.csv',
						'promotion':	'PROMOS.csv',
						'echography':	'ECO.csv',
					}

		print(self.family)

		if self.family in ['all']:
			_file_name_list = _list_all

		else:
			print(_list_dic[self.family])
			_file_name_list.append(_list_dic[self.family])

		print(_file_name_list)


		# Loop
		for file_name in _file_name_list:

			# Read csv file
			print('Read CSV file')
			fname = self.path_csv_pricelist + file_name
			print(fname)

			#df = self.open_with_pandas_read_csv(fname)
			try:
				df = self.open_with_pandas_read_csv(fname)
				print(df)

				# Loop
				for index, row in df.iterrows():

					product = pl_funcs.create_pricelist_product(self.product_ids, row, self.id)
					#print(product)


			except IOError:
				print('ERROR - PricelistContainer - File non existant !')
				#raise IOError('jx - IOError exception')

			else:
				print('jx - Else !')
	# load_csv


# --------------------------------------------- Create or update Products Products - Button ---
	@api.multi
	def create_product_products(self):
		"""
		Pricelist 2019
		Creates Product Products
		"""
		print('\n\n')
		print('Create Products Products 2019')

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
			#count = self.env['product.template'].search_count([
			count = self.env['product.product'].search_count([
																('name', '=', pro.name),
																#('pl_price_list', '=', '2019'),
														])
			#print(count)


			# Avoids PT Duplication
			if count == 0:

				# Create 
				print('CREATE !')
				#product_template = self.env['product.template'].create({
				product_product = self.env['product.product'].create({
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
				print(product_product)


			else:
				print('WRITE !!!')

				# Search
				product_product = self.env['product.product'].search([
																		('name', '=', pro.name),
																		#('pl_price_list', '=', '2019'),
																	])
				print(product_product)

				# Write 
				product_product.write({
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
		#print(products)
		#print(count)

	# create_products_products


# --------------------------------------------- Create or update Products Templates - Button ---
	@api.multi
	#def create_products_2019(self):
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
		#print(products)
		#print(count)

	# create_products_2019



# ---------------------------------------------------------- Update - Button ---
	@api.multi
	def update(self):
		"""
		Updates All Products
		"""
		print('Container Update')

		# Search
		products = self.env['product.template'].search([
															('pl_price_list', '=', '2019'),
														],
															#order='date_begin asc',
															#limit=1,
													)
		for product in products:
			product.update()
	# update


# -------------------------------------------------- Second Level - Services ---
	def open_with_pandas_read_csv(self, filename):
		"""
		Open with Pandas
		"""
		csv_delimiter = ","
		df = pandas.read_csv(filename, sep=csv_delimiter)
		#data = df.values
		#data = df
		#return data
		return df


# ----------------------------------------------------------- Clear - Button ---
	@api.multi
	def clear(self):
		"""
		Clear
		"""
		self.product_ids.unlink()

		#model = 'price_list.product'
		model = 'openhealth.product.pricelist'

		# Pricelist Products
		#products = self.env['price_list.product'].search([
		products = self.env[model].search([
															#('x_name_short', 'in', [name]),
														],
															#order='date_begin asc',
															#limit=1,
													)
		products.unlink()


# ----------------------------------------------------------- 0 Level ----------
	#@api.multi
	#def validate(self):
	#	"""
	#	Validate
	#	"""
	#	print()
	#	print('Validate')
	#	self.validate_product_templates()

# ---------------------------------------------------- First Level - Buttons ---
	@api.multi
	def validate_product_templates(self):
		"""
		Validate All Product Templates
		"""
		print()
		print('Validate - Product Templates')

		# Search
		#name = 'CO2'
		#name = 'CONSULTA'
		name = self.search_pattern
		products = self.env['product.template'].search([
															('pl_price_list', 'in', ['2019']),
															('name', 'like', name),
													],
			#order='pl_prefix,pl_idx_int asc',
			#order='pl_idx_int,pl_prefix asc',
			order='pl_prefix asc',
			limit=10,
			#limit=100,
			#limit=600,
		)
		print(products)


		# Loop
		idx = 0
		for product in products:
			#print()
			#print(product.name)
			idx = idx + 1
			if self.fix_flag:

				# Handle Exceptions
				exc_prod.handle_exceptions_treatment(product, self)
				exc_prod.handle_exceptions_family(product, self)
				exc_prod.handle_exceptions_subfamily(product, self)
		
		print(idx)
