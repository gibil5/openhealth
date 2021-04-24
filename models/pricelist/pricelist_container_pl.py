# -*- coding: utf-8 -*-
"""
	Pricelist Container

	Created: 	23 Apr 2019
	Prev: 		10 Aug 2019
	Last: 		11 apr 2021
"""
from __future__ import print_function
from openerp import models, fields, api
#import pandas
from pandas import read_csv

from . import px_vars
from . import pl_funcs


# ----------------------------------------------------------- Exceptions --------------------------
class PricelistContainer(models.Model):
	"""
	Pricelist Container 2019
	Creates, updates and manages Products
	Uses PL Products
	"""
	_name = 'openhealth.container.pricelist'
	_description = 'container'
	#_inherit = 'openhealth.container.pricelist'


# ------------------------------------------------------ Fields --------------------------------------------------

# ----------------------------------------------------------- Relational -------
	product_ids = fields.One2many(
		'openhealth.product.pricelist',
		'container_id',
	)


# ------------------------------------------------------------- Fields ---------
	name = fields.Char(
		required=True,
	)

	family = fields.Selection(
		selection=px_vars._family_file_list,
		required=True,
	)

	path_csv_pricelist = fields.Char(
		required=True,
		default='/Users/gibil/cellar/github/price_list/csv/',
	)

	search_pattern = fields.Char()
	
	fix_flag = fields.Boolean(default=False)
	

# ------------------------------------------------------------- Dep ---------
	#file_name = fields.Selection(
	#		selection=px_vars._file_name_list,
	#		required=True,
	#	)

	#caps_name = fields.Boolean(
	#		default=False,
	#	)


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

			# Read CSV file
			try:
				df = self.open_with_pandas_read_csv(fname)
				print(df)
				# Loop
				for index, row in df.iterrows():
					product = pl_funcs.create_pricelist_product(self.product_ids, row, self.id)
			except IOError:
				print('ERROR - PricelistContainer - File non existant !')
			#else:
			#	print('jx - Else !')
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

		model = 'product.product'

		# Pricelist products
		# Search
		products = self.env['openhealth.product.pricelist'].search([],)
		# Count
		count = pl_funcs.count_product_pricelistt(self)


		# Loop 
		for pro in products:
			print('\n')
			print(pro)
			print(pro.name)  		# Generates Encode Error

			# Count PTs 
			count = self.env['product.product'].search_count([('name', '=', pro.name),])
			#print(count)

			# Avoids PT Duplication
			if count == 0:
				# Create 
				print('CREATE !')
				product_product = pl_funcs.create_product(self, pro, model)
				print(product_product)

			else:
				print('WRITE !!!')

				# Search
				product_product = self.env['product.product'].search([('name', '=', pro.name),])
				#print(product_product)

				# Write 
				prod = pl_funcs.write_product(pro, product_product)

				print(prod)

		print('Created end !')

	# create_products_products


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
                    ],)
		for product in products:
			product.update()
	# update

# -------------------------------------------------- Second Level - Services ---
	def open_with_pandas_read_csv(self, filename):
		"""
		Open with Pandas
		"""
		csv_delimiter = ","
		#df = pandas.read_csv(filename, sep=csv_delimiter)
		df = read_csv(filename, sep=csv_delimiter)
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
		# Pricelist Products
		products = self.env['openhealth.product.pricelist'].search([])
		products.unlink()

# ---------------------------------------------------- First Level - Buttons ---
	@api.multi
	def validate_product_templates(self):
		"""
		Validate All Product Templates
		"""
		print()
		print('Validate - Product Templates')

		# Search
		name = self.search_pattern
		products = self.env['product.template'].search([('pl_price_list', 'in', ['2019']), ('name', 'like', name),], order='pl_prefix asc', limit=10,)
		print(products)

		# Loop
		idx = 0
		for product in products:
			#print()
			#print(product.name)
			idx = idx + 1
			if self.fix_flag:
				print('*** Disabled !')
				# Handle Exceptions
				#exc_prod.handle_exceptions_treatment(product, self)
				#exc_prod.handle_exceptions_family(product, self)
				#exc_prod.handle_exceptions_subfamily(product, self)
		
		print(idx)
