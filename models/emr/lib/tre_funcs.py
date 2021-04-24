# -*- coding: utf-8 -*-
"""
	Tre Funcs
	- Used by Treatment

	Created: 			22 aug 2020
	Last up: 	 		13 apr 2021
"""
from __future__ import print_function
from datetime import datetime, tzinfo, timedelta

# ----------------------------------------------------------- Exceptions -------
class ProductProductError(Exception):
	pass


#--------------------------------------------------------- Checkers ------------
def check_product(self, price_list, product, product_template):
	#print()
	#print('***** check_product')
	#print(price_list)
	#print(product)
	#print(product_template)

	# Correct
	if not product.pl_price_list:
		print('corr pl_price_list')
		product.pl_price_list = product_template.pl_price_list

	if not product.pl_treatment:
		print('corr pl_treatment')
		product.pl_treatment = product_template.pl_treatment

	if not product.pl_family:
		print('corr pl_family')
		product.pl_family = product_template.pl_family



#---------------------------------------------------------- Getters ------------
def get_product_template(self, name, price_list):
	#print()
	#print('Search product template')
	#print(name)
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


def get_product_product(self, name, price_list):
	#print()
	#print('Search product')
	#print(name)
	product = self.env['product.product'].search([
													('name', '=', name),
													('pl_price_list', '=', price_list),
												],
												#order='date_begin asc',
												#limit=1,
	)
	if not product.name:
		msg = 'ProductProduct not found !!!'
		raise ProductProductError(msg)

	return product


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
