# -*- coding: utf-8 -*-
"""
		qr.py

		Created: 			26 Aug 2019
		Last up: 	 		26 Aug 2019
"""
from . import lib_qr

class QR(object):

	#def __init__(self, name=None, logo=None, members=0):
	def __init__(self, ruc_company, x_type, serial_nr, amount_total, total_tax):

		self.ruc_company = ruc_company
	
		self.x_type = x_type
	
		self.serial_nr = serial_nr

		self.amount_total = amount_total

		self.total_tax = total_tax


		# Create Data
		self.x_qr_data = lib_qr.get_qr_data(self)

		# Create Img
		img_str, name = lib_qr.get_qr_img(self.x_qr_data)
