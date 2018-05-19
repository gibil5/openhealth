# -*- coding: utf-8 -*-
#
# 	Patient Line
# 
# Created: 				16 May 2018
#

from openerp import models, fields, api

import pat_vars


class PaitentLine(models.Model):
	
	_name = 'openhealth.patient.line'

	_order = 'date_create desc'





# ----------------------------------------------------------- Dates ------------------------------------------------------

	# Patient 
	patient = fields.Many2one(
			'oeh.medical.patient', 
			string="Paciente", 
		)



	# Date Created 
	date_create = fields.Datetime(
			string="Fecha de Creación", 
		)

	# Date Record 
	date_record = fields.Datetime(
			#string="Fecha de Registro", 
			string="Fecha creación", 
		)


	# Age 
	age = fields.Char(
			string = "Edad", 		
		)

	age_years = fields.Integer(
			string = "Edad", 		
			#default=0, 
			default=-1, 
		)

	dob = fields.Date(
			string="Fecha nacimiento",
			required=False, 
		)





	# Sex 
	sex = fields.Selection(
			selection = pat_vars._sex_type_list, 
			string="Sexo",
			#required=False, 
		)


	# First Contact 
	first_contact = fields.Selection(

			selection = pat_vars._first_contact_list, 
		
			string = 'Primer contacto',
		)



	# Education 
	education = fields.Selection(
			selection = pat_vars._education_level_type,
			string = 'Grado de instrucción',
		)



	# Vip 
	vip = fields.Boolean(
			string = 'Vip',
		)




	# Address

	country = fields.Char()

	city = fields.Char()

	district = fields.Char()




# ----------------------------------------------------------- Relational ------------------------------------------------------

	account_id = fields.Many2one(
			'openhealth.account.contasis'
		)


# ----------------------------------------------------------- Actions ------------------------------------------------------

	# Update Fields
	@api.multi
	def update_fields(self):  

		#print
		#print 'Update Fields - Patient'


		if self.age.split()[0] != 'No': 
			self.age_years = self.age.split()[0]
			ret = 1
			
		else:
			#print self.patient
			#print self.patient.name 
			#print self.age 
			ret = -1


		return ret 

