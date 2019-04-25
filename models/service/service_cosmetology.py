# -*- coding: utf-8 -*-
"""
		Service Cosmetology

		Created: 				 1 Nov 2016
		Last: 				 	29 Nov 2018
		24 Apr 2019:			Cleanup after 2019 PL. Must disappear:
								- Onchanges. 
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
