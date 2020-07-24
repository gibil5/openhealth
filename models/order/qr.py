# -*- coding: utf-8 -*-
"""
	qr.py
	QR Class

	Created: 			26 Aug 2019
	Last up: 	 		23 Jul 2020
"""
from . import lib_qr

class QR(object):

	#def __init__(self, date, ruc_company, receptor_id_doc_type, receptor_id_doc, receptor_ruc, x_type, serial_nr, amount_total, total_tax):
	def __init__(self, h):
		print('QR - init')

		print(h)

		self.ruc_company = h['ruc_company']
	
		self.x_type = h['x_type']
	
		self.serial_nr = h['serial_nr']

		self.amount_total = h['amount_total']

		self.total_tax = h['total_tax']

		self.date = h['date']

		self.receptor_id_doc_type = h['receptor_id_doc_type']

		self.receptor_id_doc = h['receptor_id_doc']

		self.receptor_ruc = h['receptor_ruc']

		# Create Data
		self.qr_data = lib_qr.get_qr_data(self)

		# Create Img
		self.img_str, self.name = lib_qr.get_qr_img(self.qr_data)

	def get_name(self):
		return self.name

	def get_img_str(self):
		return self.img_str

	def print_obj(self):
		print()
		print('print_obj')
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
