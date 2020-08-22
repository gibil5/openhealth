# -*- coding: utf-8 -*-
"""
	*** Image

		Created: 			21 Jun 2017
		Last up: 	 		22 Aug 2020
"""
from openerp import models, fields, api

class Image(models.Model):
	_inherit = 'base_multi_image.image'

# ----------------------------------------------------------- Fields -----------
	# Type
	xtype = fields.Selection(
		[
			('consultation', 	'Consulta'),
			('session', 		'Sesión'), 
			('control', 		'Control'),
			#('procedure', 		'Procedimiento'),
			],
		default='control', 
		string='Tipo', 		
		required=True, 
	)

	# Origin
	origin = fields.Selection(
		[
			('visia', 			'Visia'),
			('camera', 			'Cámara'), 
			('echography', 		'Ecógrafo'),
			],
		default='visia', 
		string='Orígen',
		required=True, 
	)

	# Unique name
	name_id = fields.Char(
		'Nombre unico', 
		required=True,			
		compute='_compute_name_id', 
	)

	@api.multi
	#@api.depends('state')
	def _compute_name_id(self):
		for record in self:
			nid = 'jx'
			control = record.env['openhealth.control'].search([
																('id', '=', record.owner_id), 
															],
															#order='appointment_date desc'
															limit=1,)

			if record.name != False  and  control.patient.name != False and control.evaluation_start_date != False :
				nid = control.patient.name + '_' + control.evaluation_start_date + '_' + record.name
				record.name_id = nid


	# Name 	
	name = fields.Char(
		required=True,
		string='Nombre',
		translate=True)

	# Storage 
	storage = fields.Selection(
		[
			('url', 'URL'),
			('file', 'OS file'), 
			('db', 'Database'),
			('filestore', 'Filestore'),
			],
		default='db',
		#string='Storage', 
		string='Almacenamiento', 
		required=True
		)

	# Extension 
	extension = fields.Char(
		#'File extension',
		'Extension',
		readonly=True)
