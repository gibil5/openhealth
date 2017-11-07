# -*- coding: utf-8 -*-
#
# 	sale_note 
# 
#
from openerp import models, fields, api

class SaleNote(models.Model):
	
	_name = 'openhealth.sale_note'

	_inherit='openhealth.sale_proof'



	name = fields.Char(
			string="CANJE NV #", 
		)


	family = fields.Selection(
			default='sale_note', 
		)



	# ----------------------------------------------------------- CRUD ------------------------------------------------------

 	# Create 
	@api.model
	def create(self,vals):

		#print 
		#print 'Create Override'
		#print 
		#print vals
		#print 
	
		counter = self.env['openhealth.counter'].search([('name', '=', 'sale_note')])		
		counter.increase()


		#Write your logic here
		res = super(SaleNote, self).create(vals)
		#Write your logic here

		return res

