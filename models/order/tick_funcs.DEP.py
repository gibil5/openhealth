

# ----------------------------------------------------------- Getters -------------------------
def get_date_corrected(self):
	#print()
	#print('Tic Funcs - Get date corrected')

	date_corrected = compute_date_corrected(self)
	
	print(date_corrected)
	return date_corrected 


def compute_date_corrected(self):
	#print()
	#print('Tic funds - Compute date corrected')

	DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"

	date_field1 = datetime.datetime.strptime(self.date_order, DATETIME_FORMAT)

	date_field2 = date_field1 + datetime.timedelta(hours=-5, minutes=0)
	
	DATETIME_FORMAT_2 = "%d-%m-%Y %H:%M:%S"

	date_corrected = date_field2.strftime(DATETIME_FORMAT_2)

	return date_corrected

