# 13 Dec 2019

	@api.multi
	def pl_export_txt(self):
		# Export - Here !
		#fname = pl_export.pl_export_txt(self, self.electronic_order_ids, self.export_date)


		# Init
		#base_dir = os.environ['HOME']
		#path = base_dir + "/mssoft/ventas/" + self.export_date
















			#print(error)
			#print(msg)
			#if error in [1]:
			#	raise UserError(_(msg))
			#print()



				#print line
				#print line.product_id.name
				#print line.product_uom_qty
				#print line.price_unit
				#print electronic_order
				#print



			#print(error)
			#print(msg)
			#if error in [1]:
			#	raise UserError(_(msg))
			#print()




# ----------------------------------------------------------- Correct ------------------------------
	correct_patient = fields.Many2one(
			'oeh.medical.patient',
		)

	@api.multi
	def correct(self):
		"""
		high level support for doing this and that.
		"""
		print()
		print('Pl - Correct')

		patient = self.correct_patient

		#print()
		#print(patient.name)
		#print(patient.x_id_doc_type)
		#print(patient.x_id_doc_type_code)
		#print(patient.x_id_doc)
		#print(patient.x_dni)

		if patient.x_id_doc in [False]:
			if patient.x_dni not in [False]:
				patient.x_id_doc = patient.x_dni
				patient.x_id_doc_type = 'dni'


