# -*- coding: utf-8 -*-
"""
	Service Quick 

	Last up:	27 Aug 2019

	Deprecated: 
		- Computes
		- Nex Zone and Pathology
		- Tests
"""
from openerp import models, fields, api
from datetime import datetime

from . import vars_quick

from openerp.addons.openhealth.models.product import prodvars

class ServiceQuick(models.Model):

	_inherit = 'openhealth.service'

	_name = 'openhealth.service.quick'


# ----------------------------------------------------------- Natives ------------------------------
	# Service 
	service = fields.Many2one(
			'product.template',
			default = 'QUICKLASER - Cuello - Rejuvenecimiento Cuello - 1', 
			domain = [
						('type', '=', 'service'),
						('x_treatment', '=', 'laser_quick'),
					],
	)


# ---------------------------------------------- Fields --------------------------------------------------------

	price_applied = fields.Float()

	price_vip_return = fields.Float()

	comeback = fields.Boolean()



# ---------------------------------------------- Default --------------------------------------------------------
	# Laser 
	laser = fields.Selection(
			selection = prodvars._laser_type_list, 
			string="Láser", 				
			default='laser_quick',			
			#index=True,
		)


# ----------------------------------------------------------- Fields ------------------------------------------------------

	# Treatment 
	x_treatment = fields.Selection(
			selection=prodvars._treatment_list,
			string="Tratamiento", 
			default="laser_quick", 			
		)	

	# Neck  
	quick_neck_rejuvenation = fields.Selection(
			selection = vars_quick._rejuvenation_4_list, 
			string="Rejuvenecimiento", 
			default='none',	
		)

	# Neck Hands 
	quick_neck_hands_rejuvenation = fields.Selection(
			selection = vars_quick._rejuvenation_2_list, 
			string="Rejuvenecimiento", 
			default='none',	
		)

	patient = fields.Many2one(
			'oeh.medical.patient', 
			string="Paciente", 
		)

	physician = fields.Many2one(
			'oeh.medical.physician',
			string="Médico",
			index=True, 
		)
	


# ----------------------------------------------------------- Actions ------------------------------------------------------
	# Get Nr Zones 
	@api.multi
	def get_nr_zones(self, zone): 

		if zone == 'hands':
			nr = self.nr_hands_i

		elif zone == 'body_local':
			nr = self.nr_body_local_i

		elif zone == 'face_local':
			nr = self.nr_face_local_i

		elif zone == 'cheekbones':
			nr = self.nr_cheekbones

		elif zone == 'face_all':
			nr = self.nr_face_all

		elif zone == 'face_all_hands':
			nr = self.nr_face_all_hands

		elif zone == 'face_all_neck':
			nr = self.nr_face_all_neck

		elif zone == 'neck':
			nr = self.nr_neck

		elif zone == 'neck_hands':
			nr = self.nr_neck_hands

		else:
			#print 'Error: This should not happen !'
			nr = -1

		return nr 


