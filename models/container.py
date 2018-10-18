# -*- coding: utf-8 -*-
#
# 	Container
# 
# 	Created: 				30 Sep 2018
# 	Last mod: 				16 Oct 2018
# 
from openerp import models, fields, api
import tst_pat
import creates 
import datetime
import rsync

import export 
import importx

class Container(models.Model):

	_name = 'openhealth.container'



# ----------------------------------------------------------- Relational ------------------------------------------------------

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




# ----------------------------------------------------------- Fields ------------------------------------------------------
	def my_init(self, patient, partner, doctor, treatment):
		print 
		print 'My Init'

		self.patient = patient
		self.partner = partner
		self.doctor = doctor
		self.treatment = treatment




	@api.multi 
	def create_patients(self): 
		print 
		print 'Init Patients'

		# Init 
		pl_id = self.patient.property_product_pricelist.id


		# Create Patients 
		pat_array = tst_pat.test_cases(self, self.id, self.patient.id, self.partner.id, self.doctor.id, self.treatment.id, pl_id)
		print pat_array


		# Init 
		name = 'Export'


		# Search Mgt
		self.mgt = self.env['openhealth.management'].search([
																('name', '=', name), 
													],
														#order='write_date desc',
														limit=1,
													)
		
		# Update 
		if self.mgt.name != False: 
			self.mgt.date_begin = self.export_date_begin
			self.mgt.date_end = self.export_date_end


		# Create Mgt 
		else:
			self.mgt = self.env['openhealth.management'].create({
																'name': 		name,
																'date_begin': 	self.export_date_begin,
																'date_end': 	self.export_date_end,
													})

		print self.mgt





	@api.multi 
	def create_sales(self): 
		print 
		print 'Test Patients'

		for patient in self.patient_ids: 
			print patient
			patient.test()
			print 







	# Create Electronic 
	@api.multi 
	def create_electronic(self):
		print
		print 'Create - Electronic'
		
		# Init Dates 
		date_format = "%Y-%m-%d"
		date_dt = datetime.datetime.strptime(self.export_date_begin, date_format) + datetime.timedelta(hours=+5,minutes=0)
		self.export_date = date_dt.strftime(date_format).replace('-', '_')


		# Init Mgt 
		self.mgt.date_begin = self.export_date_begin
		self.mgt.date_end = self.export_date_end
		self.mgt.container = self.id

		self.mgt.state_arr = 'sale,cancel'


		# Update Mgt 
		self.mgt.update_fast()
		self.mgt.update_electronic()









	# Sync Txt
	@api.multi 
	def sync_txt(self):
		print
		print 'Sync - Txt'

		# Sync 
		rsync.synchronize()





	# QC 
	@api.multi 
	def test_qc(self):
		print
		print 'Test - Qc'

		# Gap Analysis 
		self.mgt.update_qc('ticket_invoice')
		self.mgt.update_qc('ticket_receipt')






	# Correct 
	@api.multi 
	def test_correct(self):
		print
		print 'Correct'

		# Loop
		for order in self.electronic_order_ids: 

			# Correct DNI
			if order.id_doc in [False]: 
				if order.id_doc_type in ['dni']: 
					order.patient.x_id_doc = order.patient.x_dni

			# Correct Counter
			order.counter_value = int(order.serial_nr.split('-')[1])





# ----------------------------------------------------------- Export Import ------------------------------------------------------
	
	# Export Txt 
	@api.multi 
	def export_txt(self):
		print
		print 'Export - Txt'
		
		# Clear
		self.txt_ids.unlink()

		# Export
		export.export_txt(self, self.mgt.electronic_order, self.export_date)




	# Import Txt
	@api.multi 
	def import_txt(self):
		print
		print 'Import TXT'

		self.txt_ref_ids.unlink()


		# Import
		importx.import_txt(self)







# ----------------------------------------------------------- Fields ------------------------------------------------------
	name = fields.Char()


	patient = fields.Many2one(
			'oeh.medical.patient', 
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



	# Export
	export_date_begin = fields.Date(
			string="Fecha Inicio", 
			default = fields.Date.today, 
			#readonly=True,
			required=True, 
		)

	export_date_end = fields.Date(
			string="Fecha Fin", 
			default = fields.Date.today, 
			#readonly=True,
			required=True, 
		)

	export_date = fields.Char(
			'Export Date', 
			readonly=True,
		)



	# Management 
	mgt = fields.Many2one(
			'openhealth.management', 
		)



# ----------------------------------------------------------- Fields ------------------------------------------------------
	# Clear 
	@api.multi 
	def clear(self): 
		print 
		print 'Clear'

		# Patients 
		for patient in self.patient_ids: 
			creates.remove_patient(self, patient.name)

		# Electronic 
		self.mgt.electronic_order.unlink()

		# Txts 
		self.txt_ids.unlink()
