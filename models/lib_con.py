# -*- coding: utf-8 -*-
#
# 		lib.py
#
# 		Abstract, general purpose. Can be Unit-tested. Is completely standard. Gives service to all Users
# 
# 		Created: 			13 Aug 2018
# 		Last up: 	 		19 Oct 2018
#


#------------------------------------------------ File Name ---------------------------------------------------
def generate_serial_nr(counter, delta, pad):
	print 
	print 'Gen Serial Nr'

	return '001-' + str(counter + delta).zfill(pad)




#------------------------------------------------ File Name ---------------------------------------------------
def get_serial_nr(serial_nr, delta, pad):
	print 
	print 'Get Serial Nr'

	return '001-' + str(int(serial_nr.split('-')[1]) + delta).zfill(pad)
