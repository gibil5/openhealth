

import lib_obj




# ----------------------------------------------------------- Simple ------------------------------------------------------
class Simple():

	def __init__(self, name):		
		print 'Simple 2 - Init'
		self.name = name


	def whoami(self): 		
		print 'Simple 2 - Who am I'
		print self.name 



# ----------------------------------------------------------- Object ------------------------------------------------------
class Object():

	def __init__(self, name):		
		print 'Object - Init'
		self.name = name

	def test(self): 		
		print 'Object - Test'

	def whoami(self): 		
		print 'Object - Who am I'
		print self.name 

	obj = fields.Many2one(
			Object, 
		)

	simple = fields.Many2one(
			#lib_obj.Simple, 
			Simple, 
		)





# ----------------------------------------------------------- Test - Init ------------------------------------------------------
	# Test - Init  
	@api.multi 
	def test_init(self, container_id, patient_id=False, partner_id=False, doctor_id=False, treatment_id=False, pl_id=False):
		print 
		print 'Container - Test Init'
		print self 

		print patient_id
		print partner_id
		print doctor_id
		print treatment_id
		print pl_id

		pat_array = tst_pat.test_init(self, container_id, patient_id, partner_id, doctor_id, treatment_id, pl_id)

		return pat_array





# 8 Oct 2018 



	# Export 
	@api.multi 
	def test_export(self):
		print
		print 'Test - Export'



		# Search and Clear 
		#mgt = self.env['openhealth.management'].search([
															#('name','=', 'Hoy'),
		#													('name','=', 'Export'),
		#											],
													#order='appointment_date desc',
		#											limit=1,)
		#mgt.unlink()


		# Clear 
		#self.mgt.unlink()



# 20 oct 2018 
				# Patch 
				patient = self.owner
				receptor = patient.name 
				serial_nr = lib_con.get_serial_nr(order.serial_nr, -1)
				id_doc = '09817194'
				id_doc_type = 'dni'
				id_doc_type_code = 1
				counter_value = order.counter_value - 1

				# Create 
				electronic = self.electronic_order_ids.create({

																'receptor': 	receptor, 
																'patient': 		patient.id, 

																#'name': 			order.name, 
																'x_date_created': 	order.x_date_created, 
																#'doctor': 			order.x_doctor.id, 
																'state': 			'cancel', 
																'serial_nr': 		serial_nr, 

																# Type of Sale 
																'type_code': 		order.type_code, 
																'x_type': 			order.x_type, 

																# Id Doc  
																'id_doc': 				id_doc, 
																'id_doc_type': 			id_doc_type, 
																'id_doc_type_code': 	id_doc_type_code, 


																# Totals
																'amount_total': 		0, 
																'amount_total_net': 	0, 
																'amount_total_tax': 	0, 

																# QC 
																'counter_value': 		counter_value, 
																#'delta': 				order.x_delta, 


																# Rel 
																'management_id': self.mgt.id, 
																'container_id': self.id, 

					})


