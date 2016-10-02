# -*- coding: utf-8 -*-
#
# 	Consultation 
# 
# Created: 				20 Sep 2016
# Last updated: 	 	20 Sep 2016

from openerp import models, fields, api
from datetime import datetime





class Service(models.Model):
	_name = 'openhealth.service'


	# Name 
	name = fields.Char(
			#default='Laser Co2',
			#string='Name',
			#string='Nombre',



			default='SE',
			string='Servicio #',

			compute='_compute_name', 
			required=True, 
			)

	@api.multi
	def _compute_name(self):
		for record in self:
			#record.name = 'SE0000' + str(record.id) 
			record.name = 'SE00' + str(record.id) 





	# Consultation 
	consultation = fields.Many2one('openhealth.consultation',
			ondelete='cascade', 
			#string="Treatment", 
			string="Consulta", 
			)

	# Quotation 
	quotation = fields.Many2one('openhealth.quotation',
			ondelete='cascade', 
			#string="Treatment", 
			string="Quotation", 
			)







	# Service 
	service = fields.Many2one(
			'product.template',
			#domain = [
			#			('type', '=', 'service'),
			#			('x_treatment', '=', _jx_laser_type),
			#		],
			#string="Service", 
			string="Servicio", 
			)


	# Treatment 
	treatment_id = fields.Many2one('openextension.treatment',
			ondelete='cascade', 
			#string="Treatment", 
			string="Tratamiento", 
			)



	#required=True,





	# Laser type 
	_laser_type_list = [
			('laser_co2','Laser Co2'), 
			('laser_excilite','Laser Excilite'), 
			('laser_ipl','Laser Ipl'), 
			('laser_ndyag','Laser Ndyag'), 
			]

	laser = fields.Selection(
			selection = _laser_type_list, 
			#string="Tratamiento", 
			string="Tipo", 
			default='laser_co2',
			required=True, 
			index=True
			)


	def get_domain_service(self,cr,uid,ids,context=None):

		#print context

		#return {
		#	'warning': {
		#		'title': "Laser",
		#		'message': context,
		#}}

		mach = []
		lids = self.pool.get('product.template').search(cr,uid,[
																('x_treatment', '=', context)
																])
		return {'domain':{'service':[('id','in',lids)]}}





	# Zone
	_zone_list = [
			('areola','Areola'), 
			('armpits','Axilas'), 
			('beard','Barba'), 
			('belly','Abdomen'), 
			('bikini','Bikini'), 

			('down_lip','Bozo/Bigote'), 
			('arm','Brazo'), 
			('head','Cabeza'), 
			('neck','Cuello'), 
			('back','Espalda'), 

			('front','Frente'), 
			('gluteus','Glúteo'), 
			('shoulders','Hombros'), 
			('linea_alba','Linea Alba'), 
			('body_localized','Localizado cuerpo'), 

			('face_localized','Localizado rostro'), 
			('hands','Manos'), 
			('chin','Mentón'), 
			('nape','Nuca'), 
			('sideburns','Patillas'), 

			('breast','Pecho'), 
			('feet','Pierna'), 
			('leg','Pierna'), 
			('cheekbones','Pómulos'), 
			('face_all','Todo rostro'), 

			('nail','Uña'), 
			('vagina','Vagina'), 
			]

	zone = fields.Selection(
			selection = _zone_list, 
			string="Zona", 
			default='areola',
			required=True, 
			)



	# Pathology
	_pathology_list = [

			('acne_active','Acné Activo'),
			('acne_sequels','Acné y Secuelas'),
			('acne_sequels_1','Acné y Secuelas Grado 1'),
			('acne_sequels_2','Acné y Secuelas Grado 2'),
			('acne_sequels_3','Acné y Secuelas Grado 3'),

			('alopecia','Alopecias'),
			('cyst','Quiste'),
			('depilation','Depilacion'),
			('emangiomas','Hemangiomas'),
			('keratosis','Queratosis'),
			
			
			('keratosis_1','Queratosis Grado 1'),
			('keratosis_2','Queratosis Grado 2'),
			('keratosis_3','Queratosis Grado 3'),
			('mole_1','Lunar Pequeño'),
			('mole_2','Lunar Mediano'),

			('mole_3','Lunar Grande'),
			('monalisa_touch','Monalisa Touch'),
			('polyp','Pólipo'),
			('psoriasis','Psoriasis'),
			('rejuvenation_facial','Rejuvenecimiento Facial'),


			('rejuvenation_hands','Rejuvenecimiento en manos'),
			('rejuvenation_neck','Rejuvenecimiento en cuello'),
			('rejuvenation_face_1','Rejuvenecimiento Facial Grado 1'),
			('rejuvenation_face_2','Rejuvenecimiento Facial Grado 2'),
			('rejuvenation_face_3','Rejuvenecimiento Facial Grado 3'),

			('rejuvenation_face_neck','Rejuvenecimiento Facial + Rejuvenecimiento en Cuello'),
			('rejuvenation_face_hands','Rejuvenecimiento Facial + Rejuvenecimiento en Manos'),
			('rejuvenation_face_neck_hands','Rejuvenecimiento Facial + Rejuvenecimiento en Cuello + Rejuvenecimiento en Manos'),
			('rosacea','Rosácea'),
			('ruby_point','Punto rubí'),


			('ruby_points','Puntos Rubi'),
			('scar','Cicatriz'),
			('scar_1','Cicatriz Pequeño'),
			('scar_2','Cicatriz Mediano'),
			('scar_3','Cicatriz Grande'),

			('stains','Manchas'),
			('stains_1','Manchas Grado 1'),
			('stains_2','Manchas Grado 2'),
			('stains_3','Manchas Grado 3'),
			('telangiectasia','Telangectacias'),


			('varices','Varices'),
			('vitiligo','Vitiligo'),
			('wart','Verruga'),


			]

	pathology = fields.Selection(
			selection = _pathology_list, 
			string="Patología", 
			default='acne_active',
			required=True, 
			)







	#def get_domain_service_zone(self,cr,uid,ids,context=None):
	#def get_domain_service_multi(self,cr,uid,ids,context_1=None,context_2=None):
	def get_domain_service_multi(self,cr,uid,ids,context_1=None,context_2=None,context_3=None):

		#print context
		print 'jx'
		print context_1, context_2, context_3
		print 'jx'

		#return {
		#	'warning': {
		#		'title': "Zone domain",
		#		'message': context_1 + ' ' + context_2 + ' ' + context_3,
		#}}



		mach = []
		lids = self.pool.get('product.template').search(cr,uid,[
																	('x_treatment', '=', 	context_1), 
																	('x_zone', '=', 		context_2), 
																	('x_pathology', '=', 	context_3), 
																])
		return {'domain':{'service':[('id','in',lids)]}}






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
			string='Código interno'
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






	#------------------------------------ Buttons -----------------------------------------
	#

	# Service - Quick Self Button 
	# ---------------------------------

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



