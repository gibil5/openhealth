# -*- coding: utf-8 -*-
"""
	treatment_state.py
	TreatmentState Class

	Created: 			24 Jul 2020
	Last up: 	 		24 Jul 2020
"""

class TreatmentState(object):
	"""
	Used by Treatment
	"""
	def __init__(self, record):
		print('TreatmentState  -  init')
		self.record = record
		print(self.record)

	def get_state(self):
		"""
		Format Line Items
		"""
		print('get_state')
		state = 'empty'
		if self.record.treatment_closed:
			state = 'done'
		elif self.record.nr_controls > 0:
			state = 'controls'
		elif self.record.nr_sessions > 0:
			state = 'sessions'
		elif self.record.nr_procedures > 0:
			state = 'procedure'
		elif self.record.nr_invoices_pro > 0:
			state = 'invoice_procedure'
		elif self.record.nr_budgets_pro > 0:
			state = 'budget_procedure'
		elif self.record.nr_services > 0:
			state = 'service'
		elif self.record.consultation_progress == 100:
			state = 'consultation'
		elif self.record.nr_invoices_cons > 0:
			state = 'invoice_consultation'
		elif self.record.nr_budgets_cons > 0:
			state = 'budget_consultation'
		return state
