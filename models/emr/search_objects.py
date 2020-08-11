# -*- coding: utf-8 -*-
"""
	search_objects

	Created: 			24 Jul 2020
	Last up: 	 		24 Jul 2020
"""

class SearchObjects(object):
	"""
	Used by Treatment
	"""
	def __init__(self, env, name, value):
		#print('init')
		self.env = env
		self.name = name 
		self.value = value 
		self.obj = self.env.search([
									(name, '=', value),
							],
							limit=1,)

	def get_name(self):
		return self.obj.name