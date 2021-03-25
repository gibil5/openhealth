# -*- coding: utf-8 -*-
"""
		pl_acc_lib.py

 		Created: 				12 April 2019
 		Last up: 	 		 	12 April 2019
"""

# ----------------------------------------------------------- Get Cuentab ---------------------
def get_cuentab(self, product_type):
	"""
	Get Cuentab
	Used by Accounting
	"""
	print()
	print('Pl Acc Lib - Get Cuentab')
	#print(self)
	#print(product_type)
	#print(self.product)
	print(self.product.name)
	print(self.product.pl_account)


	# Search
	configurator = self.env['openhealth.configurator.emr'].search([
													],
														#order='date_begin asc',
														#limit=10,
												)
	#print(configurator.name)

	if product_type in ['product']:
		#cuentab = configurator.cuentab_products
		cuentab = self.product.pl_account

	elif product_type in ['service']:
		cuentab = configurator.cuentab_services

	elif product_type in ['consu']:
		cuentab = configurator.cuentab_consu

	else:
		print('Pl Acc Lib - Get Cuentab - This should not happen !')


	#print(product_type)
	#print(cuentab)

	#return acc_vars.get_cuentab(product_type)
	return cuentab
