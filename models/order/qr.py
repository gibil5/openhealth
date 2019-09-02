# -*- coding: utf-8 -*-
"""
qr.py

Created: 			26 Aug 2019
Last up: 	 		26 Aug 2019
"""
from . import lib_qr

class QR(object):

	#def __init__(self, name=None, logo=None, members=0):
	#def __init__(self, ruc_company, x_type, serial_nr, amount_total, total_tax):
	def __init__(self, date, ruc_company, receptor_id_doc_type, receptor_id_doc, receptor_ruc, x_type, serial_nr, amount_total, total_tax):

		self.ruc_company = ruc_company
	
		self.x_type = x_type
	
		self.serial_nr = serial_nr

		self.amount_total = amount_total

		self.total_tax = total_tax


		self.date = date


		self.receptor_id_doc_type = receptor_id_doc_type

		self.receptor_id_doc = receptor_id_doc

		self.receptor_ruc = receptor_ruc



		# Create Data
		#self.x_qr_data = lib_qr.get_qr_data(self)
		self.qr_data = lib_qr.get_qr_data(self)

		# Create Img
		#img_str, name = lib_qr.get_qr_img(self.x_qr_data)
		self.img_str, self.name = lib_qr.get_qr_img(self.qr_data)



	def print_obj(self):
		print()

		# Sale
		print(self.date)
		print(self.x_type)
		print(self.serial_nr)
		print(self.amount_total)
		print(self.total_tax)

		# Emitter
		print(self.ruc_company)

		# Receptor
		print(self.receptor_id_doc_type)
		print(self.receptor_id_doc)
		print(self.receptor_ruc)



	def get_img_str(self):

		return self.img_str


	def get_name(self):

		return self.name





