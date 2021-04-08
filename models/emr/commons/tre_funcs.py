# -*- coding: utf-8 -*-
"""
	Tre Funcs
	- Used by Treatment

	Created: 			22 aug 2020
	Last up: 	 		 5 apr 2021
"""
from __future__ import print_function
from datetime import datetime, tzinfo, timedelta


# ----------------------------------------------------------- Exceptions -------
class ProductErrorException(Exception):
	#print('This is my first management of product exceptions')
	pass

class ProductProductError(Exception):
	#print('This is my first management of product exceptions')
	print('jx - ProductProductError')
	#pass


#------------------------------------------------ Getters ------------
def check_product(self, price_list, product, product_template):
	print()
	print('***** check_product')
	print(price_list)
	print(product)
	print(product_template)
	#print(product_template.name)
	#print(product_template.pl_treatment)
	#print(product_template.pl_family)
	#print(product_template.pl_price_list)

	if not product.pl_price_list:
		print('corr pl_price_list')
		product.pl_price_list = product_template.pl_price_list

	if not product.pl_treatment:
		print('corr pl_treatment')
		product.pl_treatment = product_template.pl_treatment

	if not product.pl_family:
		print('corr pl_family')
		product.pl_family = product_template.pl_family




#------------------------------------------------ Getters ------------
def get_product_template(self, name, price_list):
	print()
	print('Search product template')
	print(name)
	product = self.env['product.template'].search([
													('name', '=', name),
													('pl_price_list', '=', price_list),
												],
												#order='date_begin asc',
												#limit=1,
												)
	#if not product.name:
	#	raise Exception('Product not existant !!!')
		#raise ProductErrorException('x')
	return product



#def get_product(self, name, price_list):
def get_product_product(self, name, price_list):
	print()
	print('Search product')
	print(name)

	product = self.env['product.product'].search([
													('name', '=', name),
													('pl_price_list', '=', price_list),
												],
												#order='date_begin asc',
												#limit=1,
												)

	if not product.name:
		msg = 'ProductProduct not found !!!'
		#raise Exception('Product not existant !!!')
		#raise ProductErrorException('x')
		raise ProductProductError(msg)

	return product

	#try:
	#	product.ensure_one()
	#except ValueError:
	#	raise ProductErrorException
		
	#except ProductErrorException:
	#	msg_name = "ERROR: Record Must be One Only."
	#	class_name = type(product).__name__
	#	obj_name = name
	#	msg = msg_name + '\n' + class_name + '\n' + obj_name
	#	raise ProductErrorException('msg')

	# Check if product complete 
	#print()
	#print('Check product_product complete')
	#print(product)
	#print(product.name)

	# Check if product complete 
	#print()
	#print('Check product_product complete')
	#print(product)
	#print(product.name)
	#print(product.pl_price_list)
	#print(product.pl_treatment)
	#print(product.pl_family)
	#print(product.pl_subfamily)
	#print(product.pl_zone)
	#print(product.pl_pathology)
	#print(product.pl_sessions)
	#print(product.pl_level)
	#print(product.pl_time)
	#print(product.pl_zone)




def get_partner(self, name):
	#print()
	#print('Search partner')
	partner = self.env['res.partner'].search([
												('name', '=', name),
											],
											limit=1,
	)
	# Check if partner complete 
	#print('Check res.partner complete')
	#print(partner)
	#print(partner.name)
	return partner

def get_pricelist(self):
	#print()
	#print('Search pricelist')
	pricelist = self.env['product.pricelist'].search([],limit=1,)
	# Check if pricelist complete 
	#print('Check product.pricelist complete')
	#print(pricelist)
	#print(pricelist.name)
	return pricelist

#------------------------------------------------ Get Actual Doctor ------------
def get_actual_doctor(self):
	"""
	Used by Treatment
	"""
	user_name = self.env.user.name
	doctor = self.env['oeh.medical.physician'].search([
															('x_user_name', '=', user_name),
														],
														#order='appointment_date desc',
														limit=1
													)
	return doctor
# get_actual_doctor

#------------------------------------------------ Time -------------------------
class Zone(tzinfo):
	"""
	Used by Treatment
	"""
	def __init__(self,offset,isdst,name):
		self.offset = offset
		self.isdst = isdst
		self.name = name
	def utcoffset(self, dt):
		return timedelta(hours=self.offset) + self.dst(dt)
	def dst(self, dt):
			return timedelta(hours=1) if self.isdst else timedelta(0)
	def tzname(self,dt):
		 return self.name
