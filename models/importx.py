# -*- coding: utf-8 -*-
#
#	Import
# 
#	Created: 			16 Oct 2018
# 	Last up: 	 		16 Oct 2018
#
from openerp import models, fields, api
import os
import shutil
import lib 
import io


def import_txt(self):
	print 
	print 'Import Txt'

	print(os.environ['HOME'])



	# Init 
	base_dir = os.environ['HOME']
	path = base_dir + "/mssoft/import/"

	fnames = [
				'MS_RUC20547678894-03-20170725-B001-00008888', 
				#'CC_RUC20523424221-03-20180914-B001-00000575', 
	]


	# Loop
	for fname in fnames: 

		fname_inp = path + fname + '.txt'
		#fname_out = path + fname + '.csv'

		print fname_inp
		#print fname_out
		print 

		# Open
		f_inp = io.open(fname_inp, mode="r", encoding="utf-8")
		#f_out = io.open(fname_out, mode="w", encoding="utf-8")

		
		# Read 
		#content = f_inp.readlines()

		content = ''

		# Read  
		for line in f_inp:
			# line = line.rstrip().replace('|', ',')
			print line 
			# f_out.write(line + '\n')
			#content = content +  line + '\n'		
			content = content +  line 
		print 


		# Txt - Create 
		txt = self.txt_ref_ids.create({
										'name': 			fname,
										
										'content': 			content,

										'container_ref_id': 	self.id,
			})

		# Close
		f_inp.close()
		#f_out.close()




