# -*- coding: utf-8 -*-
"""
	Mgt Line Funcs

	Created: 			27 Jul 2019
	Last mod: 			27 Jul 2019

	- The goal of functions is to hide Implementation.
"""
from __future__ import print_function
import datetime
from openerp.addons.price_list.models.lib import test_funcs
from openerp import _
from openerp.exceptions import Warning as UserError




# ----------------------------------------------------------- Line Analysis - PL -----------------------
def line_analysis(self, line):
	"""
	Line Analyses Line
	"""
	#print()
	#print('Line Analysis')

	if line.product_id.pl_price_list in ['2019']:
		line_analysis_2019(self, line)

	else:
		#mgt_line_funcs.line_analysis_2018(self, line)
		line_analysis_2018(self, line)






# ----------------------------------------------------------- Line Analysis - PL -----------------------
#def pl_line_analysis(self, line):
def line_analysis_2019(self, line):
	"""
	New - 2019
	Analyses Line to update counters
	"""
	# Print Disable
	test_funcs.disablePrint()
	#print()
	#print('Line Analysis - 2019')



	# Init
	prod = line.product_id

	print(prod.name)
	print(prod.pl_treatment)
	print(prod.pl_family)
	print(prod.pl_subfamily)

	#subfamily = prod.pl_subfamily


	# Services
	if prod.type in ['service']:
		self.nr_services = self.nr_services + line.product_uom_qty
		self.amo_services = self.amo_services + line.price_subtotal


		# Consultations
		#if prod.x_treatment in ['consultation']:
		if prod.pl_subfamily in ['consultation']:
			self.nr_consultations = self.nr_consultations + line.product_uom_qty
			self.amo_consultations = self.amo_consultations + line.price_subtotal

			if prod.pl_treatment in ['CONSULTA MEDICA']:
				self.nr_sub_con_med = self.nr_sub_con_med + line.product_uom_qty
				self.amo_sub_con_med = self.amo_sub_con_med + line.price_subtotal
				
			elif prod.pl_treatment in ['CONSULTA GINECOLOGICA']:
				self.nr_sub_con_gyn = self.nr_sub_con_gyn + line.product_uom_qty
				self.amo_sub_con_gyn = self.amo_sub_con_gyn + line.price_subtotal

			elif prod.pl_treatment in ['CONSULTA MEDICA DR. CHAVARRI']:
				self.nr_sub_con_cha = self.nr_sub_con_cha + line.product_uom_qty
				self.amo_sub_con_cha = self.amo_sub_con_cha + line.price_subtotal



		# Procedures
		else:
			self.nr_procedures = self.nr_procedures + line.product_uom_qty
			self.amo_procedures = self.amo_procedures + line.price_subtotal


			# By Family

			# Echo
			if prod.pl_family in ['echography']:
				self.nr_echo = self.nr_echo + line.product_uom_qty
				self.amo_echo = self.amo_echo + line.price_subtotal

			# Gyn
			elif prod.pl_family in ['gynecology']:
				self.nr_gyn = self.nr_gyn + line.product_uom_qty
				self.amo_gyn = self.amo_gyn + line.price_subtotal

			# Prom
			elif prod.pl_family in ['promotion']:
				self.nr_prom = self.nr_prom + line.product_uom_qty
				self.amo_prom = self.amo_prom + line.price_subtotal



			# By Sub Family

			# Co2
			#elif prod.pl_treatment in ['LASER CO2 FRACCIONAL']:
			elif prod.pl_subfamily in ['co2']:
				self.nr_co2 = self.nr_co2 + line.product_uom_qty
				self.amo_co2 = self.amo_co2 + line.price_subtotal

			# Exc
			#elif prod.pl_treatment in ['LASER EXCILITE']:
			elif prod.pl_subfamily in ['excilite']:
				self.nr_exc = self.nr_exc + line.product_uom_qty
				self.amo_exc = self.amo_exc + line.price_subtotal

			# Quick
			#elif prod.pl_treatment in ['QUICKLASER']:
			elif prod.pl_subfamily in ['quick']:
				self.nr_quick = self.nr_quick + line.product_uom_qty
				self.amo_quick = self.amo_quick + line.price_subtotal



			# By Treatment

			# Ipl
			elif prod.pl_treatment in ['LASER M22 IPL']:
				self.nr_ipl = self.nr_ipl + line.product_uom_qty
				self.amo_ipl = self.amo_ipl + line.price_subtotal

			# Ndyag
			elif prod.pl_treatment in ['LASER M22 ND YAG']:
				self.nr_ndyag = self.nr_ndyag + line.product_uom_qty
				self.amo_ndyag = self.amo_ndyag + line.price_subtotal




			else:
				# Medical
				if prod.pl_family in ['medical']:
					self.nr_medical = self.nr_medical + line.product_uom_qty
					self.amo_medical = self.amo_medical + line.price_subtotal

				# Cosmeto
				elif prod.pl_family in ['cosmetology']:
					self.nr_cosmetology = self.nr_cosmetology + line.product_uom_qty
					self.amo_cosmetology = self.amo_cosmetology + line.price_subtotal



	# Products
	elif prod.type in ['product']:
		self.nr_products = self.nr_products + line.product_uom_qty
		self.amo_products = self.amo_products + line.price_subtotal

		# Topical
		if prod.pl_family in ['topical']:
			self.nr_topical = self.nr_topical + line.product_uom_qty
			self.amo_topical = self.amo_topical + line.price_subtotal

		# Card
		elif prod.pl_family in ['card']:
			self.nr_card = self.nr_card + line.product_uom_qty
			self.amo_card = self.amo_card + line.price_subtotal

		# kit
		elif prod.pl_family in ['kit']:
			self.nr_kit = self.nr_kit + line.product_uom_qty
			self.amo_kit = self.amo_kit + line.price_subtotal




	# Consu - This should not happen - Deprecated !!
	elif prod.type in ['consu']:
		#print('Consu')
		#self.nr_other = self.nr_other + line.product_uom_qty
		#self.amo_other = self.amo_other + line.price_subtotal

		msg = "ERROR: Consumables must not exist !"
		raise UserError(_(msg))



	# Print Enable
	test_funcs.enablePrint()

	return False

# pl_line_analysis





# ----------------------------------------------------------- Line Analysis -----------------------
#def line_analysis(self, line):
def line_analysis_2018(self, line):
	"""
	Old - 2018
	Analyses Line to update counters
	"""
	#print()
	#print('Line Analysis - 2018')


	# Init
	prod = line.product_id


	# Services
	if prod.type in ['service']:
		self.nr_services = self.nr_services + line.product_uom_qty
		self.amo_services = self.amo_services + line.price_subtotal


		# Consultations
		if prod.x_treatment in ['consultation']:
			self.nr_consultations = self.nr_consultations + line.product_uom_qty
			self.amo_consultations = self.amo_consultations + line.price_subtotal

			self.nr_sub_con_med = self.nr_sub_con_med + line.product_uom_qty
			self.amo_sub_con_med = self.amo_sub_con_med + line.price_subtotal


		# Procedures
		else:
			self.nr_procedures = self.nr_procedures + line.product_uom_qty
			self.amo_procedures = self.amo_procedures + line.price_subtotal

			# Co2
			if prod.x_treatment in ['laser_co2']:
				self.nr_co2 = self.nr_co2 + line.product_uom_qty
				self.amo_co2 = self.amo_co2 + line.price_subtotal

			# Exc
			elif prod.x_treatment in ['laser_excilite']:
				self.nr_exc = self.nr_exc + line.product_uom_qty
				self.amo_exc = self.amo_exc + line.price_subtotal

			# Ipl
			elif prod.x_treatment in ['laser_ipl']:
				self.nr_ipl = self.nr_ipl + line.product_uom_qty
				self.amo_ipl = self.amo_ipl + line.price_subtotal

			# Ndyag
			elif prod.x_treatment in ['laser_ndyag']:
				self.nr_ndyag = self.nr_ndyag + line.product_uom_qty
				self.amo_ndyag = self.amo_ndyag + line.price_subtotal

			# Quick
			elif prod.x_treatment in ['laser_quick']:
				self.nr_quick = self.nr_quick + line.product_uom_qty
				self.amo_quick = self.amo_quick + line.price_subtotal

			else:
				# Medical
				if prod.x_family in ['medical']:
					self.nr_medical = self.nr_medical + line.product_uom_qty
					self.amo_medical = self.amo_medical + line.price_subtotal

				# Cosmeto
				elif prod.x_family in ['cosmetology']:
					self.nr_cosmetology = self.nr_cosmetology + line.product_uom_qty
					self.amo_cosmetology = self.amo_cosmetology + line.price_subtotal


	# Products
	#else:
	elif prod.type in ['product']:
		self.nr_products = self.nr_products + line.product_uom_qty
		self.amo_products = self.amo_products + line.price_subtotal


		# Topical
		if prod.x_family in ['topical']:
			self.nr_topical = self.nr_topical + line.product_uom_qty
			self.amo_topical = self.amo_topical + line.price_subtotal

		# card
		elif prod.x_family in ['card']:
			self.nr_card = self.nr_card + line.product_uom_qty
			self.amo_card = self.amo_card + line.price_subtotal

		# kit
		elif prod.x_family in ['kit']:
			self.nr_kit = self.nr_kit + line.product_uom_qty
			self.amo_kit = self.amo_kit + line.price_subtotal



	# Consu
	elif prod.type in ['consu']:

		#print('Consu')

		self.nr_other = self.nr_other + line.product_uom_qty
		self.amo_other = self.amo_other + line.price_subtotal


		#if prod.x_family in ['credit_note']:
		#	self.nr_credit_notes = self.nr_credit_notes + line.product_uom_qty
		#	self.amo_credit_notes = self.amo_credit_notes + line.price_subtotal

	return False

# line_analysis

