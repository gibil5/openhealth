# -*- coding: utf-8 -*-
#
#   Import
#
#   Created:            16 Oct 2018
#   Last up:            16 Oct 2018
#

"""
high level support for doing this and that.
"""

import io
import os


#------------------------------------------------ Import TXT --------------------------------------

def import_txt(self):
	"""
	high level support for doing this and that.
	"""
	#print
	#print 'Import Txt'

	#print(os.environ['HOME'])


	# Init
	base_dir = os.environ['HOME']
	path = base_dir + "/mssoft/import/"

	fnames = []

	crn_inv_fname = 'RUC20508997567-07-20170725-FC02-00009999'

	tic_inv_fname = 'RUC20478087820-01-20180712-F001-00007777'

	tic_rec_fname = 'RUC20508997567-03-20170725-B001-00008888'


	if self.cn_invoice_create:
		fnames.append(crn_inv_fname)

	if self.ticket_invoice_create:
		fnames.append(tic_inv_fname)

	if self.ticket_receipt_create:
		fnames.append(tic_rec_fname)


	#print fnames


	# Loop
	for fname in fnames:

		fname = path + fname + '.txt'

		#print fname_inp
		#print

		# Open
		f = io.open(fname, mode="r", encoding="utf-8")


		# Read
		#content = f.readlines()


		content = ''

		# Read
		for line in f:
			# line = line.rstrip().replace('|', ',')
			# f_out.write(line + '\n')
			#content = content +  line + '\n'
			#print line
			content = content +  line
		#print


		# Txt - Create
		self.txt_ref_ids.create({
			'name':                 fname,
			'content':              content,
			'container_ref_id':     self.id,
		})


		# Close
		f_inp.close()

# import_txt
