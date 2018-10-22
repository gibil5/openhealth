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
def export_txt(self, electronic_order, export_date):
	#print 
	#print 'Export Text'
	#print(os.environ['HOME'])


	# Init 
	base_dir = os.environ['HOME']
	path = base_dir + "/mssoft/ventas/" + export_date



	# Make Dirs 
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
	dname = path
	
	
	# Loop 
	for order in electronic_order: 

		#lib.print_line(order)


# Init 		
		# File name 
		file_name = lib.get_file_name(order)
		#file_name = 'CC_' + file_name


		# Content 
		content = lib.get_file_content(order)



# File 
		# Init 
		fname = dname + '/' + file_name + '.txt'


		# Open
		f = io.open(fname, mode="w", encoding="utf-8")
		
		# Write  
		print(content, file=f)

		# Close
		f.close()


# Txt 
		# Create 
		txt = self.txt_ids.create({
									'name': 			file_name,
									'content': 			content,
									'container_id': 	self.id,
			})


# Compress 
	source = 	dname
	tarred = 	dname + '.tar'
	ziped = 	dname + '.tar.gz'

	os.system("rm -rf " + tarred + " " + ziped)
	#os.system("tar cvf " + tarred + " " + source)
	os.system("tar cf " + tarred + " " + source)
	os.system("gzip " + tarred)

# export_txt

