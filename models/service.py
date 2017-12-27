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

	#_inherit = 'openhealth.base', 


	_name = 'openhealth.service'




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
			#selection = jxvars._laser_type_list, 

			#selection = service_vars._laser_type_list, 
			selection = prodvars._laser_type_list, 
			
			string="Láser", 			
			default='none',			
			#required=True, 
			index=True
			)




	x_treatment = fields.Selection(

			selection=prodvars._treatment_list,
			
			string="Tratamiento", 			
		)	








	sessions = fields.Selection(

			#selection = jxvars._pathology_list, 
			selection = prodvars._sessions_list, 
		
			string="Sesiones", 
			)






# ----------------------------------------------------------- Relationals ------------------------------------------------------

	# Treatement 
	treatment = fields.Many2one('openhealth.treatment',
			ondelete='cascade', 			
			string="Tratamiento", 
			readonly=True, 
			)


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
			#string='Price'
			string='Precio (S/.)'
			) 

	#@api.multi
	@api.depends('service')

	def _compute_price(self):
		for record in self:
			record.price= (record.service.list_price)






	# Price VIP
	price_vip = fields.Float(
			compute='_compute_price_vip', 
			#string='price_vip'
			string='Precio VIP (S/.)'
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



