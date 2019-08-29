# -*- coding: utf-8 -*-
"""
	Scheduler - Disabled - Not Dep

	Created: 			27 Dic 2018
	Last updated: 		28 Aug 2019
"""
from __future__ import print_function
import datetime
from openerp import models, fields, api


class Scheduler(models.Model):
	"""
	Allows automatic backup of all Reports - DISABLED
	"""
	_name = 'openhealth.scheduler'



# ----------------------------------------------------------- Fields ------------------------------

	name = fields.Char(
			#string="Nombre",
			required=True,
		)

	date_begin = fields.Date(
			string="Fecha Inicio",
			default=fields.Date.today,
			#readonly=True,
			#required=True,
		)

	date_end = fields.Date(
			string="Fecha Fin",
			default=fields.Date.today,
			#readonly=True,
			#required=True,
		)

	x_type = fields.Selection(
			[
				('fast', 'Fast'),
				('all', 'All'),
			],
		)


# ----------------------------------------------------------- Marketing ---------------------------

	# Marketing
	@api.model
	def update_marketing_external(self):
		"""
		Update Marketing External
		"""
		print()
		print('Scheduler - Update Marketing External')

		# Search
		configurator = self.env['openhealth.configurator.report'].search([
																			('name', 'in', ['marketing']),
																		],
																			order='date_begin,name asc',
																			limit=1,
														)
		print(configurator)
		print(configurator.name)

		if configurator.name not in [False, '']:
			date_begin = configurator.date_begin
			x_type = configurator.x_type


		# Search
		reports = self.env['openhealth.marketing'].search([
																	('date_begin', '>=', date_begin),
																	('owner', 'in', ['month']),
															],
																	order='date_begin,name asc',
																	#limit=1000,
														)
		print(reports)

		# Loop
		for repo in reports:
			print(repo.name)
			if x_type in ['fast']:
				repo.update_patients()
			elif x_type in ['all']:
				repo.update_patients()
				repo.update_sales()
				repo.update_recos()
			print()


# ----------------------------------------------------------- Management --------------------------
	# Management
	@api.model
	def update_management_external(self):
		"""
		Update Management External
		"""
		print()
		print('Scheduler - Update Management External ')



		# Search
		configurator = self.env['openhealth.configurator.report'].search([
																			('name', 'in', ['management']),
																		],
																			order='date_begin,name asc',
																			limit=1,
														)
		print(configurator)
		print(configurator.name)

		if configurator.name not in [False, '']:
			date_begin = configurator.date_begin
			x_type = configurator.x_type
			month_create = configurator.month_create
			year_create = configurator.year_create


		# Owner - Month
		owner_arr = []
		if month_create:
			owner_arr.append('month')
		if year_create:
			owner_arr.append('year')


		# Search
		reports = self.env['openhealth.management'].search([
																	('date_begin', '>=', date_begin),
																	('owner', 'in', owner_arr),
															],
																	order='owner,date_begin,name asc',
																	#limit=1000,
														)
		print(reports)

		# Loop
		for repo in reports:
			print(repo.name)
			if x_type in ['fast']:
				repo.update_fast()
			elif x_type in ['all']:
				repo.update()
			print()

		print()
		print('End')


# ----------------------------------------------------------- Update ------------------------------
	@api.multi
	def update(self):
		"""
		Update
		"""
		print()
		print('Scheduler Update')


	@api.model
	def update_external(self):
		"""
		Update External
		"""
		print()
		print('Scheduler Update External')


# ----------------------------------------------------------- Test --------------------------------
	@api.model
	def test_external(self):
		"""
		Test External
		"""
		print()
		print('Scheduler Test External')
		now = datetime.datetime.now()
		print(now)
