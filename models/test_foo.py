# -*- coding: utf-8 -*-
"""
 	test_foo.py
"""
from __future__ import print_function
from . import gen
from . import lib_exp
from . import chk_patient


# Base
class Base(object):
	
	def __init__(self, obj):
		pass

	def test(self):
		print()
		print('Test - Base')

	def __repr__(self):
		description = 'Print Base'
		return description




class LibGen(object):
	"""
	high level support for doing this and that.
	"""


	def __init__(self):

		self.generated_arr = []

		self.names_prod = [
						'acneclean',
						#'acnetopic_200ml',
						#'aloe_vital',
		]

		self.names_con = [
						'con_med',
						#'con_gyn',
		]

		self.names_co2 = [
						'co2_bol_as1_one',
						'co2_vag_mon_one',

		]


		self.names_exc = [
						'exc_are_alo_15m_one',
						'ipl_are_dep_15m_one',
						'ndy_bol_ema_15m_one',
						'car_bod_rfa_30m_one',	# Cosmeto
		]


		self.names_quick = [
						'qui_nec-han_rej_5m_one',

		]

		self.names_med = [
						'bot_1zo_rfa_one',

		]



	def test(self):
		"""
		high level support for doing this and that.
		"""
		print()
		print('Test - LibGen')


		# Test
		for name in self.names_prod:
			generated = gen.get_generated_prod(name)
			self.generated_arr.append(generated)
			#print(generated)

		for name in self.names_con:
			generated = gen.get_generated_con(name)
			self.generated_arr.append(generated)
			#print(generated)

		for name in self.names_co2:
			generated = gen.get_generated_co2(name)
			self.generated_arr.append(generated)
			#print(generated)

		for name in self.names_exc:
			generated = gen.get_generated_exc(name)
			self.generated_arr.append(generated)
			#print(generated)

		for name in self.names_quick:
			generated = gen.get_generated_quick(name)
			self.generated_arr.append(generated)
			#print(generated)

		for name in self.names_med:
			generated = gen.get_generated_med(name)
			self.generated_arr.append(generated)
			#print(generated)


	def __repr__(self):

		description = ''
		
		for generated in self.generated_arr:
			description = description + generated + '\n'
		
		return description





class LibExp(object):
	"""
	high level support for doing this and that.
	"""

	def __init__(self, electronic_order):
		self.electronic_order = electronic_order


	def test(self):
		"""
		high level support for doing this and that.
		"""
		print()
		print('Test - LibExp')

		# File name
		self.file_name = lib_exp.get_file_name(self.electronic_order)

		# Content
		self.content = lib_exp.get_file_content(self.electronic_order)

		#print(self.electronic_order)
		#print(self.content)
		#print(self.file_name)


	def __repr__(self):
		description = self.electronic_order.__class__.__name__ + '\t' + self.electronic_order.name + '\n' + \
						self.file_name
		return description





class LibChkPatient(object):
	"""
	high level support for doing this and that.
	"""

	def __init__(self, patient):
		self.patient = patient


	def test(self):
		"""
		high level support for doing this and that.
		"""
		print()
		print('Test - LibChkPatient')
		print(self.patient)

		chk_patient.check_name(self.patient)
		chk_patient.check_x_ruc(self.patient)
		chk_patient.check_x_id_doc(self.patient)
		chk_patient.check_x_id_code(self.patient)



	def __repr__(self):

		description = self.patient.__class__.__name__ + '\t' + self.patient.name

		return description







class Reports(object):
	"""
	high level support for doing this and that.
	"""

	def __init__(self, obj):

		# Marketing
		self.marketing = obj.env['openhealth.marketing'].search([
													],
												#order=self.descriptor +  ' desc',
												order='write_date desc',
												limit=1,
										)
		# Management
		self.management = obj.env['openhealth.management'].search([
													],
												#order=self.descriptor +  ' desc',
												order='write_date desc',
												limit=1,
										)


		# Closing
		self.closing = obj.env['openhealth.closing'].search([
													],
												#order=self.descriptor +  ' desc',
												order='write_date desc',
												limit=1,
										)

		# RSP
		self.resap = obj.env['openhealth.report.sale.product'].search([
													],
												#order=self.descriptor +  ' desc',
												order='write_date desc',
												limit=1,
										)

		# Account
		self.account = obj.env['openhealth.account.contasis'].search([
													],
												#order=self.descriptor +  ' desc',
												order='write_date desc',
												limit=1,
										)

		# Container
		self.container = obj.env['openhealth.container'].search([
													],
												#order=self.descriptor +  ' desc',
												order='write_date desc',
												limit=1,
										)



	def test(self):
		"""
		high level support for doing this and that.
		"""
		print()
		print('Test - Reports')
		self.marketing.update()
		self.management.update()
		self.closing.update()
		self.resap.update()
		self.account.update()

		self.container.update()
		self.container.remove_patients()
		self.container.create_patients()


	def __repr__(self):

		description = self.marketing.__class__.__name__ + '\t' + self.marketing.name + '\n' + \
						self.management.__class__.__name__ + '\t' + self.management.name + '\n' + \
						self.closing.__class__.__name__ + '\t' + self.closing.name + '\n' + \
						self.resap.__class__.__name__ + '\t' + self.resap.name + '\n' + \
						self.account.__class__.__name__ + '\t' + self.account.name + '\n' + \
						self.container.__class__.__name__ + '\t' + self.container.name 

		return description






#class Products(object):
class Products(Base):
	
	def __init__(self, obj):
		
		# Products
		self.products = obj.env['product.template'].search([
																('x_test', '=', True),

													],
												#order=self.descriptor +  ' desc',
												#order='write_date desc',
												#limit=1,
										)

		# Services Co2
		self.service_co2 = obj.env['openhealth.service.co2'].search([
													],
												order='write_date desc',
												limit=1,
										)

	
	def test(self):
		print()
		print('Test - Products')
		
		# Products
		for product in self.products:
			print(product.name)
			product.test()


		# Services Co2
		print(self.service_co2.name)
		self.service_co2.test()



	#def __repr__(self):
	#	description = ''
	#	return description









#class Patients(object):
class Patients(Base):
	
	def __init__(self, obj):
		

		# patients
		self.patients = obj.env['oeh.medical.patient'].search([
																('name', 'in', ['REVILLA RONDON JOSE JAVIER']),
																('x_test', '=', True),

													],
												#order=self.descriptor +  ' desc',
												#order='write_date desc',
												#limit=1,
										)

	def test(self):
		print()
		print('Test - Patients')
		
		# Patients
		for patient in self.patients:
			print(patient.name)
			patient.test()



	#def __repr__(self):
	#	description = ''
	#	return description





#class Payments(object):
class Payments(Base):
	
	def __init__(self, obj):

		# Payments
		self.payments = obj.env['openhealth.payment_method'].search([
																		('partner', 'in', ['REVILLA RONDON JOSE JAVIER']),

													],
												order='write_date desc',
												limit=1,
										)

	def test(self):
		print()
		print('Test - Payments')
		
		# Payments
		for payment in self.payments:
			
			print(payment.partner.name)
			
			payment.test()


	#def __repr__(self):
	#	description = ''
	#	return description







#def main():
#	lib = LibGen()
#	lib.test()

#if __name__ == '__main__':
#	main()
