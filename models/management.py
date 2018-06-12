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



		for family in self.family_line: 

			#if family.name in ['consultation', 'consultation_gyn', 'consultation_0', 'consultation_100']: 
			if family.meta == 'consultation': 

				#self.nr_consultations = self.nr_consultations +  1
				self.nr_consultations = self.nr_consultations +  family.x_count


			#elif family.name in ['laser', 'medical', 'cosmetology']: 
			elif family.meta == 'procedure': 

				self.nr_procedures = self.nr_procedures +  family.x_count


			#elif family.name in ['topical', 'card']: 
			elif family.meta == 'product': 

				self.nr_products = self.nr_products +  family.x_count




		# Ratios 
		self.ratio_pro_con = (float(self.nr_procedures) / float(self.nr_consultations)) * 100 



		print 'Done !'

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




	# All 
		# Loop 
		for doctor in self.doctor_line: 

			#for line in self.order_line: 
			for line in doctor.order_line: 


				# Doctor
				#doctor_arr.append(line.doctor)


				# Family
				family_arr.append(line.family)


				# Sub family
				sub_family_arr.append(line.sub_family)





		

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

			family = self.family_line.create({
													#'name': mgt_vars._h_family_sp[key], 
													'name': key, 
													
													'x_count': count, 
													
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




		# Loop - By Doctor 
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


			total_amount = total_amount + amount

			total_count = total_count + count

			total_tickets = total_tickets + tickets



		# Stats 
		self.total_amount = total_amount
		self.total_count = total_count
		self.total_tickets = total_tickets

		#self.stats()


		print 'Done !'

	# update_sales
