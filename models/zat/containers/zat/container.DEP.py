# 13 Ded 2019


	export_date = fields.Char(
			'Export Date',
			readonly=True,
		)




# ----------------------------------------------------------- Relational --------------------------
	# Txt - TXT
	txt_ids = fields.One2many(
			'openhealth.texto',
			'container_id',
		)


# ----------------------------------------------------------- Fields --------------------------


	# Txt File Name
	txt_pack_name = fields.Char(
			#'Paquete TXT - Name',
			'Nombre Archivo TXT',
		)


	# Download
	txt_pack = fields.Binary(
			'Descargar TXT',
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


























# ----------------------------------------------------------- Relational --------------------------


	# Electronic Order - Facturación
	electronic_order_ids = fields.One2many(
			'openhealth.electronic.order',
			'container_id',
		)





	# Txt - Ref - MsSoft - Dep ?
	#txt_ref_ids = fields.One2many(
	#		'openhealth.texto',
	#		'container_ref_id',
	#	)



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
