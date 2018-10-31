# -*- coding: utf-8 -*-
#
#       lib_exp.py
#
#       Created:            23 Oct 2018
#       Last up:            23 Oct 2018
#       Checked with:       PyFlakes
#
"""
high level support for doing this and that.
"""
import account as acc




#------------------------------------------------ Const -------------------------------------------
_DIC_PREFIX = {
	'01': 'F001',   # Ticket Invoice
	'03': 'B001',   # Ticket Receipt
	'11': 'FF01',   # Invoice               # Not Sunat Compliant !
	'13': 'BB01',   # Receipt               # Not Sunat Compliant !
}

_DIC_PREFIX_CANCEL = {
	#'01': 'FC01',   # Invoice
	'01': 'FC02',   # Invoice

	'03': 'BC01',   # Receipt
	'11': 'FFC1',   # Invoice               # Not Sunat Compliant !
	'13': 'BBC1',   # Receipt               # Not Sunat Compliant !
}


#------------------------------------------------ Format Txt --------------------------------------
# Format Txt
def format_txt(order):
	"""
	high level support for doing this and that.
	"""
	print
	print 'Format Txt'

	# Init
	#ret = "\n"
	ret = "\r\n"
	eol = "]"           # order

	sep = "|"            # Data
	eot = "!"           # Table
	blank = ""
	additional_account_id = "6"

	#empty_field = "|"


	# Prefix
	#if order.state in ['sale']:
	#   type_prefix = lvars._DIC_PREFIX[order.type_code]
	#elif order.state in ['cancel']:
	#   type_prefix = lvars._DIC_PREFIX_CANCEL[order.type_code]
	#type_prefix = lvars._DIC_PREFIX[order.type_code]





# Table 1 - General, Emitter and Receptor
	#general_1 = ""
	#general_2 = ""


# 01|F001-00007777|2018-07-12|PEN||||||||correo@gmail.com]
# 20478087820|6|CONTASIS SAC||150101|Jr. Lima 150|||||PE]
# 20345079491|6|contacom  SAC|Jr. pichis Nro. 106]
# !

	# Sale
	#if order.state in ['sale']:
	if order.state in ['sale', 'cancel']:
		# Data General
		general = order.type_code + sep + \
					order.id_serial_nr + sep + \
					order.export_date + sep + \
					order.currency_code + \
					sep + \
					sep + \
					sep + \
					sep + \
					sep + \
					sep + \
					sep + \
					sep + eol



# Credit Note - Cancel
# FC02-00009990|2017-11-09|07|PEN|||||F001-00000001|01|ERROR EN DATOS|F001-00000001|01||||]
#_gen = "FC02-00009990|2017-11-09|07|PEN|||||F001-00000001|01|ERROR EN DATOS|F001-00000001|01||||]"
#_general = "||||F001-00000001|01|ERROR EN DATOS|F001-00000001|01||||]"


	#else:
	elif order.state in ['credit_note']:
		
		# Data General

		_empty_1 = "||||"
		_empty_2 = "|||]"

		date_cn = order.export_date
		_cn = "07"
		currency_code_cn = "PEN"

		type_code_cn = order.type_code
		reason = "ERROR EN DATOS"		
		type_code = order.type_code



		# This one
		serial_nr_cn = order.serial_nr


		# Modified
		serial_nr_mod = order.credit_note_owner.x_serial_nr



		# General
		general = serial_nr_cn + sep + \
					date_cn + sep + \
					_cn + sep + \
					currency_code_cn + sep + \
					_empty_1 + \
					serial_nr_mod + sep + \
					type_code_cn + sep + \
					reason + sep + \
					serial_nr_mod + sep + \
					type_code + sep + \
					_empty_2



	# General
	#general = general_2 + ret + general_1





	# Emitter
	emitter = order.ruc               + sep + \
				additional_account_id   + sep + \
				order.firm              + sep + \
				blank                   + sep + \
				order.ubigeo            + sep + \
				order.address           + sep + \
				blank                   + sep + \
				blank                   + sep + \
				blank                   + sep + \
				blank                   + sep + \
				order.country           + eol




	# Receptor
	receptor = order.id_doc                + sep + \
				order.id_doc_type_code      + sep + \
				order.receptor              + sep + \
				order.patient.street    + eol



	# Table 1
	table_1 = general     + ret + \
				emitter     + ret + \
				receptor    + ret + \
				eot         + ret




# Table 2 - Optional
# 228.60|1000|IGV|VAT]      # opt
# |||]
# |||]
# !
	empty_line = "|||]" + ret

	tax_id = "1000"                         # ver
	tax_name = "IGV"
	tax_type_code = "VAT"



	#table_2 =  str(order.amount_total_tax)     + sep + \
	#table_2 =  "%.2f"%order.amount_total_tax   + sep + \
	table_2 = acc.fmt(order.amount_total_tax)     + sep + \
				tax_id                          + sep + \
				tax_name                        + sep + \
				tax_type_code                   + eol + ret + \
				empty_line + \
				empty_line + \
				eot + ret





# Table 3 - Total
# |1498.60|10.00]
# !
#               str(order.amount_total)     + sep + \

	table_3 = blank                       + sep + \
				acc.fmt(order.amount_total)     + sep + \
				blank                       + eol + ret + \
				eot + ret






# Table 4 - Tax
# 1001|1270.00]
# |]
# |]
# |]
# 2005|10.00]
# |||||]
# |||]
# !

	empty_1 = "|]" + ret
	empty_2 = "|||||]" + ret
	empty_3 = "|||]" + ret
	code_gravada = '1001'

#               str(order.amount_total_net) + eol + ret + \


	# Sale 
	if order.state in ['sale']:

		table_4 = code_gravada        + sep + \
					acc.fmt(order.amount_total_net) + eol + ret + \
					empty_1     + \
					empty_1     + \
					empty_1     + \
					empty_1     + \
					empty_2     + \
					empty_3     + \
					eot + ret

	# Cancel 
	else: 

		table_4 = code_gravada        + sep + \
					acc.fmt(order.amount_total_net) + eol + ret + \
					empty_1     + \
					empty_1     + \
					empty_1     + \
					empty_1     + \
					empty_2     + \
					eot + ret





# Table 5 - Addtional Property - Optional
# |]
# |]
# |]
# !
	empty_1 = "|]" + ret

	# Sale 
	if order.state in ['sale']:
		
		table_5 = empty_1     + \
					empty_1     + \
					empty_1     + \
					eot + ret
	
	# Cancel 
	else: 
		
		table_5 = empty_1     + \
					eot + ret





# Table 6 - Invoice order

# Producto 1|NIU|40.00|1120.00|
# 33.04|01|||
# 201.60|10|1000|IGV|VAT|
# |||||
# 040010007|28.00|
# |]



# Producto 2|NIU|10.00|150.00|17.7|01|||27|10|1000|IGV|VAT||||||040010008|15.00||]
# !

	# Init
	blank = ""
	unit_code = "NIU"
	tax_exemption_reason_code = "10"        # ver
	table_6 = ""

	price_type_code = "01"


	# Loop
	for line in order.electronic_line_ids:

		account_code = acc.get_account_code(line.product_id)

		#print line
		#print line.product_id.name
		#print line.product_uom_qty
		#print line.price_unit
		#print line.price_tax
		#print line.price_unit_net
		#print account_code


#                   str(line.product_uom_qty)       + sep + \
#                   str(line.price_net)             + sep + \
#                   str(line.price_unit)            + sep + \
#                   str(line.price_tax)             + sep + \
#                   str(line.price_unit_net)        + sep + \

		in_line = line.product_id.name            + sep + \
					unit_code                       + sep + \
					acc.fmt(line.product_uom_qty)       + sep + \
					acc.fmt(line.price_net)             + sep + \
					acc.fmt(line.price_unit)            + sep + \
					price_type_code                 + sep + \
					blank                           + sep + \
					blank                           + sep + \
					acc.fmt(line.price_tax)             + sep + \
					tax_exemption_reason_code       + sep + \
					tax_id                          + sep + \
					tax_name                        + sep + \
					tax_type_code                   + sep + \
					blank                           + sep + \
					blank                           + sep + \
					blank                           + sep + \
					blank                           + sep + \
					blank                           + sep + \
					account_code                    + sep + \
					acc.fmt(line.price_unit_net)        + sep + \
					blank                           + sep + \
					blank                           + eol + ret


		table_6 = table_6 + in_line

	# End of table
	table_6 = table_6 + eot




	# Content
	content = table_1 + table_2 + table_3 + table_4 + table_5 + table_6

	return content

# format_txt


#------------------------------------------------ Get File Name -----------------------------------
def get_file_name(order):
	"""
	high level support for doing this and that.
	"""
	#print
	#print 'Get File Name'


	# Prefix
	#if order.state in ['sale']:
	#    type_prefix = _DIC_PREFIX[order.type_code]
	#elif order.state in ['cancel']:
	#    type_prefix = _DIC_PREFIX_CANCEL[order.type_code]
	
	type_prefix = _DIC_PREFIX[order.type_code]


	# Id Serial Nr
	nr_zeros = 8
	order.id_serial_nr = type_prefix + '-' + str(order.counter_value).zfill(nr_zeros)


	date_export = order.export_date.replace("-", "")


	if order.state in ['sale', 'cancel']: 
		type_code = order.type_code
	else:   
		type_code = '07'


	#name = 'RUC' + order.ruc + '-' + order.type_code + '-' + date_export + '-' + order.id_serial_nr
	#name = 'RUC' + order.ruc + '-' + type_code + '-' + date_export + '-' + order.id_serial_nr
	name = 'RUC' + order.ruc + '-' + type_code + '-' + date_export + '-' + order.serial_nr

	return name
# get_file_name



#------------------------------------------------ Get File Content --------------------------------
# Get File Content
def get_file_content(order):
	"""
	high level support for doing this and that.
	"""
	return format_txt(order)
# get_file_content
