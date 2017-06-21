# -*- coding: utf-8 -*-
#
# 	*** Image  	
# 
# Created: 				 21 Jun 2017
# Last updated: 	 	 21 Jun 2017

from openerp import models, fields, api



class Image(models.Model):
	
	#_name = 'openhealth.control'

	_inherit = 'base_multi_image.image'




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
			nid = control.patient.name + '_' + control.evaluation_start_date + '_' + record.name   


			record.name_id = nid





	# Name 	
	_name_list = [
		('Frente', 'Frente'),
		('Izquierda', 'Izquierda'),
		('Derecha', 'Derecha'),
		]
	name = fields.Selection(
		selection=_name_list,
		required=True,
		#string='Image title',
		string='Nombre',
		translate=True)




	# Storage 
	storage = fields.Selection(
		[
			#('url', 'URL'),
			#('file', 'OS file'), 
			('db', 'Database'),
			#('filestore', 'Filestore'),
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



