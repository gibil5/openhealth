# -*- coding: utf-8 -*-
"""
	Mgt Funcs
	Should be unit testable - independent from openerp

	Created: 			28 May 2018
	Last up: 			 8 dec 2020

	- Use functional programming - ie pure functions.
	- Use lambda funcs, map, filter, reduce, decorators, generators, etc.

	Signature
		division
		averages_pure
		set_percentages
"""
from __future__ import print_function
from functools import reduce
from mgt_product_counter import MgtProductCounter

# ------------------------------------------------------------- Constants ------
_DATE_FORMAT = "%Y-%m-%d"
_DATE_HOUR_FORMAT = "%Y-%m-%d %H:%M"
_MODEL_SALE = "sale.order"


# ------------------------------------------------------------- Init vector ----
def init_vector(vector_type):
	"""
	Init vector
	"""
	vector = []

	for name in vector_type:
		obj = MgtProductCounter(name)
		vector.append(obj)

	# Pure functional
	obj_percentages_pure(vector, 0)

	return vector


# ----------------------------------------------------------- Line Analysis ----
#def line_analysis_sub(self, line, vector_sub):
def line_analysis_sub(line, vector_sub):
	"""
	vector sub
	Parses order lines
	Updates counters
	"""
	print('Line line_analysis_sub')

	# Init
	prod = line.product_id
	sub = ''

	# By Treatment

	if prod.pl_treatment in ['CONSULTA MEDICA']:
		sub = 'con'

	# Co2
	elif prod.pl_treatment in ['LASER CO2 FRACCIONAL']:
		sub = 'co2'

	# Exc
	elif prod.pl_treatment in ['LASER EXCILITE']:
		sub = 'exc'

	# Quick
	elif prod.pl_treatment in ['QUICKLASER']:
		sub = 'qui'

	# Ipl
	elif prod.pl_treatment in ['LASER M22 IPL']:
		sub = 'ipl'

	# Ndyag
	elif prod.pl_treatment in ['LASER M22 ND YAG']:
		sub = 'ndy'


	elif prod.pl_family in ['medical']:
		sub = 'med'

	# Cosmeto
	elif prod.pl_family in ['cosmetology']:
		sub = 'cos'

	# Echo
	elif prod.pl_family in ['echography']:
		sub = 'ech'

	# Gyn
	elif prod.pl_family in ['gynecology']:
		sub = 'gyn'

	# Prom
	elif prod.pl_family in ['promotion']:
		sub = 'pro'

	# Topical
	elif prod.pl_family in ['topical']:
		sub = 'top'

	# Card
	elif prod.pl_family in ['card']:
		sub = 'vip'

	# kit
	elif prod.pl_family in ['kit']:
		sub = 'kit'


	# Filter
	vector = filter(lambda x: x.name == sub, vector_sub)

	# Inc
	for obj in vector:
		obj.inc_amount(line.price_subtotal)
		obj.inc_count(line.product_uom_qty)


# ----------------------------------------------------------- Line Analysis ----
#def line_analysis_obj(self, line, vector_obj):
def line_analysis_obj(line, vector_obj):
	"""
	Obj vector
	Parses order lines
	Updates counters
	"""
	print('Line line_analysis_obj')

	# Init
	prod = line.product_id

	# Products
	if prod.type in ['product']:
		vector = filter(lambda x: x.name == 'products', vector_obj)

	# Services
	else:
		vector = filter(lambda x: x.name == 'services', vector_obj)

	# Inc
	for obj in vector:
		obj.inc_amount(line.price_subtotal)
		obj.inc_count(line.product_uom_qty)



# ----------------------------------------------------------- Get Totals -------
def obj_get_amount_total_pure(vector):
	"""
	Get Totals - Using reduce
	"""
	return reduce((lambda x, y: x.amount + y.amount), vector)

def obj_get_count_total_pure(vector):
	"""
	Get Totals - Using reduce
	"""
	return reduce((lambda x, y: x.count + y.count), vector)



# -------------------------------------------------------- Percentages Pure ----
def obj_percentages_pure(vector, total):
	"""
	Obj Percentages pure
	"""
	print()
	print('**** obj percentages_pure')

	print(vector)

	if total > 0:
		results = map((lambda x: round(100 * x.amount / total, 2)), vector)
	else:
		results = map((lambda x: 0), vector)

	print(results)

	return results


# -------------------------------------------------------- Percentages Pure ----
def percentages_pure(vector, total):
	"""
	Percentages pure
	"""
	print()
	print('**** percentages_pure')

	print(vector)
	results = map((lambda x: round(100 * x / total, 2)), vector)
	print(results)

	return results


# ----------------------------------------------------------- Set Totals -------
def get_sum_pure(vector):
	"""
	Get Totals - Using reduce
	"""
	return reduce((lambda x, y: x + y), vector)


# --------------------------------------------------------------- Division -----
def division(amo, number):
	"""
	Division
	"""
	return round(float(amo) / float(number), 2) if number else 0


# ----------------------------------------------------------- Set Averages -----
def averages_pure(vector, func=division):
	"""
	Set Averages Pure
	Using functional programming
	Used by: Management
	"""
	print("\n")
	print(averages_pure)
	ave = []

	for data in vector:
		tag = data[0]
		amo = data[1]
		number = data[2]
		ave.append((tag, func(amo, number)))
		print(amo, number)

	print(ave)

	return ave
# averages_pure




# --------------------------------------------------------- Set Percentages ----
def set_percentages(self, total_amount):
	"""
	Set Percentages
	Used by
		Management
	"""
	# By Month
	if total_amount != 0:
		self.per_amo_other = (self.amo_other / total_amount)

		# Families
		self.per_amo_credit_notes = (self.amo_credit_notes / total_amount)
		self.per_amo_products = (self.amo_products / total_amount)
		self.per_amo_consultations = (self.amo_consultations / total_amount)
		self.per_amo_procedures = (self.amo_procedures / total_amount)

		# Sub Families
		self.per_amo_sub_con_med = (self.amo_sub_con_med / total_amount)
		self.per_amo_sub_con_gyn = (self.amo_sub_con_gyn / total_amount)
		self.per_amo_sub_con_cha = (self.amo_sub_con_cha / total_amount)

		self.per_amo_echo = (self.amo_echo / total_amount)
		self.per_amo_gyn = (self.amo_gyn / total_amount)
		self.per_amo_prom = (self.amo_prom / total_amount)

		self.per_amo_topical = (self.amo_topical / total_amount)
		self.per_amo_card = (self.amo_card / total_amount)
		self.per_amo_kit = (self.amo_kit / total_amount)

		self.per_amo_co2 = (self.amo_co2 / total_amount)
		self.per_amo_exc = (self.amo_exc / total_amount)
		self.per_amo_ipl = (self.amo_ipl / total_amount)
		self.per_amo_ndyag = (self.amo_ndyag / total_amount)
		self.per_amo_quick = (self.amo_quick / total_amount)

		self.per_amo_medical = (self.amo_medical / total_amount)
		self.per_amo_cosmetology = (self.amo_cosmetology / total_amount)
# set_percentages
