# -*- coding: utf-8 -*-
"""
		Service Cosmetology

		Created: 				 1 Nov 2016
		Last: 				 	29 Nov 2018
		24 Apr 2019:			Cleanup after 2019 PL. Must disappear:
								- Onchanges. 
"""
from openerp import models, fields, api
from . import cosvars

from openerp.addons.openhealth.models.product import prodvars


class ServiceCosmetology(models.Model):
	"""
	high level support for doing this and that.
	"""
	_name = 'openhealth.service.cosmetology'

	_inherit = 'openhealth.service'



# ----------------------------------------------------------- Dep ------------------------------
	#cos_tri_fac = fields.Char()

	time_1 = fields.Char()

	# Criosurgery
	cos_dia = fields.Char()

	# Carboxytherapy
	cos_car_fac = fields.Char()

	cos_car_bod = fields.Char()

	# Laser Triactive
	cos_tri_fac = fields.Char()

	cos_tri_bod = fields.Char()



# ----------------------------------------------------------- Natives ------------------------------
	service = fields.Many2one(
			'product.template',
			domain=[
						('x_family', '=', 'cosmetology'),
					],
		)


# ---------------------------------------------- Default --------------------------------------------------------
	# Laser
	laser = fields.Selection(
			#selection=prodvars._laser_type_list,
			selection=prodvars.get_laser_type_list(),
			string="Láser",
			default='cosmetology',
			index=True,
		)
