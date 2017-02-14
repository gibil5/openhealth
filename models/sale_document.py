# -*- coding: utf-8 -*-
#
# 	Sale document 
# 
#

from openerp import models, fields, api


class SaleDocument(models.Model):
	
	_name = 'openhealth.sale_document'

	#_inherit='sale.order'




	name = fields.Char(

			#string="Factura #", 

			#compute='_compute_name', 

			#required=True, 
		)





	patient = fields.Many2one(
			'oeh.medical.patient',
			string = "Paciente", 	
			required=True, 
		)


	doctor = fields.Many2one(
			'oeh.medical.physician',
			string = "Médico", 	
			required=True, 
			)


	#amount_total = fields.Monetary(
	#amount_total = fields.Integer(
	#total = fields.Char(
	
	total = fields.Float(
			string = 'Total', 
		)





	order = fields.Many2one(
			'sale.order',
			string="Presupuesto",
			ondelete='cascade', 
			required=True, 
		)

