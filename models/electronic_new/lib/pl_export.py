# -*- coding: utf-8 -*-
"""
	Export

	Created: 			11 Sep 2018
	Last updated: 		 9 Aug 2019
"""
from __future__ import print_function  # Only needed for Python 2
import os
import shutil
import io

#from openerp.addons.openhealth.models.containers import lib_exp

from . import pl_lib_exp


# -------------------------------------------------------------------------------------------------

def create_txt_for_all_electronic_orders(self, electronic_order, path):
	"""
	Create TXT 
	For all Electronic Orders
	"""
	print()
	print('X - Create Txt for all EOs')
	
	#print(os.environ['HOME'])


# Clean

	# Remove dir
	if os.path.isdir(path) and not os.path.islink(path):
		shutil.rmtree(path)		# If dir
	
	# Create dir
	os.mkdir(path)




# Loop - For all Electronic Lines
	for order in electronic_order:

		
		# Instantiate Txt Line
		#txt_line = TxtLine()



		# Get File Name
		file_name, id_serial_nr = pl_lib_exp.pl_get_file_name(order)		


		# Init Electronic
		order.pl_init(id_serial_nr, path, file_name)


		# Create Content 
		order.pl_create_txt()			# Object Oriented


		# Create File
		order.pl_create_file()			# Object Oriented




# Shut down and Clean

	# Compress and Remove
	source = path
	tarred = path + '.tar'
	ziped = path + '.tar.gz'
	os.system("rm -rf " + tarred + " " + ziped)
	os.system("tar cf " + tarred + " " + source)
	os.system("gzip " + tarred)


	return ziped
# export_txt

