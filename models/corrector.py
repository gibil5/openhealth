# -*- coding: utf-8 -*-
"""
	Corrector

	Created: 				 6 Nov 2018
	Last mod: 				 8 Nov 2018
"""
import os
import csv
from openerp import models, fields, api

class Corrector(models.Model):
	"""
	high level support for doing this and that.
	"""
	_name = 'openhealth.corrector'

	_description = 'Corrector'

	#_inherit = 'openhealth.container'

	#_order = 'date_begin asc'



	name = fields.Char(
			required=True,
		)

	vspace = fields.Char(
			'',
		)


	delta = fields.Integer(
			default=1,
		)


	# Flags
	go_flag = fields.Boolean()
	product_flag = fields.Boolean()
	co2_flag = fields.Boolean()
	exc_flag = fields.Boolean()
	ipl_flag = fields.Boolean()
	ndy_flag = fields.Boolean()
	qui_flag = fields.Boolean()
	cos_flag = fields.Boolean()
	med_flag = fields.Boolean()
	con_flag = fields.Boolean()

	# Count
	fix_count = fields.Integer()



# ----------------------------------------------------------- Relational --------------------------
	pl_item_ids = fields.One2many(
			'product.pricelist.item',
			'corrector_id',
		)


# ----------------------------------------------------------- Pricelist ---------------------------

	# Clear Pl Items
	@api.multi
	def clear_pl_items(self):
		"""
		high level support for doing this and that.
		"""
		print
		print 'Clear Pl Items'

		# Clear
		self.pl_item_ids.unlink()





# ----------------------------------------------------------- Pricelist ---------------------------
	# Create Pl Items
	@api.multi
	def create_pl_items(self):
		"""
		high level support for doing this and that.
		"""
		print
		print 'Create Pl Items'


		# Clear
		self.pl_item_ids.unlink()



		# Search

		# Product
		if self.product_flag:
			products = self.env['product.template'].search([
																('type', 'in', ['product']),
														],
														#order='appointment_date desc',
														#limit=1,
													)
		
		# Consultation
		elif self.con_flag:
			products = self.env['product.template'].search([
																('type', 'in', ['service']),
																('x_treatment', 'in', ['consultation']),
														],
														#order='appointment_date desc',
														#limit=1,
													)

		# Co2
		elif self.co2_flag:
			products = self.env['product.template'].search([
																('type', 'in', ['service']),
																('x_treatment', 'in', ['laser_co2']),
														],
														#order='appointment_date desc',
														#limit=1,
													)
		# Excilite
		elif self.exc_flag:
			products = self.env['product.template'].search([
																('type', 'in', ['service']),
																('x_treatment', 'in', ['laser_excilite']),
														],
														#order='appointment_date desc',
														#limit=1,
													)

		# Ipl
		elif self.ipl_flag:
			products = self.env['product.template'].search([
																('type', 'in', ['service']),
																('x_treatment', 'in', ['laser_ipl']),
														],
														#order='appointment_date desc',
														#limit=1,
													)

		# Ndyag
		elif self.ndy_flag:
			products = self.env['product.template'].search([
																('type', 'in', ['service']),
																('x_treatment', 'in', ['laser_ndyag']),
														],
														#order='appointment_date desc',
														#limit=1,
													)

		# Quick
		elif self.qui_flag:
			products = self.env['product.template'].search([
																('type', 'in', ['service']),
																('x_treatment', 'in', ['laser_quick']),
														],
														#order='appointment_date desc',
														#limit=1,
													)






		# Init
		name_pl = 'VIP'
		pricelist_id = self.env['product.pricelist'].search([
																('name', '=', name_pl),
													],
													#order='appointment_date desc',
													limit=1,
												).id
		min_quantity = 1
		applied_on = '1_product'
		x_type = 'product'



		# Create
		for product in products:

			print product

			#name = row['Name']
			#fixed_price = row['Sale Price']
			#x_type = row['Type']
			#name_short = row['Name Short']
			#product_tmpl_id = self.env['product.template'].search([
			#														('x_name_short', '=', name_short),
			#									],
												#order='appointment_date desc',
			#									limit=1,
			#								).id
			
			# Init
			name = product.name
			fixed_price = product.list_price
			x_type = product.type
			name_short = product.x_name_short
			product_tmpl_id = product.id


			# Create
			pl_item = self.pl_item_ids.create({
												'name': name,
												'product_tmpl_id': product_tmpl_id,
												'fixed_price': fixed_price,
												'x_type': x_type,
												'min_quantity': min_quantity,
												'applied_on': applied_on,

												'pricelist_id': pricelist_id,
												'corrector_id': self.id,
				})

			print pl_item







# ----------------------------------------------------------- Pricelist ---------------------------
	# Import Pl Items
	@api.multi
	def import_pl_items(self):
		"""
		high level support for doing this and that.
		"""
		print
		print 'Create Pl Items'


		# Clear
		self.pl_item_ids.unlink()



		# Read from file
		file_name = 'product_pl_import.csv'
		base_dir = os.environ['HOME']
		fname = base_dir + "/import/" + file_name
		with open(fname, mode='r') as csv_file:
			csv_reader = csv.DictReader(csv_file, delimiter=',')
			data = []
			for row in csv_reader:
				#print row
				data.append(row)



		# Init
		name_pl = 'VIP'
		pricelist_id = self.env['product.pricelist'].search([
																('name', '=', name_pl),
													],
													#order='appointment_date desc',
													limit=1,
												).id
		min_quantity = 1
		applied_on = '1_product'
		x_type = 'product'



		# Create
		for row in data:
			print row

			# Init
			name = row['Name']
			fixed_price = row['Sale Price']
			x_type = row['Type']
			name_short = row['Name Short']
			product_tmpl_id = self.env['product.template'].search([
																	('x_name_short', '=', name_short),
												],
												#order='appointment_date desc',
												limit=1,
											).id


			# Create
			pl_item = self.pl_item_ids.create({
												'name': name,
												'product_tmpl_id': product_tmpl_id,
												'fixed_price': fixed_price,
												'x_type': x_type,
												'min_quantity': min_quantity,
												'applied_on': applied_on,

												'pricelist_id': pricelist_id,
												'corrector_id': self.id,
				})

			print pl_item

		# Print
		#print data




# ----------------------------------------------------------- Unfix ------------------------------

	# Fix Names
	@api.multi
	def unfix_names(self):
		"""
		high level support for doing this and that.
		"""
		print
		print 'Unfix Names'


		# Init
		treatments = False
		families = False


		# Conditional
		if self.co2_flag:
			treatments = 'laser_co2'

		elif self.exc_flag:
			treatments = 'laser_excilite'

		elif self.ipl_flag:
			treatments = 'laser_ipl'

		elif self.ndy_flag:
			treatments = 'laser_ndyag'

		elif self.qui_flag:
			treatments = 'laser_quick'

		elif self.cos_flag:
			families = 'cosmetology'

		else:
			treatments = False
			families = False




		# Search
		if treatments != False:

			# Search by Treatment
			products = self.env['product.template'].search([
																('type', 'in', ['service']),
																('sale_ok', 'in', [True]),

																('x_treatment', 'in', [treatments]),
													],
														order='x_name_short asc',
														#limit=1,
														limit=self.fix_count,
													)

		if families != False:

			# Search by Family
			products = self.env['product.template'].search([
																('type', 'in', ['service']),
																('sale_ok', 'in', [True]),

																('x_family', 'in', [families]),
													],
														order='x_name_short asc',
														#limit=1,
														limit=self.fix_count,
													)




		# Loop
		for product in products:
			print product.name
			if self.go_flag:
				print
				product.unfix_name()




# ----------------------------------------------------------- Fix ------------------------------

	# Fix Names
	@api.multi
	def fix_names(self):
		"""
		high level support for doing this and that.
		"""
		print
		print 'Fix Names'


		# Init
		treatments = False
		families = False


		# Conditional
		if self.co2_flag:
			treatments = 'laser_co2'

		elif self.exc_flag:
			treatments = 'laser_excilite'

		elif self.ipl_flag:
			treatments = 'laser_ipl'

		elif self.ndy_flag:
			treatments = 'laser_ndyag'

		elif self.qui_flag:
			treatments = 'laser_quick'

		elif self.cos_flag:
			families = 'cosmetology'

		else:
			treatments = False
			families = False



		# Search
		if treatments != False:

			# Search by Treatment
			products = self.env['product.template'].search([
																('type', 'in', ['service']),
																('sale_ok', 'in', [True]),

																('x_treatment', 'in', [treatments]),
													],
														order='x_name_short asc',
														#limit=1,
														limit=self.fix_count,
													)

		if families != False:

			# Search by Family
			products = self.env['product.template'].search([
																('type', 'in', ['service']),
																('sale_ok', 'in', [True]),

																('x_family', 'in', [families]),
													],
														order='x_name_short asc',
														#limit=1,
														limit=self.fix_count,
													)





		# Loop
		for product in products:
			print product.name

			product.x_go_flag = self.go_flag

			product.fix_name()



# ----------------------------------------------------------- Creates ------------------------------

	# Create Codes
	@api.multi
	def create_codes(self):
		"""
		high level support for doing this and that.
		"""
		print
		print 'Create - Codes'


		# Product
		if self.product_flag:

			count = self.env['product.product'].search_count([
																('type', 'in', ['product']),
																('sale_ok', 'in', [True]),
												],
													#order='name asc',
													#limit=1,
												)

			products = self.env['product.product'].search([
																('type', 'in', ['product']),
																('sale_ok', 'in', [True]),
												],
													order='name asc',
													#limit=1,
												)


		# Laser

		if self.co2_flag:
			treatment = 'laser_co2'

		if self.exc_flag:
			treatment = 'laser_excilite'

		if self.ipl_flag:
			treatment = 'laser_ipl'

		if self.ndy_flag:
			treatment = 'laser_ndyag'

		if self.qui_flag:
			treatment = 'laser_quick'



		#if self.co2_flag:
		if self.co2_flag or self.exc_flag or self.ipl_flag or self.ndy_flag or self.qui_flag:

			count = self.env['product.product'].search_count([
																('type', 'in', ['service']),
																('sale_ok', 'in', [True]),
																#('x_treatment', 'in', ['laser_co2']),
																('x_treatment', 'in', [treatment]),
												],
													#order='name asc',
													#limit=1,
												)

			products = self.env['product.product'].search([
																('type', 'in', ['service']),
																('sale_ok', 'in', [True]),
																#('x_treatment', 'in', ['laser_co2']),
																('x_treatment', 'in', [treatment]),
												],
													order='x_name_short asc',
													#limit=1,
												)


		# Correct
		idx = self.delta

		#for product in products.sorted(key=lambda l: l.type in ['product']):
		for product in products:

			print product.name
			print product.x_name_short

			if self.go_flag:
				product.x_counter = idx

			idx = idx + 1


		print
		print count
		print

	# create_codes
