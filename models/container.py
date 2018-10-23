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

#import lib_con

class Container(models.Model):

	_name = 'openhealth.container'



# ----------------------------------------------------------- Test Cases - Creates ------------------------------------------------------

	ticket_invoice_create = fields.Boolean(
			'Ticket Invoice', 
		)


	ticket_receipt_create = fields.Boolean(
			'Ticket Receipt', 
		)

	cn_invoice_create = fields.Boolean(
			'Credit Note Invoice', 
		)


	#receipt_create = fields.Boolean(
	#	)
	#invoice_create = fields.Boolean(
	#	)
	#cn_receipt_create = fields.Boolean(
	#	)





# ----------------------------------------------------------- Relational ------------------------------------------------------

	# Patient 
	patient = fields.Many2one(
			'oeh.medical.patient', 
			string="patient", 
			required=True, 
			domain = [
						('x_test', '=', 'True'),
					],
		)

	# Doctor 
	doctor = fields.Many2one(
			'oeh.medical.physician', 
			string="Doctor", 
			#domain = [
			#			('x_test', '=', 'True'),
			#		],
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
		self.mgt.update_qc('ticket_receipt')
		self.mgt.update_qc('receipt')
		self.mgt.update_qc('ticket_invoice')




#jx 
	# Create Sales 
	@api.multi 
	def create_sales(self): 
		print 
		print 'Create Sales'

		# Loop 
		for patient in self.patient_ids: 
			print patient

			# Init 
			patient_id = patient.id
			doctor_id = self.doctor.id 
			treatment_id = False
			short_name = 	'product_1'
			qty = 			40


			# Clean 
			creates.remove_orders(self, patient_id)



			# Credit Note Invoice 
			if self.cn_invoice_create:
				print 'Create Credit Note - Ticket Invoice'				
				x_type = 'ticket_invoice'

				# Create 
				order = creates.create_order_fast(self, patient_id, doctor_id, treatment_id, short_name, qty, x_type)
				
				ret = order.write({
									'state': 'cancel',
								})


			# Invoice 
			if self.ticket_invoice_create:
				print 'Create Ticket Invoice'
				
				x_type = 'ticket_invoice'

				# Create 
				order = creates.create_order_fast(self, patient_id, doctor_id, treatment_id, short_name, qty, x_type)
				print order 



			# Receipt
			if self.ticket_receipt_create:	
				print 'Create Ticket receipt'

				x_type = 'ticket_receipt'

				# Create 
				order = creates.create_order_fast(self, patient_id, doctor_id, treatment_id, short_name, qty, x_type)
				print order 



				
			print 





	# Correct 
	@api.multi 
	def test_correct(self):
		print
		print 'Correct'

		# Loop
		for electronic in self.electronic_order_ids: 

			# Correct DNI
			#if order.id_doc in [False]: 
			#	if order.id_doc_type in ['dni']: 
			#		order.patient.x_id_doc = order.patient.x_dni

			# Correct Counter
			#order.counter_value = int(order.serial_nr.split('-')[1])


			# Correct Gap 
			if electronic.delta != 1: 

				#print 'Patch the Gap !'
				#print electronic.receptor 
				#print electronic.serial_nr
				#print electronic.counter_value


				# Init 
				patient_id = 	self.patient.id				
				doctor_id = 	self.doctor.id
				short_name = 	'product_1'
				qty = 			1
				treatment_id = False
				x_type = 'receipt'


				# Create 
				order = creates.create_order_fast(self, patient_id, doctor_id, treatment_id, short_name, qty, x_type)


				# Pay 
				test_case = 'dni,receipt,product_1,1'
				order.test(test_case)

				# Update 
				counter = electronic.counter_value - 1 
				ret = order.write({
							'x_counter_value': counter,
						})
				#print ret 

				# Generate 
				order.generate_serial_nr()
				delta_hou = 0 
				delta_min = 0
				delta_sec = -30 
				order.generate_date_order(electronic.x_date_created, delta_hou, delta_min, delta_sec)

				# Update 
				state = 'cancel'
				ret = order.write({
							'state': state,
						})



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
			required=True, 
		)



# ----------------------------------------------------------- Fields ------------------------------------------------------
	# Clear 
	@api.multi 
	def clear(self): 
		#print 
		#print 'Clear'

		# Patients 
		for patient in self.patient_ids: 

			patient_id = patient.id 

			# Clean 
			creates.remove_orders(self, patient_id)

			#creates.remove_patient(self, patient.name)


		# Electronic 
		self.mgt.electronic_order.unlink()

		# Txts 
		self.txt_ids.unlink()


