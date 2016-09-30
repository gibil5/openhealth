# -*- coding: utf-8 -*-
#
# 	Quotation 
# 

from openerp import models, fields, api
from datetime import datetime





#------------------------------------------------------------------------
class Quotation(models.Model):
	_name = 'openhealth.quotation'
	#_inherit = 'oeh.medical.evaluation'


	name = fields.Char(
			string = 'Presupuesto #',
			#string = 'Procedimiento #',
			)


	consultation = fields.Many2one('openhealth.consultation',
			ondelete='cascade', 
			)



	# Service 
	#service = fields.Many2one('product.template',
	service = fields.One2many('openhealth.service', 
			'quotation', 
			string="Service", 
			#compute='_compute_service', 
			#required=True, 
			)

	@api.multi

	def _compute_service(self):
		for record in self:
			record.service = record.consultation.service_ids 






	# ----------------------------- Services -----------------------------------


	# Laser 
	#_laser_type_list = [
	#		('laser_co2','Laser Co2'), 
	#		('laser_excilite','Laser Excilite'), 
	#		('laser_ipl','Laser Ipl'), 
	#		('laser_ndyag','Laser Ndyag'), 
	#		]

	#laser = fields.Selection(
	#		selection = _laser_type_list, 
	#		string="Tipo de Laser",  
	#		default='laser_co2',
	#		required=True, 
	#		index=True
	#		)



	# Name short 
	#code = fields.Char(
	#		compute='_compute_code', 
			#string='Short name'
	#		string='Código'
	#		)

	#@api.depends('service')

	#def _compute_code(self):
	#	for record in self:
	#		record.code = record.service.x_name_short 




	#Price 
	#price = fields.Float(
	#		compute='_compute_price', 
			#string='Price'
	#		string='Precio'
	#		) 

	#@api.multi
	#@api.depends('service')

	#def _compute_price(self):
	#	for record in self:
	#		record.price= (record.service.list_price)



	#def get_domain_service(self,cr,uid,ids,context=None):

		#print context

		#return {
		#	'warning': {
		#		'title': "Laser",
		#		'message': context,
		#}}

	#	mach = []
	#	lids = self.pool.get('product.template').search(cr,uid,[('x_treatment', '=', context)])
	#	return {'domain':{'service':[('id','in',lids)]}}


