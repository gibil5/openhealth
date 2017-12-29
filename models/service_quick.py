# -*- coding: utf-8 -*-
#
# 	Service Quick 
# 

from openerp import models, fields, api
from datetime import datetime
from . import service_quick_vars
from . import serv_funcs
from . import prodvars




class ServiceQuick(models.Model):

	_inherit = 'openhealth.service'

	_name = 'openhealth.service.quick'

	



	# Get Nr Zones 
	@api.multi
	def get_nr_zones(self, zone): 

		if zone == 'hands':
			nr = self.patient.x_nr_quick_hands

		elif zone == 'body_local':
			nr = self.patient.x_nr_quick_body_local

		elif zone == 'face_local':
			nr = self.patient.x_nr_quick_face_local

		elif zone == 'cheekbones':
			nr = self.patient.x_nr_quick_cheekbones

		elif zone == 'face_all':
			nr = self.patient.x_nr_quick_face_all

		elif zone == 'face_all_hands':
			nr = self.patient.x_nr_quick_face_all_hands

		elif zone == 'face_all_neck':
			nr = self.patient.x_nr_quick_face_all_neck

		elif zone == 'neck':
			nr = self.patient.x_nr_quick_neck

		else:
			print 'Error: This should not happen !'
			nr = -1



		return nr 






	# Comeback 
	comeback = fields.Boolean(
			string='Regreso', 
			
			compute='_compute_comeback', 
		)


	@api.multi

	def _compute_comeback(self):

		for record in self:

			zone = record.zone			
			nr = record.get_nr_zones(zone)

			if nr > 1:
				comeback = True
			else:
				comeback = False


			record.comeback = comeback













	# Patient 
	patient = fields.Many2one(
			'oeh.medical.patient', 

			string="", 

			required=True, 


			#compute='_compute_patient', 
		)

	#@api.multi
	#def _compute_patient(self):
	#	print 'jx'
	#	print 'compute patient'
	#	for record in self:
	#		record.patient = record.treatment.patient









	# Zone 
	nex_zone = fields.Many2one(
			'openhealth.zone',
			string="Nex Zone", 

			domain = [
						#('categ', '=', 'laser_quick'),
						('treatment', '=', 'laser_quick'),
					],
		)


	@api.onchange('nex_zone')
	def _onchange_nex_zone(self):

		if self.nex_zone != False:	

			self.zone = self.nex_zone.name_short


			#if self.nex_zone == 'body_local': 


			return {

				'domain': {		
								'service': 	[
												('x_treatment', '=', 'laser_quick'),
												('x_zone', '=', self.zone),
											], 

								'nex_pathology': [
													#('body_local', '=', True),
													(self.nex_zone.name_short, '=', True),
												], 
						},
				}









	# Pathology
	nex_pathology = fields.Many2one(
			'openhealth.pathology',
			string="Nex Pathology", 

			domain = [
						('treatment', '=', 'laser_quick'),
					],
		)



	@api.onchange('nex_pathology')

	def _onchange_nex_pathology(self):

		if self.nex_pathology != False:	

			self.pathology = self.nex_pathology.name_short

			return {
						'domain': {'service': [
												('x_treatment', '=', 'laser_quick'),
												('x_pathology', '=', self.pathology),
												('x_zone', '=', self.zone)			
										]},
			}



















	# Service 
	service = fields.Many2one(

			'product.template',

			default = 'QUICKLASER - Cuello - Rejuvenecimiento Cuello - 1', 

			domain = [
						('type', '=', 'service'),
						('x_treatment', '=', 'laser_quick'),
					],
	)
	



	# Treatment 
	x_treatment = fields.Selection(
			selection=prodvars._treatment_list,
			string="Tratamiento", 

			default="laser_quick", 			
		)	





	# Service
	@api.onchange('service')
	def _onchange_service(self):
		print 'jx'

		#if self.service != 'none':
		#	self.time_1 = self.service.x_time
		



# ---------------------------------------------- Zones --------------------------------------------------------

	# Neck  
	#neck_rejuvenation = fields.Selection(
	quick_neck_rejuvenation = fields.Selection(
			selection = service_quick_vars._rejuvenation_4_list, 
		
			string="Rejuvenecimiento", 
		
			default='none',	
		)


	# Neck Hands 
	#neck_hands_rejuvenation = fields.Selection(
	quick_neck_hands_rejuvenation = fields.Selection(

			selection = service_quick_vars._rejuvenation_2_list, 
		
			string="Rejuvenecimiento", 
		
			default='none',	
		)









