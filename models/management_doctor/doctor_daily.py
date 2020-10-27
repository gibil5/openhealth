# -*- coding: utf-8 -*-
"""
	Doctor Daily - Too complex - Refactor !

	Inherits - doctor_line

	Created: 			 8 Dec 2019
	Last up: 			 8 Dec 2019
"""
import datetime
from openerp import models, fields, api

from openerp.addons.openhealth.models.order import ord_vars

class DoctorDaily(models.Model):
	"""
	DoctorDaily
		DoctorLine
			ManagementLine
	"""
	_inherit = 'openhealth.management.doctor.line'
	_name = 'doctor.daily'

# ----------------------------------------------------------- Relationals -------
	management_id = fields.Many2one(
			'openhealth.management',
			#ondelete='cascade',
			required=True,
		)

	doctor_id = fields.Many2one(
			'openhealth.management.doctor.line',
			ondelete='cascade',  	# When the doctor_line is deleted, the doctor_daily is also deleted
			required=True,
		)

	# Sales
	order_line = fields.One2many(
			'openhealth.management.order.line',
			#'doctor_daily_id',
			'doctor_id',
		)

# ----------------------------------------------------------- Required ---------
	date = fields.Date(
			'Fecha',
			required=True,
		)

# ----------------------------------------------------------- Optional ---------
	weekday = fields.Selection(
			selection=ord_vars._weekday_list,
			string='Dia de semana',
		)

	duration = fields.Float(
			'Duracion',
		)

# ----------------------------------------------------------- Update -----------
	# Update 
	def update(self):
		"""
		Update
		Weekday and duration
		"""
		print()
		print('Y - Doctor Daily - Update')

		print(self.date)
		print()

		#date_format_1 = "%Y-%m-%d %H:%M:%S"
		date_format_1 = "%Y-%m-%d"

		date_dt = datetime.datetime.strptime(self.date, date_format_1) + datetime.timedelta(hours=0, minutes=0)
		#print(date_dt)

		# Weekday
		weekday = date_dt.weekday()
		self.weekday = ord_vars._dic_weekday[weekday]

		# Duration
		if weekday in [5]:
			self.duration = 0.5
		else:
			self.duration = 1


# ----------------------------------------------------------- Update Line ------------------------------
	# Update 
	def update_line(self, line):
		"""
		Update Line
		"""
		print()
		print('Y - Doctor Daily - Update Line')

		print(self.date)
		print(line)

		# Create order_line for a doctor
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


										# Handles
										#'doctor_day_id': self.id,
										'doctor_daily_id': self.id,

									})


		#line.update_fields()  # Dep !


										# Id Doc
										#'id_doc': 				id_doc,
										#'id_doc_type': 			id_doc_type,
										#'id_doc_type_code': 	id_doc_type_code,
										#'doctor_id': doctor.id,
										#'management_id': self.id,

# ----------------------------------------------------------- 2019 ------------------------------
	# Update 
	def pl_update_macro(self):
		"""
		Update
		"""
		print()
		print('X - Doctor Daily  - Pl Update Macro')

# ----------------------------------------------------------- 2018 ------------------------------
	# Update 
	#def update_macro(self):
	#	"""
	#	Update
	#	"""
	#	print()
	#	print('X - Doctor Daily - Update Macro')

