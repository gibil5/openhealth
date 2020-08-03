# -*- coding: utf-8 -*-
"""
	counter_objects

	Created: 			24 Jul 2020
	Last up: 	 		24 Jul 2020
"""

class CounterObjects(object):
	"""
	Used by Treatment
	"""
	#def __init__(self, env, state, family, owner_id, family_tag='pl_family'):
	def __init__(self, env, owner_id, state='draft', family='CONSULTA',  family_tag='pl_family'):
		print('init')
		self.env = env
		self.state = state
		self.family = family
		self.owner_id = owner_id
		self.family_tag = family_tag

	def count(self):
		count = self.env.search_count([
										('treatment', '=', self.owner_id),
										('state', '=', self.state),
										#('pl_family', '=', self.family),
										(self.family_tag, '=', self.family),
								])
		return count
		
	def count_fast(self):
		count = self.env.search_count([
										('treatment', '=', self.owner_id),
										])
		return count