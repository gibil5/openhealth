# -*- coding: utf-8 -*-
"""
	Data Model

	Created: 			13 Dic 2018
	Last updated: 		13 Dic 2018
"""
from __future__ import print_function
import csv
import rsync
import matplotlib.pyplot as plt

class DataModel(object):
	"""
	high level support for doing this and that.
	"""

	def __init__(self, path):
		"""
		high level support for doing this and that.
		"""
		print()
		print("Init")

		#self.fname = fname
		self.fname = path + 'mgt.csv'

		#self.fig_pie_year = path + 'img/fig_pie_year.png'
		#self.fig_pie_year_micro = path + 'img/fig_pie_year_micro.png'
		self.fig_pie_year = path + 'img/fig_pie_year_2018.png'
		self.fig_pie_year_micro = path + 'img/fig_pie_year_2018_micro.png'


		self.fig_line_year = path + 'img/fig_line_year_2018.png'
		self.fig_line_year_micro = path + 'img/fig_line_year_micro_2018.png'



		# Floats
		self.per_amo_products = 0
		self.per_amo_consultations = 0
		self.per_amo_procedures = 0

		self.per_amo_co2 = 0
		self.per_amo_exc = 0
		self.per_amo_ipl = 0
		self.per_amo_ndyag = 0
		self.per_amo_quick = 0

		self.per_amo_medical = 0
		self.per_amo_cosmetology = 0

		self.per_amo_topical = 0
		self.per_amo_card = 0
		self.per_amo_kit = 0



		# Arrays
		self.per_amo_products_arr = []
		self.per_amo_consultations_arr = []
		self.per_amo_procedures_arr = []

		self.per_amo_co2_arr = []
		self.per_amo_exc_arr = []
		self.per_amo_ipl_arr = []
		self.per_amo_ndyag_arr = []
		self.per_amo_quick_arr = []

		self.per_amo_medical_arr = []
		self.per_amo_cosmetology_arr = []

		self.per_amo_topical_arr = []
		self.per_amo_card_arr = []
		self.per_amo_kit_arr = []


		self.name_arr = []




	def read_macro(self):
		"""
		high level support for doing this and that.
		"""
		print()
		print("Read Macro")

		# Read
		with open(self.fname, mode='r') as csv_file:

			csv_reader = csv.DictReader(csv_file)

			for row in csv_reader:

				if 'Anual' in row['name']:

					print(row)

					# Time
					#self.sec.append(float(row['sec']))

					self.per_amo_products = float(row['per_amo_products'])
					self.per_amo_consultations = float(row['per_amo_consultations'])
					self.per_amo_procedures = float(row['per_amo_procedures'])


					self.per_amo_co2 = float(row['per_amo_co2'])
					self.per_amo_exc = float(row['per_amo_exc'])
					self.per_amo_ipl = float(row['per_amo_ipl'])
					self.per_amo_ndyag = float(row['per_amo_ndyag'])
					self.per_amo_quick = float(row['per_amo_quick'])

					self.per_amo_medical = float(row['per_amo_medical'])
					self.per_amo_cosmetology = float(row['per_amo_cosmetology'])

					self.per_amo_topical = float(row['per_amo_topical'])
					self.per_amo_card = float(row['per_amo_card'])
					self.per_amo_kit = float(row['per_amo_kit'])


			# Prints
			if False:
				print(self.per_amo_products)
				print(self.per_amo_consultations)
				print(self.per_amo_procedures)

				print(self.per_amo_co2)
				print(self.per_amo_exc)
				print(self.per_amo_ipl)
				print(self.per_amo_ndyag)
				print(self.per_amo_quick)

				print(self.per_amo_medical)
				print(self.per_amo_cosmetology)

				print(self.per_amo_topical)
				print(self.per_amo_card)
				print(self.per_amo_kit)





	def read_micro(self):
		"""
		high level support for doing this and that.
		"""
		print()
		print("Read Micro")

		# Read
		with open(self.fname, mode='r') as csv_file:

			csv_reader = csv.DictReader(csv_file)

			for row in csv_reader:

				if 'Anual' not in row['name']:

					if row['per_amo_products'] not in ['0.0']:

						#print(row)

						# Time
						#self.sec.append(float(row['sec']))


						self.name_arr.append(row['name'][:3])


						self.per_amo_products_arr.append(float(row['per_amo_products']))
						self.per_amo_consultations_arr.append(float(row['per_amo_consultations']))
						self.per_amo_procedures_arr.append(float(row['per_amo_procedures']))


						self.per_amo_co2_arr.append(float(row['per_amo_co2']))
						self.per_amo_exc_arr.append(float(row['per_amo_exc']))
						self.per_amo_ipl_arr.append(float(row['per_amo_ipl']))
						self.per_amo_ndyag_arr.append(float(row['per_amo_ndyag']))
						self.per_amo_quick_arr.append(float(row['per_amo_quick']))

						self.per_amo_medical_arr.append(float(row['per_amo_medical']))
						self.per_amo_cosmetology_arr.append(float(row['per_amo_cosmetology']))

						self.per_amo_topical_arr.append(float(row['per_amo_topical']))
						self.per_amo_card_arr.append(float(row['per_amo_card']))
						self.per_amo_kit_arr.append(float(row['per_amo_kit']))




			# Prints
			print(self.name_arr)


			print(self.per_amo_products_arr)
			print(self.per_amo_consultations_arr)
			print(self.per_amo_procedures_arr)

			print(self.per_amo_co2_arr)
			print(self.per_amo_exc_arr)
			print(self.per_amo_ipl_arr)
			print(self.per_amo_ndyag_arr)
			print(self.per_amo_quick_arr)

			print(self.per_amo_medical_arr)
			print(self.per_amo_cosmetology_arr)

			print(self.per_amo_topical_arr)
			print(self.per_amo_card_arr)
			print(self.per_amo_kit_arr)





	def plot_line(self):
		"""
		Plots Micros.
		To view:
		python -m SimpleHTTPServer 8080
		"""
		print()
		print("Plot Line")

		# Clean
		plt.clf()


		#pl.scatter(g1.sec, g1.speed)

		#pl.plot(self.sec, self.speed, 'bo--', label='Speed')
		plt.plot(self.name_arr, self.per_amo_products_arr, 'o--', label='Productos')
		plt.plot(self.name_arr, self.per_amo_consultations_arr, 'o--', label='Consultas')
		plt.plot(self.name_arr, self.per_amo_procedures_arr, 'o--', label='Procedimientos')

		plt.legend()
		plt.ylabel('Porcentaje')
		plt.xlabel('Por Mes')
		
		#plt.title('Ventas - Por Mes - 2018')

		plt.savefig(self.fig_line_year)

		#pl.show()




	def plot_line_micro(self):
		"""
		Plots Micros.
		To view:
		python -m SimpleHTTPServer 8080
		"""
		print()
		print("Plot Line Micro")


		# Clean
		plt.clf()


		#pl.scatter(g1.sec, g1.speed)


		#plt.plot(self.name_arr, self.per_amo_products_arr, 'o--', label='Productos')
		#plt.plot(self.name_arr, self.per_amo_procedures_arr, 'o--', label='Procedimientos')

		plt.plot(self.name_arr, self.per_amo_topical_arr, 'o--', label='Cremas')
		plt.plot(self.name_arr, self.per_amo_card_arr, 'o--', label='Vip')
		plt.plot(self.name_arr, self.per_amo_kit_arr, 'o--', label='Kit')

		plt.plot(self.name_arr, self.per_amo_consultations_arr, 'o--', label='Consultas')

		plt.plot(self.name_arr, self.per_amo_co2_arr, 'o--', label='Co2')
		plt.plot(self.name_arr, self.per_amo_exc_arr, 'o--', label='Exc')
		plt.plot(self.name_arr, self.per_amo_ipl_arr, 'o--', label='Ipl')
		plt.plot(self.name_arr, self.per_amo_ndyag_arr, 'o--', label='Ndyag')
		plt.plot(self.name_arr, self.per_amo_quick_arr, 'o--', label='Quick')

		plt.plot(self.name_arr, self.per_amo_medical_arr, 'o--', label='Med')
		plt.plot(self.name_arr, self.per_amo_cosmetology_arr, 'o--', label='Cos')


		plt.legend()
		plt.ylabel('Porcentaje')
		plt.xlabel('Por Mes')

		#plt.title('Ventas - Por Mes - 2018 - Detalle')

		plt.savefig(self.fig_line_year_micro)
		#pl.show()





	def plot_pie(self):
		"""
		Plots Macros.
		To view:
		python -m SimpleHTTPServer 8080
		"""
		print()
		print("Plot")


		# Clean
		plt.clf()


		# Plot
		labels = 'Productos', 'Consultas', 'Procedimientos'

		sizes = [self.per_amo_products, self.per_amo_consultations, self.per_amo_procedures]

		explode = (0, 0, 0)

		fig1, ax1 = plt.subplots()

		ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=False, startangle=90)

		ax1.axis('equal')

		#plt.title('Ventas - Anual 2018')

		#plt.show()

		fig1.savefig(self.fig_pie_year)




	def plot_pie_micro(self):
		"""
		Plots Micros.
		To view:
		python -m SimpleHTTPServer 8080
		"""
		print()
		print("Plot Micro")


		# Clean
		plt.clf()


		# Plot
		labels = 'Cremas', 'Vip', 'Kits', 'Consultas', 'Co2', 'Exc', 'Ipl', 'Ndyag', 'Quick', 'Cos', 'Med'

		sizes = [

					self.per_amo_topical,
					self.per_amo_card,
					self.per_amo_kit,

					self.per_amo_consultations,

					self.per_amo_co2,
					self.per_amo_exc,
					self.per_amo_ipl,
					self.per_amo_ndyag,
					self.per_amo_quick,

					self.per_amo_cosmetology,
					self.per_amo_medical,

			]



		explode = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

		fig1, ax1 = plt.subplots()

		ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=False, startangle=90)

		ax1.axis('equal')

		#plt.title('Ventas - Anual 2018 - Detalle')

		#plt.show()

		fig1.savefig(self.fig_pie_year_micro)





	def synchro(self):
		"""
		high level support for doing this and that.
		"""
		print()
		print("Synchro")
		rsync.synchronize()





print('Data Model - In')


#fname = '/Users/gibil/reports/'
fname = '/home/odoo/reports/'
dm = DataModel(fname)


print(dm)

dm.read_macro()
dm.plot_pie()
dm.plot_pie_micro()

dm.read_micro()
dm.plot_line_micro()
dm.plot_line()

dm.synchro()

print('Data Model - Out')
