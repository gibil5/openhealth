# -*- coding: utf-8 -*-
#
# 		lib.py
#
# 		Abstract, general purpose. Can be Unit-tested. Is completely standard. Gives service to all Users
# 
# 		Created: 			13 Aug 2018
# 		Last up: 	 		20 Sep 2018
#
import datetime
import unicodedata
import account



#------------------------------------------------ Checksum ---------------------------------------------------
# Get Checksum Generated
def get_checksum_tic(generated):
	#print 
	#print 'Get Checksum'

	if generated == 'x': 
		checksum = '0'
	else: 
		checksum = '1'

	return checksum




#------------------------------------------------ Checksum ---------------------------------------------------
# Get Checksum Generated
def get_checksum_gen(generated, name):
	#print 
	#print 'Get Checksum'

	if generated == name: 
		checksum = '1'
	else: 
		checksum = '0'
	return checksum




#------------------------------------------------ Format Txt ---------------------------------------------------
# Format Txt  
def format_txt(order):
	print 
	print 'Format Txt'

	# Init 
	se = "|"			# Data 
	eol = "]"			# order 
	eot = "!"			# Table 
	lr = "\n"

	empty_field = "|"		

	blank = ""		

	date_format = "%Y-%m-%d"

	type_prefix = _dic[order.type_code]


	additional_account_id = "6"





# Table 1 - General, Emitter and Receptor 

# 01|F001-00007777|2018-07-12|PEN||||||||correo@gmail.com]
# 20478087820|6|CONTASIS SAC||150101|Jr. Lima 150|||||PE]
# 20345079491|6|contacom  SAC|Jr. pichis Nro. 106]
# !


	# Data General 
	general = 	order.type_code + se + \
				order.id_serial_nr + se + \
				get_todays_name(date_format) + se + \
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
				blank 					+ se + \
				blank 					+ se + \
				blank 					+ se + \
				blank 					+ se + \
				blank 					+ se + \
				blank 					+ se + \
				blank 					+ eol 



	# Data Receptor 
	#print 'Receptor'
	#print order.id_doc
	#print order.id_doc_type_code
	#print order.patient.name

	receptor = 	order.id_doc 			+ se + \
				order.id_doc_type_code 	+ se + \
				order.receptor 			+ se + \
				blank 					+ eol 



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



	table_2 = 	str(order.amount_total_tax) 	+ se + \
				tax_id 							+ se + \
				tax_name 						+ se + \
				tax_type_code 					+ eol + lr + \
				empty_line + \
				empty_line + \
				eot + lr





# Table 3 - Total  
# |1498.60|10.00]
# !

	table_3 = 	blank 						+ se + \
				str(order.amount_total) 	+ se + \
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
	empty_3 = "||]" + lr 

	code_gravada = '1001'



	table_4 = 	code_gravada 		+ se + \
				str(order.amount_total_net) + eol + lr + \
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



	for line in order.electronic_line_ids: 


		account_code = account.get_account_code(line.product_id)


		print line 
		print line.product_id.name
		print line.product_uom_qty
		print line.price_unit
		print line.price_tax
		print line.price_unit_net 
		#print line.product_id.default_code
		print account_code



		in_line = 	line.product_id.name 			+ se + \
					unit_code 						+ se + \
					str(line.product_uom_qty)  		+ se + \
					str(line.price_net)				+ se + \
					blank							+ se + \
					blank 							+ se + \
					blank 							+ se + \
					blank 							+ se + \
					str(line.price_tax)				+ se + \
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
					str(line.price_unit_net)		+ se + \
					blank							+ se + \
					blank 							+ eol + lr 



		table_6 = table_6 + in_line


	# End of table 
	table_6 = table_6 + eot



	# Content 
	content = table_1 + table_2 + table_3 + table_4 + table_5 + table_6

	return content









#------------------------------------------------ File Content ---------------------------------------------------
# Get File Content  
def get_file_content(order):
	print 
	print 'Get File Content'

	content = format_txt(order)

	return content




#------------------------------------------------ Get Tax ---------------------------------------------------
# Get Tax 
def get_net_tax(amount):
	#print 
	#print 'Get Tax'

	# Net 
	net = amount/1.18
	net = round(net, 2)
	
	# Tax 
	tax = net * 0.18
	tax = round(tax, 2)

	return net, tax 





#------------------------------------------------ Format Standard ---------------------------------------------------
# Format Standard  
def format_std(line):
	print 
	print 'Format Standard'

	se = ","

	content = 	correct_date(line.x_date_created) + se + \
				line.serial_nr + se + \
				line.patient.name + se + \
				line.patient.x_id_doc_type + se + \
				line.patient.x_id_doc + se + \
				line.product_id.name  

				#line.patient.x_firm + se + \
				#line.patient.x_ruc + se + \
				#line.patient.email + se + \
				
				#line.patient.name.encode('utf-8') 
				#line.patient.name + se + 
				#line.patient.x_dni + se + 
				#lr.encode('utf-8') 

	return content



#------------------------------------------------ Print ---------------------------------------------------
# Print  
#def print_line(line):
def print_line(order):
	print 
	print 'Print'

	print (order)
	print (order.x_date_created)
	print (order.patient.name)
	print (order.patient.x_id_doc)
	print (order.patient.x_id_doc_type)
	print (order.patient.x_firm)
	print (order.patient.x_ruc)
	print (order.patient.email)
	print ()
	print (order.serial_nr)
	print (order.product_id.name)
	print ()





#------------------------------------------------ Const ---------------------------------------------------
_dic = {
				#'01': 'F', 	# Invoice 
				#'03': 'B', 	# Receipt 
				'01': 'F001', 	# Invoice 
				'03': 'B001', 	# Receipt 

				#'14': 'P', 	# Advertisement 
				#'15': 'N', 	# Sale Note 
}

#------------------------------------------------ File Name ---------------------------------------------------
# Get File Name 
def get_file_name(order):
	print 
	print 'Get File Name'

# Ref 
#00009999
# Serial
#0000000575

	#date_format = "%Y_%m_%d-%H_%M_%S"
	date_format = "%Y%m%d"




	# Init 
	ruc = 'RUC' + order.ruc 
	type_code = order.type_code
	type_prefix = _dic[type_code]
	
	today_name = get_todays_name(date_format)

	
	#serial_nr = order.serial_nr
	#str(value).zfill(padding)
	#serial_nr = str(order.counter_value).zfill(nr_zeros)


	# Id Serial Nr
	nr_zeros = 8 
	order.id_serial_nr = type_prefix + '-' + str(order.counter_value).zfill(nr_zeros)


	# Prints 
	print ruc 
	print type_code
	print today_name
	print order.id_serial_nr

	#name = ruc + '-' + type_code  + '-' + today_name + '-' + type_prefix + '-' + serial_nr
	name = ruc + '-' + type_code  + '-' + today_name + '-' + order.id_serial_nr

	return name 




#------------------------------------------------ Date - Todays Name ---------------------------------------------------
# Get Todays Name
def get_todays_name(date_format):
	#print 
	#print 'Get Todays Name'


	today = datetime.datetime.today() + datetime.timedelta(hours=-5,minutes=0)	

	name = today.strftime(date_format)

	#print today
	#print name
	#print 

	#name = '2018_09_04-11_28_00'
	return name 




#------------------------------------------------ Date - Correct for Utc ---------------------------------------------------
# Correct Date 
def correct_date(date):
	print 
	print 'Correct Date'

	date_format = "%Y-%m-%d %H:%M:%S"
	
	date_dt = datetime.datetime.strptime(date, date_format) + datetime.timedelta(hours=-5,minutes=0)	

	date_s = date_dt.strftime(date_format)

	return date_s






#------------------------------------------------ Date - If Today ---------------------------------------------------
# Adds Nr to start date 
def is_today(date, state):
	#print 
	#print 'Is Today'

	#date_format = "%Y-%m-%d"
	date_format = "%Y-%m-%d %H:%M:%S"
	date_dt = datetime.datetime.strptime(date, date_format) + datetime.timedelta(hours=-5,minutes=0)	


	if date_dt.date() == datetime.datetime.today().date(): 
		is_today = True 
	else: 
		is_today = False


	# Prints
	#print date
	#print date_dt
	#print is_today 

	#return is_today 
	return is_today and state != 'Scheduled'



#------------------------------------------------ Patient - Unidecode ---------------------------------------------------

# Strip all accents - But keep Ñ
def strip_accents(s):
	good_accents = {
				    u'\N{COMBINING TILDE}',
				    #u'\N{COMBINING CEDILLA}'
	}
	#return s 
	return ''.join(c for c in unicodedata.normalize('NFD', s)
	              if unicodedata.category(c) != 'Mn'	or 	c in good_accents)
# strip_accents





#------------------------------------------------ Patient - Test content ---------------------------------------------------

# Length 
def test_for_length(self, token, length):
	print 
	print 'Lib - Test for Length'
	print token
	print length

	if token and (len(str(token))!= length):
		return {
				'warning': {
					'title': "Error: Debe tener " + str(length) + " caracteres.",
					'message': token,
				}}
	else:
		return 0
# test_for_length



# Digits 
def test_for_digits(self, token):
	if token and (not token.isdigit()):
		return {
				'warning': {
					'title': "Error: Debe ser número.",
					'message': token,
				}}
	else:
		return 0
# test_for_digits



# Name 
#def test_name(self, token):
def test_for_one_last_name(self, last_name):
	if last_name != False:
		nr_words = len(last_name.split())
		if nr_words == 1:
			return {
					'warning': {
						'title': "Error: Introduzca los dos Apellidos.",
						'message': last_name,
					}}
		else:
			return 0
# test_for_one_name





#------------------------------------------------ Get Next Date ---------------------------------------------------
# Adds Nr to start date 
def get_next_date(self, evaluation_start_date, nr_days):

	#print 
	#print 'Get Next Date'

	import datetime

	date_format = "%Y-%m-%d %H:%M:%S"

	delta = datetime.timedelta(days=nr_days)

	start = datetime.datetime.strptime(evaluation_start_date, date_format)
	
	next_date = delta + start

	return next_date

# get_next_date



# ----------------------------------------------------------- Delta from Now ------------------------------------------------------

# Delta

def get_delta_now(self, date_1): 

	#date_format = "%Y-%m-%d"
	date_format = "%Y-%m-%d %H:%M:%S"

	#date_1 = '2018-07-02 09:00:00'
	#date_2 = '2018-07-02 12:00:00'

	now = datetime.datetime.now()
	dt_1 = datetime.datetime.strptime(date_1, date_format)
	#dt_2 = datetime.datetime.strptime(date_2, date_format)

	delta = dt_1 - now 
	#delta = dt_2 - dt_1
	delta_sec = delta.total_seconds()

	return delta, delta_sec

# get_delta_now




# ----------------------------------------------------------- Get Next Slot--------------------------------------------

# Get Next Slot

def get_next_slot(self): 

	#print 
	#print 'Get Next Slot'

	# Init 
	date_format = "%Y-%m-%d %H:%M:%S"
	date_2_format = "%Y-%m-%d"
	now = datetime.datetime.now() + datetime.timedelta(hours=-5,minutes=0)	
	now_date_str = now.strftime(date_2_format)

	# Loop 
	for idx in range(0, 48): 

		#slot = lib.get_slot(idx)
		slot = get_slot(idx)

		slot_x = now_date_str + ' ' + slot
		slot_dt = datetime.datetime.strptime(slot_x, date_format)
		delta = slot_dt - now 
		delta_sec = delta.total_seconds()

		# Prints 
		#print slot
		#print slot_x
		#print slot_dt
		#print delta 
		#print delta_sec
		#print 

		if delta_sec > 0: 
			#print 'Gotcha !'
			return (slot_dt + datetime.timedelta(hours=5,minutes=0)).strftime(date_format)

	#return False							# If no slot available 
	return now_date_str + ' 14:00:00'		# If no slot available 

# get_next_slot




# ----------------------------------------------------------- Doctor Available--------------------------------------------

# Doctor Available 
# Check if not too late (before 21:00)

def doctor_available(self, app_date_str): 

	#print 
	#print 'Doctor Available'

	# Init 
	date_2_format = "%Y-%m-%d"
	now = datetime.datetime.now() + datetime.timedelta(hours=-5,minutes=0)	
	now_date_str = now.strftime(date_2_format)
	app_limit_str = now_date_str + ' 21:00:00'

	#date_format = "%H:%M:%S"
	date_format = "%Y-%m-%d %H:%M:%S"
	
	# Delta 
	app_date_dt = datetime.datetime.strptime(app_date_str, date_format) + datetime.timedelta(hours=-5,minutes=0)	
	app_limit_dt = datetime.datetime.strptime(app_limit_str, date_format)
	delta = app_limit_dt - app_date_dt
	delta_sec = delta.total_seconds()

	if delta_sec < 0: 
		available = False
	else:
		available = True

	return available 

# doctor_available





# ----------------------------------------------------------- Get Nr Days--------------------------------------------

# Get Nr Days 

def get_nr_days(self, date_ref_str, date_str): 

	#print 
	#print 'Get Nr Days'
	#print date_ref_str
	#print date_str

	# Init
	delta_days = 0 
	
	if date_ref_str != False and date_str != False: 

		#date_format_2 = "%Y-%m-%d %H:%M:%S"
		date_format = "%Y-%m-%d"

		date_ref_str = date_ref_str.split()[0]
		date_ref_dt = datetime.datetime.strptime(date_ref_str, date_format)

		date_str = date_str.split()[0]
		date_dt = datetime.datetime.strptime(date_str, date_format)

		delta = date_dt - date_ref_dt
	
		#delta_sec = delta.total_seconds()
		delta_days = delta.days

	return delta_days



#------------------------------------------------ Get Slot ---------------------------------------------------

# Change the state of the Object 

def get_slot(idx):
	
	#print 
	#print 'Get Slot'

	date_format = "%H:%M:%S"

	date_str = "09:00:00"

	date_dt = datetime.datetime.strptime(date_str, date_format) + datetime.timedelta(minutes=idx*15)	

	slot = date_dt.strftime(date_format)

	return slot


#------------------------------------------------ Change State ---------------------------------------------------

# Change the state of the Object 

def change_state(obj, state):
	#print 
	#print 'Change State'

	#print obj
	#print obj.state 
	#print state

	if obj.state != False: 
		obj.state = state

# change_state

