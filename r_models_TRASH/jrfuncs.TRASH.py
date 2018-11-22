

# 3 Jul 2018 


#from datetime import datetime,tzinfo,timedelta


#------------------------------------------------ Unidecode ---------------------------------------------------

#import unicodedata
#def strip_accents(s):
#   return ''.join(c for c in unicodedata.normalize('NFD', s)
#                  if unicodedata.category(c) != 'Mn')



# 20 Jul 2018


#------------------------------------------------ Appointment ---------------------------------------------------

# Update Apps - Deprecated 
@api.multi
#def update_appointment_go(self, appointment_id, owner_id, x_type):
def update_appointment_go_dep(self, appointment_id, owner_id, x_type):

	# Get all Apps 	
	rec_set = self.env['oeh.medical.appointment'].browse([
															appointment_id
														])
	#print rec_set


	# By type 
	if x_type == 'consultation':
		ret = rec_set.write({
								'consultation': owner_id,
							})

	elif x_type == 'procedure':
		ret = rec_set.write({
								'procedure': owner_id,
							})

	elif x_type == 'session':
		ret = rec_set.write({
								'session': owner_id,
							})

	elif x_type == 'control':
		ret = rec_set.write({
								'control': owner_id,
							})
	return ret

# update_appointment_go

