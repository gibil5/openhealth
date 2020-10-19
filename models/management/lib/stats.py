# -*- coding: utf-8 -*-
"""
	Stats

	Helper Class

	Created: 			27 Jul 2019
	Last mod: 			27 Jul 2019

"""
from __future__ import print_function
from . import mgt_line_funcs

class Statistics:


	#def initialize(self, name):
	def __init__(self, name):
		#print()
		#print('Stats - Initialize')

		# Init
		self.name = name

		# Nr - 1st level
		self.nr_products = 0
		self.nr_services = 0
		self.nr_consultations = 0
		self.nr_procedures = 0

		# Nr - 2nd level
		self.nr_topical = 0
		self.nr_card = 0
		self.nr_kit = 0
		self.nr_co2 = 0
		self.nr_exc = 0
		self.nr_ipl = 0
		self.nr_ndyag = 0
		self.nr_quick = 0
		self.nr_medical = 0
		self.nr_cosmetology = 0
		self.nr_echo = 0
		self.nr_gyn = 0
		self.nr_prom = 0
		self.nr_credit_notes = 0
		self.nr_other = 0
		self.nr_sub_con_med = 0
		self.nr_sub_con_gyn = 0
		self.nr_sub_con_cha = 0



		# Amo - 1st Level
		self.amo_products = 0
		self.amo_services = 0
		self.amo_consultations = 0
		self.amo_procedures = 0
		self.amo_credit_notes = 0
		self.amo_other = 0

		# Amo - 2nd Level
		self.amo_topical = 0
		self.amo_card = 0
		self.amo_kit = 0
		self.amo_co2 = 0
		self.amo_exc = 0
		self.amo_ipl = 0
		self.amo_ndyag = 0
		self.amo_quick = 0
		self.amo_medical = 0
		self.amo_cosmetology = 0
		self.amo_echo = 0
		self.amo_gyn = 0
		self.amo_prom = 0
		self.amo_sub_con_med = 0
		self.amo_sub_con_gyn = 0
		self.amo_sub_con_cha = 0



	def print(self):
		#print()
		#print('Stats - Print')
		#print(self.locals())

		#for name, value in globals().items():
		#for name, value in locals().items():
		#for name, value in dir():
		#	print(name, value)

		#print(self.__dict__)
		#for key, value in sampleDict.items():
		

		dic = self.__dict__

		for key, value in dic.items():
		    #print value.keys()[0]
			print(key, '\t', value)



	def print_short(self):
		print()
		print('Stats - Print Short')
		print('Nr Products:\t', self.nr_products)
		print('Nr Consultations:\t', self.nr_consultations)
		print('Nr Procedures:\t', self.nr_procedures)
		print('Nr Other:\t', self.nr_other)
		print('Nr Credit Notes:\t', self.nr_credit_notes)





	def update(self, line):
		#print()
		#print('Stats - Update')
		#print(line)
		mgt_line_funcs.line_analysis(self, line)



	def set_stats(self):
		print()
		print('Stats - Set Stats')


