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
		print()
		print('TreatmentState  -  init')
		self.record = record
		#print(self.record)
		
		print("nr_budgets_cons: {}".format(self.record.nr_budgets_cons))
		print("nr_invoices_cons: {}".format(self.record.nr_invoices_cons))
		print("consultation_progress: {}".format(self.record.consultation_progress))
		
		print("nr_services: {}".format(self.record.nr_services))

		print("nr_budgets_pro: {}".format(self.record.nr_budgets_pro))
		print("nr_invoices_pro: {}".format(self.record.nr_invoices_pro))

		print("nr_procedures: {}".format(self.record.nr_procedures))
		print("nr_sessions: {}".format(self.record.nr_sessions))
		print("nr_controls: {}".format(self.record.nr_controls))

		print("treatment_closed: {}".format(self.record.treatment_closed))


	def get_state(self):
		"""
		Format Line Items
		"""
		print()
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
