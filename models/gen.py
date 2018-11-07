# -*- coding: utf-8 -*-
"""
 		gen.py

 		Generates Names and Description, from Short Names. 
 
 		Created: 			21 Sep 2018
		Last up: 	 		 5 Nov 2018
"""
import gen_vars as gv



#------------------------------------------------  Products - 1 Param ---------------------------------------------------
# Get Generated - 1 Param
def get_generated_prod(short_name):
	#print 
	#print 'Get Generated Prod'
	generated = ''
	prod = 		short_name
	if 	prod in gv._dic_prod: 

			generated = gv._dic_prod[prod]

	return generated



#------------------------------------------------  Consultations - 2 Params ---------------------------------------------------
# Get Generated - 2 Params 
def get_generated_con(short_name):
	#print 
	#print 'Get Generated Con'
	generated = ''
	tre = 		short_name.split('_')[0]
	zone = 		short_name.split('_')[1]
	if 	tre in gv._dic_tre and zone in gv._dic_zo: 

			generated = gv._dic_tre[tre] + ' ' + gv._dic_zo[zone]

	return generated




#------------------------------------------------ Co2 - 3 Params ---------------------------------------------------
# Get Generated - 3 Params 
def get_generated_co2(short_name):
	#print 
	#print 'Get Generated Co2'
	generated = ''
	tre = 		short_name.split('_')[0]
	zone = 		short_name.split('_')[1]
	patho = 	short_name.split('_')[2][:2]
	deg = 		short_name.split('_')[2][-1:]
	third = 	short_name.split('_')[2]

	# All but MT 
	if third != 'mon': 	
		if 	tre in gv._dic_tre 	and 	zone in gv._dic_zo 	and 	patho in gv._dic_patho_co2 	and 	deg in gv._dic_deg:

				generated = gv._dic_tre[tre] + ' - ' + gv._dic_zo[zone] + ' - ' + gv._dic_patho_co2[patho] + ' ' + gv._dic_deg[deg]

	# Only Monalisa Touch
	else: 

		generated = gv._dic_tre[tre] + ' - ' + gv._dic_zo[zone] + ' - ' + gv._dic_patho_co2[third]

	return generated




#------------------------------------------------  Medical - 4 Params ---------------------------------------------------
# Get Generated - 4 Params 
def get_generated_med(short_name):
	#print 
	#print 'Get Generated Med'
	generated = ''
	arr = short_name.split('_')
	# Generate 
	if len(arr) > 2: 
		tre = 		arr[0]
		zone = 		arr[1]
		patho = 	arr[2]

		# Generate 
		# Intravenous Vitamin
		if 	tre in ['ivc']: 

			generated = gv._dic_tre_med[tre]
		
		# Infiltrations 
		elif tre in ['inf']: 
		
			generated = gv._dic_tre_med[tre] + ' - ' + gv._dic_patho[patho]
		
		elif tre in gv._dic_tre_med and zone in gv._dic_zo and patho in gv._dic_patho: 

			if len(arr) > 3: 
				ses = 		arr[3]
		
				generated = gv._dic_tre_med[tre] + ' - ' + gv._dic_zo[zone] + ' - ' + gv._dic_patho[patho] + ' - ' + gv._dic_ses[ses]

	return generated





#------------------------------------------------  5 Params - Exc, Ipl, Ndyag, Cosmeto  ---------------------------------------------------
# Get Generated - 5 Params 
def get_generated_exc(short_name):
	#print 
	#print 'Get Generated Laser'

	# Init 
	generated = ''
	arr = short_name.split('_')
	tre = 		short_name.split('_')[0]
	zone = 		short_name.split('_')[1]
	patho = 	short_name.split('_')[2]

	# Prints 
	#print short_name
	#print arr 
	#print tre 
	#print zone 
	#print patho 


	# Generate 
	if len(arr) > 4: 
		time = 		short_name.split('_')[3]
		ses = 		short_name.split('_')[4]	
		if 	tre in gv._dic_tre and zone in gv._dic_zo  and patho in gv._dic_patho 	and 	time in gv._dic_time: 

				generated = gv._dic_tre[tre] + ' - ' + gv._dic_zo[zone] + ' - ' + gv._dic_patho[patho] + ' - ' + gv._dic_time[time] + ' - ' + gv._dic_ses[ses] 

	# Prints 
	#if tre in ['exc']: 
	#if True: 
	#	print 
	#	print 'Get Generated Exc'
	#	print tre + '.'
	#	print zone + '.'
	#	print patho + '.'
	#	print time + '.' 
	#	print ses + '.'
	#	print generated + '.'
	#	print 	
	return generated






#------------------------------------------------  5 Params - Quick  ---------------------------------------------------
# Get Generated - 5 Params 
def get_generated_quick(short_name):
	#print 
	#print 'Get Generated Quick'
	# Init 
	generated = ''
	arr = short_name.split('_')
	tre = 		arr[0]
	zone = 		arr[1]
	patho = 	arr[2]
	# Generate
	if len(arr) > 4: 
		time = 		short_name.split('_')[3]
		ses = 		short_name.split('_')[4]
		if 	tre in gv._dic_tre 	and 	zone in gv._dic_zo 	and 	patho in gv._dic_patho:

			generated = gv._dic_tre[tre] + ' - ' + gv._dic_zo[zone] + ' - ' + gv._dic_patho[patho] + ' - ' + gv._dic_time[time] + ' - ' + gv._dic_ses[ses]
	
	return generated

