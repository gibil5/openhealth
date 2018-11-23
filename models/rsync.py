# -*- coding: utf-8 -*-
"""
#	Rsync. 
# 
#	Created: 			 1 Oct 2018
# 	Last up: 	 		 1 Oct 2018
"""
import os
import shutil
import io

# ----------------------------------------------------------- Sync  -------------------------------
def synchronize():
	#print
	#print "Synchronize"
	
	# Init
	base_dir = os.environ['HOME']
	source = base_dir + "/mssoft/ventas/"
	destination = 'root@165.227.25.8:/var/www/html/ventas'

	# Rsync
	os.system("rsync -rv " + source + " " + destination)

	# List
	#ret = os.listdir(path)
	#print ret
