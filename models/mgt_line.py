# -*- coding: utf-8 -*-
#
# 	Management Line 
# 
# Created: 				18 May 2018
#

from openerp import models, fields, api


class ManagementLine(models.Model):
	
	#_inherit = 'openhealth.management.line'

	_name = 'openhealth.management.line'

	#_order = 'x_count desc'
	_order = 'amount desc'



	# ----------------------------------------------------------- Relational ------------------------------------------------------

	management_id = fields.Many2one(
			'openhealth.management'
		)




	# ----------------------------------------------------------- Primitive ------------------------------------------------------
	name = fields.Char(
			'Nombre',
		)



	x_count = fields.Integer(
			'Nr',
		)

	amount = fields.Float(
			'Monto',
			digits=(16,1), 
		)


	#----------------------------------------------------------- Quick Button ------------------------------------------------------------

	# For quick access
	@api.multi
	def open_line_current(self):  

		#consultation_id = self.id 
		res_id = self.id 

		return {
				'type': 'ir.actions.act_window',
				'name': ' Edit Order Current', 
				'view_type': 'form',
				'view_mode': 'form',
				'res_model': self._name,

				#'res_id': consultation_id,
				'res_id': res_id,
				
				'target': 'current',
				'flags': {
						#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
						'form': {'action_buttons': True, }
						},
				'context': {}
		}




# ----------------------------------------------------------- Doctor ------------------------------------------------------

import collections
import mgt_vars

class DoctorLine(models.Model):	

	_inherit = 'openhealth.management.line'
	
	_name = 'openhealth.management.doctor.line'
	
	_order = 'amount desc'




	# Sales
	order_line = fields.One2many(

			'openhealth.management.order.line', 
		
			'doctor_id',
		)


	# Family 
	family_line = fields.One2many(

			'openhealth.management.family.line', 
			
			'doctor_id',
		)


	# Sub family 
	sub_family_line = fields.One2many(

			'openhealth.management.sub_family.line', 
			
			'doctor_id',
		)





	# Set Stats
	@api.multi
	def set_stats(self):  

		print 
		print 'Set Stats'
		print 


		# Using collections - More Abstract !


		# Clear 
		self.sub_family_line.unlink()
		self.family_line.unlink()
		print 
		print 


		# Init
		family_arr = []
		sub_family_arr = []



		#for line in self.order_line: 



		# Loop 
		for line in self.order_line: 

			# Family
			#family_arr.append( (line.family, line.price_total)  )
			family_arr.append(line.family)


			# Sub family
			sub_family_arr.append(line.sub_family)




		# Family 
	
		# Count
		counter_family = collections.Counter(family_arr)

		# Create 
		for key in counter_family: 

			count = counter_family[key]

			print key 
			print count

			family = self.family_line.create({
												#'name': mgt_vars._h_family_sp[key], 
												'name': key, 
												'x_count': count, 
												'doctor_id': self.id, 
											})



		# Subfamily 
		
		# Count
		counter_sub_family = collections.Counter(sub_family_arr)

		# Create 
		for key in counter_sub_family: 

			count = counter_sub_family[key]

			sub_family = self.sub_family_line.create({
														'name': key, 
														'x_count': count, 
														'doctor_id': self.id, 
												})







		# Amounts 

		# Family 
		for family in self.family_line: 
			
			amount = 0 

			orders = self.env['openhealth.management.order.line'].search([
																			('family', '=', family.name),
																			('doctor_id', '=', self.id),
																	],
																		#order='x_serial_nr asc',
																		#limit=1,
																	)

			for order in orders: 
				amount = amount + order.price_total


			family.amount = amount

			print family.name 
			print orders
			print 



		# Sub Family 
		for sub_family in self.sub_family_line: 
			
			amount = 0 

			orders = self.env['openhealth.management.order.line'].search([
																			('sub_family', '=', sub_family.name),
																			('doctor_id', '=', self.id),
																	],
																		#order='x_serial_nr asc',
																		#limit=1,
																	)

			for order in orders: 
				amount = amount + order.price_total


			sub_family.amount = amount

			print sub_family.name 
			print orders
			print 



	# set_stats






# ----------------------------------------------------------- Family ------------------------------------------------------
class FamilyLine(models.Model):	

	_inherit = 'openhealth.management.line'
	
	#_name = 'openhealth.management.family.line'
	_name = 'openhealth.management.family.line'
	
	#_order = 'idx asc'


	doctor_id = fields.Many2one(
			'openhealth.management.doctor.line'
		)


# ----------------------------------------------------------- Subfamily ------------------------------------------------------
class SubFamilyLine(models.Model):	

	_inherit = 'openhealth.management.line'
	
	#_name = 'openhealth.management.sub_family.line'
	_name = 'openhealth.management.sub_family.line'
	
	#_order = 'idx asc'


	doctor_id = fields.Many2one(
			'openhealth.management.doctor.line'
		)

