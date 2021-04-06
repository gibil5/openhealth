# -*- coding: utf-8 -*-
"""
	Mgt Funcs

	Should be unit testable - independent from openerp
	
	Very important !
	Every error should be caught, using an exception. 

	Created: 			28 May 2018
	Last up: 			 1 apr 2021

	- Use functional programming - ie pure functions. 	# Dep !
	- Use lambda funcs, map, filter, reduce, decorators, generators, etc.  # Dep !

	Signature
		reset_vector(vector)
		init_vector(vector_type)
		line_analysis_vector_type(line, vector_obj)
		line_analysis_vector_sub(line, vector_sub)
		
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

# ----------------------------------------------------------- Line Analysis ----
def line_analysis_type(line, vector):
	"""
	Obj vector
	Parses an order line
	Updates a vector of object counters
	"""
	print('Line analysis type')

	_dic = { 'product': 'products',
			 'service': 'services',
			}

	# Init
	_type = line.product_id.type
	total = line.price_subtotal 
	qty = line.product_uom_qty
	
	# Inc using Product counter, which is completely decoupled from Mgt 
	for obj in vector:
		obj.line_analysis(_dic[_type], total, qty)



# ----------------------------------------------------------- Line Analysis ----
def line_analysis_sub(line, vector):
	"""
	Obj vector
	Parses an order line
	Updates a vector of counters
	"""
	print('Line analysis sub')

	_dic_tre = { 
			 'CONSULTA MEDICA': 'con', 

			 'LASER CO2 FRACCIONAL': 'co2', 
			 'LASER EXCILITE': 'exc', 
			 'QUICKLASER': 'qui', 
			 'LASER M22 IPL': 'ipl', 
			 'LASER M22 ND YAG': 'ndy', 
	}
	
	_dic_fam = { 
			#'consultation': 'con', 
			'medical': 'med', 
			'cosmetology': 'cos', 
			'echography': 'ech', 
			'gynecology': 'gyn', 
			'promotion': 'pro', 
			'topical': 'top', 
			'card': 'vip', 
			'kit': 'kit', 
	}

	# Init
	prod = line.product_id

	pricelist = prod.pl_price_list

	treatment = prod.pl_treatment
	family = prod.pl_family

	total = line.price_subtotal
	qty = line.product_uom_qty



	# Product
	if prod.type in ['product']:
		name = 'top'

	# Service
	elif treatment in _dic_tre:
		name = _dic_tre[treatment]

	elif family in _dic_fam:
		name = _dic_fam[family]

	# Exc 
	else: 
		print('\n\nThis should not happen !')
		name = 'error'
		#print(line)
		print(prod)
		print(prod.name)
		print(pricelist)
		print(treatment)
		print(family)


	# Inc
	for obj in vector:
		obj.line_analysis(name, total, qty)


# ----------------------------------------------------------- Averages Vector -----
def get_totals(vector):
	"""
	Get totals from vector
	"""
	amount = 0.
	count = 0
	# Avg using Product counter, which is completely decoupled from Mgt 
	for obj in vector:
		amount += obj.amount
		count += obj.count

	return amount, count



# ----------------------------------------------------------- Averages Vector -----
def set_averages_vector(vector):
	"""
	Set averages in vector
	"""
	# Avg using Product counter, which is completely decoupled from Mgt 
	for obj in vector:
		obj.set_average()


# ----------------------------------------------------------- Averages Vector -----
def set_percentages_vector(vector, amount):
	"""
	Set percentages in vector
	"""
	# Avg using Product counter, which is completely decoupled from Mgt 
	for obj in vector:
		obj.set_percentage(amount)


# ----------------------------------------------------------- Averages Vector -----
#def set_ratios_vector(nr_consultations, nr_procedures):
def set_ratios_vector(vector):
	"""
	Set ratios in vector ?
	"""
	nr_consultations = 0
	nr_procedures = 0 
	ratio_pro_con = 0 

	# Using counters
	for obj in vector:
		if obj.name == 'consultations':
			nr_consultations = obj.count
		if obj.name == 'procedures':
			nr_procedures = 0
	
		if nr_consultations != 0:
			ratio_pro_con = (float(nr_procedures) / float(nr_consultations))

	return ratio_pro_con
	# set_ratios_vector








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



# ----------------------------------------------------------- Calc Averages -----
def division(amo, number):
	"""
	Division
	"""
	return round(float(amo) / float(number), 2) if number else 0


def averages_pure(vector, func=division):
	"""
	*** Unit tested 

	Input: 
		Vector of tuples 
		[ (total, count), (), () ]
		Ex: [ (1350, 2), (2950, 50) ]
	
	Averages Pure
	Using functional programming
	Used by: Management
	"""
	print("averages_pure")
	ave = []
	for data in vector:
		amo = data[0]
		number = data[1]
		ave.append((func(amo, number)))
		#print(amo, number)
	#print(ave)

	return ave
# averages_pure


def averages_pure_tag(vector, func=division):
	"""
	*** Unit tested 

	Input: 
		Tagged vector of tuples 
		[ (tag, total, count), (), () ]
		Ex: [ ('tag_0', 1350, 2), ('tag_1', 2950, 50) ]
	
	Averages Pure Tag
	Using functional programming
	Used by: Management
	"""
	print("averages_pure_tag")
	ave = []
	for data in vector:
		tag = data[0]
		amo = data[1]
		number = data[2]
		ave.append((tag, func(amo, number)))
		#print(amo, number)
	#print(ave)
	return ave
# averages_pure_tag


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
