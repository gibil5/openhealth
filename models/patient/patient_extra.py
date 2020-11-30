"""
	*** Patient extra

	Created: 			29 nov 2020
	Last up: 			29 nov 2020
"""
from __future__ import print_function
from openerp import models, fields, api

class Patient(models.Model):
	"""
    Patient extra.
    Everything that does not fit in a tight model.
	"""
	_inherit = 'oeh.medical.patient'
	#_description = 'Patient extra'
	#_order = 'x_id_code desc'

# ----------------------------------------------------------- Test - Fields -----------------------

# ----------------------------------------------------------- Test - Computes----------------------
	# Computes
	def test_computes(self):
		"""
		Test computes
		"""
		print()
		print('Patient - Computes')

		# Patient
		print()
		print('Computes')
		print(self.name)
		print(self.x_legacy)
		print(self.x_treatment_count)
		print(self.x_counter)
		print(self.x_vip)
		print(self.x_card)

		# Partner
		print()
		print('Computes - Partner')
		print(self.partner_id.city_char)
		print(self.partner_id.x_address)
		print(self.partner_id.x_vip)

	# Actions
	def test_actions(self):
		"""
		Test actions
		"""
		#print
		#print 'Patient - Actions'
		self.deactivate_patient()
		self.activate_patient()
		self.open_treatment()
		self.generate_order_report()
		if self.x_test:
			self.autofill()


	# Actions
	def test_services(self):
		"""
		Test services
		"""
		#print
		#print 'Patient - Services'
		for treatment in self.treatment_ids:
			for service in treatment.service_co2_ids:
				service.test()
			for service in treatment.service_excilite_ids:
				service.test()
			for service in treatment.service_ipl_ids:
				service.test()
			for service in treatment.service_ndyag_ids:
				service.test()
			for service in treatment.service_product_ids:
				service.test()
			for service in treatment.service_quick_ids:
				service.test()

# ------------------------------------------------------------------- Test -----
	# Test - Integration
	@api.multi
	def test(self):
		"""
		High level testing
		"""
		print()
		print('Patient - Test')

		# Test Unit
		self.test_computes()
		self.test_actions()
		self.test_services()

		# Test Cycle - Dep ?
		#self.test_cycle()
	# test


# ----------------------------------------------------------- Validate - Button -----------
	@api.multi
	def validate(self):
		"""
		Just a wrapper
		"""
		print()
		print('Wrapper')
