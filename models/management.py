# -*- coding: utf-8 -*-
#
# 	Report Management
# 
# Created: 				28 Mayo 2018
#

from openerp import models, fields, api

import resap_funcs

import numpy as np
import collections



class Management(models.Model):

	_inherit='openhealth.repo'

	_name = 'openhealth.management'

	#_order = 'create_date desc'
	#_order = 'date_begin asc,name asc'





# ----------------------------------------------------------- Inheritable ------------------------------------------------------




# ----------------------------------------------------------- Relational ------------------------------------------------------

	# Sales
	order_line = fields.One2many(

			'openhealth.management.order.line', 
		
			'management_id',
		)




	# doctor 
	doctor_line = fields.One2many(
			'openhealth.mgt.doctor.line', 
			
			'management_id', 
		)

	# family 
	family_line = fields.One2many(
			'openhealth.mgt.family.line', 
			
			'management_id', 
		)

	# sub_family 
	sub_family_line = fields.One2many(
			'openhealth.mgt.sub_family.line', 
			
			'management_id', 
		)






# ----------------------------------------------------------- Actions ------------------------------------------------------

	# Set Stats
	@api.multi
	def set_stats(self):  

		print 
		print 'Set Stats'
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
		self.doctor_line.unlink()

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
		self.family_line.unlink()

		# Create 
		for key in counter_family: 

			count = counter_family[key]

			family = self.family_line.create({
													'name': key, 
													
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
		self.sub_family_line.unlink()

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








# ----------------------------------------------------------- Update ------------------------------------------------------

	# Update Orders 
	@api.multi
	def update_repo(self):  

		print
		print 'Update Patients'



		# Clear 
		self.order_line.unlink()




		# Orders 
		orders,count = resap_funcs.get_orders_filter(self, self.date_begin, self.date_end)

		#self.total_count = count



		amount = 0 
		count = 0 



		# Loop 
		for order in orders: 


			amount = amount + order.amount_total


			# Order Lines 
			for line in order.order_line:
				
				count = count + 1

				print 

				order_line = self.order_line.create({
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




														'management_id': self.id, 
													})
				ret = order_line.update_fields()




		# Stats 
		self.total_amount = amount

		self.total_count = count

		self.set_stats()



	# update_repo




