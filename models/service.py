# -*- coding: utf-8 -*-
#
# 	Service 
# 
# Created: 				20 Sep 2016
# Last updated: 	 	12 Oct 2016


from openerp import models, fields, api
from datetime import datetime

from . import exc
from . import ipl
from . import prodvars
from . import serv_funcs




class Service(models.Model):

	_name = 'openhealth.service'

	#_inherit = 'openhealth.base', 




	# Treatement 
	treatment = fields.Many2one('openhealth.treatment',
			ondelete='cascade', 			
			string="Tratamiento", 
			readonly=True, 
			)








	nr_hands_i = fields.Integer(
	#nr_hands = fields.Integer(
			'hands', 
			#default=0, 

			#required=True,
			required=False,
		)

	nr_body_local_i = fields.Integer(
	#nr_body_local = fields.Integer(
			'body local', 
			#default = 0, 
			
			#required=True,
			required=False,
		)

	nr_face_local_i = fields.Integer(
	#nr_face_local = fields.Integer(
			'face local', 
			#default = 0, 
			
			#required=True,
			required=False,
		)






	nr_cheekbones = fields.Integer(
			'cheek', 
			#default=0, 
			
			#required=True,
			required=False,
		)

	nr_face_all = fields.Integer(
			'face all', 
			#default=0, 
			
			#required=True,
			required=False,
		)
	nr_face_all_hands = fields.Integer(
			'face all hands', 
			#default=0, 
			
			#required=True,
			required=False,
		)






	nr_face_all_neck = fields.Integer(
			'face all neck', 
			#default=0, 
			
			#required=True,
			required=False,
		)

	nr_neck = fields.Integer(
			'neck', 
			#default=0, 
			
			#required=True,
			required=False,
		)

	nr_neck_hands = fields.Integer(
			'neck hands', 
			#default=0, 
			
			#required=True,
			required=False,
		)






	#nr_hands = fields.Many2one(
	#		'openhealth.counter_raw',
	#		required=False,
	#	)

	#nr_body_local = fields.Many2one(
	#		'openhealth.counter_raw',
	#		required=False,
	#	)

	#nr_face_local = fields.Many2one(
	#		'openhealth.counter_raw',
	#		required=False,
	#	)









	# Comeback 
	comeback = fields.Boolean(
			string='Regreso', 			
		)







	# Patient 
	patient = fields.Many2one(
			'oeh.medical.patient', 
		)

	#@api.onchange('write_date')
	#def _onchange_write_date(self):
	#@api.onchange('service')
	#def _onchange_service(self):
	#@api.onchange('nex_zone')
	#def _onchange_nex_zone(self):

	#	print 'jx'
	#	print 'On change Write date'
	#	print self.treatment.patient
	#	print self.treatment.patient.name 

	#	self.patient = self.treatment.patient.name

	#	print self.patient







	# Treatment (for Product)
	x_treatment = fields.Selection(
			selection=prodvars._treatment_list,
			string="Tratamiento", 			
		)	




	# Zone 
	zone = fields.Selection(
			selection = prodvars._zone_list, 
			string="Zona", 
		)

	nex_zone = fields.Many2one(
			'openhealth.zone',
			string="Nex Zone", 
		)




	# Pathology
	pathology = fields.Selection(
			selection = prodvars._pathology_list, 
			string="Patología", 
		)

	nex_pathology = fields.Many2one(
			'openhealth.pathology',
			string="Nex Pathology", 
		)





	# Service 
	service = fields.Many2one(
			'product.template',

			domain = [
						('type', '=', 'service'),
					],

			string="Servicio",
			required=True, 
		)









	#_dic = {
	#			'Male':		'Masculino', 
	#			'Female':	'Femenino', 
	#			'none':		'Ninguno', 
	#			'one':			'', 
	#			'two':			'', 
	#			'three':			'', 
	#			'rejuvenation_capilar':			'Rejuvenecimiento capilar', 
	#			'body_local':					'Localizado cuerpo', 
	#			'':			'', 
	#		}

	#vspace = fields.Char(
	#		' ', 
	#		readonly=True
	#		)


	# Vertical space 
	vspace = fields.Char(
			' ', 
			readonly=True
			)





	# Name 
	name = fields.Char(
			default='SE',
			string='Servicio #',
			compute='_compute_name', 
			#required=True, 
			)

	@api.multi
	def _compute_name(self):
		for record in self:
			record.name = 'SE00' + str(record.id) 







	# Open Treatment
	@api.multi 
	def open_treatment(self):

		#print 
		#print 'Open Treatment'


		ret = self.treatment.open_myself()

		return ret 
	# open_treatment












	# Canonical 

	family = fields.Selection(
		string="Familia", 

		selection=prodvars._family_list,
		)	

	laser = fields.Selection(

			selection = prodvars._laser_type_list, 
			
			string="Láser", 			
			default='none',			
			#required=True, 
			index=True
			)












	sessions = fields.Selection(

			#selection = jxvars._pathology_list, 
			selection = prodvars._sessions_list, 
		
			string="Sesiones", 
			)






# ----------------------------------------------------------- Relationals ------------------------------------------------------



	cosmetology = fields.Many2one('openhealth.cosmetology',
			ondelete='cascade', 			
			string="Cosmiatría", 
			)





	# Consultation 
	consultation = fields.Many2one('openhealth.consultation',
			ondelete='cascade', 		
			string="Consulta", 
			
			required=False, 
			)









	# Commons 
	def clear_all(self,token):
		
		self.clear_commons()
		
		self.clear_local() 
		return token


		
	def clear_commons(self):	

		#self.zone = 'none'
		self.pathology = 'none'
		


	def clear_times(self,token):
		self.time = ''
		self.time_1 = 'none'		
		return token
		
		

		
		

	
	# Time 
	time = fields.Char(
			default='',
			string="Tiempo", 
	)
	


	time_1 = fields.Selection(
			selection = exc._time_list, 
			string="Tiempo", 
			default='none',	
			)



	@api.onchange('time_1')
	def _onchange_time_1(self):
	
		if self.time_1 != 'none':				
			self.time_1 = self.clear_times(self.time_1)
			self.time = self.time_1
			

			#serv_funcs.product(self)

			return {
				'domain': {'service': [('x_treatment', '=', self.laser),('x_zone', '=', self.zone),('x_pathology', '=', self.pathology),('x_time', '=', self.time)]},				
			}





	
	# Nr sessions
	
	nr_sessions = fields.Char(
			default='',	
	)
	
	
	nr_sessions_1 = fields.Selection(
			selection = ipl._nr_sessions_list, 
			string="Número de sesiones", 
			default='none',	
	)

	@api.onchange('nr_sessions_1')
	def _onchange_nr_sessions_1(self):
	
		if self.nr_sessions_1 != 'none':	
			self.nr_sessions = self.nr_sessions_1
			
			return {
				'domain': {'service': [('x_treatment', '=', self.laser),('x_zone', '=', self.zone),('x_pathology', '=', self.pathology),('x_time', '=', self.time),('x_sessions', '=', self.nr_sessions) ]},
			}
			



		

	# Service
	@api.onchange('service')
	def _onchange_service(self):
	
		if self.service != 'none':
			self.time_1 = self.service.x_time
		
			
































	# Code 
	code = fields.Char(
			compute='_compute_code', 
			string='Code'
			)

	@api.depends('service')
	def _compute_code(self):
		for record in self:
			record.code= record.service.name 






	# Name short 
	name_short = fields.Char(
			compute='_compute_name_short', 
			#string='Short name'
			#string='Código'
			#string='Código interno'
			)

	@api.depends('service')

	def _compute_name_short(self):
		for record in self:
			record.name_short = record.service.x_name_short 








	#Price 
	price = fields.Float(
			compute='_compute_price', 

			string='Precio Standard', 
		) 

	#@api.multi
	@api.depends('service')

	def _compute_price(self):
		for record in self:
			record.price= (record.service.list_price)





	# Price VIP
	price_vip = fields.Float(
			compute='_compute_price_vip', 
			
			string='Precio VIP', 
		) 

	#@api.multi
	@api.depends('service')

	def _compute_price_vip(self):
		for record in self:
			record.price_vip= (record.service.x_price_vip)








	# Other
			
	title = fields.Char(
			string='Title', 
			default='',
			readonly=True,
			)
	
	notebook_over = fields.Char(
			string='Over notebook', 
			default='',
			readonly=True,
			)






	# ---------------------------------------------- Open Line --------------------------------------------------------

	@api.multi
	def open_line_current(self): 

		service_id = self.id 

		return {
				'type': 'ir.actions.act_window',
				'name': ' Edit Service Current', 
				'view_type': 'form',
				'view_mode': 'form',
				'res_model': self._name,
				'res_id': service_id,
				'target': 'current',
				'flags': {
						'form': {'action_buttons': True, }
						},

				'context': {
				}
		}

	# open_line_current 

