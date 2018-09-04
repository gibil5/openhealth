# -*- coding: utf-8 -*-

# 	lib_obj.py
# 	Integration Tests for the Treatment Class
#
# 	Created: 			14 Aug 2018
# 	Last up: 	 		14 Aug 2018



class Object():



	#def __init__(self, caller, name, model, 	patient_id=False, partner_id=False, doctor_id=False, treatment_id=False):
	def __init__(self, caller, name, model, 	patient_id=False, partner_id=False, doctor_id=False, treatment_id=False, pl_id=False):
		
		print 'Object - Init'
		#print caller
		
		self.env = caller.env 
		self.name = name
		self.model = model
		
		self.patient_id = patient_id
		self.partner_id = partner_id
		self.doctor_id = doctor_id
		self.treatment_id = treatment_id

		# Obj
		#self.db_objs = self.env[self.model].test_init(patient_id, partner_id, doctor_id, treatment_id)
		self.db_objs = self.env[self.model].test_init(patient_id, partner_id, doctor_id, treatment_id, pl_id)



	def __repr__(self): 
		return 'Object(*{!r})'.format(self.model)		# !r chooses repr to format the value 



	def test(self): 
		
		print 'Object - Test'
		
		#self.db_obj.test()
		for db_obj in self.db_objs: 
			db_obj.test()






