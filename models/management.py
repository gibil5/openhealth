# -*- coding: utf-8 -*-
#
# 	Report Management
# 
# Created: 				28 Mayo 2018
#

from openerp import models, fields, api

import resap_funcs


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




