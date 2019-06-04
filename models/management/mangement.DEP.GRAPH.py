# 4 May 2019

import pandas as pd
#import csv



# ----------------------------------------------------------- Create CSV --------------------------
	# 1. Create CSV
	@api.multi
	def create_csv(self):
		"""
		1. Create CSV files with Data.
		"""
		print()
		print('Create CSV')

		# Init
		names = []
		total_amounts = []

		amo_products = []
		amo_consultations = []
		amo_procedures = []

		per_amo_products = []
		per_amo_consultations = []
		per_amo_procedures = []

		per_amo_co2 = []
		per_amo_exc = []
		per_amo_ipl = []
		per_amo_ndyag = []
		per_amo_quick = []

		per_amo_medical = []
		per_amo_cosmetology = []

		per_amo_topical = []
		per_amo_card = []
		per_amo_kit = []




		# Search
		managements = self.env['openhealth.management'].search([
																	('owner', 'not in', ['account']),
															],
																	#order='date_begin asc',
																	order='date_begin,name asc',
																	#limit=1000,
														)
		# Loop
		for mgt in managements:

			names.append(mgt.name)
			total_amounts.append(mgt.total_amount)

			amo_products.append(mgt.amo_products)
			amo_consultations.append(mgt.amo_consultations)
			amo_procedures.append(mgt.amo_procedures)

			per_amo_products.append(mgt.per_amo_products)
			per_amo_consultations.append(mgt.per_amo_consultations)
			per_amo_procedures.append(mgt.per_amo_procedures)


			per_amo_co2.append(mgt.per_amo_co2)
			per_amo_exc.append(mgt.per_amo_exc)
			per_amo_ipl.append(mgt.per_amo_ipl)
			per_amo_ndyag.append(mgt.per_amo_ndyag)
			per_amo_quick.append(mgt.per_amo_quick)

			per_amo_medical.append(mgt.per_amo_medical)
			per_amo_cosmetology.append(mgt.per_amo_cosmetology)

			per_amo_topical.append(mgt.per_amo_topical)
			per_amo_card.append(mgt.per_amo_card)
			per_amo_kit.append(mgt.per_amo_kit)



		# Prints
		if True:
			print(names)
			print(total_amounts)

			print(amo_products)
			print(amo_consultations)
			print(amo_procedures)


			print(per_amo_products)
			print(per_amo_consultations)
			print(per_amo_procedures)

			print(per_amo_co2)
			print(per_amo_exc)
			print(per_amo_ipl)
			print(per_amo_ndyag)
			print(per_amo_quick)

			print(per_amo_medical)
			print(per_amo_cosmetology)

			print(per_amo_topical)
			print(per_amo_card)
			print(per_amo_kit)




		# Export to CSV

		#path = '/Users/gibil/reports/' + self.fname + '.csv'
		#path = '/Users/gibil/reports/mgt.csv'
		#self.fname = '/Users/gibil/reports/mgt.csv'


		# Init
		csv_fname = 'mgt.csv'
		base_dir = os.environ['HOME']
		self.fname = base_dir + "/reports/" + csv_fname



		data_frame = pd.DataFrame({
										"name": names,
										"total_amount": total_amounts,

										"amo_products": amo_products,
										"amo_consultations": amo_consultations,
										"amo_procedures": amo_procedures,

										"per_amo_products": per_amo_products,
										"per_amo_consultations": per_amo_consultations,
										"per_amo_procedures": per_amo_procedures,

										"per_amo_co2": per_amo_co2,
										"per_amo_exc": per_amo_exc,
										"per_amo_ipl": per_amo_ipl,
										"per_amo_ndyag": per_amo_ndyag,
										"per_amo_quick": per_amo_quick,
										
										"per_amo_medical": per_amo_medical,
										"per_amo_cosmetology": per_amo_cosmetology,

										"per_amo_topical": per_amo_topical,
										"per_amo_card": per_amo_card,
										"per_amo_kit": per_amo_kit,
						})


		data_frame.to_csv(self.fname, index=False)


	# Fname
	fname = fields.Char()

	# create_csv



# ----------------------------------------------------------- Create Graph --------------------------
	# 1. Create Graph
	@api.multi
	def create_graph(self):
		"""
		2. Create Graph files with MatPlotLib.
		"""
		print()
		print('Create Graph')

		path = '/Users/gibil/Virtualenvs/Odoo9-min/odoo/'

		#cmd = 'python ' + path + 'addons/openhealth/models/management/data_model.py'
		cmd = 'python ' + path + 'addons/openhealth/models/management/data_model.py -s local'

		print(cmd)

		os.system(cmd)




# ----------------------------------------------------------- Export --------------------------

	# Export
	@api.multi
	def export_stats(self):
		"""
		1. Create CSV files with Data.
		2. Generate Plot using MatPlotLib.
		3. Export to Docean with Rsync.
		"""
		print()
		print('Export Stats')
		self.create_csv()
		self.create_graph()





# ----------------------------------------------------------- Graph Server ------------------------
	# Create Graph Server
	@api.multi
	def create_graph_remote(self):
		"""
		2. Create Graph files with MatPlotLib.
		"""
		print()
		print('Create Graph')
		path = '/root/openerp/'
		#cmd = 'python ' + path + 'addons/openhealth/models/management/data_model.py'
		cmd = 'python ' + path + 'addons/openhealth/models/management/data_model.py -s remote'
		print(cmd)
		os.system(cmd)



