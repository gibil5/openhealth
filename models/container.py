# -*- coding: utf-8 -*-
#
# 	Container
# 
# 	Created: 				30 Sep 2018
# 	Last mod: 				 1 Oct 2018
# 
from openerp import models, fields, api
import tst_pat
import creates 
import export 
import datetime
import rsync



# ----------------------------------------------------------- Container ------------------------------------------------------
class Container(models.Model):

	_name = 'openhealth.container'



# ----------------------------------------------------------- Relational ------------------------------------------------------

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




	# Export 
	@api.multi 
	def export_txt(self):
		print
		print 'Export - Txt'
		
		# Export
		export.export_txt(self.mgt.electronic_order, self.export_date)





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


		# Correct DNIs
		for order in self.electronic_order_ids: 

			if order.id_doc in [False]: 

				if order.id_doc_type in ['dni']: 

					#order.id_doc = order.patient.x_dni
					order.patient.x_id_doc = order.patient.x_dni





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
		)


	# Management 
	mgt = fields.Many2one(
			'openhealth.management', 
		)

