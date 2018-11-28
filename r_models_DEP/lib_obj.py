# -*- coding: utf-8 -*-
"""
 	lib_obj.py
 	Integration Tests for the Treatment Class

 	Created: 			14 Aug 2018
	Last up: 	 		30 Sep 2018
"""

# ----------------------------------------------------------- Simple ------------------------------
class Simple():

	def __init__(self, name):		
		#print 'Simple - Init'
		self.name = name


	def whoami(self): 		
		#print 'Simple - Who am I'
		#print self.name 
		pass


# ----------------------------------------------------------- Object ------------------------------
class Object():

	def __init__(self, caller, name, model, patient_id=False, partner_id=False, doctor_id=False, treatment_id=False, pl_id=False):		
		#print 'Object - Init'
		# Init		
		self.env = caller.env 
		self.name = name
		self.model = model		
		self.patient_id = patient_id
		self.partner_id = partner_id
		self.doctor_id = doctor_id
		self.treatment_id = treatment_id

		# Obj
		self.db_objs = self.env[self.model].test_init(patient_id, partner_id, doctor_id, treatment_id, pl_id)


	def __repr__(self): 
		return 'Object(*{!r})'.format(self.model)		# !r chooses repr to format the value 


	def whoami(self): 		
		#print 'Object - Who am I'
		pass


	def test(self): 		
		#print 'Object - Test'
		for db_obj in self.db_objs: 
			if db_obj != False: 
				db_obj.test()


