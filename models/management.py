# -*- coding: utf-8 -*-
#
# 	Report Management
# 
# Created: 				28 Mayo 2018
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





# ----------------------------------------------------------- Inheritable ------------------------------------------------------

	# Count
	total_tickets = fields.Integer(
			'Nr Tickets',
			readonly=True, 
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
			'Prom. Consultas', 
			#default=-1, 
			#digits=(16,1), 
		)

	# avg Products 
	avg_products = fields.Float(
			'Prom. Productos', 
			#default=-1, 
			#digits=(16,1), 
		)

	# avg Proc
	avg_procedures = fields.Float(
			'Prom. Procedimientos', 
			#default=-1, 
			#digits=(16,1), 
		)








	# Ratios 
	ratio_pro_con = fields.Float(
			'Ratio (proc/con) %', 
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
		#self.doctor_line.unlink()
		#self.family_line.unlink()
		#self.sub_family_line.unlink()
		self.family_line.unlink()
		self.sub_family_line.unlink()



		# Init
		doctor_arr = []
		family_arr = []
		sub_family_arr = []



		_h_amount = {

				'consultation': 	0, 		
				'consultation_gyn': 0, 		
				'consultation_100': 0, 		
				'consultation_0': 	0, 		

				#'procedure': 	0, 		
				'laser': 		0, 		
				'medical': 		0, 		
				'cosmetology': 	0, 	

				'product': 		0,
				'card': 		0, 	
				'kit': 			0, 	
				'topical': 		0, 	
		}

		
		print _h_amount


	# All 
		# Loop - Doctors 
		for doctor in self.doctor_line: 

			# Loop - Order Lines 
			for line in doctor.order_line: 

				# Doctor
				#doctor_arr.append(line.doctor)

				# Family
				family_arr.append(line.family)

				# Sub family
				sub_family_arr.append(line.sub_family)


				_h_amount[line.family] = _h_amount[line.family] + line.price_total 


		print _h_amount


		

	# Doctor 

		# Count
		#counter_doctor = collections.Counter(doctor_arr)


		# Create 
		#for key in counter_doctor: 

		#	count = counter_doctor[key]

		#	doctor = self.doctor_line.create({
		#											'name': key.name, 

		#											'x_count': count, 

		#											'management_id': self.id, 
		#										})
			#print key 
			#print count
			#print doctor
		#print self.doctor_line
		#print 





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

			sub_family = self.sub_family_line.create({
														'name': key, 

														'x_count': count, 
														
														'management_id': self.id, 
												})


			sub_family.update_fields()

			#print key 
			#print count
			#print sub_family
		#print self.sub_family_line
		#print 




	# Doctors 
		#for doctor in self.doctor_line: 
		#	doctor.stats()


		print 'Done !'
		print 

	# update_stats




# ----------------------------------------------------------- Update ------------------------------------------------------

	# Update Orders 
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
					'Clinica Chavarri', 
					'Eulalia', 
					'Dr. Abriojo', 
					'Dr. Castillo', 
					'Dr. Loaiza', 
					'Dr. Escudero', 
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
