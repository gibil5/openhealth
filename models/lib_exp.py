# -*- coding: utf-8 -*-
#
# 		lib_exp.py
#
# 		Created: 			13 Aug 2018
# 		Last up: 	 		19 Oct 2018
#
import lib_vars as lvars
import account as acc



#------------------------------------------------ File Name ---------------------------------------------------
def get_file_name(order):
	#print 
	#print 'Get File Name'
	
	# Prefix 
	if order.state in ['sale']: 
		type_prefix = lvars._dic_prefix[order.type_code]
	elif order.state in ['cancel']: 
		type_prefix = lvars._dic_prefix_cancel[order.type_code]
	
	# Id Serial Nr
	nr_zeros = 8 
	order.id_serial_nr = type_prefix + '-' + str(order.counter_value).zfill(nr_zeros)
	
	name = 'RUC' + order.ruc + '-' + order.type_code  + '-' + order.export_date.replace("-", "") + '-' + order.id_serial_nr
	return name 


#------------------------------------------------ File Content ---------------------------------------------------
# Get File Content  
def get_file_content(order):
	#print 
	#print 'Get File Content'
	return format_txt(order)




#------------------------------------------------ Format Txt ---------------------------------------------------
# Format Txt  
def format_txt(order):
	print 
	print 'Format Txt'

	# Init 
	#lr = "\n"
	lr = "\r\n"
	se = "|"			# Data 	
	eol = "]"			# order 
	eot = "!"			# Table 
	empty_field = "|"		
	blank = ""		
	additional_account_id = "6"

	# Prefix 
	if order.state in ['sale']: 
		type_prefix = lvars._dic_prefix[order.type_code]
	elif order.state in ['cancel']: 
		type_prefix = lvars._dic_prefix_cancel[order.type_code]





# Table 1 - General, Emitter and Receptor 

# 01|F001-00007777|2018-07-12|PEN||||||||correo@gmail.com]
# 20478087820|6|CONTASIS SAC||150101|Jr. Lima 150|||||PE]
# 20345079491|6|contacom  SAC|Jr. pichis Nro. 106]
# !

	# Data General 
	general = 	order.type_code + se + \
				order.id_serial_nr + se + \
				order.export_date + se + \
				order.currency_code + \
				se + \
				se + \
				se + \
				se + \
				se + \
				se + \
				se + \
				se + eol 



	# Data Emitter
	emitter = 	order.ruc 				+ se + \
				additional_account_id 	+ se + \
				order.firm 				+ se + \
				blank 					+ se + \
				order.ubigeo 			+ se + \
				order.address 			+ se + \
				blank 					+ se + \
				blank 					+ se + \
				blank 					+ se + \
				blank 					+ se + \
				order.country 			+ eol 




	# Data Receptor 
	#print 'Receptor'
	#print order.id_doc
	#print order.id_doc_type_code
	#print order.patient.name

	receptor = 	order.id_doc 				+ se + \
				order.id_doc_type_code 		+ se + \
				order.receptor 				+ se + \
				order.patient.street 	+ eol 



	# Table 1 
	table_1 = 	general  	+ lr + \
				emitter  	+ lr + \
				receptor 	+ lr + \
				eot 		+ lr




# Table 2 - Optional 
# 228.60|1000|IGV|VAT]		# opt 
# |||]
# |||]
# !
	empty_line = "|||]" + lr 

	tax_id = "1000"							# ver
	tax_name = "IGV"
	tax_type_code = "VAT"



	#table_2 = 	str(order.amount_total_tax) 	+ se + \
	#table_2 = 	"%.2f"%order.amount_total_tax 	+ se + \
	table_2 = 	acc.fmt(order.amount_total_tax) 	+ se + \
				tax_id 							+ se + \
				tax_name 						+ se + \
				tax_type_code 					+ eol + lr + \
				empty_line + \
				empty_line + \
				eot + lr





# Table 3 - Total  
# |1498.60|10.00]
# !
#				str(order.amount_total) 	+ se + \

	table_3 = 	blank 						+ se + \
				acc.fmt(order.amount_total) 	+ se + \
				blank 						+ eol + lr + \
				eot + lr






# Table 4 - Tax
# 1001|1270.00]
# |]
# |]
# |]
# 2005|10.00]
# |||||]
# |||]
# !


	empty_1 = "|]" + lr 
	empty_2 = "|||||]" + lr 
	#empty_3 = "||]" + lr 
	empty_3 = "|||]" + lr 

	code_gravada = '1001'

#				str(order.amount_total_net) + eol + lr + \


	table_4 = 	code_gravada 		+ se + \
				acc.fmt(order.amount_total_net) + eol + lr + \
				empty_1 	+ \
				empty_1 	+ \
				empty_1 	+ \
				empty_1 	+ \
				empty_2 	+ \
				empty_3 	+ \
				eot + lr




# Table 5 - Addtional Property - Optional 
# |]
# |]
# |]
# !
	empty_1 = "|]" + lr 

	table_5 = 	empty_1 	+ \
				empty_1 	+ \
				empty_1 	+ \
				eot + lr






# Table 6 - Invoiceorder 

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
	tax_exemption_reason_code = "10"		# ver
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


#					str(line.product_uom_qty)  		+ se + \
#					str(line.price_net)				+ se + \
#					str(line.price_unit)			+ se + \
#					str(line.price_tax)				+ se + \
#					str(line.price_unit_net)		+ se + \

		in_line = 	line.product_id.name 			+ se + \
					unit_code 						+ se + \
					acc.fmt(line.product_uom_qty)  		+ se + \
					acc.fmt(line.price_net)				+ se + \
					acc.fmt(line.price_unit)			+ se + \
					price_type_code 				+ se + \
					blank 							+ se + \
					blank 							+ se + \
					acc.fmt(line.price_tax)				+ se + \
					tax_exemption_reason_code 		+ se + \
					tax_id  						+ se + \
					tax_name   						+ se + \
					tax_type_code  					+ se + \
					blank							+ se + \
					blank 							+ se + \
					blank 							+ se + \
					blank 							+ se + \
					blank 							+ se + \
					account_code 					+ se + \
					acc.fmt(line.price_unit_net)		+ se + \
					blank							+ se + \
					blank 							+ eol + lr 


		table_6 = table_6 + in_line

	# End of table 
	table_6 = table_6 + eot



	# Content 
	content = table_1 + table_2 + table_3 + table_4 + table_5 + table_6

	return content

# format_txt


