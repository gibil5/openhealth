# -*- coding: utf-8 -*-
"""
	Txt Line - Object Oriented
	
	For Account - Creates a File for each Txt Line

	Separate Structure and Business Logic

	Created: 				13 Dec 2019
	Last up: 				13 Dec 2019
"""
from __future__ import print_function
from openerp import models, fields, api

import pl_lib_exp

import io

class TxtLine(models.Model):
	"""
	Used by Account
	"""

	_name = 'openhealth.account.txt.line'

	_description = 'Openhealth Account Txt Line'

	#_order = 'date_create asc'



# ----------------------------------------------------------- Methods ------------------------------

	def get_file_name(self):
		"""
		Get File Name
		"""
		print()
		print('Get File Name')

		self.file_name, self.serial_number = pl_lib_exp.pl_get_file_name(self.order)		

		print(self.file_name)
		print(self.serial_number)




	def complete_order(self):
		"""
		Complete Order - Dep ?
		"""
		print()
		print('Complete Order')

		# Init Electronic
		self.order.pl_init(self.serial_number, self.path, self.file_name)





	def generate_content(self):
		"""
		Generate Content
		"""
		print()
		print('Generate Content')

		self.order.pl_create_txt()			# Object Oriented


		self.content = self.order.content





	def create_file(self):
		"""
		Create File
		"""

		# Create File
		#self.order.pl_create_file()			# Object Oriented
		self.create_actual_file()						# Object Oriented



	def create_actual_file(self):
		"""
		Create Acutal File
		"""
		print()
		print('X - Create Actual File')


		# Create File
		fname = self.path + '/' + self.file_name + '.txt'

		f = io.open(fname, mode="w", encoding="utf-8")

		print(self.content, file=f)
		
		f.close()



		# Create Txt Line
		#self.container_id.txt_ids.create({
		#									'name': 			self.file_name,
		#									'content': 			self.content,
		#									'container_id': 	self.container_id.id,
		#	})




# ----------------------------------------------------------- Relational -----------------------------

	# Electronic Order
	order = fields.Many2one(
			
			'openhealth.electronic.order',
			
			ondelete='cascade',
		)



# ----------------------------------------------------------- Handles -----------------------------
	# Electronic Container
	container_id = fields.Many2one(
			
			'openhealth.container',
			
			ondelete='cascade',
		)


# ----------------------------------------------------------- Fields ------------------------------

	name = fields.Char()

	path = fields.Char()


	content = fields.Char()

	file_name = fields.Char()

	serial_number = fields.Char()


