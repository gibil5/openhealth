
# ----------------------------------------------------------- Ticket - Get Raw Line ----------------
#jx
# Raw Line
def get_ticket_raw_line(self, argument):
	"""
	Abstraction. 
	Used by tickets.
	Can be used by all entries. 
	Types:
		- Receipt, 
		- Invoice, 
		- Credit note. 
	"""

	print()
	print('Get Ticket Raw Line')

	print(argument)

	line = 'empty'


	# Credit note
	if argument in ['date_credit_note']:
		tag = 'Fecha:'
		value = self.get_date_corrected()

	elif argument in ['denomination_credit_note_owner']:
		tag = 'Denominacion:'
		value = self.x_credit_note_owner.x_serial_nr

	elif argument in ['date_credit_note_owner']:
		tag = 'Fecha de emision:'
		value = self.x_credit_note_owner.get_date_corrected()

	elif argument in ['reason_credit_note']:
		tag = 'Motivo:'
		value = self.get_credit_note_type()



	# Receipt


	# Invoice



	else:
		print('This should not happen !')


	line = self.format_line(tag, value)


	#print(line)
	return line
