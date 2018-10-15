# -*- coding: utf-8 -*-



#------------------------------------------------ Constants ---------------------------------------------------
_dic_prefix = {
				'01': 'F001', 	# Ticket Invoice 
				'03': 'B001', 	# Ticket Receipt 
				'11': 'FF01', 	# Invoice 				# Not Sunat Compliant !
				'13': 'BB01', 	# Receipt 				# Not Sunat Compliant !

				#'14': 'P', 	# Advertisement 
				#'15': 'N', 	# Sale Note 
}

_dic_prefix_cancel = {
				'01': 'FC01', 	# Invoice 
				'03': 'BC01', 	# Receipt 
				'11': 'FFC1', 	# Invoice 				# Not Sunat Compliant !
				'13': 'BBC1', 	# Receipt 				# Not Sunat Compliant !

				#'14': 'P', 	# Advertisement 
				#'15': 'N', 	# Sale Note 
}