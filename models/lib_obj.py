# -*- coding: utf-8 -*-

# 	lib_obj.py
# 	Integration Tests for the Treatment Class
#
# Created: 			14 Aug 2018
# Last up: 	 		14 Aug 2018


class Report:

	def __init__(self, name, model, descriptor, caller): 		
		print 'Report - Init'

		self.env = caller.env 

		self.name = name
		self.model = model
		self.descriptor = descriptor

		self.db_obj = self.env[self.model].search([],
												order=self.descriptor +  ' desc',
												limit=1,
											)

	def update(self): 
		print 'Report - Update'
		self.db_obj.update()


	def __repr__(self): 
		return 'Report(*{!r})'.format(self.model)		# !r chooses repr to format the value 




#class Object(Report):
class Object():


	def __init__(self, name, model, patient_id, partner_id, doctor_id, treatment_id, caller): 		
		print 'Report - Init'

		self.env = caller.env 
		self.name = name
		self.model = model
		
		self.patient_id = patient_id
		self.partner_id = partner_id
		self.doctor_id = doctor_id
		self.treatment_id = treatment_id


		self.db_obj = self.env[self.model].test_init(patient_id, partner_id, doctor_id, treatment_id)



	def test(self): 
		print 'Object - Test'
		
		self.db_obj.test()




	def __repr__(self): 
		return 'Object(*{!r})'.format(self.model)		# !r chooses repr to format the value 









