# -*- coding: utf-8 -*-
#
# 	lib.py
#
# 	Abstract, general purpose. 
#	Can be Unit-tested. Is completely standard. 
#	Gives service to all Users
# 
# 	Created: 			13 Aug 2018
# 	Last up: 	 		25 Aug 2018
#
import datetime
import unicodedata



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

