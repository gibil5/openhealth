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
#import openerp.addons.decimal_precision as dp


#import matplotlib.pyplot as plt
#import pandas as pd
import numpy as np
import collections


import pat_vars



class Marketing(models.Model):

	_inherit='openhealth.repo'

	_name = 'openhealth.marketing'

	#_order = 'create_date desc'
	_order = 'date_begin asc,name asc'






# ----------------------------------------------------------- Inheritable ------------------------------------------------------

	# Name 
	#name = fields.Char(
	#		string="Nombre", 		
	#		required=True, 
	#	)


	# Dates 
	#date_begin = fields.Date(
	#		string="Fecha Inicio", 
	#		default = fields.Date.today, 
			#readonly=True,
	#		required=True, 
	#	)


	#date_end = fields.Date(
	#		string="Fecha Fin", 
	#		default = fields.Date.today, 
			#readonly=True,
	#		required=True, 
	#	)


	# Count
	#total_count = fields.Integer(
	#		'Nr',
	#		readonly=True, 
	#	)



	# Spacing
	#vspace = fields.Char(
	#		' ', 
	#		readonly=True
	#	)




	# Count
	total_count = fields.Integer(
			#'Total Ventas',
			#'Nr Ventas',
			'Nr Pacientes',
			readonly=True, 
		)






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



	# Media Lines 
	media_line = fields.One2many(
			'openhealth.media.line', 
			'marketing_id', 
		)





	# Country 
	country_line = fields.One2many(
			'openhealth.country.line', 
			'marketing_id', 
		)

	# City 
	city_line = fields.One2many(
			'openhealth.city.line', 
			'marketing_id', 
		)


	# District 
	district_line = fields.One2many(
			'openhealth.district.line', 
			'marketing_id', 
		)





# ----------------------------------------------------------- Counts ------------------------------------------------------

	patient_budget_count = fields.Integer(

			'Nr Presupuestos', 
		)


	patient_sale_count = fields.Integer(

			'Nr Ventas', 
		)

	patient_consu_count = fields.Integer(

			'Nr Consultas', 
		)

	patient_reco_count = fields.Integer(

			'Nr Recomendaciones', 
		)

	patient_proc_count = fields.Integer(

			'Nr Procedimientos', 
		)








# ----------------------------------------------------------- Update Sales ------------------------------------------------------

	# Update Patients
	@api.multi
	def update_sales(self):  

		print
		print 'Update Sales'
		print 


		# Clean Macros 
		self.patient_budget_count = 0 
		self.patient_sale_count = 0 
		self.patient_consu_count = 0 
		self.patient_proc_count = 0 




		# Patient Lines 
		for pat_line in self.patient_line: 


			# Update Mkt 
			pat_line.update_fields_mkt()






		# Budgets
			budgets = self.env['sale.order'].search([
															('state', '=', 'draft'),
															('patient', '=', pat_line.patient.name),
													],
														order='date_order asc',
														#limit=1,
												)
			# Clean 
			pat_line.budget_line.unlink()

			# Create
			for budget in budgets: 


				# Doctor 
				doctor = budget.x_doctor


				for line in budget.order_line: 
					

					# Budget is a procedure 
					if line.price_total >= 1500: 

						# Budgets 
						budget_line = pat_line.budget_line.create({
																	'name': line.name, 

																	'doctor': doctor.id, 


																	'product_id': line.product_id.id, 
																	'x_date_created': budget.date_order, 
																	'product_uom_qty': line.product_uom_qty, 
																	'price_unit': line.price_unit, 

																	'patient_line_budget_id': pat_line.id, 
																	'marketing_id': self.id, 
							})



			# Count
			self.patient_budget_count = self.patient_budget_count + len(pat_line.budget_line)

			# Update Nrs
			pat_line.update_nrs()





		# Orders 
			orders = self.env['sale.order'].search([
															('state', '=', 'sale'),
															('patient', '=', pat_line.patient.name),
													],
														order='date_order asc',
														#limit=1,
												)
			#print orders


			# Clean 
			pat_line.sale_line.unlink()
			pat_line.consu_line.unlink()
			pat_line.procedure_line.unlink()


			# Create
			for order in orders: 

				for line in order.order_line: 
					
					prod = line.product_id


					# Sale
					sale_line = pat_line.sale_line.create({
															'name': line.name, 
															'product_id': line.product_id.id, 
															'x_date_created': order.date_order, 
															'product_uom_qty': line.product_uom_qty, 
															'price_unit': line.price_unit, 

															'patient_line_sale_id': pat_line.id, 
															'marketing_id': self.id, 
						})



					# Consu
					if prod.x_family in ['consultation']: 

						consu_line = pat_line.consu_line.create({
																	'name': line.name, 
																	'product_id': line.product_id.id, 
																	'x_date_created': order.date_order, 
																	'product_uom_qty': line.product_uom_qty, 
																	'price_unit': line.price_unit, 

																	'patient_line_consu_id': pat_line.id, 
																	'marketing_id': self.id, 
																})


					# Proc 
					if 	(prod.type not in ['product'])   and   (prod.x_family not in ['consultation']): 

						procedure_line = pat_line.procedure_line.create({
																			'name': line.name, 
																			'product_id': line.product_id.id, 
																			'x_date_created': order.date_order, 
																			'product_uom_qty': line.product_uom_qty, 
																			'price_unit': line.price_unit, 

																			'patient_line_proc_id': pat_line.id, 
																			'marketing_id': self.id, 
																		})






			# Count
			self.patient_sale_count = self.patient_sale_count + len(pat_line.sale_line)
			self.patient_consu_count = self.patient_consu_count + len(pat_line.consu_line)
			self.patient_proc_count = self.patient_proc_count + len(pat_line.procedure_line)


			# Update Nrs
			pat_line.update_nrs()


		print 'Done !'

	# update_sales









# ----------------------------------------------------------- Update Recommendations ------------------------------------------------------
	
	# Recommendations
	@api.multi  
	def update_recos(self):  
		print 
		print 'Update Recos'
		print 


		# Clean 
		self.patient_reco_count = 0 


		# Patient Lines 
		for pat_line in self.patient_line: 


			# Clean 
			pat_line.reco_line.unlink()


			# Recommendations
			patient = pat_line.patient


			# Loop 
			for treatment in patient.treatment_ids: 

				# Create - Co2 
				for reco in treatment.service_co2_ids: 


					reco_line = pat_line.reco_line.create({
																'product_id': reco.service.id, 
																'sub_family': reco.service.x_treatment, 
																'x_date_created': reco.create_date, 
																'doctor': reco.physician.id, 
																'price': reco.price, 
																'price_vip': reco.price_vip, 
																'price_manual': reco.price_manual, 
																'price_applied': reco.price_applied, 

																'patient_line_id': pat_line.id, 
																'marketing_id': self.id, 
															})



				# Create - Exc 
				for reco in treatment.service_excilite_ids: 
					

					reco_line = pat_line.reco_line.create({
																'product_id': reco.service.id, 
																'sub_family': reco.service.x_treatment, 
																'x_date_created': reco.create_date, 
																'doctor': reco.physician.id, 
																'price': reco.price, 
																'price_vip': reco.price_vip, 
																'price_manual': reco.price_manual, 
																'price_applied': reco.price_applied, 

																'patient_line_id': pat_line.id, 
																'marketing_id': self.id, 
															})


				# Create - Ipl 
				for reco in treatment.service_ipl_ids: 
					

					reco_line = pat_line.reco_line.create({
																'product_id': reco.service.id, 
																'sub_family': reco.service.x_treatment, 
																'x_date_created': reco.create_date, 
																'doctor': reco.physician.id, 
																'price': reco.price, 
																'price_vip': reco.price_vip, 
																'price_manual': reco.price_manual, 
																'price_applied': reco.price_applied, 

																'patient_line_id': pat_line.id, 
																'marketing_id': self.id, 
															})


				# Create - Ndyag 
				for reco in treatment.service_ndyag_ids: 
					

					reco_line = pat_line.reco_line.create({
																'product_id': reco.service.id, 
																'sub_family': reco.service.x_treatment, 
																'x_date_created': reco.create_date, 
																'doctor': reco.physician.id, 
																'price': reco.price, 
																'price_vip': reco.price_vip, 
																'price_manual': reco.price_manual, 
																'price_applied': reco.price_applied, 

																'patient_line_id': pat_line.id, 
																'marketing_id': self.id, 
															})



				# Create - Medical 
				for reco in treatment.service_medical_ids: 
					


					reco_line = pat_line.reco_line.create({
																'product_id': reco.service.id, 
																'sub_family': reco.service.x_treatment, 
																'x_date_created': reco.create_date, 
																'doctor': reco.physician.id, 
																'price': reco.price, 
																'price_vip': reco.price_vip, 
																'price_manual': reco.price_manual, 
																'price_applied': reco.price_applied, 

																'patient_line_id': pat_line.id, 
																'marketing_id': self.id, 
															})


				# Create - Quick 
				for reco in treatment.service_quick_ids: 
					

					reco_line = pat_line.reco_line.create({
																'product_id': reco.service.id, 
																'sub_family': reco.service.x_treatment, 
																'x_date_created': reco.create_date, 
																'doctor': reco.physician.id, 
																'price': reco.price, 
																'price_vip': reco.price_vip, 
																'price_manual': reco.price_manual, 
																'price_applied': reco.price_applied, 

																'patient_line_id': pat_line.id, 
																'marketing_id': self.id, 
															})


				# Create - Vip 
				for reco in treatment.service_vip_ids: 
					

					reco_line = pat_line.reco_line.create({
																'product_id': reco.service.id, 
																'sub_family': reco.service.x_treatment, 
																'x_date_created': reco.create_date, 
																'doctor': reco.physician.id, 
																'price': reco.price, 
																'price_vip': reco.price_vip, 
																'price_manual': reco.price_manual, 
																'price_applied': reco.price_applied, 

																'patient_line_id': pat_line.id, 
																'marketing_id': self.id, 
															})
				#print 



			# Update 
			pat_line.update_nrs()


			# Counts 
			self.patient_reco_count = self.patient_reco_count + len(pat_line.reco_line)


		print 'Done !'
	# update_recos








# ----------------------------------------------------------- Vip Orders ------------------------------------------------------
	
	# Correct
	@api.multi
	def update_vip_sales(self):  

		print 
		print 'Vip Sales'
		print 

		# Patient Lines 
		for pl in self.patient_line: 


			if pl.vip: 
				
				#print pl.patient.name
				#print 


				# Clean 
				pl.order_line.unlink()
				pl.order_line_vip.unlink()



				# Orders 
				orders = self.env['sale.order'].search([
															('state', '=', 'sale'),
															('patient', '=', pl.patient.name),
													],
														#order='x_serial_nr asc',
														order='date_order asc',
														#limit=1,
												)
				#print orders





				# Find Vip Date - First Method 
				for order in orders: 
					for ol in order.order_line: 
						if ol.product_id.default_code == '495': 		# Vip Card 
							pl.vip_date = order.date_order


				# Find Vip Date - Second Method - Legacy 
				if pl.vip_date == False: 
					# Card 
					card = self.env['openhealth.card'].search([
																	('patient_name', '=', pl.patient.name),
														],
															#order='x_serial_nr asc',
															limit=1,
													)
					pl.vip_date = card.create_date







				# Order Lines - Create Order Line 
				for order in orders: 

					# Create Vip 
					for ol in order.order_line: 
					
						pl_ol = pl.order_line.create({
														'name': ol.name, 
														'product_id': ol.product_id.id, 
														'x_date_created': order.date_order, 
														'product_uom_qty': ol.product_uom_qty, 
														'price_unit': ol.price_unit, 

														'patient_line_id': pl.id, 
							})
						#print pl_ol



						# Create - Vip sale 
						if pl.vip_date != False: 

							if order.date_order >= pl.vip_date		and 	ol.product_id.type in ['service']: 


								pl_ol_vip = pl.order_line_vip.create({
																		'name': ol.name, 
																		'product_id': ol.product_id.id, 
																		'x_date_created': order.date_order, 
																		'product_uom_qty': ol.product_uom_qty, 
																		'price_unit': ol.price_unit, 

																		'patient_line_id_vip': pl.id, 
									})
								#print pl_ol

				pl.update_fields_vip()
				#print 
		#print 

	# update_vip_sales





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
	# correct_patients






# ----------------------------------------------------------- Cities ------------------------------------------------------

	# Cities
	@api.multi
	def build_cities(self):  

		print 
		print 'Build Cities'
		print 

		# Create Collection

		city_arr = []

		for line in self.patient_line: 
			#if line.city in ['Lima']: 
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
			#total = self.total_count
			#name = city
			sector = _h_sector_city[city]


			# Count - Search in Collections 
			if city in counter_city: 
				count = counter_city[city]
			else: 
				count = 0 


			# Create 
			line = self.city_line.create({
												'name' : 		city, 
												#'code' :		code, 
												'sector' : 		sector, 
												'count' :		count,

												'marketing_id' :	self.id, 
										})
			
			# Update 
			line.update_fields()

	# build_cities







# ----------------------------------------------------------- Districts ------------------------------------------------------

	# Districts
	@api.multi
	def build_districts(self):  

		print 
		print 'Build Districts'
		print 


		# Create Collection
		district_arr = []
		for line in self.patient_line: 
			if line.city in ['Lima']: 
				district_arr.append(line.district)

		counter_district = collections.Counter(district_arr)


		#for key in counter_district: 
		#	count = counter_district[key]




		# Build 
		#district_arr = [
		#					'none', 
		#					'recommendation', 
		#					'tv', 
		#					'internet', 
		#					'website', 
		#					'mail', 
		#					'undefined', 
		#			]
		#idx = 0 




		# Clear 
		self.district_line.unlink()


		# Build Code Array 
		code_arr = np.arange(44)


		# Loop 
		for code in code_arr: 
			
			if code != 0: 


				# Init vars 
				#total = self.total_count
				name = pat_vars.zip_dic_inv[code]
				sector = pat_vars._h_sector[name]


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






# ----------------------------------------------------------- Media ------------------------------------------------------

	# Histogram
	@api.multi
	def build_media(self):  

		print 
		print 'Build Media'
		print 


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





# ----------------------------------------------------------- Histogram ------------------------------------------------------

	# Histogram
	@api.multi
	def build_histogram(self):  

		print 
		print 'Build Histogram'
		print 


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


		bins = histo[1]

		counts = histo[0]
		counts_m = histo_m[0]
		counts_f = histo_f[0]


		#print bins
		#print counts



		# Total 
		total = len(input_arr)



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
				#print

	# build_histogram









	




# ----------------------------------------------------------- Stats ------------------------------------------------------


	# Percentages - Float 


	# Age 
	age_undefined_per = fields.Float(
			'Error %',
			readonly=True, 

			digits=(16,1), 
		)


	# Sex 
	sex_male_per = fields.Float(
			'M %',
			#'%',
			readonly=True, 

			digits=(16,1), 
		)

	sex_female_per = fields.Float(
			'F %',
			#'%',
			readonly=True, 

			digits=(16,1), 
		)

	sex_undefined_per = fields.Float(
			#'%',
			'Error %',
			readonly=True, 

			digits=(16,1), 
		)



	# First Contact 
	how_u_per = fields.Float(
			#'Indefinido %',
			'No Definido %',
			readonly=True, 

			#digits=dp.get_precision('Product Price'), 
			digits=(16,1), 
		)

	how_none_per = fields.Float(
			'Ninguno %',
			readonly=True, 

			digits=(16,1), 
		)

	how_reco_per = fields.Float(
			'Recomendación %',
			readonly=True, 

			digits=(16,1), 
		)

	how_tv_per = fields.Float(
			'Tv %',
			readonly=True, 

			digits=(16,1), 
		)

	how_radio_per = fields.Float(
			'Radio %',
			readonly=True, 
			digits=(16,1), 
		)

	how_inter_per = fields.Float(
			'Internet %',
			readonly=True, 
			digits=(16,1), 
		)

	how_web_per = fields.Float(
			'Web %',
			readonly=True, 
			digits=(16,1), 
		)

	how_mail_per = fields.Float(
			'Mail %',
			readonly=True, 
			digits=(16,1), 
		)





	# Education Level 
	edu_u_per = fields.Float(
			#'Indefinido %',
			'No Definido %',
			readonly=True, 
			digits=(16,1), 
		)

	edu_fir_per = fields.Float(
			'Primaria %',
			readonly=True, 
			digits=(16,1), 
		)

	edu_sec_per = fields.Float(
			'Secundaria %',
			readonly=True, 
			digits=(16,1), 
		)
	
	edu_tec_per = fields.Float(
			'Instituto %',
			readonly=True, 
			digits=(16,1), 
		)
	
	edu_uni_per = fields.Float(
			'Universidad %',
			readonly=True, 
			digits=(16,1), 
		)
	
	edu_mas_per = fields.Float(
			'Posgrado %',
			readonly=True, 
			digits=(16,1), 
		)



	# Vip 
	vip_true_per = fields.Float(
			'Vip Si %',
			readonly=True, 
			digits=(16,1), 
		)

	vip_false_per = fields.Float(
			'Vip No %',
			readonly=True, 
			digits=(16,1), 
		)






	# Age
	age_mean = fields.Float(
			'Edad Promedio',
			readonly=True, 

			digits=(16,1), 
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
			#'Edad Ind',
			'Edad Error',
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
			'Sexo Error',
			readonly=True, 	
		)










	# First Contact 

	how_u = fields.Integer(
			'No Definido',
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










	# Education

	edu_u = fields.Integer(
			#'Edu Indefinido',
			'No Definido',
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








	

	# Vip 

	vip_true = fields.Integer(
			'Vip Si',
			readonly=True, 
		)

	vip_false = fields.Integer(
			'Vip No',
			readonly=True, 
		)











# ----------------------------------------------------------- Actions ------------------------------------------------------

# jx 
	# Set Stats
	@api.multi
	def set_stats(self):  

		print 
		print 'Set Stats'
		print



		# Init vars 

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




		# Collections
		country_arr = []
		#city_arr = []
		#district_arr = []





		# Loop 
		for line in self.patient_line: 



			# Sex
			if line.sex == 'Male': 
				count_m = count_m + 1
			elif line.sex == 'Female': 
				count_f = count_f + 1
			else: 
				count_u = count_u + 1



			# Age Max and Min 
			if line.age_years not in[ -1, 0]: 			# Not an Error 
				count_a = count_a + line.age_years 
				if line.age_years > age_max: 
					age_max = line.age_years
				if line.age_years < age_min: 
					age_min = line.age_years
			else: 										# Error 
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




			# Address - Using collections

			# Countries 
			country_arr.append(line.country)

			# Cities
			#city_arr.append(line.city)

			# Districts - Only for Lima
			#if line.city in ['Lima']: 
			#	district_arr.append(line.district)








		# Update Object 

		# Sex 
		# Absolutes 
		self.sex_male = count_m
		self.sex_female = count_f
		self.sex_undefined = count_u

		# Per
		if self.total_count != 0: 
			self.sex_male_per = ( float(self.sex_male) / float(self.total_count) ) * 100
			self.sex_female_per = ( float(self.sex_female) / float(self.total_count) ) * 100
			self.sex_undefined_per = ( float(self.sex_undefined) / float(self.total_count) ) * 100



		# Ages 
		self.age_min = age_min
		self.age_max = age_max
		self.age_undefined = count_age_u
		
		if self.total_count != 0: 
			self.age_mean = count_a / self.total_count
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

		#counter_city = collections.Counter(city_arr)
		
		#counter_district = collections.Counter(district_arr)



		#print country_arr
		#print 
		#print city_arr
		#print 
		#print district_arr
		#print 
		#print 
		#print counter_country
		#print 
		#print counter_country['Peru']



		# Clear 
		self.country_line.unlink()
		self.city_line.unlink()
		self.district_line.unlink()



		# Country
		#print 'Create Country Line '
		for key in counter_country: 

			count = counter_country[key]

			country = self.country_line.create({
													'name': key, 
													'count': count, 

													'marketing_id': self.id, 
												})
			#print key 
			#print count
			#print country

		#print self.country_line
		#print 



		
		# City 
		#print 'Create City Line '
		#for key in counter_city: 
		#	count = counter_city[key]
		#	city = self.city_line.create({
		#											'name': key, 
		#											'count': count, 
		#											'marketing_id': self.id, 
		#										})
			#print key 
			#print count
			#print country

		#print self.city_line
		#print 
		


		# District 
		#print 'Create District Line '
		#for key in counter_district: 
		#	count = counter_district[key]
			#district = self.district_line.create({
			#										'name': key, 
													#'count': count, 
			#										'marketing_id': self.id, 
			#									})
			#print key 
			#print count
			#print country

		#print self.district_line
		#print 




		#print counter_city
		#print 
		#print counter_district
		#print 
		#print 

	# set_stats









# ----------------------------------------------------------- Update Patients ------------------------------------------------------

	# Update Patients
	@api.multi
	def update_patients(self):  

		print
		print 'Update Patients'
		print

		# Clear 
		self.patient_line.unlink()


		# Orders 
		#patients,count = resap_funcs.get_patients_filter(self, self.date_begin, self.date_end)
		mode = 'normal'
		patients,count = resap_funcs.get_patients_filter(self, self.date_begin, self.date_end, mode)

		self.total_count = count



		# Loop 
		for patient in patients: 


			pat_line = self.patient_line.create({
														'patient': patient.id, 
														#'doctor': doctor.id, 



														'date_create': patient.create_date,
														'date_record': patient.x_date_record,

														'sex': patient.sex, 
														'dob': patient.dob, 
														'age': patient.age, 

														'first_contact': patient.x_first_contact, 
														'education': patient.x_education_level, 
														'vip': patient.x_vip, 
														
														'country': patient.country_id.name, 
														'city': patient.city, 
														'district': patient.street2, 


														'marketing_id': self.id, 
					})


			ret = pat_line.update_fields()


			#if ret == -1:
			#	print 'Age undefined !'




		# Set Stats 
		self.set_stats()

		# Build Vip Sales 
		self.update_vip_sales()




		# Build Histo
		self.build_histogram()


		# Build Media
		self.build_media()



		# Build Places  
		self.build_districts()
		self.build_cities()



		print 'Done !'

	# update_patients


