# -*- coding: utf-8 -*-
"""
	Container

	Created: 				30 Sep 2018
	Last mod: 				 4 Nov 2018
"""
import base64
import io
import datetime
from openerp import models, fields, api
import tst_pat
import creates
import export


class Container(models.Model):
	"""
	high level support for doing this and that.
	"""
	_name = 'openhealth.container'




# ----------------------------------------------------------- TXT ----------------------------

	txt_pack = fields.Binary(
			'Paquete TXT',
		)

	txt_pack_name = fields.Char(
			'Paquete TXT - Name',
		)



# ----------------------------------------------------------- Export ------------------------------

	# Export Txt
	@api.multi
	def export_txt(self):
		"""
		high level support for doing this and that.
		"""
		print
		print 'Export - Txt'


		# Clean
		self.txt_ids.unlink()



		# Export
		fname = export.export_txt(self, self.mgt.electronic_order, self.export_date)


		fname_txt = fname.split('/')[-1]
		print fname_txt


		#self.txt_pack_name = fname


		# Read Binary
		#f = io.open(fname, mode="rb", encoding="utf-8")
		f = io.open(fname, mode="rb")
		out = f.read()
		f.close()


		#print out
		print fname
		print fname_txt



		self.write({
					'txt_pack': base64.b64encode(out),
					'txt_pack_name': fname_txt,
				})

	# export_txt





# ----------------------------------------------------------- Patients ----------------------------
	# Create Patients
	@api.multi
	def create_patients(self):
		"""
		high level support for doing this and that.
		"""
		print
		print 'Init Patients'


		# Init
		#pl_id = self.patient.property_product_pricelist.id
		#pl_id = False
		container_id = self.id
		doctor_id = self.doctor.id


		# Create Patients
		pat_array = tst_pat.test_cases(self, container_id, doctor_id)

		print pat_array



		# Init
		name = 'Export'

		# Search Mgt
		#self.mgt = self.env['openhealth.management'].search([
		#														('name', '=', name),
		#											],
														#order='write_date desc',
		#												limit=1,
		#											)



		# Update
		if self.mgt.name != False:
			self.mgt.date_begin = self.export_date_begin

			#self.mgt.date_end = self.export_date_end
			self.mgt.date_end = self.export_date_begin


		# Create Mgt
		else:
			self.mgt = self.env['openhealth.management'].create({
																'name': 		name,
																'date_begin': 	self.export_date_begin,

																#'date_end': 	self.export_date_end,
																'date_end': 	self.export_date_begin,
													})

		print self.mgt

	# create_patients






# ----------------------------------------------------------- Create Sales -------------------------------

	# Create Sales
	@api.multi
	def create_sales(self):
		"""
		high level support for doing this and that.
		"""
		print
		print 'Create Sales'


		# Search
		patients = self.env['oeh.medical.patient'].search([
																('x_test', '=', True),
															],
															#order='appointment_date desc',
															#limit=1,
														)


		# Loop
		for patient in patients:

			# Init
			patient_id = patient.id
			partner_id = patient.partner_id.id
			doctor_id = self.doctor.id
			treatment_id = False
			short_name = 'product_1'
			qty = 40
			pricelist_id = patient.property_product_pricelist.id



			# Invoice
			if self.ticket_invoice_create:

				x_type = 'ticket_invoice'

				# Create
				invoice = creates.create_order_fast(self, patient_id, partner_id, doctor_id, treatment_id,\
																							 short_name, qty, x_type, pricelist_id)


			# Receipt
			if self.ticket_receipt_create:

				x_type = 'ticket_receipt'

				# Create
				receipt = creates.create_order_fast(self, patient_id, partner_id, doctor_id, treatment_id,\
																							 short_name, qty, x_type, pricelist_id)




			# Invoice Cancel
			if self.ticket_invoice_cancel:
				#print
				invoice.cancel_order()



			# Receipt Cancel
			if self.ticket_receipt_cancel:
				#print
				receipt.cancel_order()




		# QC
		#self.test_qc()

	# create_sales




# ----------------------------------------------------------- Electronic --------------------------
	# Create Electronic
	@api.multi
	def create_electronic(self):
		"""
		high level support for doing this and that.
		"""
		print
		print 'Create - Electronic'


		# Clean
		self.electronic_order_ids.unlink()


		# Init Dates
		date_format = "%Y-%m-%d"

		date_dt = datetime.datetime.strptime(self.export_date_begin, date_format) + \
																					datetime.timedelta(hours=+5, minutes=0)

		self.export_date = date_dt.strftime(date_format).replace('-', '_')



		# Init Mgt
		self.mgt.date_begin = self.export_date_begin
		#self.mgt.date_end = self.export_date_end
		self.mgt.date_end = self.export_date_begin




		self.mgt.container = self.id
		self.mgt.state_arr = 'sale,cancel,credit_note'


		# Update Mgt
		self.mgt.update_fast()


		#self.amount_total = self.mgt.update_electronic()
		self.amount_total, self.receipt_count, self.invoice_count = self.mgt.update_electronic()


	# create_electronic






# ----------------------------------------------------------- Relational --------------------------
	# Patient
	#patient = fields.Many2one(
	#		'oeh.medical.patient',
	#		string="patient",
	#		required=True,
	#		domain=[
	#					('x_test', '=', 'True'),
	#				],
	#	)

	#patient = fields.Many2one(
	#		'oeh.medical.patient',
	#	)

	# Doctor
	doctor = fields.Many2one(
			'oeh.medical.physician',
			string="Doctor",
		)

	# Txt
	txt_ids = fields.One2many(
			'openhealth.texto',
			'container_id',
		)

	# Txt - Ref
	txt_ref_ids = fields.One2many(
			'openhealth.texto',
			'container_ref_id',
		)

	# Patients
	patient_ids = fields.One2many(
			'oeh.medical.patient',
			'container_id',
		)

	# Electronic Order
	electronic_order_ids = fields.One2many(
			'openhealth.electronic.order',
			'container_id',
		)




# ----------------------------------------------------------- Fields ------------------------------

	# Flags
	ticket_invoice_create = fields.Boolean(
			'Invoice',
		)

	ticket_receipt_create = fields.Boolean(
			'Receipt',
		)

	ticket_invoice_cancel = fields.Boolean(
			'Invoice Cancel',
		)

	ticket_receipt_cancel = fields.Boolean(
			'Receipt Cancel',
		)





	# Total
	amount_total = fields.Float(
			'Total',
			digits=(16, 2),
		)

	# Receipt count
	receipt_count = fields.Integer(
			'Recibos Nr',
		)

	# Invoice count
	invoice_count = fields.Integer(
			'Facturas Nr',
		)






	# Name
	name = fields.Char(
			'Nombre',
		)


	partner = fields.Many2one(
			'res.partner',
		)

	doctor = fields.Many2one(
			'oeh.medical.physician',
		)

	treatment = fields.Many2one(
			'openhealth.treatment',
		)

	# Management
	mgt = fields.Many2one(
			'openhealth.management',
			required=True,
		)



	# Dates
	export_date_begin = fields.Date(
			string="Fecha Inicio",
			default=fields.Date.today,
			required=True,
		)


	#export_date_end = fields.Date(
	#		string="Fecha Fin",
	#		default=fields.Date.today,
	#		required=True,
	#	)


	export_date = fields.Char(
			'Export Date',
			readonly=True,
		)





# ----------------------------------------------------------- Actions -----------------------------

	# QC
	@api.multi
	def test_qc(self):
		"""
		high level support for doing this and that.
		"""
		print
		print 'Test - Qc'

		# Gap Analysis
		self.mgt.update_qc('ticket_receipt')
		self.mgt.update_qc('receipt')
		self.mgt.update_qc('ticket_invoice')

	# test_qc



	# Clear
	@api.multi
	def clear(self):
		"""
		high level support for doing this and that.
		"""

		# Loop
		for patient in self.patient_ids:
			patient_id = patient.id
			if patient.x_test:
				creates.remove_orders(self, patient_id)

		# Electronic
		self.mgt.electronic_order.unlink()

		# Txt
		self.txt_ids.unlink()

		# Stats
		self.amount_total = 0
		self.invoice_count = 0
		self.receipt_count = 0

	# clear



