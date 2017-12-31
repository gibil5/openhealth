


# 16 Dec 2017


	# Ooor - For consistency 
	#nr_treatments = fields.Integer(
	#		compute='_compute_nr_treatments',
	#		string = "Número de vacunas",
	#		default = 55, 
	#		)

	#@api.multi
	#def _compute_nr_treatements(self):
	#	for record in self:
	#		record.nr_treatments = 5  
	
			#record.x_nr_treatments = 5  
			#sub_total = 0 
			#for tr in record.treatment_ids:   
			#	sub_total = sub_total + 1  
			#record.x_nr_treatments= sub_total  



# 30 Dec 2017

	#_order = 'x_date_created desc'





	#@api.onchange('x_service_quick_ids')
	#def _onchange_x_service_quick_ids(self):
			

	#	print 'jx'
		#print 'On change service quick ids'


	#	for service in self.x_service_quick_ids:
	#		service.nr_hands_i = 3
	#		service.nr_body_local_i = 3
	#		service.nr_face_local_i = 3 

		#for service in self.x_service_quick_ids:

		#	zone = service.zone 
		#	print zone 

		#	if zone == 'hands': 
		#		print 'gotcha hands'
		#		service.nr_hands_i = service.nr_hands_i + 1

		#	elif zone == 'body_local':
		#		print 'gotcha bl'
		#		service.nr_body_local_i = service.nr_body_local_i + 1

		#	elif zone == 'face_local':
		#		print 'gotcha fl'
		#		service.nr_face_local_i = service.nr_face_local_i + 1






			# Counters 
			#print 'Counters'
			#for service in record.x_service_quick_ids:
			#	print service
			#	service.nr_hands_i = 6
			#	service.nr_body_local_i = 6
			#	service.nr_face_local_i = 6






