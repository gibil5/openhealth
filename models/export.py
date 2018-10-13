# -*- coding: utf-8 -*-
from __future__ import print_function  # Only needed for Python 2
#
#	Export
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
def export_txt(electronic_order, export_date):
	#print 
	#print 'Export Text'

	#print(os.environ['HOME'])




	# Init 
	#base_dir = '/Users/gibil/Virtualenvs/Odoo9-min/odoo'
	#base_dir = '.'
	base_dir = os.environ['HOME']
	path = base_dir + "/mssoft/ventas/" + export_date



	# Make  
	target = base_dir + "/mssoft/"
	if not os.path.isdir(target):
		os.mkdir(target)  
		
	target = base_dir + "/mssoft/ventas/"
	if not os.path.isdir(target):
		os.mkdir(target)  




	# Remove 
	if os.path.isdir(path) and not os.path.islink(path):
		shutil.rmtree(path)		# If dir 
	#elif os.path.exists(path):
	#	os.remove(path)			# If file 


	# Create 
	os.mkdir(path)  


	# Dir Name 
	#dname = "mssoft/ventas/" + export_date
	dname = path
	
	
	# Loop 
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



		# Write 		
		print(content, file=f)

		# Close 		
		f.close()


	# Compress 
	source = 	dname
	tarred = 	dname + '.tar'
	ziped = 	dname + '.tar.gz'
	
	#source = 	'./' + export_date
	#tarred = 	export_date + '.tar'
	#ziped = 	export_date + '.tar.gz'



	os.system("rm -rf " + tarred + " " + ziped)

	os.system("tar cvf " + tarred + " " + source)

	os.system("gzip " + tarred)



# export_txt

