# -*- coding: utf-8 -*-
"""
#	Rsync. 
# 
#	Created: 			 14 Dec 2018
# 	Last up: 	 		 14 Dec 2018
"""
from __future__ import print_function

import os
#import shutil
#import io


# ----------------------------------------------------------- Sync  -------------------------------
def synchronize():
	print()
	print("Synchronize")
	
	# Init
	base_dir = os.environ['HOME']

	#source = base_dir + "/mssoft/ventas/"
	#source = base_dir + "/reports/"
	source = base_dir + "/reports/img/"
	
	destination = 'root@165.227.25.8:/var/www/html/reports'

	# Rsync
	os.system("rsync -rv " + source + " " + destination)

	# List
	#ret = os.listdir(path)
	#print ret
