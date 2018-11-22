# -*- coding: utf-8 -*-
#
# 	Service Quick 
# 
from openerp import models, fields, api
from datetime import datetime
import prodvars
import quick
class ServiceQuick(models.Model):
	_inherit = 'openhealth.service'
	_name = 'openhealth.service.quick'


# ---------------------------------------------- Prices --------------------------------------------------------
	
	# Price Applied
	price_applied = fields.Float(
			string='Precio Aplicado', 

			compute='_compute_price_applied', 
		) 

	#@api.multi
	@api.depends('service')
	def _compute_price_applied(self):
		for record in self:
			
			if record.patient.x_vip: 

				if record.comeback 		and 	record.service.x_price_vip_return != 0: 	# Return 
					record.price_applied = record.service.x_price_vip_return
				else:
					#record.price_applied = record.service.x_price_vip
					record.price_applied = -1 								# Std and Vip 
			
			else:
				#record.price_applied = record.service.list_price		# Std 
				record.price_applied = -1 								# Std and Vip 




# ---------------------------------------------- Default --------------------------------------------------------
	# Laser 
	laser = fields.Selection(
			selection = prodvars._laser_type_list, 
			string="Láser", 			
			
			#default='none',			
			default='laser_quick',			
			
			#required=True, 
			index=True,
		)


# ----------------------------------------------------------- Fields ------------------------------------------------------

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


	# Neck  
	quick_neck_rejuvenation = fields.Selection(
			selection = quick._rejuvenation_4_list, 
			#selection = _rejuvenation_4_list, 
			string="Rejuvenecimiento", 
			default='none',	
		)

	# Neck Hands 
	quick_neck_hands_rejuvenation = fields.Selection(
			selection = quick._rejuvenation_2_list, 
			#selection = _rejuvenation_2_list, 
			string="Rejuvenecimiento", 
			default='none',	
		)


	# Pathology
	nex_pathology = fields.Many2one(
			'openhealth.pathology',
			string="Nex Pathology", 
			domain = [
						('treatment', '=', 'laser_quick'),
					],
		)


	# Zone 
	nex_zone = fields.Many2one(
			'openhealth.nexzone',
			string="Nex Zone", 
			domain = [
						('treatment', '=', 'laser_quick'),
					],
		)


	# Patient 
	patient = fields.Many2one(
			'oeh.medical.patient', 
			string="Paciente", 
			#required=True, 
		)


	# Physician
	physician = fields.Many2one(
			'oeh.medical.physician',
			string="Médico",
			index=True, 
			#required=True, 
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


# ----------------------------------------------------------- Computes ------------------------------------------------------
	
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
			if nr > 0:
				comeback = True
			else:
				comeback = False
			record.comeback = comeback


	# Price Vip Return
	price_vip_return = fields.Float(
			string='Precio Vip Return', 

			compute='_compute_price_vip_return', 
		) 
	#@api.multi
	@api.depends('service')
	def _compute_price_vip_return(self):
		for record in self:
			record.price_vip_return= (record.service.x_price_vip_return)






# ----------------------------------------------------------- On Changes ------------------------------------------------------

	# Service
	@api.onchange('service')
	def _onchange_service(self):
		#print 'jx'
		pass

	@api.onchange('nex_zone')
	def _onchange_nex_zone(self):
		if self.nex_zone != False:	
			self.zone = self.nex_zone.name_short
			return {
						'domain': {		
									'service': 	[
													('x_treatment', '=', 'laser_quick'),
													('x_zone', '=', self.zone),
												], 
									'nex_pathology': [
														(self.nex_zone.name_short, '=', True),
													], 
									},
					}

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



# ----------------------------------------------------------- Test ------------------------------------------------------

	# Computes
	def test_computes(self):
		#print 
		#print 'Service Quick - Computes'

		super(ServiceQuick, self).test_computes()

		#print 
		#print 'comeback: ', self.comeback
		#print 'price_vip_return: ', self.price_vip_return
		#print 'price_applied: ', self.price_applied


	def test_actions(self):
		#print 
		#print 'Service Quick - Actions'

		super(ServiceQuick, self).test_actions()

		#print 
		#print 'nr_zones: ', self.get_nr_zones('token')






