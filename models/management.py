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





# ----------------------------------------------------------- Inheritable ------------------------------------------------------

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

	# Nr Proc
	nr_procedures = fields.Integer(
			'Nr Procedimientos', 
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

	# Amo Proc
	amo_procedures = fields.Float(
			'Monto Procedimientos', 
			#default=-1, 
		)





	# avg Consus 
	avg_consultations = fields.Float(
			'Precio Promedio Consultas', 
			#default=-1, 
			#digits=(16,1), 
		)

	# avg Products 
	avg_products = fields.Float(
			'Precio Productos', 
			#default=-1, 
			#digits=(16,1), 
		)

	# avg Proc
	avg_procedures = fields.Float(
			'Precio Procedimientos', 
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
		self.nr_procedures = 0 
		self.nr_products = 0 

		self.amo_consultations = 0 
		self.amo_procedures = 0 
		self.amo_products = 0 



		# Loop - Families 
		for family in self.family_line: 

			#if family.name in ['consultation', 'consultation_gyn', 'consultation_0', 'consultation_100']: 
			if family.meta == 'consultation': 

				self.nr_consultations = self.nr_consultations +  family.x_count

				self.amo_consultations = self.amo_consultations + family.amount



			#elif family.name in ['laser', 'medical', 'cosmetology']: 
			elif family.meta == 'procedure': 

				self.nr_procedures = self.nr_procedures +  family.x_count

				self.amo_procedures = self.amo_procedures + family.amount



			#elif family.name in ['topical', 'card']: 
			elif family.meta == 'product': 

				self.nr_products = self.nr_products +  family.x_count

				self.amo_products = self.amo_products + family.amount




		# Ratios 
		self.ratio_pro_con = (float(self.nr_procedures) / float(self.nr_consultations)) * 100 

		self.avg_consultations = self.amo_consultations / self.nr_consultations

		self.avg_procedures = self.amo_procedures / self.nr_procedures

		self.avg_products = self.amo_products / self.nr_products



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


		print 
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
