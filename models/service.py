# -*- coding: utf-8 -*-
#
# 	Service 
# 
# Created: 				20 Sep 2016
# Last updated: 	 	 5 Jul 2018
#

from openerp import models, fields, api
from datetime import datetime
from . import prodvars
from . import serv_funcs
from . import ipl

#from . import serv_vars
#from . import exc


class Service(models.Model):

	_name = 'openhealth.service'

	#_inherit = 'openhealth.base', 



# ----------------------------------------------------------- Tmp ------------------------------------------------------

	x_time = fields.Char()

	


# ----------------------------------------------------------- Prices ------------------------------------------------------

	# Price 
	price = fields.Float(
			#string='Precio Standard', 
			string='Precio', 

			compute='_compute_price', 
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



	# Price Manual 
	price_manual = fields.Float(

			string="Precio Manual",
		)



	# Price Applied
	price_applied = fields.Float(
			#string='Precio Aplicado', 
			#compute='_compute_price_applied', 
		) 




# ----------------------------------------------------------- Primitives ------------------------------------------------------

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




	# State 
	state = fields.Selection(
			[
				('draft', 		'Inicio'),			
				('budget', 		'Presupuestado'),	
			], 
			#selection = serv_vars._state_list, 
			string='Estado', 			
			default = 'draft', 
		)




	# Family 
	family = fields.Selection(
			string="Familia", 
			selection=prodvars._family_list,
		)	


	# Laser 
	laser = fields.Selection(
			selection = prodvars._laser_type_list, 
			string="Láser", 			
			default='none',			
			#required=True, 
			index=True
		)


	# Sessions 
	sessions = fields.Selection(
			#selection = jxvars._pathology_list, 
			selection = prodvars._sessions_list, 
			string="Sesiones", 
		)




	# Comeback 
	comeback = fields.Boolean(
			string='Regreso', 			
		)


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



	# Pathology
	pathology = fields.Selection(
			selection = prodvars._pathology_list, 
			string="Patología", 
		)


	# Vertical space 
	vspace = fields.Char(
			' ', 
			readonly=True
		)


	
	# Time 
	time = fields.Char(
			default='',
			string="Tiempo", 
		)
	


	_time_list = [
					('15 min','15 min'),	
					('30 min','30 min'),
					('none',''),
		]

	time_1 = fields.Selection(

			#selection = exc._time_list, 
			selection = _time_list, 

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






	# Title 
	title = fields.Char(
			string='Title', 
			default='',
			readonly=True,
		)
	
	# Over notebook
	notebook_over = fields.Char(
			string='Over notebook', 
			default='',
			readonly=True,
		)




# ----------------------------------------------------------- Deprecated ------------------------------------------------------

	# Cosmetology 
	#cosmetology = fields.Many2one('openhealth.cosmetology',
	#		ondelete='cascade', 			
	#		string="Cosmiatría", 
	#	)


	# Consultation 
	#consultation = fields.Many2one('openhealth.consultation',
	#		ondelete='cascade', 		
	#		string="Consulta", 		
	#		required=False, 
	#	)




# ----------------------------------------------------------- Relationals ------------------------------------------------------

	# Patient 
	patient = fields.Many2one(
			'oeh.medical.patient', 
			'Paciente', 
		)


	# Physician
	physician = fields.Many2one(
			'oeh.medical.physician',
			string="Médico",
			index=True
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



	# Treatement 
	treatment = fields.Many2one('openhealth.treatment',
			ondelete='cascade', 			
			string="Tratamiento", 
			readonly=True, 
			
			required = True, 
		)


	 # Nex zone
	nex_zone = fields.Many2one(
			'openhealth.zone',
			string="Nex Zone", 
		)


	# Nex Pathology 
	nex_pathology = fields.Many2one(
			'openhealth.pathology',
			string="Nex Pathology", 
		)




# ----------------------------------------------------------- Nr ofs ------------------------------------------------------

	#nr_hands = fields.Integer(
	nr_hands_i = fields.Integer(
			'hands', 
			#default=0, 

			#required=True,
			required=False,
		)

	#nr_body_local = fields.Integer(
	nr_body_local_i = fields.Integer(
			'body local', 
			#default = 0, 
			
			#required=True,
			required=False,
		)


	#nr_face_local = fields.Integer(
	nr_face_local_i = fields.Integer(
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





# ----------------------------------------------------------- Actions ------------------------------------------------------

	# Open Treatment
	@api.multi 
	def open_treatment(self):
		
		#print 
		#print 'Open Treatment'
		ret = self.treatment.open_myself()
		return ret 
	# open_treatment



	# Clear all
	def clear_all(self,token):		
		self.clear_commons()
		self.clear_local() 
		return token

	# Clear commons
	def clear_commons(self):	
		#self.zone = 'none'
		self.pathology = 'none'

	# Clear times
	def clear_times(self,token):
		self.time = ''
		self.time_1 = 'none'		
		return token
		

	

# ---------------------------------------------- Open Line --------------------------------------------------------

	# Open Line 
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


