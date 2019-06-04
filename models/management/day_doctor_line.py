# -*- coding: utf-8 -*-
"""
	Day Doctor Line

	Created: 			25 Jan 2019
	Last up: 			25 Jan 2019
"""
from __future__ import print_function

import datetime
from openerp import models, fields, api
from openerp.addons.openhealth.models.order import ord_vars

class DayDoctorLine(models.Model):
	"""
	high level support for doing this and that.
	"""

	_name = 'openhealth.management.day.doctor.line'

	_inherit = 'openhealth.management.day.line'

	_order = 'date asc'



# ----------------------------------------------------------- Relational --------------------------
	# Sales
	order_line = fields.One2many(
			
			'openhealth.management.order.line',

			'doctor_day_id',
		)



# ----------------------------------------------------------- Primitive ---------------------------

	amount = fields.Float(
			'Monto Total',
		)

	nr_consultations = fields.Integer(
			'Nr Consultas',
		)

	nr_procedures = fields.Integer(
			'Nr Procs',
		)

	ratio_pro_con = fields.Float(
			'Ratio (proc/con) %',
		)


# ----------------------------------------------------------- reset ------------------------------
	@api.multi
	def reset_macro(self):
		"""
		high level support for doing this and that.
		"""
		print()
		print('Reset - Macro')

		self.amount = 0
		self.nr_consultations = 0
		self.nr_procedures = 0
		self.ratio_pro_con = 0

# ----------------------------------------------------------- Update ------------------------------
	def update(self):
		"""
		high level support for doing this and that.
		"""
		print()
		print('Doctor Day Line - Update')
		print(self.date)
		print()

		#date_format_1 = "%Y-%m-%d %H:%M:%S"
		date_format_1 = "%Y-%m-%d"
		date_dt = datetime.datetime.strptime(self.date, date_format_1) + datetime.timedelta(hours=0, minutes=0)
		print(date_dt)

		weekday = date_dt.weekday()

		self.weekday = ord_vars._dic_weekday[weekday]

		# Duration
		if weekday in [5]:
			self.duration = 0.5
		else:
			self.duration = 1





# ----------------------------------------------------------- Update ------------------------------
	def update_line(self, line):
		"""
		high level support for doing this and that.
		"""
		print()
		print('Doctor Day Line - Update')

		print(self.date)
		print(line)


		line = self.order_line.create({
										'date_order_date': 	line.date_order_date,
										'x_date_created': 	line.x_date_created,

										'name': 			line.name,
										'receptor': 		line.receptor,
										'patient': 			line.patient.id,
										'doctor': 			line.doctor.id,
										'serial_nr': 		line.serial_nr,

										# Type of Sale
										'type_code': 		line.type_code,
										'x_type': 			line.x_type,

										# Line
										'product_id': 		line.product_id.id,
										'product_uom_qty': 	line.product_uom_qty,
										'price_unit': 		line.price_unit,

										# State
										'state': 			line.state,


										# Id Doc
										#'id_doc': 				id_doc,
										#'id_doc_type': 			id_doc_type,
										#'id_doc_type_code': 	id_doc_type_code,


										# Handles
										#'doctor_id': doctor.id,
										#'management_id': self.id,
										'doctor_day_id': self.id,
									})
		line.update_fields()






# ----------------------------------------------------------- Update ------------------------------
	@api.multi
	def update_macro(self):
		"""
		high level support for doing this and that.
		"""
		print()
		print('Update - Macro')

		# Clean		
		self.reset_macro()

		for line in self.order_line:
			self.amount = self.amount + line.price_total

			if line.product_id.x_family in ['consultation']:
				self.nr_consultations = self.nr_consultations + line.product_uom_qty

			if line.product_id.x_family in ['laser', 'medical', 'cosmetology']:
				self.nr_procedures = self.nr_procedures + line.product_uom_qty


		if self.nr_consultations != 0:
			print('Gotcha !')
			self.ratio_pro_con = float(self.nr_procedures) / float(self.nr_consultations)

	# update_macro
