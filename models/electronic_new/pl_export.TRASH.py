



# -------------------------------------------------------------------------------------------------
def create_file(self, content, path, file_name):

	# Create File
	fname = path + '/' + file_name + '.txt'

	f = io.open(fname, mode="w", encoding="utf-8")
	
	print(content, file=f)
	
	f.close()


	# Create Txt Ids
	self.txt_ids.create({
								'name': 			file_name,
								'content': 			content,
								'container_id': 	self.id,
		})

# create_txt



# -------------------------------------------------------------------------------------------------
#def create_txt(self, order, path):
#def create_txt(self, order, path, file_name):
def create_txt(self, order):
	"""
	high level support for doing this and that.
	"""
	print()
	print('Create Txt')
	print(self)
	print(order)

	# Watchout - Changes order !
	#file_name = lib_exp.get_file_name(order)		# File name
	#file_name = pl_lib_exp.pl_get_file_name(order)		
	#file_name, id_serial_nr = pl_lib_exp.pl_get_file_name(order)
	#order.id_serial_nr = id_serial_nr


	# Content - This !!!
	content = lib_exp.get_file_content(order)

	return content
