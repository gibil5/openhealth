# -*- coding: utf-8 -*-
#
# 	Zones 
# 
# Created: 				26 Jan 2018
# 
from openerp import models, fields, api


class Zone(models.Model):
	_name = 'openhealth.zone'
	_order = 'name_short asc'

	name = fields.Char(
			string="Nombre", 
		)

	name_short = fields.Char(
		)

	treatment = fields.Selection(
			selection=[
							('laser_quick',		'Quick'), 
							('laser_co2',		'Co2'), 
							('laser_excilite',	'Excilite'), 
							('laser_ipl',		'ipl'), 
							('laser_ndyag',		'ndyag'), 
				],
		)



class ZoneQuick(models.Model):
	_inherit = 'openhealth.zone', 
	_name = 'openhealth.zone.quick'


class ZoneCo2(models.Model):
	_inherit = 'openhealth.zone', 
	_name = 'openhealth.zone.co2'


class ZoneExcilite(models.Model):
	_inherit = 'openhealth.zone', 
	_name = 'openhealth.zone.excilite'

class ZoneNdyag(models.Model):
	_inherit = 'openhealth.zone', 
	_name = 'openhealth.zone.ndyag'


class ZoneIpl(models.Model):
	_inherit = 'openhealth.zone', 
	_name = 'openhealth.zone.ipl'



