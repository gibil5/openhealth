# -*- coding: utf-8 -*-

from __future__ import print_function
from openerp import _
from openerp.exceptions import Warning as UserError


# ----------------------------------------------------------- Exceptions -------------------------
class CompanyRucValueException(Exception):
	pass

class CompanyNameValueException(Exception):
	pass



# ----------------------------------------------------------- Handle Exceptions -------------------------

def handle_exceptions(self):
	"""
	Handle Exceptions
	Try
		- Company's data is (RUC)
	"""
	print()
	print('ORD - Handle Exceptions')


	# Try several things

	try:
		self.configurator.ensure_one()

	except:
		msg_name = "ERROR: Configurator not existant"
		class_name = type(self.configurator).__name__
		#obj_name = self.configurator.name
		#msg =  msg_name
		#msg =  msg_name + '\n' + class_name + '\n' + obj_name
		msg =  msg_name + '\n' + class_name

		raise UserError(_(msg))


	try:
		#if self.x_my_company.name in (False, ''):
		if self.configurator.name in (False, ''):

			msg = "ERROR: Clínica no es válida"

			raise CompanyNameValueException


		#if self.x_my_company.x_ruc in (False, ''):
		if self.configurator.company_ruc in (False, ''):

			msg = "ERROR: RUC Clínica no es válido"

			raise CompanyRucValueException


	# Raise Exceptions
	except CompanyNameValueException:

		raise UserError(_(msg))


	except CompanyRucValueException:

		raise UserError(_(msg))




	# Other
	#except:
		#msg_name = "ERROR: Configurator not existant"
		#class_name = type(self.configurator).__name__
		#obj_name = self.configurator.name
		#msg =  msg_name
		#msg =  msg_name + '\n' + class_name + '\n' + obj_name
		#msg =  msg_name + '\n' + class_name



# handle_exceptions
