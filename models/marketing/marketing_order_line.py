# -*- coding: utf-8 -*-
"""
 	Marketing Order Line - Used by Marketing
 
 	Created: 				28 May 2018
 	Last up: 	 			29 Jun 2019
"""
from openerp import models, fields, api

class marketing_order_line(models.Model):

	_inherit='openhealth.line'

	_name = 'openhealth.marketing.order.line'

	_description = "Openhealth Marketing Order Line"


# ----------------------------------------------------------- Handles ------------------------------------------------------

	# Marketing Id
	marketing_id = fields.Many2one(			
			'openhealth.marketing',
			ondelete='cascade', 			
		)

	# Budget 
	#patient_line_budget_id = fields.Many2one(			
	#		'openhealth.patient.line',
	#		ondelete='cascade', 			
	#	)

	# Sale 
	#patient_line_sale_id = fields.Many2one(			
	#		'openhealth.patient.line',
	#		ondelete='cascade', 			
	#	)

	# Consu 
	patient_line_consu_id = fields.Many2one(			
			'openhealth.patient.line',
			ondelete='cascade', 			
		)

	# Product
	patient_line_product_id = fields.Many2one(			
			'openhealth.patient.line',
			ondelete='cascade', 			
		)

	# Proc
	#patient_line_proc_id = fields.Many2one(
	#		'openhealth.patient.line',
	#		ondelete='cascade', 			
	#	)

	# Patient Line - Vip
	patient_line_id = fields.Many2one(			
			'openhealth.patient.line',
			ondelete='cascade', 			
		)

	# Patient Line - Vip with card 
	patient_line_id_vip = fields.Many2one(
			'openhealth.patient.line',
			ondelete='cascade', 			
		)



# ----------------------------------------------------------- Inheritable ------------------------------------------------------

	# Doctor 
	doctor = fields.Many2one(
			'oeh.medical.physician',
			string = "Médico", 	
		)
