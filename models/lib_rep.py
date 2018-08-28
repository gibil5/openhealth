# -*- coding: utf-8 -*-

# 	lib_rep.py
# 	Integration Tests for the Treatment Class
#
# 	Created: 			14 Aug 2018
# 	Last up: 	 		27 Aug 2018



class Report:

	def __init__(self, name, model, descriptor, caller): 		
		
		print 'Class Report - Init'

		self.env = caller.env 

		self.name = name
		self.model = model
		self.descriptor = descriptor

		self.db_obj = self.env[self.model].search([
														('test_target', '=', True), 

													],
												#order=self.descriptor +  ' desc',
												limit=1,
										)
		print self.db_obj
		print 


	def update(self): 
		print 
		print 'Class Report - Update'
		
		if self.db_obj.name != False: 
			self.db_obj.update()
			print 


	def __repr__(self): 
		return 'Report(*{!r})'.format(self.model)		# !r chooses repr to format the value 
