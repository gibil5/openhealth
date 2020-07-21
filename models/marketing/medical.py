# -*- coding: utf-8 -*-
#
# 	Medical - Used by Marketing
# 
# Created: 				26 May 2018
#
from openerp import models, fields, api

#from emr import prodvars
from openerp.addons.openhealth.models.product import prodvars


class Medical(models.Model):	
	_name = 'openhealth.medical'
	#_order = 'date_create asc'



# ----------------------------------------------------------- Primitive ------------------------------------------------------

	# Date Created 
	x_date_created = fields.Datetime(
			string='Fecha', 
		)


	# Patient 
	patient = fields.Many2one(
			'oeh.medical.patient', 
			string="Paciente", 
		)


	# Doctor 
	doctor = fields.Many2one(
			'oeh.medical.physician',
			string = "Médico", 	
		)



	# Product
	product_id = fields.Many2one(

			#'product.product', 
			'product.template', 
			
			string='Producto', 
			domain=[('sale_ok', '=', True)], 
			change_default=True, 
			ondelete='restrict', 
			required=True, 
		)


	# Sub Family
	#x_treatment = fields.Selection(
	sub_family = fields.Selection(
			selection=prodvars._treatment_list,
			required=False, 
		)	



