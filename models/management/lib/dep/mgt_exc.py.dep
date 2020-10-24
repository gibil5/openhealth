# -*- coding: utf-8 -*-

from __future__ import print_function
from openerp import _
from openerp.exceptions import Warning as UserError

# ----------------------------------------------------------- Handle Exceptions -------------------------

#@api.multi
def handle_exceptions(self):
	"""
	Handle Exceptions
	"""
	#print()
	#print('MGT - Handle Exceptions')


	# Configurator not existant
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

# handle_exceptions
