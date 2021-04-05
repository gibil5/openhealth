# -*- coding: utf-8 -*-
"""
	MgtProductCounter Class
	Object counter which is completely decoupled from Mgt 

	Keeps track of:
		name 
		amount 
		count 

	SRP
		Responsibility of this class:
		Build a counter that counts anything.
		For vector pure functions.

	Created:             31 oct 2020
	Last up: 			  3 apr 2021
"""

class MgtProductCounter():
	"""
	Used by Management
	"""
	def __init__(self, name):
		#print()
		#print('ProductCounter  -  init')
		#print(name)
		self.name = name
		self.amount = 0.
		self.count = 0.
		self.average = 0.
		self.percentage = 0.

	def inc_amount(self, amount):
		self.amount += amount

	def inc_count(self, count):
		self.count += count


	def line_analysis(self, name, total, qty):
		"""
		Analyse sale line. 
		If it belongs to the counter. 
		Increase total and qty.
		"""
		#print('line_analysis')
		if name == self.name:
			print('Gotcha !')
			print(name)
			self.inc_amount(total)
			self.inc_count(qty)

	def set_average(self):
		"""
		Average
		"""
		#print('set_average')
		if self.amount != 0:
			self.average = self.amount / self.count

	def set_percentage(self, total):
		"""
		Percentage
		"""
		#print('set_percentage')
		if total != 0:
			self.percentage = (self.amount / total) * 100




