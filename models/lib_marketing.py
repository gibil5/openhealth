# -*- coding: utf-8 -*-
"""
 	lib_marketing.py

 	Created: 			27 Nov 2018
 	Last up: 	 		27 Nov 2018
"""
import collections
try:
	import numpy as np
except (ImportError, IOError) as err:
	_logger.debug(err)

from . import pat_vars
from . import mkt_vars


# ----------------------------------------------------------- Cities ------------------------------
def build_cities(self):
	#print 
	#print 'Build Cities'

	# Create Collection

	city_arr = []

	for line in self.patient_line: 
		city_arr.append(line.city)

	counter_city = collections.Counter(city_arr)


	city_arr = [
				'Lima',
				'Abancay',
				'Huaraz', 
				'Ancash',
				'Arequipa',
				'Ayacucho',
				'Cajamarca',
				'Callao',
				'Cerro de Pasco', 
				'Chachapoyas',
				'Chiclayo',
				'Cuzco',
				'Huacho',
				'Huancavelica',
				'Huancayo',
				'Huanuco',	
				'Ica',
				'Iquitos',
				'Moquegua',
				'Moyobamba',
				'Piura',
				'Pucallpa',
				'Puerto Maldonado', 
				'Puno',
				'Tacna',
				'Trujillo',
				'Tumbes',
				'Otros',
				]


	_h_sector_city =  {
					'Lima':			'Lima',
					'Callao': 		'Lima',
					'Huacho': 		'Lima',
					'Ancash': 		'Centro',
					'Huancavelica': 'Centro',
					'Huancayo': 	'Centro',
					'Huanuco': 		'Centro',
					'Huaraz': 		'Centro', 
					'Pucallpa': 	'Centro',
					'Cerro de Pasco': 	'Centro', 
					'Chiclayo': 	'Costa Norte',
					'Cajamarca': 	'Costa Norte',
					'Piura': 		'Costa Norte',
					'Trujillo': 	'Costa Norte',
					'Tumbes': 		'Costa Norte',
					'Ica': 			'Costa Sur',
					'Arequipa': 	'Costa Sur',
					'Tacna': 		'Costa Sur',
					'Moquegua': 	'Costa Sur',
					'Abancay': 		'Sur Este',
					'Ayacucho': 	'Sur Este',
					'Cuzco': 		'Sur Este',
					'Puerto Maldonado': 	'Sur Este', 		# Madre de Dios 
					'Puno': 		'Sur Este',
					'Iquitos': 		'Nor Este',
					'Chachapoyas': 	'Nor Este',
					'Moyobamba': 	'Nor Este',						# San Martin
					'Otros': 		'Otros',
				}


	# Clear 
	self.city_line.unlink()


	# Loop 
	for city in city_arr: 
		
		# Init vars 
		sector = _h_sector_city[city]


		# Count - Search in Collections 
		if city in counter_city: 
			count = counter_city[city]
		else: 
			count = 0 


		# Create 
		line = self.city_line.create({
											'name' : 		city, 
											'sector' : 		sector, 
											'count' :		count,
											'marketing_id' :	self.id, 
									})
		
		# Update 
		line.update_fields()

# build_cities




# ----------------------------------------------------------- Districts ---------------------------
def build_districts(self):  
	#print 
	#print 'Build Districts'


	# Create Collection
	district_arr = []
	for line in self.patient_line: 
		if line.city in ['Lima']: 
			district_arr.append(line.district)

	counter_district = collections.Counter(district_arr)


	# Clear 
	self.district_line.unlink()


	# Build Code Array 
	code_arr = np.arange(44)


	# Loop 
	for code in code_arr: 
		
		if code != 0: 


			# Init vars
			name = pat_vars.zip_dic_inv[code]

			#sector = pat_vars._h_sector[name]
			sector = mkt_vars._h_sector[name]


			# Count - Search in Collections 
			if name in counter_district: 
				count = counter_district[name]
			else: 
				count = 0 


			# Create 
			line = self.district_line.create({
												'code' :		code, 
												'name' : 		name, 
												'sector' : 		sector, 
												'count' :		count,
												'marketing_id' :	self.id, 
										})
			# Update 
			line.update_fields()

# build_districts






# ----------------------------------------------------------- Media -------------------------------
def build_media(self):  
	#print 
	#print 'Build Media'

	# Clear 
	self.media_line.unlink()


	# Build 
	media_arr = [
					'none', 
					'recommendation', 
					'tv', 
					'internet', 
					'website', 
					'mail', 
					'undefined', 
				]

	idx = 0 

	for media in media_arr: 

		if media == 'none': 
			count = self.how_none
		
		elif media == 'recommendation': 
			count = self.how_reco
		
		elif media == 'tv': 
			count = self.how_tv

		elif media == 'internet': 
			count = self.how_inter

		elif media == 'website': 
			count = self.how_web

		elif media == 'mail': 
			count = self.how_mail

		elif media == 'undefined': 
			count = self.how_u  

		total = self.total_count


		line = self.media_line.create({
										'name' : 	media, 
										'count' :		count, 
										'idx' : 		idx, 
										'total' :		total, 
										'marketing_id' :		self.id, 
									})

		line.update_fields()
		idx = idx + 1

# build_media





# ----------------------------------------------------------- Histogram ---------------------------
def build_histogram(self):  
	#print 
	#print 'Build Histogram'

	#input_arr = [15, 25, 26, 30, 44, 70]

	# Build Input Array
	input_arr = []
	input_arr_m = []
	input_arr_f = []

	for line in self.patient_line: 
		if line.age_years not in [0, -1]: 		# Not an Error 

			input_arr.append(line.age_years)

			if line.sex == 'Male': 
				input_arr_m.append(line.age_years)
			elif line.sex == 'Female': 
				input_arr_f.append(line.age_years)

	
	#print inp_arr


	# Bins
	inp_bins = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 100]


	# Histogram 
	#histo = np.histogram([1, 2, 1], bins=[0, 1, 2, 3])
	histo = np.histogram(input_arr, bins=inp_bins)
	histo_m = np.histogram(input_arr_m, bins=inp_bins)
	histo_f = np.histogram(input_arr_f, bins=inp_bins)


	# Update
	bins = histo[1]
	counts = histo[0]
	counts_m = histo_m[0]
	counts_f = histo_f[0]

	#print bins
	#print counts


	# Total 
	total = len(input_arr)


	# Init
	idx = 0 
	idx_max = 14

	# Clear 
	self.histo_line.unlink()

	for count in counts: 

		if idx < idx_max: 

			x_bin = bins[idx]

			#print idx 
			#print x_bin
			#print count 

			line = self.histo_line.create({
											'x_bin': x_bin, 
											'idx': idx, 
											'total': total, 
											'total_m': self.sex_male, 
											'total_f': self.sex_female, 
											'count': count, 
											'count_m': counts_m[idx], 
											'count_f': counts_f[idx], 
											'marketing_id': self.id, 
					})

			line.update_fields()
			idx = idx + 1

# build_histogram
