# -*- coding: utf-8 -*-
"""
	Patient Origin

	Created: 			21 Nov 2019
	Last mod: 			21 Nov 2019
"""

from openerp import models, fields, api
from openerp.addons.openhealth.models.order import ord_vars

class PatientOrigin(models.Model):
	"""
	Patient Origin Class
	"""

	_name = 'openhealth.patient.origin'

	_description = 'Openhealth Patient Origin'



# ----------------------------------------------- Fields --------------------------------

	# Name
	name = fields.Char(
			string='Nombre',
			
			compute="_compute_name",
		)

	@api.multi
	def _compute_name(self):


		_dic_fam = {
					'tv': 	'TV',
					'social_networks': 	'Redes Sociales',
					'web': 				'Página web/Buscador',
					'recommendation': 	'Recomendación',
					'other': 			'Otros',
		}


		_dic_sub = {
					'two': '2',
					'four': '4',
					'nine': '9',

					'facebook': 	'Facebook',
					'instagram': 	'Instagram',
					'youtube': 		'Youtube',
					'twitter': 		'Twitter',

					'recommendation': 	'Recomendación',
					'other': 			'Otros',
		}


		se = '-'
		for record in self:


			if record.subfamily in _dic_sub:
				record.name = _dic_fam[record.family] + se + _dic_sub[record.subfamily]
			
			else:
				record.name = _dic_fam[record.family]



	# Family
	family = fields.Selection(
			[
				('tv', 				'TV'),
				('social_networks', 'Redes Sociales'),
				('web', 			'Página web/Buscador'),
				('recommendation', 	'Recomendación'),
				('other', 			'Otros'),
			],

			string='Familia',

			required=True,
		)



	# Subfamily
	subfamily = fields.Selection(
			[
				# Tv
				('two', 				'2'),
				('four', 				'4'),
				('nine', 				'9'),

				# Social networks
				('facebook', 	'Facebook'),
				('instagram', 	'Instagram'),
				('youtube', 	'Youtube'),
				('twitter', 	'Twitter'),
			],

			string='Sub-Familia',
		)

