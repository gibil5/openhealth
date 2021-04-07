# -*- coding: utf-8 -*-
"""
	*** Pl Funcs

	Used by:
		pricelist_container.py

	Created: 			 7 apr 2021
	Last up: 	 		 7 apr 2021
"""
from __future__ import print_function


# -------------------------------------------------------------- Create Pl products ----
def create_pricelist_product(line, row, container_id):
	"""
	create_pricelist_product
	"""
	print()
	print('create_pricelist_product')

	#print(row['idx'], row['name'])
	#print(row['name'])
	#print(row['name_short'])

	time_stamp = row['time_stamp']

	# Check Values	
	level = check(row['level'])
	time = check(row['time'])
	price = check(row['price'])
	price_vip = check(row['price_vip'])
	price_company = check(row['price_company'])
	price_session = check(row['price_session'])
	price_session_next = check(row['price_session_next'])
	price_max = check(row['price_max'])

	if row['x_type'] in ['product']:
		manufacturer = row['manufacturer']
		brand = row['brand']
		name = row['name'].upper()
		name_short = row['name_short'].upper()
	else:
		manufacturer = False
		brand = False
		name = row['name']
		name_short = row['name_short']

	# Create
	#product = self.product_ids.create({
	product = line.create({
										'name': 			name,
										'name_short': 		name_short,
										'time_stamp': 		time_stamp,
										'prefix': 			row['prefix'],
										'idx': 				row['idx'],
										'code': 			False,
										'x_type': 			row['x_type'],
										'family': 			row['family'],
										'subfamily': 		row['subfamily'],
										'treatment': 		row['treatment'],
										'zone': 			row['zone'],
										'pathology': 		row['pathology'],
										'sessions': 		row['sessions'],
										'level': 			level,
										'time': 				time,
										'price': 				price,
										'price_vip': 			price_vip,
										'price_company': 		price_company,
										'price_session': 		price_session,
										'price_session_next': 	price_session_next,
										'price_max': 			price_max,

										# Only Prods
										'manufacturer': 	manufacturer,
										'brand': 			brand,

										# Handle
										#'container_id': 	self.id,
										'container_id': 	container_id,
	})

# -------------------------------------------------------------- Check ----
#def check(self, value):
def check(value):
	"""
	Check parameters, for consistence
	Convert -1 to False
	"""
	#print('Check')
	#print(value)
	if value in ['-1', -1]:
		return False
	else:
		return value
