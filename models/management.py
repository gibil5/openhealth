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



# ----------------------------------------------------------- Relational ------------------------------------------------------

	# Sales
	order_line = fields.One2many(

			'openhealth.management.order.line', 
		
			'management_id',
		)




	# doctor 
	doctor_line = fields.One2many(
			#'openhealth.mgt.doctor.line', 
			'openhealth.management.doctor.line', 
			
			'management_id', 
		)



	# family 
	family_line = fields.One2many(
			#'openhealth.mgt.family.line', 
			'openhealth.management.family.line', 
			
			'management_id', 
		)

	# sub_family 
	sub_family_line = fields.One2many(
			#'openhealth.mgt.sub_family.line', 
			'openhealth.management.sub_family.line', 
			
			'management_id', 
		)






# ----------------------------------------------------------- Actions ------------------------------------------------------

	# Set Stats
	@api.multi
	def stats(self):  

		print 
		print 'Stats - Management'
		print 


		# Using collections - More Abstract !


		# Init
		doctor_arr = []
		family_arr = []
		sub_family_arr = []




		# Loop 
		for line in self.order_line: 

			# Doctor
			doctor_arr.append(line.doctor)

			# Family
			family_arr.append(line.family)

			# Sub family
			sub_family_arr.append(line.sub_family)





		

# Doctor 
		# Count
		counter_doctor = collections.Counter(doctor_arr)

		# Clear 
		#self.doctor_line.unlink()

		# Create 
		for key in counter_doctor: 

			count = counter_doctor[key]

			doctor = self.doctor_line.create({
													#'name': key, 
													'name': key.name, 

													'x_count': count, 

													'management_id': self.id, 
												})
			#print key 
			#print count
			#print doctor
		#print self.doctor_line
		#print 



# Family 
		# Count
		counter_family = collections.Counter(family_arr)

		# Clear 
		#self.family_line.unlink()

		# Create 
		for key in counter_family: 

			count = counter_family[key]

			family = self.family_line.create({
													#'name': key, 
													'name': mgt_vars._h_family_sp[key], 
													
													'x_count': count, 
													
													'management_id': self.id, 
												})

			#print key 
			#print count
			#print family
		#print self.family_line
		#print 



# Subfamily 
		# Count
		counter_sub_family = collections.Counter(sub_family_arr)

		# Clear 
		#self.sub_family_line.unlink()

		# Create 
		for key in counter_sub_family: 

			count = counter_sub_family[key]

			sub_family = self.sub_family_line.create({
													'name': key, 

													'x_count': count, 
													
													'management_id': self.id, 
												})


			#print key 
			#print count
			#print sub_family
		#print self.sub_family_line
		#print 



		# Doctors 
		for doctor in self.doctor_line: 

			doctor.stats()






# ----------------------------------------------------------- Update ------------------------------------------------------

	# Update Orders 
	@api.multi
	def update_repo(self):  

		print
		print 'Update Doctors'



		# Clean 
		self.doctor_line.unlink()

		total_amount = 0 
		total_count = 0 



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

		for doctor in doctors: 
			
			doctor = self.doctor_line.create({
												'name': doctor, 
	
												#'x_count': count, 

												'management_id': self.id, 
										})




		# Create Sales - By Doctor 
		for doctor in self.doctor_line: 

			print doctor.name 


			# Clear 
			#self.order_line.unlink()
			doctor.order_line.unlink()



			# Orders 
			#orders,count = resap_funcs.get_orders_filter(self, self.date_begin, self.date_end)
			#doctor = 'all'
			#orders,count = mgt_funcs.get_orders_filter(self, self.date_begin, self.date_end, doctor)
			orders,count = mgt_funcs.get_orders_filter(self, self.date_begin, self.date_end, doctor.name)


			#self.total_count = count



			amount = 0 
			count = 0 



			# Loop 
			for order in orders: 


				amount = amount + order.amount_total


				# Order Lines 
				for line in order.order_line:
					
					count = count + 1

					#print 

					#order_line = self.order_line.create({
					order_line = doctor.order_line.create({
															'name': order.name, 

															'product_id': line.product_id.id, 

															'x_date_created': order.date_order, 
															
															'product_uom_qty': line.product_uom_qty, 
															
															'price_unit': line.price_unit, 

															'patient': order.patient.id, 

															'doctor': order.x_doctor.id, 

															'state': order.state, 

															#'family': order.x_family, 
															
															#'sub_family': order.sub_family, 



															#'management_id': self.id, 
															'doctor_id': doctor.id, 
														})
					ret = order_line.update_fields()



			# Stats 
			doctor.amount = amount
			doctor.x_count = count
			doctor.stats()

			total_amount = total_amount + amount
			total_count = total_count + count



		# Stats 
		self.total_amount = total_amount
		self.total_count = total_count
		#self.stats()


	# update_repo
