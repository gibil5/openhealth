# -*- coding: utf-8 -*-
"""
 	Management Report

 	Created: 			28 May 2018
	Last updated: 		 6 Nov 2018
"""
import collections
from timeit import default_timer as timer
from openerp import models, fields, api
from . import mgt_funcs
from . import export
from . import mgt_vars

class Management(models.Model):
	"""
	high level support for doing this and that.
	"""
	_inherit = 'openhealth.repo'

	_name = 'openhealth.management'

	_order = 'date_begin asc'



# ----------------------------------------------------------- Export to Text ----------------------
	# Export TXT
	@api.multi
	def export_txt(self):
		"""
		high level support for doing this and that.
		"""
		#print
		#print 'Export Text'
		export.export_txt(self.order_line)

	# State Array
	state_arr = fields.Selection(
			selection=mgt_vars._state_arr_list,
			string='States',
			default='sale',
		)

	# Type Array
	type_arr = fields.Selection(
			selection=mgt_vars._type_arr_list,
			string='Types',
			default='ticket_receipt,ticket_invoice',
		)




# ----------------------------------------------------------- Relational --------------------------

	# Container
	container = fields.Many2one(
			'openhealth.container',
		)

	# Electronic
	electronic_order = fields.One2many(
			'openhealth.electronic.order',
			'management_id',
		)

	# Sales
	order_line = fields.One2many(
			'openhealth.management.order.line',
			'management_id',
		)

	# Doctor
	doctor_line = fields.One2many(
			'openhealth.management.doctor.line',
			'management_id',
		)

	# Family
	family_line = fields.One2many(
			'openhealth.management.family.line',
			'management_id',
		)

	# Sub_family
	sub_family_line = fields.One2many(
			'openhealth.management.sub_family.line',
			'management_id',
		)

	# Sales
	sale_line_tkr = fields.One2many(
			'openhealth.management.order.line',
			'management_tkr_id',
		)


# ----------------------------------------------------------- Legacy ------------------------------
	legacy = fields.Boolean(
			'Legacy',
		)


# ----------------------------------------------------------- Totals ------------------------------
	# Count
	total_tickets = fields.Integer(
			'Nr Tickets',
			readonly=True,
		)

	# Ratios
	ratio_pro_con = fields.Float(
			'Ratio (proc/con) %',
		)


# ----------------------------------------------------------- QC ----------------------------------
	test_target = fields.Boolean(
			string="Test Target",
		)

	delta_1 = fields.Float(
			'Delta 1',
		)

	delta_2 = fields.Float(
			'Delta 2',
		)

# ----------------------------------------------------------- Counters ----------------------------

	# Procedures
	nr_procedures = fields.Integer(
			'Nr Procedimientos',
		)

	amo_procedures = fields.Float(
			'Monto Procedimientos',
			#digits=(16,1),
		)

	avg_procedures = fields.Float(
			'Precio Prom. Procedimientos',
		)


	# Co2
	nr_co2 = fields.Integer(
			'Nr Co2',
		)

	amo_co2 = fields.Float(
			'Monto Co2',
		)

	avg_co2 = fields.Float(
			'Precio Prom. Co2',
		)


	# Exc
	nr_exc = fields.Integer(
			'Nr Exc',
		)

	amo_exc = fields.Float(
			'Monto Exc',
		)

	avg_exc = fields.Float(
			'Precio Prom. Exc',
		)


	# Ipl
	nr_ipl = fields.Integer(
			'Nr Ipl',
		)

	amo_ipl = fields.Float(
			'Monto Ipl',
		)

	avg_ipl = fields.Float(
			'Precio Prom. Ipl',
		)

	# Ndyag
	nr_ndyag = fields.Integer(
			'Nr Ndyag',
		)

	amo_ndyag = fields.Float(
			'Monto Ndyag',
		)

	avg_ndyag = fields.Float(
			'Precio Prom. Ndyag',
		)


	# Quick
	nr_quick = fields.Integer(
			'Nr Quick',
		)

	amo_quick = fields.Float(
			'Monto Quick',
		)

	avg_quick = fields.Float(
			'Precio Prom. Quick',
		)


	# Medical
	nr_medical = fields.Integer(
			'Nr TM',
		)

	amo_medical = fields.Float(
			'Monto TM',
		)

	avg_medical = fields.Float(
			'Precio Prom. TM',
		)


	# Cosmetology
	nr_cosmetology = fields.Integer(
			'Nr Cosmiatria',
		)

	amo_cosmetology = fields.Float(
			'Monto Cosmiatria',
		)

	avg_cosmetology = fields.Float(
			'Precio Prom. Cosmiatria',
		)

	# Nr Consus
	nr_consultations = fields.Integer(
			'Nr Consultas',
		)

	# Amo Consus
	amo_consultations = fields.Float(
			'Monto Consultas',
		)

	# avg Consus
	avg_consultations = fields.Float(
			'Precio Prom. Consultas',
			#digits=(16,1),
		)

	# Nr Products
	nr_products = fields.Integer(
			'Nr Productos',
		)

	# Amo Products
	amo_products = fields.Float(
			'Monto Productos',
		)

	# avg Products
	avg_products = fields.Float(
			'Precio Prom. Productos',
		)

	# Nr Services
	nr_services = fields.Integer(
			'Nr Servicios',
		)

	# Amo services
	amo_services = fields.Float(
			'Monto Servicios',
		)

	# avg services
	avg_services = fields.Float(
			'Precio Prom. Servicios',
			#digits=(16,1),
		)


# ----------------------------------------------------------- Update Stats ------------------------

	# Update Stats - Doctors, Families, Sub-families
	def update_stats(self):
		"""
		high level support for doing this and that.
		"""
		#print
		#print 'Update Stats'


		# Using collections - More Abstract !

		# Clean
		self.family_line.unlink()
		self.sub_family_line.unlink()


		# Init
		doctor_arr = []
		family_arr = []
		sub_family_arr = []
		_h_amount = {}
		_h_sub = {}



	# All
		# Loop - Doctors
		for doctor in self.doctor_line:

			# Loop - Order Lines
			for line in doctor.order_line:

				# Family
				family_arr.append(line.family)

				# Sub family
				sub_family_arr.append(line.sub_family)

				# Amount - Family
				if line.family in _h_amount:
					_h_amount[line.family] = _h_amount[line.family] + line.price_total

				else:
					_h_amount[line.family] = line.price_total

				# Amount - Sub Family
				if line.sub_family in _h_sub:
					_h_sub[line.sub_family] = _h_sub[line.sub_family] + line.price_total

				else:
					_h_sub[line.sub_family] = line.price_total

			# Doctor Stats
			doctor.stats()


	# By Family

		# Count
		counter_family = collections.Counter(family_arr)

		# Create
		for key in counter_family:
			count = counter_family[key]
			amount = _h_amount[key]
			family = self.family_line.create({
													'name': key,
													'x_count': count,
													'amount': amount,
													'management_id': self.id,
												})
			family.update()



	# Subfamily

		# Count
		counter_sub_family = collections.Counter(sub_family_arr)

		# Create
		for key in counter_sub_family:
			count = counter_sub_family[key]
			amount = _h_sub[key]
			sub_family = self.sub_family_line.create({
														'name': key,
														'x_count': count,
														'amount': amount,
														'management_id': self.id,
												})
			sub_family.update()

	# update_stats



# ----------------------------------------------------------- Update Sales - By Doctor ------------

	# Update Sales
	def update_sales_by_doctor(self):
		"""
		high level support for doing this and that.
		"""
		#print
		#print 'Update Sales - By Doctor'


		# Clean
		self.doctor_line.unlink()


		# Init vars
		total_amount = 0
		total_count = 0
		total_tickets = 0


		# Create Doctors
		doctors = [
					'Dr. Chavarri',
					'Dr. Canales',
					'Dr. Gonzales',
					'Dr. Monteverde',
					'Eulalia',
					'Dr. Abriojo',
					'Dr. Castillo',
					'Dr. Loaiza',
					'Dr. Escudero',
					'Clinica Chavarri',
				]

		# Loop
		for doctor in doctors:
			doctor = self.doctor_line.create({
												'name': doctor,
												'management_id': self.id,
										})




		# Create Sales - By Doctor
		for doctor in self.doctor_line:

			#print doctor.name


			# Clear
			#self.order_line.unlink()
			doctor.order_line.unlink()



			# Orders
			orders, count = mgt_funcs.get_orders_filter_by_doctor\
															(self, self.date_begin, self.date_end, doctor.name)


			#self.total_count = count


			# Init Loop
			amount = 0
			count = 0
			tickets = 0

			# Loop
			for order in orders:

				# Tickets
				tickets = tickets + 1

				# Amount
				amount = amount + order.amount_total

				# Id Doc
				if order.x_type in ['ticket_invoice', 'invoice']:
					receptor = order.patient.x_firm.upper()
					id_doc = order.patient.x_ruc
					id_doc_type = 'ruc'
					id_doc_type_code = '6'

				else:
					receptor = order.patient.name
					id_doc = order.patient.x_id_doc
					id_doc_type = order.patient.x_id_doc_type
					id_doc_type_code = order.patient.x_id_doc_type_code



				# Order Lines
				for line in order.order_line:

					count = count + 1


					# Here !!!
					order_line = doctor.order_line.create({
															'receptor': 	receptor,
															'patient': 		order.patient.id,

															'name': order.name,
															'x_date_created': order.date_order,
															'doctor': order.x_doctor.id,
															'state': order.state,
															'serial_nr': order.x_serial_nr,


															# Type of Sale
															'type_code': 	order.x_type_code,
															'x_type': 		order.x_type,


															# Id Doc
															'id_doc': 				id_doc,
															'id_doc_type': 			id_doc_type,
															'id_doc_type_code': 	id_doc_type_code,


															# Line
															'product_id': 			line.product_id.id,
															'product_uom_qty': 		line.product_uom_qty,
															'price_unit': 			line.price_unit,


															'doctor_id': doctor.id,
															'management_id': self.id,
														})
					ret = order_line.update_fields()



			# Stats
			doctor.amount = amount
			doctor.x_count = count


			# Dr Stats
			#doctor.stats()


			# Totals
			total_amount = total_amount + amount
			total_count = total_count + count
			total_tickets = total_tickets + tickets



		# Totals
		#self.total_amount = total_amount
		#self.total_count = total_count
		#self.total_tickets = total_tickets

		#self.stats()

		#print 'Done !'
	# update_sales





# ----------------------------------------------------------- Update Doctors ----------------------
	# Update
	@api.multi
	def update_doctors(self):
		"""
		high level support for doing this and that.
		"""
		#print
		#print 'Management - Update Doctors'
		t0 = timer()
		self.update_sales_by_doctor()
		self.update_stats()
		#self.update_counters()
		#self.update_qc()
		t1 = timer()
		self.delta_2 = t1 - t0
		#print self.delta_2
		#print
	# update_doctors











# ----------------------------------------------------------- Electronic - Clear ------------------
	# Clear
	@api.multi
	def clear_electronic(self):
		"""
		high level support for doing this and that.
		"""
		#print
		#print 'Electronic - Clear'
		# Clean
		self.electronic_order.unlink()






# ----------------------------------------------------------- Update Sales - Electronic -----------

	# Update Electronic
	@api.multi
	def update_electronic(self):
		"""
		high level support for doing this and that.
		"""
		#print
		#print 'Update - Electronic'

		# Clean
		self.electronic_order.unlink()

		# Orders
		orders, count = mgt_funcs.get_orders_filter(self, self.date_begin, self.date_end, self.state_arr, self.type_arr)
		#print orders
		#print count


		amount_total = 0
		receipt_count = 0
		invoice_count = 0

		# Loop
		for order in orders:
			#print order
			#print order.x_type

			# Generate Id Doc
			if order.x_type in ['ticket_invoice', 'invoice']:
				receptor = order.patient.x_firm.upper()
				id_doc = order.patient.x_ruc
				id_doc_type = 'ruc'
				id_doc_type_code = '6'
			else:
				receptor = order.patient.name
				id_doc = order.patient.x_id_doc
				id_doc_type = order.patient.x_id_doc_type
				id_doc_type_code = order.patient.x_id_doc_type_code

			# Patch
			if order.patient.x_id_doc == False and order.patient.x_id_doc_type == False:
				if order.patient.x_dni != False:
					id_doc = order.patient.x_dni
					id_doc_type = 'dni'
					id_doc_type_code = 1

			#print receptor
			#print id_doc
			#print id_doc_type
			#print id_doc_type_code



			# Create Electronic Order
			electronic_order = self.electronic_order.create({
																'receptor': 	receptor,
																'patient': 		order.patient.id,

																'name': 			order.name,
																'x_date_created': 	order.date_order,
																'doctor': 			order.x_doctor.id,
																'state': 			order.state,
																'serial_nr': 		order.x_serial_nr,

																# Type of Sale
																'type_code': 		order.x_type_code,
																'x_type': 			order.x_type,

																# Id Doc
																'id_doc': 				id_doc,
																'id_doc_type': 			id_doc_type,
																'id_doc_type_code': 	id_doc_type_code,

																# Line
																#'product_id': 			line.product_id.id,
																#'product_uom_qty': 		line.product_uom_qty,
																#'price_unit': 			line.price_unit,


																# Totals
																'amount_total': 		order.amount_total,
																'amount_total_net': 	order.x_total_net,
																'amount_total_tax': 	order.x_total_tax,


																# QC
																'counter_value': 		order.x_counter_value,
																'delta': 				order.x_delta,


																# Rel
																'management_id': self.id,
																'container_id': self.container.id,


																# Credit Note
																'credit_note_owner': 	order.x_credit_note_owner.id,
			})


			# Create Lines
			for line in order.order_line:
				#print line
				#print line.product_id.name
				#print line.product_uom_qty
				#print line.price_unit
				#print electronic_order
				#print

				electronic_line = electronic_order.electronic_line_ids.create({
																					# Line
																					'product_id': 			line.product_id.id,
																					'product_uom_qty': 		line.product_uom_qty,
																					'price_unit': 			line.price_unit,

																					# Rel
																					'electronic_order_id': electronic_order.id,
				})


			# Update Amount Total
			if order.state in ['sale', 'cancel']:
				amount_total = amount_total + order.amount_total

				if order.x_type in ['ticket_receipt']:
					receipt_count = receipt_count + 1

				elif order.x_type in ['ticket_invoice']:
					invoice_count = invoice_count + 1



		return amount_total, receipt_count, invoice_count

	# update_electronic





# ----------------------------------------------------------- Update Sales - Fast -----------------
	# Update Sales - Fast
	def update_sales_fast(self):
		"""
		high level support for doing this and that.
		"""
		#print
		#print 'Update Sales'


		# Clean
		self.reset_macro()


		# Orders
		orders, count = mgt_funcs.get_orders_filter\
											(self, self.date_begin, self.date_end, self.state_arr, self.type_arr)
		#print orders
		#print count


		# Init Loop
		tickets = 0
		first = True

		# Loop
		for order in orders:
			tickets = tickets + 1

			# Order Lines
			for line in order.order_line:
				if first:
					verbosity = True
					first = False
				else:
					verbosity = False

				# Line Analysis
				#stats = mgt_funcs.line_analysis(self, line, verbosity)
				stats = mgt_funcs.line_analysis(self, line)




		# Ratios
		if self.nr_consultations != 0:
			self.ratio_pro_con = (float(self.nr_procedures) / float(self.nr_consultations)) * 100

		# Families
		if self.nr_products != 0:
			self.avg_products = self.amo_products / self.nr_products

		if self.nr_services != 0:
			self.avg_services = self.amo_services / self.nr_services

		if self.nr_consultations != 0:
			self.avg_consultations = self.amo_consultations / self.nr_consultations

		if self.nr_procedures != 0:
			self.avg_procedures = self.amo_procedures / self.nr_procedures

		# Subfamilies
		if self.nr_co2 != 0:
			self.avg_co2 = self.amo_co2 / self.nr_co2

		if self.nr_exc != 0:
			self.avg_exc = self.amo_exc / self.nr_exc

		if self.nr_ipl != 0:
			self.avg_ipl = self.amo_ipl / self.nr_ipl

		if self.nr_ndyag != 0:
			self.avg_ndyag = self.amo_ndyag / self.nr_ndyag

		if self.nr_quick != 0:
			self.avg_quick = self.amo_quick / self.nr_quick

		if self.nr_medical != 0:
			self.avg_medical = self.amo_medical / self.nr_medical

		if self.nr_cosmetology != 0:
			self.avg_cosmetology = self.amo_cosmetology / self.nr_cosmetology


		# Totals
		self.total_amount = self.amo_products + self.amo_services
		self.total_count = self.nr_products + self.nr_services
		self.total_tickets = tickets

	# update_sales_fast






# ----------------------------------------------------------- Update - Fast -----------------------
	# Update
	@api.multi
	def update_fast(self):
		"""
		high level support for doing this and that.
		"""
		#print
		#print 'Management - Update Fast'
		t0 = timer()
		self.update_sales_fast()
		t1 = timer()
		self.delta_1 = t1 - t0
		#print self.delta_1
		#print
	# update




# ----------------------------------------------------------- Reset -------------------------------
	# Reset
	@api.multi
	def reset(self):
		"""
		high level support for doing this and that.
		"""
		#print
		#print 'Reset'
		self.reset_macro()
		self.reset_micro()
	# reset


	# Reset Macros
	def reset_macro(self):
		"""
		high level support for doing this and that.
		"""
		#print
		#print 'Reset Macros'

		# Clear
		self.total_amount = 0
		self.total_count = 0
		self.total_tickets = 0

		self.nr_products = 0
		self.nr_services = 0
		self.nr_consultations = 0
		self.nr_procedures = 0

		self.amo_products = 0
		self.amo_services = 0
		self.amo_consultations = 0
		self.amo_procedures = 0

		self.avg_products = 0
		self.avg_services = 0
		self.avg_consultations = 0
		self.avg_procedures = 0

		self.nr_co2 = 0
		self.nr_exc = 0
		self.nr_ipl = 0
		self.nr_ndyag = 0
		self.nr_quick = 0
		self.nr_medical = 0
		self.nr_cosmetology = 0

		self.amo_co2 = 0
		self.amo_exc = 0
		self.amo_ipl = 0
		self.amo_ndyag = 0
		self.amo_quick = 0
		self.amo_medical = 0
		self.amo_cosmetology = 0

		self.avg_co2 = 0
		self.avg_exc = 0
		self.avg_ipl = 0
		self.avg_ndyag = 0
		self.avg_quick = 0
		self.avg_medical = 0
		self.avg_cosmetology = 0
	# reset_macro


	# Reset Micro (Doctors, Families, Sub-families)
	def reset_micro(self):
		"""
		high level support for doing this and that.
		"""
		#print
		#print 'Reset Doctors'
		self.order_line.unlink()
		self.doctor_line.unlink()
		self.family_line.unlink()
		self.sub_family_line.unlink()
	# reset_micro



# ----------------------------------------------------------- Update All --------------------------
	# Update
	@api.multi
	def update(self):
		"""
		high level support for doing this and that.
		"""
		#print
		#print 'Management - Update'
		self.reset()
		self.update_fast()
		self.update_doctors()
	# update



# ----------------------------------------------------------- Update - QC -------------------------
	# Update QC
	@api.multi
	def update_qc(self, x_type):
		"""
		high level support for doing this and that.
		"""
		#print
		#print 'Management - Update QC'

		# Init
		serial_nr_last = 0

		# Orders
		orders, count = mgt_funcs.get_orders_filter_type(self, self.date_begin, self.date_end, x_type)

		# Loop
		for order in orders:

			# Gap
			serial_nr = int(order.x_serial_nr.split('-')[1])
			if serial_nr_last != 0:
				delta = serial_nr - serial_nr_last
			else:									# First one
				delta = 1
			serial_nr_last = serial_nr
			# Update Delta
			order.x_delta = delta
			# Update Counter Value
			#order.x_counter_value = int(order.x_serial_nr.split('-')[1])


			# Checksum
			order.checksum()

	# update_qc



	# Update QC All
	@api.multi
	def update_qc_all(self, x_type):
		"""
		high level support for doing this and that.
		"""
		#print
		#print 'Update QC All'

		# Gap and Checksum
		self.update_qc('ticket_receipt')
		self.update_qc('ticket_invoice')

