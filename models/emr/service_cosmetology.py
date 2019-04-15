# -*- coding: utf-8 -*-
"""
		Service Cosmetology

		Created: 				 1 Nov 2016
		Last: 				 	29 Nov 2018
"""
from openerp import models, fields, api
from . import prodvars
from . import cosvars

class ServiceCosmetology(models.Model):
	"""
	high level support for doing this and that.
	"""
	_name = 'openhealth.service.cosmetology'

	_inherit = 'openhealth.service'




# ----------------------------------------------------------- Natives ------------------------------

	# Service
	service = fields.Many2one(
			'product.template',
			domain=[
						('x_family', '=', 'cosmetology'),
					],
		)




# ----------------------------------------------------------- Canonicals --------------------------
	# Laser
	laser = fields.Selection(
			#selection=prodvars._laser_type_list,
			selection=prodvars.get_laser_type_list(),
			string="Láser",
			default='cosmetology',
			index=True,
		)



	time_1 = fields.Selection(
			#selection=prodvars._time_list,
			selection=prodvars.get_time_list(),
			string="Tiempo",
			default='none',
		)




	# Criosurgery
	cos_dia = fields.Selection(
			#selection=cosvars._cos_dia_list,
			selection=cosvars.get_cos_dia_list(),
			default='none',
			string="Rostro (Limpieza facial profunda)",
		)


	# Carboxytherapy
	cos_car_fac = fields.Selection(
			#selection=cosvars._cos_car_list,
			selection=cosvars.get_cos_car_list(),
			default='none',
			string="Rostro",
			)

	cos_car_bod = fields.Selection(
			#selection=cosvars._cos_car_list(),
			selection=cosvars.get_cos_car_list(),
			default='none',
			string="Cuerpo",
			)

	# Laser Triactive
	cos_tri_fac = fields.Selection(
			#selection=cosvars._cos_tri_list,
			selection=cosvars.get_cos_tri_list(),
			default='none',
			string="Rostro, Papada y Cuello",
			)

	cos_tri_bod = fields.Selection(
			#selection=cosvars._cos_tri_list,
			selection=cosvars.get_cos_tri_list(),
			default='none',
			string="Todo Cuerpo",
			)




# ----------------------------------------------------------- Actions ---------------------------

	@api.multi
	def open_cosmetology(self):
		"""
		high level support for doing this and that.
		"""
		ret = self.cosmetology.open_myself()
		return ret


	def clear_all_med(self, token):
		"""
		high level support for doing this and that.
		"""
		self.clear_local_cos()
		return token


	def clear_local_cos(self):
		"""
		high level support for doing this and that.
		"""
		self.cos_dia = 'none'
		self.cos_car = 'none'
		self.cos_tri = 'none'



# ----------------------------------------------------------- On Changes --------------------------

	# Diamond
	@api.onchange('cos_dia')
	def _onchange_cos_dia(self):
		if self.cos_dia != 'none':
			self.cos_dia = self.clear_all_med(self.cos_dia)
			self.x_treatment = 'diamond_tip'
			self.zone = 'face'
			self.pathology = 'deep_face_cleansing'
			self.time = '30 min'
			self.sessions = self.cos_dia
			return {
				'domain': {'service': [
										('x_treatment', '=', self.x_treatment),
										('x_sessions', '=', self.sessions),
										]},
			}


	# Carboxytherapy - Face
	@api.onchange('cos_car_fac')
	def _onchange_cos_car_fac(self):
		if self.cos_car_fac != 'none':
			self.cos_car_fac = self.clear_all_med(self.cos_car_fac)
			self.x_treatment = 'carboxytherapy'
			self.zone = 'face'
			self.pathology = 'rejuvenation_face'
			self.time = '30 min'
			self.sessions = self.cos_car_fac
			return {
				'domain': {'service': [
										('x_treatment', '=', self.x_treatment),
										('x_zone', '=', self.zone),
										('x_sessions', '=', self.sessions),
										]},
			}


	# Carboxytherapy - Body
	@api.onchange('cos_car_bod')
	def _onchange_cos_car_bod(self):
		if self.cos_car_bod != 'none':
			self.cos_car_bod = self.clear_all_med(self.cos_car_bod)
			self.x_treatment = 'carboxytherapy'
			self.zone = 'body'
			self.pathology = 'rejuvenation_face'
			self.time = '30 min'
			self.sessions = self.cos_car_bod
			return {
				'domain': {'service': [
										('x_treatment', '=', self.x_treatment),
										('x_zone', '=', self.zone),
										('x_sessions', '=', self.sessions),

										]},
			}


	# Laser Triactive - Face
	@api.onchange('cos_tri_fac')
	def _onchange_cos_tri_fac(self):
		if self.cos_tri_fac != 'none':
			self.cos_tri_fac = self.clear_all_med(self.cos_tri_fac)
			self.x_treatment = 'triactive_carboxytherapy'
			self.zone = 'face_doublechin_neck'
			self.pathology = 'reaffirmation'
			self.time = '30 min'
			self.sessions = self.cos_tri_fac
			return {
				'domain': {'service': [
										('x_treatment', '=', self.x_treatment),

										('x_zone', '=', self.zone),

										('x_sessions', '=', self.sessions),
										]},
			}


	# Laser Triactive - Body
	@api.onchange('cos_tri_bod')
	def _onchange_cos_tri_bod(self):
		if self.cos_tri_bod != 'none':
			self.cos_tri_bod = self.clear_all_med(self.cos_tri_bod)
			self.x_treatment = 'triactive_carboxytherapy_reductionchamber'
			self.zone = 'body_all'
			self.pathology = 'reduction_weight_measures'
			self.time = '30 min'
			self.sessions = self.cos_tri_bod
			return {
						'domain': {'service': [
												('x_treatment', '=', self.x_treatment),
												('x_zone', '=', self.zone),
												('x_sessions', '=', self.sessions),
										]},
			}
