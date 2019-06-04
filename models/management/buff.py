

	# Procedures
	nr_co2 = fields.Integer(
			'Nr Co2',
		)
	amo_co2 = fields.Float(
			'Monto Co2',
		)

	per_amo_co2 = fields.Float(
			'% Monto Co2',
		)





# Management


# ----------------------------------------------------------- Graph --------------------------
	# 1. Create Graph
	@api.multi
	def create_graph(self):
		"""
		2. Create Graph files with MatPlotLib.
		"""
		print()
		print('Create Graph')


		# Read
		with open(self.fname, mode='r') as csv_file:

			csv_reader = csv.DictReader(csv_file)

			ctr = 0

			for row in csv_reader:

				#if ctr < self.count:
				if 'Anual' in row['name']:

					print(row)

					# Time
					#self.sec.append(float(row['sec']))

					per_amo_products = float(row['per_amo_products'])
					per_amo_consultations = float(row['per_amo_consultations'])
					per_amo_procedures = float(row['per_amo_procedures'])

					print(per_amo_products)
					print(per_amo_consultations)
					print(per_amo_procedures)


		# Plot
		labels = 'Productos', 'Consultas', 'Procedimientos'
		sizes = [per_amo_products, per_amo_consultations, per_amo_consultations]
		explode = (0, 0, 0)
		fig1, ax1 = plt.subplots()
		ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
		ax1.axis('equal')

		#plt.show()
		
		#fig.savefig('foo.png')
		#fig.savefig('path/to/save/image/to.png')   # save the figure to file

# ----------------------------------------------------------- Dep --------------------------
	#test_target = fields.Boolean(
	#		string="Test Target",
	#	)

	#fname = fields.Selection(
	#		[
	#			('2018_12', '2018_12'),
	#			('2018', 	'2018'),
	#		],
	#	)






