# -*- coding: utf-8 -*-
#
# 		account.py
# 
# 		Created: 			14 Sep 2018
# 		Last up: 	 		14 Sep 2018
#


#------------------------------------------------ Const ---------------------------------------------------
_dic = {
				'CONSULTA MEDICA': 														'2041100011', 
				'PROTECTOR SOLAR': 														'101111007', 
				'LASER CO2 FRACCIONAL - Cuello - Rejuvenecimiento Cuello Grado 1 - 1': 	'2041100151', 

				'Producto 1': 															'40010007', 	
}


#------------------------------------------------ File Content ---------------------------------------------------
# Get Code 
def get_account_code(product):
	print 
	print 'Get Account Code'

	if product.name in _dic: 
		code = _dic[product.name]
	else:
		code = 'x'

	return code 

