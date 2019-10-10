# -*- coding: utf-8 -*-
"""
	Container

	Created: 				30 Sep 2018
	Last mod: 				 4 Nov 2018
"""
from __future__ import print_function

import base64
import io
import datetime
from openerp import models, fields, api
from . import export

class Container(models.Model):
	"""
	high level support for doing this and that.
	"""
	_name = 'openhealth.container'




# ----------------------------------------------------------- Relational --------------------------

	# Electronic Order
	electronic_order_ids = fields.One2many(
			'openhealth.electronic.order',
			'container_id',
		)

	# Txt
	txt_ids = fields.One2many(
			'openhealth.texto',
			'container_id',
		)

	# Txt - Ref - MsSoft
	txt_ref_ids = fields.One2many(
			'openhealth.texto',
			'container_ref_id',
		)



# ----------------------------------------------------------- Natives ----------------------------
	# Name
	name = fields.Char(
			'Nombre',
		)

	# Dates
	export_date_begin = fields.Date(
			string="Fecha Inicio",
			default=fields.Date.today,
			required=True,
		)

	export_date = fields.Char(
			'Export Date',
			readonly=True,
		)


	# Total
	amount_total = fields.Float(
			'Total',
			digits=(16, 2),
		)

	# Receipt count
	receipt_count = fields.Integer(
			'Recibos Nr',
		)

	# Invoice count
	invoice_count = fields.Integer(
			'Facturas Nr',
		)



	# Download
	txt_pack = fields.Binary(
			'Descargar TXT',
		)

	txt_pack_name = fields.Char(
			#'Paquete TXT - Name',
			'Nombre Archivo TXT',
		)



# ----------------------------------------------------------- Clean -----------------------------
	# Clear
	@api.multi
	def clear(self):
		"""
		Cleans all variables.
		"""
		# Electronic
		self.electronic_order_ids.unlink()
		# Txt
		self.txt_ids.unlink()
		# Stats
		self.amount_total = 0
		self.invoice_count = 0
		self.receipt_count = 0
	# clear
