# -*- coding: utf-8 -*-
#
# 	Management Report
# 
# Created: 				28 May 2018
# Last updated: 		19 June 2018
#

from openerp import models, fields, api

#import resap_funcs
import mgt_funcs

import numpy as np

import collections

import mgt_vars



class Management(models.Model):

	_inherit='openhealth.repo'

	_name = 'openhealth.management'

	#_order = 'create_date desc'
	#_order = 'date_begin asc,name asc'
	_order = 'date_begin asc'





# ----------------------------------------------------------- Counters ------------------------------------------------------
	
	# Procedures 
	nr_procedures = fields.Integer(
			'Nr Procedimientos', 
			#default=-1, 
		)

	amo_procedures = fields.Float(
			'Monto Procedimientos', 
			#default=-1, 
		)

	avg_procedures = fields.Float(
			'Precio Prom. Procedimientos', 
			#default=-1, 
			#digits=(16,1), 
		)




	# Co2
	nr_co2 = fields.Integer(
			'Nr Co2', 
		)

	amo_co2 = fields.Float(
			'Monto Co2', 
		)

	avg_co2 = fields.Float(
			'Precio Prom. Co2', 
		)



	# Exc
	nr_exc = fields.Integer(
			'Nr Exc', 
		)
	
	amo_exc = fields.Float(
			'Monto Exc', 
		)

	avg_exc = fields.Float(
			'Precio Prom. Exc', 
		)




	# Ipl
	nr_ipl = fields.Integer(
			'Nr Ipl', 
		)
	
	amo_ipl = fields.Float(
			'Monto Ipl', 
		)

	avg_ipl = fields.Float(
			'Precio Prom. Ipl', 
		)





	# Ndyag
	nr_ndyag = fields.Integer(
			'Nr Ndyag', 
		)

	amo_ndyag = fields.Float(
			'Monto Ndyag', 
		)

	avg_ndyag = fields.Float(
			'Precio Prom. Ndyag', 
		)



	# Quick
	nr_quick = fields.Integer(
			'Nr Quick', 
		)

	amo_quick = fields.Float(
			'Monto Quick', 
		)

	avg_quick = fields.Float(
			'Precio Prom. Quick', 
		)



	# Medical
	nr_medical = fields.Integer(
			'Nr TM', 
		)

	amo_medical = fields.Float(
			'Monto TM', 
		)

	avg_medical = fields.Float(
			'Precio Prom. TM', 
		)




	# Cosmetology
	nr_cosmetology = fields.Integer(
			'Nr Cosmiatria', 
		)

	amo_cosmetology = fields.Float(
			'Monto Cosmiatria', 
		)

	avg_cosmetology = fields.Float(
			'Precio Prom. Cosmiatria', 
		)





# ----------------------------------------------------------- Clear ------------------------------------------------------
	
	# Clear 
	@api.multi
	def clear(self, patient_name, doctor_name): 

		print 
		print 'Clear'

		# Treatment 
		treatment = self.env['openhealth.treatment'].search([
																('patient', '=', patient_name),
																('physician', '=', doctor_name),
											],
												order='start_date desc',
												limit=1,
											)
		print treatment


		for order in treatment.order_ids: 
			order.remove_myself()

		treatment.appointment_ids.unlink()

		treatment.procedure_ids.unlink()





	# Test Clear 
	@api.multi
	def test_clear(self):  

		# Init 
		patient_name = 'TOTTI TOTTI FRANCESCO'
		doctor_name = 'Dr. Chavarri'
		
		# Clear 
		self.clear(patient_name, doctor_name)			






# ----------------------------------------------------------- Test ------------------------------------------------------

	# Test
	@api.multi
	def test_integration(self):  

		print 
		print 'Test'

		if self.test: 


			# Init 
			#patient_name = 'REVILLA RONDON JOSE JAVIER'
			patient_name = 'TOTTI TOTTI FRANCESCO'
			doctor_name = 'Dr. Chavarri'

			# Clear 
			self.clear(patient_name, doctor_name)			

			

			# Products 
			products = [
							# Products 
							('acneclean', 	1, 'product'), 

							# Consultations 
							('con_med', 	1, 'consultation'), 
							('con_gyn', 	1, 'consultation'), 

							# Laser 
							('co2_nec_rn1_one', 	1, 'laser'), 
							('exc_bel_alo_15m_one', 1, 'laser'), 
							('ipl_bel_dep_15m_six', 1, 'laser'), 
							('ndy_bol_ema_15m_six', 1, 'laser'), 
							('quick_neck_hands_rejuvenation_1', 1, 'laser'), 
							
							# Cosmeto
							('car_bod_rfa_30m_six', 1, 'cosmetology'), 

							# Other 
							('other', 	1, 'other'), 




							# Medical
							('bot_1zo_rfa_one', 1, 'medical'), 	# Bot
							('cri_faa_acn_ten', 1, 'medical'), 	# Crio
							('hac_1hy_rfa_one', 1, 'medical'), 	# Hial

							('infiltration_scar', 1, 'medical'), 	# Infil
							('infiltration_keloid', 1, 'medical'), 	# Infil

							('ivc_na_na_one', 1, 'medical'), 		# Intra
							('lep_faa_acn_one', 1, 'medical'), 		# Lep

							('pla_faa_rfa', 1, 'medical'), 			# Pla
							('men_faa_rfa', 1, 'medical'), 			# Meso
							('scl_leg_var_one', 1, 'medical'), 		# Escl
						]


			type_arr = [
							'product', 
							'consultation', 
							'laser', 

							'medical', 
							'cosmetology', 
							
							'other', 
			]



			# Create 
			print 'Create'
			order = self.create_order(patient_name, doctor_name, products, type_arr)

			# Pay
			order.pay_myself()



			# Update
			print 'Update'

			self.update_sales()
			self.update_stats()
			self.update_counters()
			
			#self.update_qc()





# ----------------------------------------------------------- Create Order ------------------------------------------------------
	
	# Create Order 
	@api.multi
	def create_order(self, patient_name, doctor_name, products, type_arr):  

		print 
		print 'Create Order'



		# Treatment 
		treatment = self.env['openhealth.treatment'].search([
																('patient', '=', patient_name),
																('physician', '=', doctor_name),
											],
												order='start_date desc',
												limit=1,
											)
		#print treatment



		# Patient
		patient = self.env['oeh.medical.patient'].search([
																('name', '=', patient_name),
											],
												order='create_date desc',
												limit=1,
											)
		#print patient




		# Doctor
		doctor = self.env['oeh.medical.physician'].search([
																('name', '=', doctor_name),
											],
												order='create_date desc',
												limit=1,
											)
		#print doctor





		# Partner
		partner = self.env['res.partner'].search([
																('name', '=', patient_name),
											],
												order='create_date desc',
												limit=1,
											)
		#print partner








		# Pricelist 
 		pricelist = self.env['product.pricelist'].search([
															('name', '=', 'Public Pricelist'), 
													],
														#order='write_date desc',
														limit=1,
													)
 		#print pricelist






		# Create Order 
		order = self.env['sale.order'].create({
													'patient': patient.id,	
													'pricelist_id': pricelist.id, 
													'partner_id': partner.id,

													'x_doctor': doctor.id,	
													
													#'x_family': target, 

													'state':'draft',

													'treatment': treatment.id,
												}
											)
		#print order



		# Order line 
		for product in products: 

			name = 	product[0]
			qty = 	product[1]
			x_type = product[2]


			#if x_type in type_arr: 
			if 	(x_type == 'product' and self.prod_test) or 		\
				(x_type == 'consultation' and self.consu_test) or 	\
				(x_type == 'laser' and self.laser_test) or 			\
				(x_type == 'medical' and self.medi_test) or			\
				(x_type == 'cosmetology' and self.cosme_test) or  	\
				(x_type == 'other' and self.other_test):


				# Product
				product = self.env['product.product'].search([
																('x_name_short', '=', name),
													],
														order='create_date desc',
														limit=1,
													)
				#print product


				# Order line 
				order_line = order.order_line.create({
														'product_id': product.id,
														'product_uom_qty': qty, 

														'order_id': order.id,
										})
				#print order_line

		return order 










# ----------------------------------------------------------- Inheritable ------------------------------------------------------

	# Test 
	test = fields.Boolean(
			'Test', 
		)


	prod_test = fields.Boolean(
			'Prod', 
		)

	consu_test = fields.Boolean(
			'Consu', 
		)

	laser_test = fields.Boolean(
			'Laser', 
		)

	medi_test = fields.Boolean(
			'Med', 
		)

	cosme_test = fields.Boolean(
			'Cos', 
		)

	other_test = fields.Boolean(
			'Otros', 
		)




	# Count
	total_tickets = fields.Integer(
			'Nr Tickets',
			readonly=True, 
		)



	# Nr Deltas 
	nr_delta = fields.Integer(
			'Nr Deltas', 
			#default=-1, 
		)



	# Nr Consus 
	nr_consultations = fields.Integer(
			'Nr Consultas', 
			#default=-1, 
		)

	# Nr Products 
	nr_products = fields.Integer(
			'Nr Productos', 
			#default=-1, 
		)







	# Amo Consus 
	amo_consultations = fields.Float(
			'Monto Consultas', 
			#default=-1, 
		)

	# Amo Products 
	amo_products = fields.Float(
			'Monto Productos', 
			#default=-1, 
		)






	# avg Consus 
	avg_consultations = fields.Float(
			#'Precio Promedio Consultas', 
			'Precio Prom. Consultas', 
			#default=-1, 
			#digits=(16,1), 
		)

	# avg Products 
	avg_products = fields.Float(
			#'Precio Productos', 
			'Precio Prom. Productos', 
			#default=-1, 
			#digits=(16,1), 
		)








	# Ratios 
	ratio_pro_con = fields.Float(
			'Ratio Total (proc/con) %', 
		)






# ----------------------------------------------------------- Relational ------------------------------------------------------

	# Sales
	order_line = fields.One2many(
			'openhealth.management.order.line', 
			'management_id',
		)




	# Doctor 
	doctor_line = fields.One2many(

			'openhealth.management.doctor.line', 
			
			'management_id', 
		)



	# Family 
	family_line = fields.One2many(

			'openhealth.management.family.line', 
			
			'management_id', 
		)



	# Sub_family 
	sub_family_line = fields.One2many(

			'openhealth.management.sub_family.line', 
			
			'management_id', 
		)





	# Sales
	sale_line_tkr = fields.One2many(
			'openhealth.management.order.line', 
			'management_tkr_id',
		)





# ----------------------------------------------------------- Update Qc ------------------------------------------------------

	# Update Qc
	@api.multi
	def update_qc(self):  

		print 
		print 'Update Qc'
		print 


		# Checksum 

		# Orders 
		orders,count = mgt_funcs.get_orders_filter_all(self, self.date_begin, self.date_end)

		# All 
		for order in orders: 
			order.check_payment_method()
			order.check_sum()




		# Serial Number 

		# Init 
		serial_nr_last = 0 
		self.nr_delta = 0 

		# Orders 
		x_type = 'ticket_receipt'
		orders,count = mgt_funcs.get_orders_filter_type(self, self.date_begin, self.date_end, x_type)
		#print count
		#print orders
		
		# All 
		for order in orders: 
		
			# Serial Nr
			serial_nr = int(order.x_serial_nr.split('-')[1])
			if serial_nr_last != 0:
				delta = serial_nr - serial_nr_last
			else:
				delta = 1
			if delta == 2: 
				self.nr_delta = self.nr_delta + 1
			order.x_delta = delta
			serial_nr_last = serial_nr


			#print order 
			#print order.x_serial_nr
			#print serial_nr
			#print serial_nr_last			
			#print delta 
			#print 

		print 'Done !'
		print 
		
	# update_qc





# ----------------------------------------------------------- Update Counters ------------------------------------------------------

	# Update counters
	@api.multi
	def update_counters(self):  

		print 
		print 'Update counters'
		print 


		self.nr_consultations = 0 
		self.nr_products = 0 
		self.nr_procedures = 0 

		self.amo_consultations = 0 
		self.amo_products = 0 
		self.amo_procedures = 0 

		self.avg_consultations = 0 
		self.avg_products = 0 
		self.avg_procedures = 0 


		self.ratio_pro_con = 0 




		self.nr_co2 = 0 
		self.nr_exc = 0 
		self.nr_ipl = 0 
		self.nr_ndyag = 0 
		self.nr_quick = 0 
		self.nr_medical = 0 
		self.nr_cosmetology = 0 


		self.amo_co2 = 0 
		self.amo_exc = 0 
		self.amo_ipl = 0 
		self.amo_ndyag = 0 
		self.amo_quick = 0 
		self.amo_medical = 0 
		self.amo_cosmetology = 0 


		self.avg_co2 = 0 
		self.avg_exc = 0 
		self.avg_ipl = 0 
		self.avg_ndyag = 0 
		self.avg_quick = 0 
		self.avg_medical = 0 
		self.avg_cosmetology = 0 



		#print 
		#print 'Families'
		
		# Loop - Families 
		for family in self.family_line: 

			# Consultations 
			if family.meta == 'consultation': 
				self.nr_consultations = self.nr_consultations +  family.x_count
				self.amo_consultations = self.amo_consultations + family.amount

			# Products 
			elif family.meta == 'product': 
				self.nr_products = self.nr_products +  family.x_count
				self.amo_products = self.amo_products + family.amount

			# Procedures 
			elif family.meta == 'procedure': 
				self.nr_procedures = self.nr_procedures +  family.x_count
				self.amo_procedures = self.amo_procedures + family.amount


		
		#print 
		#print 'Sub families'

		# Loop - Subfamilies 
		for sub_family in self.sub_family_line: 

			#print sub_family
			#print sub_family.name
			#print sub_family.meta
			#print 

			if sub_family.name == 'laser_co2': 				
				self.nr_co2 = self.nr_co2 +  sub_family.x_count
				self.amo_co2 = self.amo_co2 + sub_family.amount

			elif sub_family.name == 'laser_excilite': 
				self.nr_exc = self.nr_exc +  sub_family.x_count
				self.amo_exc = self.amo_exc + sub_family.amount

			elif sub_family.name == 'laser_ipl': 
				self.nr_ipl = self.nr_ipl +  sub_family.x_count
				self.amo_ipl = self.amo_ipl + sub_family.amount

			elif sub_family.name == 'laser_ndyag': 
				self.nr_ndyag = self.nr_ndyag +  sub_family.x_count
				self.amo_ndyag = self.amo_ndyag + sub_family.amount

			elif sub_family.name == 'laser_quick': 
				self.nr_quick = self.nr_quick +  sub_family.x_count
				self.amo_quick = self.amo_quick + sub_family.amount

			elif sub_family.name == 'cosmetology': 
				self.nr_cosmetology = self.nr_cosmetology +  sub_family.x_count
				self.amo_cosmetology = self.amo_cosmetology + sub_family.amount


			# Special Case, by Meta !
			elif sub_family.meta == 'medical': 
				self.nr_medical = self.nr_medical +  sub_family.x_count
				self.amo_medical = self.amo_medical + sub_family.amount










		# Calc. Avoid division by zero !		

		# Ratios	
		if self.nr_consultations != 0:
			self.ratio_pro_con = (float(self.nr_procedures) / float(self.nr_consultations)) * 100 



		# Average prices 
		
		# Families 
		if self.nr_consultations != 0:
			self.avg_consultations = self.amo_consultations / self.nr_consultations

		if self.nr_products != 0: 
			self.avg_products = self.amo_products / self.nr_products


		if self.nr_procedures != 0: 
			self.avg_procedures = self.amo_procedures / self.nr_procedures


		# Subfamilies
		if self.nr_co2 != 0: 
			self.avg_co2 = self.amo_co2 / self.nr_co2

		if self.nr_exc != 0: 
			self.avg_exc = self.amo_exc / self.nr_exc

		if self.nr_ipl != 0: 
			self.avg_ipl = self.amo_ipl / self.nr_ipl

		if self.nr_ndyag != 0: 
			self.avg_ndyag = self.amo_ndyag / self.nr_ndyag

		if self.nr_quick != 0: 
			self.avg_quick = self.amo_quick / self.nr_quick

		if self.nr_medical != 0: 
			self.avg_medical = self.amo_medical / self.nr_medical

		if self.nr_cosmetology != 0: 
			self.avg_cosmetology = self.amo_cosmetology / self.nr_cosmetology



		print 'Done !'
		print 		
	# update_counters




# ----------------------------------------------------------- Update Stats ------------------------------------------------------

	# Update Stats
	@api.multi
	def update_stats(self):  

		print 
		print 'Update Stats'
		print 


		# Using collections - More Abstract !


		# Clean 
		self.family_line.unlink()
		self.sub_family_line.unlink()


		# Init
		doctor_arr = []
		family_arr = []
		sub_family_arr = []

		_h_amount = {}
		_h_sub = {}




	# All 
		# Loop - Doctors 
		for doctor in self.doctor_line: 

			# Loop - Order Lines 
			for line in doctor.order_line: 

				# Family
				family_arr.append(line.family)

				# Sub family
				sub_family_arr.append(line.sub_family)



				# Amount - Family 
				if line.family in _h_amount: 
					_h_amount[line.family] = _h_amount[line.family] + line.price_total 

				else: 
					_h_amount[line.family] = line.price_total 



				# Amount - Sub Family 
				if line.sub_family in _h_sub: 
					_h_sub[line.sub_family] = _h_sub[line.sub_family] + line.price_total 

				else: 
					_h_sub[line.sub_family] = line.price_total 



			# Doctor Stats 
			doctor.stats()

		#print _h_amount
		#print _h_sub




	# Family 

		# Count
		counter_family = collections.Counter(family_arr)


		# Create 
		for key in counter_family: 

			count = counter_family[key]

			amount = _h_amount[key]

			family = self.family_line.create({
													'name': key, 
													'x_count': count, 
													'amount': amount, 

													'management_id': self.id, 
												})

			family.update_fields()

			#print key 
			#print count
			#print family
		#print self.family_line
		#print 





	# Subfamily 

		# Count
		counter_sub_family = collections.Counter(sub_family_arr)




		# Create 
		for key in counter_sub_family: 

			count = counter_sub_family[key]

			amount = _h_sub[key]

			sub_family = self.sub_family_line.create({
														'name': key, 
														'x_count': count, 
														'amount': amount, 

														'management_id': self.id, 
												})


			sub_family.update_fields()

			#print key 
			#print count
			#print sub_family
		#print self.sub_family_line
		#print 



		print 'Done !'
		print 

	# update_stats





# ----------------------------------------------------------- Update Sales ------------------------------------------------------

	# Update Sales 
	@api.multi
	def update_sales(self):  

		print
		print 'Update Sales'
		print 


		# Clean 
		self.doctor_line.unlink()


		# Init vars
		total_amount = 0 
		total_count = 0 
		total_tickets = 0 




		# Create Doctors 
		doctors = [
					'Dr. Chavarri', 
					'Dr. Canales', 
					'Dr. Gonzales', 
					'Dr. Monteverde', 
					'Eulalia', 
					'Dr. Abriojo', 
					'Dr. Castillo', 
					'Dr. Loaiza', 
					'Dr. Escudero', 

					#'Clinica Chavarri', 
				]

		# Loop
		for doctor in doctors: 
			doctor = self.doctor_line.create({
												'name': doctor, 
												'management_id': self.id, 
										})




		# Create Sales - By Doctor 
		for doctor in self.doctor_line: 

			#print doctor.name 


			# Clear 
			#self.order_line.unlink()
			doctor.order_line.unlink()



			# Orders 
			#orders,count = resap_funcs.get_orders_filter(self, self.date_begin, self.date_end)
			#doctor = 'all'
			orders,count = mgt_funcs.get_orders_filter(self, self.date_begin, self.date_end, doctor.name)


			#self.total_count = count



			amount = 0 
			count = 0 

			tickets = 0 



			# Loop 
			for order in orders: 


				amount = amount + order.amount_total

				tickets = tickets + 1


				# Order Lines 
				for line in order.order_line:
					
					count = count + 1

					#print 



					# CREATE !!!

					#order_line = self.order_line.create({
					order_line = doctor.order_line.create({
															'name': order.name, 
															'x_date_created': order.date_order, 
															'patient': order.patient.id, 
															'doctor': order.x_doctor.id, 
															'state': order.state, 



															'serial_nr': order.x_serial_nr, 



															'product_id': line.product_id.id, 															
															'product_uom_qty': line.product_uom_qty, 
															'price_unit': line.price_unit, 

															#'family': order.x_family, 															
															#'sub_family': order.sub_family, 


															'doctor_id': doctor.id, 
															'management_id': self.id, 
														})
					ret = order_line.update_fields()



			# Stats 
			doctor.amount = amount
			doctor.x_count = count
			

			# Dr Stats 
			#doctor.stats()


			# Totals 
			total_amount = total_amount + amount
			total_count = total_count + count
			total_tickets = total_tickets + tickets



		# Totals  
		self.total_amount = total_amount
		self.total_count = total_count
		self.total_tickets = total_tickets

		#self.stats()


		print 'Done !'
		print 

	# update_sales
