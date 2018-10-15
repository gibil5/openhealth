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
		file_name = lib.get_file_name(order)
		fname = dname + '/' + file_name + '.txt'


		# Open file 
		f = io.open(fname, mode="w", encoding="utf-8")

		# Create Content 
		content = lib.get_file_content(order)

		# Write content 
		print(content, file=f)

		# Close file 
		f.close()


		# Create Txt 
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
	os.system("tar cvf " + tarred + " " + source)
	os.system("gzip " + tarred)

# export_txt

