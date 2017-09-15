# -*- coding: utf-8 -*-
#
#
# 		*** OPEN HEALTH - Physician
# 
# Created: 				6 Mar 2017
# Last updated: 	 	Id.



from openerp import models, fields, api



class Physician(models.Model):
	

	_inherit = 'oeh.medical.physician'	
	
	#_name = 'openhealth.physician'
	



	#name = fields.Char(
	#		string="Terapeuta #", 
			#compute='_compute_name', 
	#	)


	vspace = fields.Char(
			' ', 
			readonly=True
		)
	






	consultancy_type = fields.Selection(
			
			string='Tipo', 
		)

	#institution = fields.Many2one(
	#		'oeh.medical.health.center',
	#		string='Escuela', 
	#	)

	institution = fields.Many2one('oeh.medical.health.center',string='Institución',help="Donde el médico trabaja")
	
	#'institution': fields.many2one('oeh.medical.health.center','Institution',help="Institution where doctor works"),




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
			string=Dirección, 
		)


	#mobile_phone 
	mobile_phone = fields.Char(
			'Celular', 
		)

	work_email = fields.Char(
			'Email'
		)


	work_phone = fields.Char(
			'Teléfono fijo'
		)



	address_id = fields.Many2one(

			'res.partner', 
			string='Institución de trabajo', 
		)


	speciality = fields.Many2one(
			'oeh.medical.speciality', 
			string='Especialidad', 
		)







	x_therapist = fields.Boolean(
			string='Terapeuta', 
			default=False,
		)	


	_phy_list = [

		('therapist','therapist'), 
		('doctor','doctor'), 

		#('',''), 

	]



	x_type = fields.Selection(
			string='Tipo', 

			selection = _phy_list, 

			#default='therapist',
		)



