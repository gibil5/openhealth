# -*- coding: utf-8 -*-
"""
	Management - Extra

    Useless functions. 
    Too coupled with odoo 

	Created: 			 3 apr 2021
	Last up: 			 3 apr 2021
"""



# ------------------------------------------------------------------- Class -----------------------
#class Management(models.Model):
class Management():
	"""
	Finance module
	"""
	#_name = 'openhealth.management'
	_order = 'date_begin desc'
	_inherit = 'openhealth.management'



# ----------------------------------------------------------- Line Analysis ----
	def line_analysis(self, line):
		"""
		Parses order lines
		Updates counters
		"""
		print('Line analysis')

		# Init
		prod = line.product_id

		#print('name: ', prod.name)
		#print('treatment: ', prod.pl_treatment)
		#print('family: ', prod.pl_family)
		#print('sub_family: ', prod.pl_subfamily)
		#print()


		# Products
		if prod.type in ['product']:
			self.nr_products = self.nr_products + line.product_uom_qty
			self.amo_products = self.amo_products + line.price_subtotal

			# Topical
			if prod.pl_family in ['topical']:
				self.nr_topical = self.nr_topical + line.product_uom_qty
				self.amo_topical = self.amo_topical + line.price_subtotal
				return

			# Card
			elif prod.pl_family in ['card']:
				self.nr_card = self.nr_card + line.product_uom_qty
				self.amo_card = self.amo_card + line.price_subtotal
				return

			# kit
			elif prod.pl_family in ['kit']:
				self.nr_kit = self.nr_kit + line.product_uom_qty
				self.amo_kit = self.amo_kit + line.price_subtotal
				return



		# Services
		else:
			self.nr_services = self.nr_services + line.product_uom_qty
			self.amo_services = self.amo_services + line.price_subtotal

			# Consultations
			if prod.pl_treatment in ['CONSULTA MEDICA']:
				self.nr_sub_con_med = self.nr_sub_con_med + line.product_uom_qty
				self.amo_sub_con_med = self.amo_sub_con_med + line.price_subtotal
				return

			# Procedures
			else:
				self.nr_procedures = self.nr_procedures + line.product_uom_qty
				self.amo_procedures = self.amo_procedures + line.price_subtotal

				# By Treatment
				# Co2
				if prod.pl_treatment in ['LASER CO2 FRACCIONAL']:
					self.nr_co2 = self.nr_co2 + line.product_uom_qty
					self.amo_co2 = self.amo_co2 + line.price_subtotal
					return

				# Exc
				elif prod.pl_treatment in ['LASER EXCILITE']:
					self.nr_exc = self.nr_exc + line.product_uom_qty
					self.amo_exc = self.amo_exc + line.price_subtotal
					return

				# Quick
				elif prod.pl_treatment in ['QUICKLASER']:
					self.nr_quick = self.nr_quick + line.product_uom_qty
					self.amo_quick = self.amo_quick + line.price_subtotal
					return

				# Ipl
				elif prod.pl_treatment in ['LASER M22 IPL']:
					self.nr_ipl = self.nr_ipl + line.product_uom_qty
					self.amo_ipl = self.amo_ipl + line.price_subtotal
					return

				# Ndyag
				elif prod.pl_treatment in ['LASER M22 ND YAG']:
					self.nr_ndyag = self.nr_ndyag + line.product_uom_qty
					self.amo_ndyag = self.amo_ndyag + line.price_subtotal
					return

				# Medical
				elif prod.pl_family in ['medical']:
					self.nr_medical = self.nr_medical + line.product_uom_qty
					self.amo_medical = self.amo_medical + line.price_subtotal
					return

				# Cosmeto
				elif prod.pl_family in ['cosmetology']:
					self.nr_cosmetology = self.nr_cosmetology + line.product_uom_qty
					self.amo_cosmetology = self.amo_cosmetology + line.price_subtotal
					return

				# Echo
				elif prod.pl_family in ['echography']:
					self.nr_echo = self.nr_echo + line.product_uom_qty
					self.amo_echo = self.amo_echo + line.price_subtotal
					return

				# Gyn
				elif prod.pl_family in ['gynecology']:
					self.nr_gyn = self.nr_gyn + line.product_uom_qty
					self.amo_gyn = self.amo_gyn + line.price_subtotal
					return

				# Prom
				elif prod.pl_family in ['promotion']:
					self.nr_prom = self.nr_prom + line.product_uom_qty
					self.amo_prom = self.amo_prom + line.price_subtotal
					return

	# line_analysis
    
