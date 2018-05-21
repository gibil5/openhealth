# -*- coding: utf-8 -*-
#
# 	Report Marketing
# 
# Created: 				19 Mayo 2018
#

from openerp import models, fields, api

import datetime
import resap_funcs
import acc_funcs

#import matplotlib.pyplot as plt
#import numpy as np
#import pandas as pd

import collections


class Marketing(models.Model):

	#_inherit='sale.closing'

	_name = 'openhealth.marketing'

	#_order = 'create_date desc'
	#_order = 'date_begin asc'
	_order = 'date_begin asc,name asc'






# ----------------------------------------------------------- Correct ------------------------------------------------------
	
	# Correct
	@api.multi
	def correct_patients(self):  
		print 
		print 'Correct Patients'

		# Loop 
		for line in self.patient_line: 
			# Filter 1 
			if line.patient.x_date_record == False: 
				# Filter 2
				if line.patient.x_date_record != line.patient.create_date:
					# This !
					line.patient.x_date_record = line.patient.create_date
					print 'Correct !'
		print 




# ----------------------------------------------------------- Histogram ------------------------------------------------------

	# Histogram
	@api.multi
	def show_histogram(self):  

		print 
		print 'Show Histogram'



		# Input Array
		#inp_arr = [15, 25, 26, 30, 44, 70]
		inp_arr = []
		for line in self.patient_line: 
			if line.age_years not in [0, -1]: 
				inp_arr.append(line.age_years)
		print inp_arr


		# Bins
		inp_bins = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 100]



		# Histogram 
		#histo = np.histogram([1, 2, 1], bins=[0, 1, 2, 3])
		histo = np.histogram(inp_arr, bins=inp_bins)

		bins = histo[1]
		counts = histo[0]

		print bins
		print counts



		# Total 
		total = len(inp_arr)



		idx = 0 
		idx_max = 14


		# Clear 
		self.histo_line.unlink()


		for count in counts: 

			if idx < idx_max: 

				x_bin = bins[idx]

				print idx 
				print x_bin
				print count 

				line = self.histo_line.create({
												'count': count, 
												'x_bin': x_bin, 
												'idx': idx, 
												'total': total, 

												'marketing_id': self.id, 
						})

				line.update_fields()
				idx = idx + 1
				print

	# show_histogram






# ----------------------------------------------------------- Relational ------------------------------------------------------

	# Patient Lines 
	patient_line = fields.One2many(
			'openhealth.patient.line', 

			'marketing_id', 
		)


	# Histo Lines 
	histo_line = fields.One2many(
			'openhealth.histo.line', 
			
			'marketing_id', 
		)





	# Country 
	country_line = fields.One2many(
			#'openhealth.place.line', 
			'openhealth.country.line', 
			
			'marketing_id', 
		)

	# City 
	city_line = fields.One2many(
			#'openhealth.place.line', 
			'openhealth.city.line', 
			
			'marketing_id', 
		)

	# District 
	district_line = fields.One2many(
			#'openhealth.place.line', 
			'openhealth.district.line', 
			
			'marketing_id', 
		)












# ----------------------------------------------------------- Primitives ------------------------------------------------------
	
	# Name 
	name = fields.Char(
			string="Nombre", 		
			required=True, 
		)



	# Type 
	x_type = fields.Selection(

			selection=[	
						('order', 		'Ventas'),
						('patient', 	'Pacientes'),
			], 

			string="Tipo",
			required=True, 
		)






	# Dates
	#date = fields.Date(
	#		string="Fecha", 
	#		default = fields.Date.today, 
			#readonly=True,
	#		required=True, 
	#	)



	date_begin = fields.Date(
			string="Fecha Inicio", 
			default = fields.Date.today, 
			#readonly=True,
			required=True, 
		)


	date_end = fields.Date(
			string="Fecha Fin", 
			default = fields.Date.today, 
			#readonly=True,
			required=True, 
		)








	# Totals
	#total_amount = fields.Float(
			#'Total Monto',
	#		'Total',
	#		readonly=True, 
	#	)



	# Totals Count
	total_count = fields.Integer(
			#'Total Ventas',
			#'Nr Pacientes',
			'Nr',
			readonly=True, 
		)



	# Spacing
	vspace = fields.Char(
			' ', 
			readonly=True
		)





# ----------------------------------------------------------- Stats ------------------------------------------------------

	# Age
	age_mean = fields.Float(
			'Edad Promedio',
			readonly=True, 
		)

	age_max = fields.Integer(
			'Edad Max',
			readonly=True, 
		)

	age_min = fields.Integer(
			'Edad Min',
			readonly=True, 
		)

	age_undefined = fields.Integer(
			'Edad Ind',
			readonly=True, 
		)

	age_undefined_per = fields.Float(
			'I %',
			readonly=True, 
		)





	# Sex
	sex_male = fields.Integer(
			'Sexo M',
			readonly=True, 
		)

	sex_female = fields.Integer(
			'Sexo F',
			readonly=True, 
		)

	sex_undefined = fields.Integer(
			'Sexo Ind',
			readonly=True, 
		)


	# Per
	sex_male_per = fields.Float(
			'M %',
			#'%',
			readonly=True, 
		)

	sex_female_per = fields.Float(
			'F %',
			#'%',
			readonly=True, 
		)

	sex_undefined_per = fields.Float(
			#'%',
			'I %',
			readonly=True, 
		)









	# First Contact 

# how_u 
# how_none 
# how_reco 
# how_tv
# how_radio
# how_inter
# how_web
# how_mail 


	how_u = fields.Integer(
			'Pri Indefinido',
			readonly=True, 
		)

	how_none = fields.Integer(
			'Pri Ninguno',
			readonly=True, 
		)

	how_reco = fields.Integer(
			'Pri Recomendación',
			readonly=True, 
		)

	how_tv = fields.Integer(
			'Pri Tv',
			readonly=True, 
		)

	how_radio = fields.Integer(
			'Pri Radio',
			readonly=True, 
		)

	how_inter = fields.Integer(
			'Pri Internet',
			readonly=True, 
		)

	how_web = fields.Integer(
			'Pri Web',
			readonly=True, 
		)

	how_mail = fields.Integer(
			'Pri Mail',
			readonly=True, 
		)





	# Percentages 
	how_u_per = fields.Float(
			'Indefinido %',
			readonly=True, 
		)

	how_none_per = fields.Float(
			'Ninguno %',
			readonly=True, 
		)

	how_reco_per = fields.Float(
			'Recomendación %',
			readonly=True, 
		)

	how_tv_per = fields.Float(
			'Tv %',
			readonly=True, 
		)

	how_radio_per = fields.Float(
			'Radio %',
			readonly=True, 
		)

	how_inter_per = fields.Float(
			'Internet %',
			readonly=True, 
		)

	how_web_per = fields.Float(
			'Web %',
			readonly=True, 
		)

	how_mail_per = fields.Float(
			'Mail %',
			readonly=True, 
		)







	# Education

#_education_level_type = [
#			('first', 'Primaria'),
#			('second', 'Secundaria'),
#			('technical', 'Instituto'),
#			('university', 'Universidad'),
#			('masterphd', 'Posgrado'),
#			]

# edu_u 
# edu_fir 
# edu_sec
# edu_tec 
# edu_uni 
# edu_mas 


	edu_u = fields.Integer(
			'Edu Indefinido',
			readonly=True, 
		)

	edu_fir = fields.Integer(
			'Edu Primaria',
			readonly=True, 
		)

	edu_sec = fields.Integer(
			'Edu Secundaria',
			readonly=True, 
		)
	
	edu_tec = fields.Integer(
			'Edu Instituto',
			readonly=True, 
		)
	
	edu_uni = fields.Integer(
			'Edu Universidad',
			readonly=True, 
		)
	
	edu_mas = fields.Integer(
			'Edu Posgrado',
			readonly=True, 
		)





	# Percentage
	edu_u_per = fields.Float(
			'Indefinido %',
			readonly=True, 
		)

	edu_fir_per = fields.Float(
			'Primaria %',
			readonly=True, 
		)

	edu_sec_per = fields.Float(
			'Secundaria %',
			readonly=True, 
		)
	
	edu_tec_per = fields.Float(
			'Instituto %',
			readonly=True, 
		)
	
	edu_uni_per = fields.Float(
			'Universidad %',
			readonly=True, 
		)
	
	edu_mas_per = fields.Float(
			'Posgrado %',
			readonly=True, 
		)





	

	# Vip 

# vip_true
# vip_false
# vip_true_per
# vip_false_per

	vip_true = fields.Integer(
			'Vip Si',
			readonly=True, 
		)

	vip_false = fields.Integer(
			'Vip No',
			readonly=True, 
		)


	vip_true_per = fields.Float(
			'Vip Si %',
			readonly=True, 
		)

	vip_false_per = fields.Float(
			'Vip No %',
			readonly=True, 
		)




	# Address






# ----------------------------------------------------------- Actions ------------------------------------------------------

# jx 
	# Get Stats
	@api.multi
	def set_stats(self):  

		print 
		print 'Set Stats'

		# Sex 
		count_m = 0
		count_f = 0
		count_u = 0


		# Age 
		count_a = 0
		age_min = 100 
		age_max = 0 
		count_age_u = 0


		# First Contact 
		how_u = 0 
		how_none = 0 
		how_reco = 0 
		how_tv = 0
		how_radio = 0 
		how_inter = 0 
		how_web = 0 
		how_mail = 0 


		# Education 
		edu_u = 0
		edu_fir = 0
		edu_sec = 0
		edu_tec = 0
		edu_uni = 0
		edu_mas = 0


		# Vip 
		vip_true = 0 
		vip_false = 0 



		# Address
		country_arr = []
		city_arr = []
		district_arr = []




		# Loop 
		for line in self.patient_line: 


			# Sex
			if line.sex == 'Male': 
				count_m = count_m + 1
			elif line.sex == 'Female': 
				count_f = count_f + 1
			else: 
				count_u = count_u + 1



			# Age
			if line.age_years not in[ -1, 0]: 
				count_a = count_a + line.age_years 
				if line.age_years > age_max: 
					age_max = line.age_years
				if line.age_years < age_min: 
					age_min = line.age_years
			else: 
				count_age_u = count_age_u + 1




			# First Contact 
			if line.first_contact == 'none': 
				how_none = how_none + 1

			elif line.first_contact == 'recommendation': 
				how_reco = how_reco + 1

			elif line.first_contact == 'tv': 
				how_tv = how_tv + 1

			elif line.first_contact == 'radio': 
				how_radio = how_radio + 1

			elif line.first_contact == 'internet': 
				how_inter = how_inter + 1

			elif line.first_contact == 'website':
				how_web = how_web + 1

			elif line.first_contact == 'mail_campaign':
				how_mail = how_mail + 1

			else: 
				how_u = how_u + 1








			# Education 
			if line.education == 'first': 
				edu_fir = edu_fir + 1

			elif line.education == 'second': 
				edu_sec = edu_sec + 1

			elif line.education == 'technical': 
				edu_tec = edu_tec + 1

			elif line.education == 'university': 
				edu_uni = edu_uni + 1

			elif line.education == 'masterphd': 
				edu_mas = edu_mas + 1

			else: 
				edu_u = edu_u + 1




			# Vip 
			if line.vip: 
				vip_true = vip_true + 1

			else: 
				vip_false = vip_false + 1





			
			# Using collections

			# Address
			country_arr.append(line.country)

			city_arr.append(line.city)

			# Only for Lima 
			if line.city in ['Lima']: 
				district_arr.append(line.district)





		# Sex 
		# Absolutes 
		self.sex_male = count_m
		self.sex_female = count_f
		self.sex_undefined = count_u

		# Per
		self.sex_male_per = ( float(self.sex_male) / float(self.total_count) ) * 100
		self.sex_female_per = ( float(self.sex_female) / float(self.total_count) ) * 100
		self.sex_undefined_per = ( float(self.sex_undefined) / float(self.total_count) ) * 100



		# Ages 
		self.age_mean = count_a / self.total_count
		self.age_min = age_min
		self.age_max = age_max
		self.age_undefined = count_age_u
		self.age_undefined_per = ( float(self.age_undefined) / float(self.total_count) ) * 100



		# First Contact
		self.how_none = how_none
		self.how_reco = how_reco
		self.how_tv = how_tv
		self.how_radio = how_radio		
		self.how_inter = how_inter
		self.how_web = how_web
		self.how_mail = how_mail
		self.how_u = how_u

		# Per
		self.how_none_per = resap_funcs.get_per(self, how_none, self.total_count)
		self.how_reco_per = resap_funcs.get_per(self, how_reco, self.total_count)
		self.how_tv_per = resap_funcs.get_per(self, how_tv, self.total_count)
		self.how_radio_per = resap_funcs.get_per(self, how_radio, self.total_count)
		self.how_inter_per = resap_funcs.get_per(self, how_inter, self.total_count)
		self.how_web_per = resap_funcs.get_per(self, how_web, self.total_count)
		self.how_mail_per = resap_funcs.get_per(self, how_mail, self.total_count)
		self.how_u_per = resap_funcs.get_per(self, how_u, self.total_count)



		# Education 
		self.edu_fir = edu_fir
		self.edu_sec = edu_sec
		self.edu_tec = edu_tec
		self.edu_uni = edu_uni
		self.edu_mas = edu_mas
		self.edu_u = edu_u

		# Per 
		self.edu_fir_per = resap_funcs.get_per(self, edu_fir, self.total_count)
		self.edu_sec_per = resap_funcs.get_per(self, edu_sec, self.total_count)
		self.edu_tec_per = resap_funcs.get_per(self, edu_tec, self.total_count)
		self.edu_uni_per = resap_funcs.get_per(self, edu_uni, self.total_count)
		self.edu_mas_per = resap_funcs.get_per(self, edu_mas, self.total_count)
		self.edu_u_per = resap_funcs.get_per(self, edu_u, self.total_count)




		# Vip 
		self.vip_true = vip_true
		self.vip_false = vip_false

		 # Per 
		self.vip_true_per = resap_funcs.get_per(self, vip_true, self.total_count)
		self.vip_false_per = resap_funcs.get_per(self, vip_false, self.total_count)





		
		# Using collections
		
		# City 
		counter_country = collections.Counter(country_arr)

		counter_city = collections.Counter(city_arr)
		
		counter_district = collections.Counter(district_arr)


		#print country_arr
		#print 
		#print city_arr
		#print 
		#print district_arr
		print 
		print 
		print counter_country
		print 

		#print counter_country['Peru']


		self.country_line.unlink()
		self.city_line.unlink()
		self.district_line.unlink()



		# Country
		print 'Create Country Line '
		for key in counter_country: 

			count = counter_country[key]

			country = self.country_line.create({
													'name': key, 

													#'count': count, 
													'x_count': count, 


													'marketing_id': self.id, 
												})
			#print key 
			#print count
			#print country

		print self.country_line
		print 



		
		# City 
		print 'Create City Line '
		for key in counter_city: 

			count = counter_city[key]
			
			city = self.city_line.create({
													'name': key, 

													#'count': count, 
													'x_count': count, 

													'marketing_id': self.id, 
												})
			#print key 
			#print count
			#print country

		print self.city_line
		print 
		

		# District 
		print 'Create District Line '
		for key in counter_district: 

			count = counter_district[key]
			
			district = self.district_line.create({
													'name': key, 

													#'count': count, 
													'x_count': count, 

													'marketing_id': self.id, 
												})

			#print key 
			#print count
			#print country

		print self.district_line
		print 



		#print counter_city
		#print 
		#print counter_district
		print 
		print 


# Counter({u'Peru': 92, u'United States': 1})






# ----------------------------------------------------------- Update ------------------------------------------------------

	# Update Patients
	@api.multi
	def update_patients(self):  

		print
		print 'Update Patients'


		# Clear 
		self.patient_line.unlink()



		# Orders 
		patients,count = resap_funcs.get_patients_filter(self, self.date_begin, self.date_end)

		self.total_count = count


		#amount_sum = 0 
		#count = 0 



		# Loop 
		for patient in patients: 

			#count = count + 1


			pat_line = self.patient_line.create({
														'patient': patient.id, 
														
														'date_create': patient.create_date,

														'date_record': patient.x_date_record,


														
														'sex': patient.sex, 

														'dob': patient.dob, 

														'age': patient.age, 



														'first_contact': patient.x_first_contact, 

														'education': patient.x_education_level, 

														'vip': patient.x_vip, 



														
														'country': patient.country_id.name, 

														#'city': patient.city.title(), 
														'city': patient.city, 

														#'district': patient.street2.title(), 
														'district': patient.street2, 




														'marketing_id': self.id, 
					})



			ret = pat_line.update_fields()


			if ret == -1:
				print 'Age undefined !'



		# Stats 
		self.set_stats()

	# update_patients


