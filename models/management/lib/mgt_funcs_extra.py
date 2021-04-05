"""
	Mgt Funcs Extra - Suboptimal approachs

	Should be unit testable - independent from openerp
	
	Very important !
	Every error should be caught, using an exception. 

	Created: 			 3 apr 2021
	Last up: 			 3 apr 2021

	Signature
		line_analysis_vector_type(line, vector_obj)
		line_analysis_vector_sub(line, vector_sub)
"""
from __future__ import print_function


# ------------------------------------------------------------- Reset var ----
def reset_vector(vec):
	"""
	Reset vector
	"""
	#for var in vector:
	for var in vec:
		var = 0.



# ----------------------------------------------------------- Line Analysis ----
def line_analysis_vector_type(line, vector_obj):
	"""
	Obj vector
	Parses an order line
	Updates a vector of counters
	"""
	print('Line analysis vector type')

	# Init
	prod = line.product_id

	# Filter vector - Products
	if prod.type in ['product']:
		vector = filter(lambda x: x.name == 'products', vector_obj)

	# Filter vector - Services
	else:
		vector = filter(lambda x: x.name == 'services', vector_obj)

	# Inc
	for obj in vector:
		obj.inc_amount(line.price_subtotal)
		obj.inc_count(line.product_uom_qty)


# ----------------------------------------------------------- Line Analysis ----
def line_analysis_vector_sub(line, vector_sub):
	"""
	vector sub
	Parses order lines
	Updates counters
	"""
	print('Line analysis vector sub')

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

# line_analysis_sub
