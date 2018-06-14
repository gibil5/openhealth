# -*- coding: utf-8 -*-
#
# 	Quotation 
# 

from openerp import models, fields, api
from datetime import datetime





#------------------------------------------------------------------------
class Quotation(models.Model):
	_name = 'openhealth.quotation'
	
	
	#_inherit = 'oeh.medical.evaluation'
	#_inherit = 'oeh.medical.quotation'
	#_inherit = 'oeh.medical.order'
	#_inherit = 'account.invoice'


	
	_inherit = 'sale.order'	
	#_inherit = 'openhealth.order'
	



	name = fields.Char(
			string = 'Presupuesto #',
			#string = 'Procedimiento #',
			)


	consultation = fields.Many2one('openhealth.consultation',
			ondelete='cascade', 
			)







	# Service 
	#service = fields.One2many('openhealth.service', 
	#		'quotation', 
	#		string="Service", 
			#compute='_compute_service', 
			#required=True, 
	#		)

	#@api.multi

	#def _compute_service(self):
	#	for record in self:
	#		record.service = record.consultation.service_ids 





