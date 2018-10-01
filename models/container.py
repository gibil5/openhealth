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

# ----------------------------------------------------------- Container ------------------------------------------------------
class Container(models.Model):

	_name = 'openhealth.container'


	def my_init(self, patient, partner, doctor, treatment):
		print 
		print 'My Init'

		self.patient = patient
		self.partner = partner
		self.doctor = doctor
		self.treatment = treatment



	@api.multi 
	def init_patients(self): 
		print 
		print 'Init Patients'


		pl_id = self.patient.property_product_pricelist.id

		pat_array = tst_pat.test_init(self, self.id, self.patient.id, self.partner.id, self.doctor.id, self.treatment.id, pl_id)

		print pat_array



	@api.multi 
	def test_patients(self): 
		print 
		print 'Test Patients'

		for patient in self.patient_ids: 

			print patient
			patient.test()
			print 



	@api.multi 
	def remove_patients(self): 
		print 
		print 'Remove Patients'

		for patient in self.patient_ids: 

			creates.remove_patient(self, patient.name)



	# Export 
	@api.multi 
	def test_export(self):
		print
		print 'Test - Export'
		
		
		# Search and Clear 
		mgt = self.env['openhealth.management'].search([
															#('name','=', 'Hoy'),
															('name','=', 'Export'),
													],
													#order='appointment_date desc',
													limit=1,)
		mgt.unlink()



		# Init 
		name = 'Export'

		#date_format = "%Y-%m-%d %H:%M:%S"
		date_format = "%Y-%m-%d"
		#date_dt = datetime.datetime.strptime(self.export_date_begin, date_format)
		date_dt = datetime.datetime.strptime(self.export_date_begin, date_format) + datetime.timedelta(hours=+5,minutes=0)

		self.export_date = date_dt.strftime(date_format).replace('-', '_')




		# Create 
		mgt = self.env['openhealth.management'].create({
															'name': 		name,
															'date_begin': 	self.export_date_begin,
															'date_end': 	self.export_date_end,
												})
		print mgt


		# Update
		mgt.update_fast()
		mgt.update_electronic()



		# Export
		export.export_txt(mgt.electronic_order, self.export_date)

		# Sync 




# ----------------------------------------------------------- Fields ------------------------------------------------------
	name = fields.Char()


	patient_ids = fields.One2many(
			'oeh.medical.patient', 
			'container_id', 
		)


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

