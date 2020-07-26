# -*- coding: utf-8 -*-
"""
	fix_treatment.py
	FixTreament Class

	Created: 			25 Jul 2020
	Last up: 	 		25 Jul 2020
"""

class FixTreatment(object):
	"""
	Used by Order.
	Contains the fixer rules. 
	"""

	def __init__(self, env, patient_id, doctor_id):
		print('Init')
		self.env = env
		self.patient_id = patient_id
		self.doctor_id = doctor_id

	def fix(self): 
		print('Fix')

		# Get Treatment
		treatment = self.env.search([
										('patient', '=', self.patient_id),
										('physician', '=', self.doctor_id),
				],
					order='start_date desc',
					limit=1,
				)
		print(treatment.name)
