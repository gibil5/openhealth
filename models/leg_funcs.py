# -*- coding: utf-8 -*-
#
# 	*** Leg Funcs
# 
# Created: 				 26 Feb 2017
# Last updated: 	 	 id

from openerp import models, fields, api

#from datetime import timedelta
import datetime
from . import leg_vars





#------------------------------------------------ Create order ---------------------------------------------------

def create_order(self, serial_nr, pricelist_id, partner_id, patient_id, state, 
																#max_count, 
																date, 
																note):

	print
	print 'Create Order'

	print serial_nr
	print pricelist_id
	print partner_id
	print patient_id
	print state
	#print max_count
	print date
	print note


	order = self.env['sale.order'].create({

											'x_serial_nr': serial_nr,

											'note': note,
											
											'pricelist_id': pricelist_id,

											'partner_id': partner_id,

											'state': state,

											'patient': patient_id,

											'date_order': date,

											#'name': name,
										})

	#print order 


	name = 'test'
	price_unit = 55
	product_uom_qty = 2



	name = 'Producto Genérico'
	product = self.env['product.product'].search([
														('name', '=', name), 
													],
														#order='write_date desc',
														limit=1,
													)
	product_id = product.id
	
	#print product
	#print product_id



	order_id = order.id





	# All lines 
 	models = self.env['openhealth.legacy.order'].search([
															#('name', '=', name), 
															#('NombreCompleto', '!=', 'AAA'), 

															('serial_nr', '=', serial_nr), 
												
												],
															#order='FechaFactura_d desc',
															#limit=max_count,
											)

 	#print models


 	for model in models: 
 	#if False: 

 		print 'Create Order Line'
 		#print model


		name = model.descripcion
		product_uom_qty = model.cantidadtotal
		price_unit = model.Punit 		


		if name == False: 
			name = 'x'



		print name
		print product_uom_qty
		print price_unit
		print product_id
		print order_id


		ol = order.order_line.create({
										'name': name,
										'product_uom_qty': product_uom_qty, 
										'price_unit': price_unit, 

										'product_id': product_id,
										'order_id': order_id,
								})
		
		#print ol
		#print 

	return order










#------------------------------------------------ Update Patient ---------------------------------------------------

def update_patient(self, 	
							patient, 
							name, 
							hc_code, 
							doc_code, 
							sex, 		
							date_record, 
							date_created, 
							date_birth, 		
							address, 
							district, 
							phone, 
							mobile, 
							email, 
							comment, 
							completeness,
							):

	patient.name = name 

	patient.x_id_code = hc_code
	
	patient.x_dni = doc_code
	

	#patient.sex = sex
	patient.sex = leg_vars._hac[sex]



	patient.x_date_record = date_record

	patient.x_date_created = date_created

	patient.x_datetime_created = date_created

	patient.dob = date_birth




	patient.street = address

	patient.x_district = district

	patient.phone = phone

	patient.mobile = mobile

	patient.email = email


	patient.comment = comment


	patient.completeness = completeness


	return patient 





#------------------------------------------------ Create Patient ---------------------------------------------------
def create_patient(self, 	name, hc_code, doc_code, sex, 		date_record, date_created, date_birth, 		address, district, phone, mobile, email, 
							comment, 
							completeness):


	#_hac = {
	#			'F': 				'Female', 
	#			'M': 				'Male', 
	#			False:				False, 
	#		}


	#sex_h = _hac[sex]
	sex_h = leg_vars._hac[sex]



	ret = self.env['oeh.medical.patient'].create({

															'name': name,

															'x_id_code': hc_code,

															'x_dni': doc_code,

															'sex': sex_h,

															'x_date_record': date_record,

															'x_date_created': date_created,
															
															'x_datetime_created': date_created,

															'dob': date_birth,

															'street': address,

															'x_district': district,

															'phone': phone,

															'mobile': mobile,

															'email': email,

															'comment': comment,

															'x_completeness': completeness,
													})

	print ret 







#------------------------------------------------ Correct Time ---------------------------------------------------

def correct_time(self, date):

	#print 'jx'
	#print 'Correct'
	#print date 



	#if date != False  and  year >= 1900:
	if date != False: 


		#1876-10-10 00:00:00
		year = int(date.split('-')[0])
		#print year 


		if year >= 1900:


			DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"


			date_field1 = datetime.datetime.strptime(date, DATETIME_FORMAT)


			date_corr = date_field1 + datetime.timedelta(hours=+5,minutes=0)


			return date_corr





#------------------------------------------------ Date From Char ---------------------------------------------------

def get_date_from_char(self, date_char):

	#print 'jx'
	#print 'Get date from c'
	#print date_char



	if date_char != False: 


		a = date_char


		e = a.split()

		#b = a.split('/')
		b = e[0].split('/')


		#c = b[2] + '-' + b[1] + '-' + b[0] #+ ' ' + e[1]
		#c = b[2].zfill(4) + '-' + b[1].zfill(2) + '-' + b[0].zfill(2) 
		c = b[2].zfill(4) + '-' + b[1].zfill(2) + '-' + b[0].zfill(2) + ' ' + e[1]
	 	

		#c = c +  timedelta(hour=5)

	 	#+ ' ' + e[1]
		#.zfill()



		#date_d = date_char
		date_d = c


		#print date_d
		return date_d
