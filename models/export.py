# -*- coding: utf-8 -*-
from __future__ import print_function  # Only needed for Python 2
#
#	Export. 
# 
#	Created: 			11 Sep 2018
# 	Last up: 	 		12 Sep 2018
#
from openerp import models, fields, api
import os
import shutil
import lib 
import io


# ----------------------------------------------------------- Create Services  ------------------------------------------------------
def sync(electronic_order):
	print 
	print 'Sync'





# ----------------------------------------------------------- Create Services  ------------------------------------------------------
#def export_txt(electronic_order):
def export_txt(electronic_order, export_date):
	#print 
	#print 'Export Text'


	# Init 
	base_dir = '/Users/gibil/Virtualenvs/Odoo9-min/odoo'
	#path = base_dir + "/mssoft/ventas"
	#path = base_dir + "/mssoft/ventas/2018_09_25"
	path = base_dir + "/mssoft/ventas/" + export_date


	# Remove 
	if os.path.isdir(path) and not os.path.islink(path):
		shutil.rmtree(path)		# If dir 
	#elif os.path.exists(path):
	#	os.remove(path)			# If file 


	# Create 
	os.mkdir(path)  



	# Init 
	#dname = "mssoft/ventas"
	#dname = "mssoft/ventas/2018_09_25"
	dname = "mssoft/ventas/" + export_date
	
	
	for order in electronic_order: 


		# Prints 
		lib.print_line(order)


		# Init 
		rname = lib.get_file_name(order)
		
		fname = dname + '/' + rname + '.txt'


		# Open file 
		f = io.open(fname, mode="w", encoding="utf-8")
		


		# Create Content 
		content = 	lib.get_file_content(order)


		
		print(content, file=f)
		f.close()

# export_txt

