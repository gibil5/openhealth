# -*- coding: utf-8 -*-
"""
	Order Exceptions

	Created: 			26 mar 2021
	Previous: 			26 mar 2021
	Last: 			 	26 mar 2021
"""

from __future__ import print_function
from openerp import _
from openerp.exceptions import Warning as UserError

# ----------------------------------------------------------- Exceptions -------------------------
class OrderRequiredParameterException(Exception):
    pass


# ----------------------------------------------------------- Handle Exceptions Electronic -------------------------
def handle_exceptions_electronic(self):
	"""
	Handle Exceptions Electronic
	"""
	print()
	print('ORD - Handle Exceptions Electronic')


	# Required parameters
	try:
		#if self.x_type in [False] or self.x_type_code in [False]		or self.x_serial_nr in [False]   	or self.pl_receptor in [False, '']:

		if self.x_serial_nr in [False]:
			msg = "ERROR 1: Venta - Falta Numero de Serie"
			raise OrderRequiredParameterException


		if self.x_type in [False] or self.x_type_code in [False]:
			msg = "ERROR 2: Venta - Paciente falta Documento de Identidad"
			raise OrderRequiredParameterException


		if self.pl_receptor in [False, '']:
			msg = "ERROR 3: Venta Falta Nombre de cliente"
			raise OrderRequiredParameterException


	except OrderRequiredParameterException:
		raise UserError(_(msg))

# handle_exceptions_electronic



# ----------------------------------------------------------- Handle Exceptions -------------------------
#@api.multi
#def handle_exceptions(self):
#	"""
#	Handle Exceptions
#	"""
#	print()
#	print('ORD - Handle Exceptions Electronic')
# handle_exceptions_electronic


