# -*- coding: utf-8 -*-
"""
	Mgt Funcs
	Should be unit testable - independent from openerp

	Created: 			28 May 2018
	Last updated: 		26 oct 2020

	- Use functional programming - ie pure functions.
	- Use lambda funcs, map, filter, reduce, decorators, generators, etc.

	Signature
		division
		averages_pure
		set_percentages
"""
from __future__ import print_function
import datetime

# ------------------------------------------------------------- Constants ------
_DATE_FORMAT = "%Y-%m-%d"
_DATE_HOUR_FORMAT = "%Y-%m-%d %H:%M"
_MODEL_SALE = "sale.order"


# --------------------------------------------------------------- Division -----
def division(amo, nr):
    return round(float(amo) / float(nr), 2) if nr else 0


# ----------------------------------------------------------- Set Averages -----
def averages_pure(vector, func=division):
	"""
	Set Averages Pure 
	Using functional programming
	Used by: Management
	"""
	print("\n")
	print(averages_pure)
	ave = []

	for data in vector: 
		tag = data[0]
		amo = data[1]
		nr = data[2]

		#ave.append(func(amo, nr))
		ave.append((tag, func(amo, nr)))

		print(amo, nr)
	
	print(ave)

	return ave
# averages_pure


# --------------------------------------------------------- Set Percentages ----
def set_percentages(self, total_amount):
	"""
	Set Percentages
	Used by 
		Management
	"""
	# By Month
	if total_amount != 0:
		self.per_amo_other = (self.amo_other / total_amount)

		# Families
		self.per_amo_credit_notes = (self.amo_credit_notes / total_amount)
		self.per_amo_products = (self.amo_products / total_amount)
		self.per_amo_consultations = (self.amo_consultations / total_amount)
		self.per_amo_procedures = (self.amo_procedures / total_amount)

		# Sub Families
		self.per_amo_sub_con_med = (self.amo_sub_con_med / total_amount)
		self.per_amo_sub_con_gyn = (self.amo_sub_con_gyn / total_amount)
		self.per_amo_sub_con_cha = (self.amo_sub_con_cha / total_amount)

		self.per_amo_echo = (self.amo_echo / total_amount)
		self.per_amo_gyn = (self.amo_gyn / total_amount)
		self.per_amo_prom = (self.amo_prom / total_amount)

		self.per_amo_topical = (self.amo_topical / total_amount)
		self.per_amo_card = (self.amo_card / total_amount)
		self.per_amo_kit = (self.amo_kit / total_amount)

		self.per_amo_co2 = (self.amo_co2 / total_amount)
		self.per_amo_exc = (self.amo_exc / total_amount)
		self.per_amo_ipl = (self.amo_ipl / total_amount)
		self.per_amo_ndyag = (self.amo_ndyag / total_amount)
		self.per_amo_quick = (self.amo_quick / total_amount)

		self.per_amo_medical = (self.amo_medical / total_amount)
		self.per_amo_cosmetology = (self.amo_cosmetology / total_amount)
# set_percentages
