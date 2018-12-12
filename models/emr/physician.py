# -*- coding: utf-8 -*-
#
# 		*** Physician
# 
# Created: 				6 Mar 2017
#

from openerp import models, fields, api



# ----------------------------------------------------------- Physician ------------------------------------------------------

class Physician(models.Model):

	_inherit = 'oeh.medical.physician'	
	
	#_order = 'name'
	_order = 'idx asc'

	#_name = 'openhealth.physician'
	



	#x_type = fields.Selection(
	#		[
	#			('therapist','therapist'), 
	#			('doctor','doctor'), 
	#		], 
	#		string='Tipo', 
	#	)



	#idx = fields.Integer(
	idx = fields.Char(
			#default=-1, 
		)


	x_therapist = fields.Boolean(
			string='Terapeuta', 
			default=False,
		)	
	
	x_user_name = fields.Many2one(		
			'res.users',
			string = "Nombre de usuario", 	
		)

	vspace = fields.Char(
			' ', 
			readonly=True
		)




	consultancy_type = fields.Selection(			
			string='Tipo', 
		)

	institution = fields.Many2one('oeh.medical.health.center',string='Institución',help="Donde el médico trabaja")
	
	is_pharmacist = fields.Boolean(
			string='Farmaceútico ?', 
		)

	consultancy_price = fields.Integer(			
			string='Precio de consulta', 
		)

	code = fields.Char(
			string='Número de licencia', 
		)

	oeh_user_id = fields.Many2one(
			'res.users', 
			string='Responsable', 
		)

	work_location = fields.Char(
			string='Dirección', 
		)


	#mobile_phone 
	mobile_phone = fields.Char(
			'Celular', 
		)

	work_email = fields.Char(
			'Email', 
		)


	work_phone = fields.Char(
			'Teléfono fijo', 
		)



	address_id = fields.Many2one(

			'res.partner', 
			string='Institución de trabajo', 
		)


	speciality = fields.Many2one(
			'oeh.medical.speciality', 
			string='Especialidad', 
		)






# ----------------------------------------------------------- Physician Line ------------------------------------------------------

class PhysicianLine(models.Model):
	_inherit = 'oeh.medical.physician.line'  

	# Array containing different days name
	PHY_DAY = [
		('Monday', 'Lunes'),
		('Tuesday', 'Martes'),
		('Wednesday', 'Miercoles'),
		('Thursday', 'Jueves'),
		('Friday', 'Viernes'),
		('Saturday', 'Sabado'),
		('Sunday', 'Domingo'),
		]

	name = fields.Selection(
		PHY_DAY, 
		'Dia', 
		required=True
	)

	start_time = fields.Float(
		'Inicio', 
	)

	end_time =  fields.Float(
		'Final', 
	)

