# -*- coding: utf-8 -*-
"""
	Management - Extra

	SRP
		Responsibility of this class:
		All methods that are smart but not used.

	Created: 			28 oct 2020
	Last up: 			28 oct 2020
"""
from __future__ import print_function
from openerp import models, fields, api

# ------------------------------------------------------------------- Class -----------------------
class ManagementExtra(models.Model):
	"""
    Extra: smart but not used.
	"""
	_inherit = "openhealth.management"

# ----------------------------------------------------------- Update Max -----------------------
	@api.multi
	def update_max(self):
		"""
		Update Year Max
		"""
		print()
		print('X - Update Max')

		# Clear
		mgts = self.env[_MODEL_MGT].search([
															('owner', 'in', ['month']),
															('year', 'in', [self.year]),
														],
														order='date_begin asc',
														#limit=1,
													)
		for mgt in mgts:
			#print(mgt.name)
			mgt.pl_max = False
			mgt.pl_min = False

		# Max
		mgt = self.env[_MODEL_MGT].search([
															('owner', 'in', ['month']),
															('year', 'in', [self.year]),
															('month', 'not in', [False]),
														],
														order='total_amount asc',
														limit=1,
													)
		mgt.pl_min = True

		# Max
		mgt = self.env[_MODEL_MGT].search([
															('owner', 'in', ['month']),
															('year', 'in', [self.year]),
															('month', 'not in', [False]),
														],
														order='total_amount desc',
														limit=1,
													)
		mgt.pl_max = True



# ----------------------------------------------------------- Update Year all -----------------------
	@api.multi
	def update_year_all(self):
		"""
		Update Year All
		"""
		print()
		print('X - Update Year All')

		# Mgts
		mgts = self.env[_MODEL_MGT].search([
															('owner', 'in', ['month']),
															('year', 'in', [self.year]),
														],
														order='date_begin asc',
														#limit=1,
													)
		# Count
		count = self.env[_MODEL_MGT].search_count([
															('owner', 'in', ['month']),
															('year', 'in', [self.year]),
														],
															#order='x_serial_nr asc',
															#limit=1,
														)
		print(mgts)
		print(count)

		for mgt in mgts:
			print(mgt.name)
			mgt.update_year()


# ------------------------------------------------------- Validate external ----
	# Validate
	@api.multi
	def validate_external(self):
		"""
		Validates Data Coherency - External. 
		Looks for data coherency between reports.
		Builds a Report Sale Product for the month. 
		Compares it to Products stats.
		"""
		#print()
		#print('Validate External')

		if self.report_sale_product.name in [False]:
			date_begin = self.date_begin
			self.report_sale_product = self.env['openhealth.report.sale.product'].create({
																							'name': date_begin,
																							'management_id': self.id,
																						})
		rsp = self.report_sale_product
		#print(rsp)
		#print(rsp.name)

		rsp.update()

		self.rsp_count = rsp.total_qty
		self.rsp_total = rsp.total
		self.rsp_count_delta = self.nr_products - self.rsp_count
		self.rsp_total_delta = self.amo_products - self.rsp_total


# ----------------------------------------------------------- Update Year ------
	@api.multi
	def update_year(self):
		"""
		Update Yearly total amounts
		"""
		print()
		print('** Update Year')

		# Mgts
		mgts = self.env["openhealth.management"].search([
												('owner', 'in', ['month']),
												('year', 'in', [self.year]),
											],
												#order='x_serial_nr asc',
												#limit=1,
											)
		# Count
		count = self.env["openhealth.management"].search_count([
													('owner', 'in', ['month']),
													('year', 'in', [self.year]),
											],
												#order='x_serial_nr asc',
												#limit=1,
											)

		#print(mgts)
		#print(count)
		total = 0
		for mgt in mgts:
			total = total + mgt.total_amount
		self.total_amount_year = total
		if self.total_amount_year != 0:
			self.per_amo_total = self.total_amount / self.total_amount_year

	# update_year


