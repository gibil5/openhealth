# -*- coding: utf-8 -*-
"""
	Export

	Created: 			11 Sep 2018
	Last up: 	 		12 Sep 2018
"""
from __future__ import print_function  # Only needed for Python 2
import os
import shutil
import io
from . import lib_exp



# -------------------------------------------------------------------------------------------------
def export_txt(self, electronic_order, export_date):
	"""
	high level support for doing this and that.
	"""
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





	# Loop
	for order in electronic_order:

		create_txt(self, order, path)

		#if order.state in ['cancel']:
		#	create_txt(self, order, path)





# At the End
# Compress
	source = path
	tarred = path + '.tar'
	ziped = path + '.tar.gz'
	os.system("rm -rf " + tarred + " " + ziped)
	os.system("tar cf " + tarred + " " + source)
	os.system("gzip " + tarred)

	return ziped
# export_txt




# -------------------------------------------------------------------------------------------------
def create_txt(self, order, path):
	"""
	high level support for doing this and that.
	"""

	# Init

	# File name
	file_name = lib_exp.get_file_name(order)


	# Content
	content = lib_exp.get_file_content(order)



	# Create File

	# Init
	fname = path + '/' + file_name + '.txt'

	# Open
	f = io.open(fname, mode="w", encoding="utf-8")

	# Write
	print(content, file=f)

	# Close
	f.close()



	# Create Ids
	self.txt_ids.create({
								'name': 			file_name,
								'content': 			content,
								'container_id': 	self.id,
		})

# create_txt
