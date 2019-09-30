# -*- coding: utf-8 -*-
"""
	Patient Report

	Created: 			25 Sep 2019
	Last mod: 			25 Sep 2019
"""
#from __future__ import print_function

from openerp import models, fields, api

from openerp.addons.openhealth.models.order import ord_vars

class patient_report(models.Model):
	"""
	Patient Report Class
	"""
	
	_name = 'openhealth.patient.report'

	_description = 'Openhealth Patient Report'

	#_inherit = 'openhealth.patient.report'



# ----------------------------------------------------------- Natives -------------------------------


	# Patient Handle
	patient_id = fields.Many2one(
			
			'oeh.medical.patient',
			
			string="Paciente",
			
			required=False,
			
			ondelete='cascade',  		# Ok
		)



	# Date
	date = fields.Datetime(
		'Fecha',
	)

	
	# Patient
	patient = fields.Many2one(
			'oeh.medical.patient',
			string='Paciente',
		)


	# Doctor
	doctor = fields.Many2one(
			'oeh.medical.physician',
			string="Médico",
		)



	# Product
	product = fields.Char(
			string="Pl - Producto",
		)


	# Family
	family = fields.Char(
			string="Familia",
		)


	# State
	state = fields.Selection(
			selection=ord_vars._state_list,
			string='Estado',
		)



	# Res Handles

	res_id = fields.Integer()

	res_model = fields.Char()


#----------------------------------------------------------- Quick Button ---------
	@api.multi
	def open_line_current(self):
		"""
		# Quick access Button
		"""
		
		res_id = self.res_id
		res_model = self.res_model

		return {
				'type': 'ir.actions.act_window',
				'name': ' Edit Order Current',
				'view_type': 'form',
				'view_mode': 'form',


				#'res_model': 'sale.order',
				'res_model': res_model,
				'res_id': res_id,
				

				'target': 'current',
				'flags': {
						#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
						'form': {'action_buttons': True, }
						},
				'context': {}
		}
