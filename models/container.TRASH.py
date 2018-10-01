

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

