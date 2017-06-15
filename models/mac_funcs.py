# -*- coding: utf-8 -*-

from openerp import models, fields, api
import datetime

from . import appfuncs


# ----------------------------------------------------------- Machines  ------------------------------------------------------

@api.multi

#def search_machine(self, appointment_date, doctor_name, duration):
def search_machine(self, appointment_date, doctor_name, duration, start_machine):

	#print 
	#print
	#print 'jx'
	#print 'Reserve - Machine'

	target = 'machine'

	#print appointment_date
	#print doctor_name
	#print duration
	#print start_machine
	#print target


	#m_list = ['laser_co2_1', 'laser_co2_2', 'laser_co2_3']


	_hash_machine_idx = {

							False:			0, 

							'laser_co2_1':	1, 
							'laser_co2_2':	2, 
							'laser_co2_3':	0, 

							'laser_excilite':	0, 
							'laser_m22':	0, 



							'laser_triactive':	0, 
							'chamber_reduction':	0, 
							'carboxy_diamond':	0, 
					}


	m_dic = {
				'laser_co2_1': 		['laser_co2_1', 'laser_co2_2', 'laser_co2_3'],

				'laser_excilite': 	['laser_excilite'], 
				
				'laser_m22': 		['laser_m22'], 



				'laser_triactive': 		['laser_triactive'], 
				'chamber_reduction': 	['chamber_reduction'], 
				'carboxy_diamond': 		['carboxy_diamond'], 
	}


	
	

	idx = _hash_machine_idx[start_machine]


	m_list = m_dic[start_machine]


	x_machine = m_list[idx]







	ret = 1 



	while not ret == 0:


		#ret, doctor_name, start, end = check_for_collisions(self, appointment_date, doctor_name, duration, x_machine)
		#ret, doctor_name, start, end = check_for_collisions(self, appointment_date, doctor_name, duration, x_machine, target)
		#ret, doctor_name, start, end = check_for_collisions(self, appointment_date, doctor_name, duration, x_machine, target, 'procedure')
		ret, doctor_name, start, end = appfuncs.check_for_collisions(self, appointment_date, doctor_name, duration, x_machine, target, 'procedure')



		if ret != 0:	# Error 

			idx = idx + 1

			if idx == 3:
				#idx = 0
				return False



			x_machine = m_list[idx]




			#return {'warning': {'title': "Error: Colisión !",'message': 'La sala ya está reservada: ' + start + ' - ' + end + '.',}}


		else: 			# Success 

			#print 'Success !'

			return x_machine



	# search_machine
