


# 16 June 2017 


#------------------------------------------------ Appointment ---------------------------------------------------

@api.multi
def update_appointment_go(self, appointment_id, owner_id, x_type):

		rec_set = self.env['oeh.medical.appointment'].browse([
																appointment_id																
															])

		if x_type == 'consultation':
			ret = rec_set.write({
									'consultation': owner_id,
								})

		elif x_type == 'procedure':
			ret = rec_set.write({
									'procedure': owner_id,
									'state': 'Scheduled',

								})

		elif x_type == 'session':
			ret = rec_set.write({
									'session': owner_id,
								})

		elif x_type == 'control':
			ret = rec_set.write({
									'control': owner_id,
								})

		else:
			tra = 1

		return ret