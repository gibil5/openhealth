# -*- coding: utf-8 -*-
"""
	Mgt Bridge

    Concentrates state change.

	Created: 			30 oct 2018
	Last up: 			28 nov 2020
"""
from __future__ import print_function
from . import mgt_funcs


# Totals
def set_totals(self, vector):
	"""
	Set totals
	"""
	self.vec_amount = mgt_funcs.obj_get_amount_total_pure(vector)
	self.vec_count = mgt_funcs.obj_get_count_total_pure(vector)


# Types
def set_types(self, vector):
	"""
	Set types
	"""
	obj = filter(lambda x: x.name == 'products', vector)[0]
	self.vec_products_amount = obj.amount
	self.vec_products_count = obj.count

	obj = filter(lambda x: x.name == 'services', vector)[0]
	self.vec_services_amount = obj.amount
	self.vec_services_count = obj.count


# Sub families
def set_subfamilies(self, vector):
	"""
	Set subfamilies
	"""
	# Laser
	obj = filter(lambda x: x.name == 'co2', vector)[0]
	self.vec_co2_amount = obj.amount
	self.vec_co2_count = obj.count

	obj = filter(lambda x: x.name == 'exc', vector)[0]
	self.vec_exc_amount = obj.amount
	self.vec_exc_count = obj.count

	obj = filter(lambda x: x.name == 'ndy', vector)[0]
	self.vec_ndy_amount = obj.amount
	self.vec_ndy_count = obj.count

	obj = filter(lambda x: x.name == 'ipl', vector)[0]
	self.vec_ipl_amount = obj.amount
	self.vec_ipl_count = obj.count

	obj = filter(lambda x: x.name == 'qui', vector)[0]
	self.vec_qui_amount = obj.amount
	self.vec_qui_count = obj.count


	# Medical

	obj = filter(lambda x: x.name == 'med', vector)[0]
	self.vec_med_amount = obj.amount
	self.vec_med_count = obj.count

	obj = filter(lambda x: x.name == 'cos', vector)[0]
	self.vec_cos_amount = obj.amount
	self.vec_cos_count = obj.count



	obj = filter(lambda x: x.name == 'gyn', vector)[0]
	self.vec_gyn_amount = obj.amount
	self.vec_gyn_count = obj.count

	obj = filter(lambda x: x.name == 'ech', vector)[0]
	self.vec_ech_amount = obj.amount
	self.vec_ech_count = obj.count

	obj = filter(lambda x: x.name == 'pro', vector)[0]
	self.vec_pro_amount = obj.amount
	self.vec_pro_count = obj.count


	# Prod
	obj = filter(lambda x: x.name == 'top', vector)[0]
	self.vec_top_amount = obj.amount
	self.vec_top_count = obj.count

	obj = filter(lambda x: x.name == 'vip', vector)[0]
	self.vec_vip_amount = obj.amount
	self.vec_vip_count = obj.count

	obj = filter(lambda x: x.name == 'kit', vector)[0]
	self.vec_kit_amount = obj.amount
	self.vec_kit_count = obj.count
