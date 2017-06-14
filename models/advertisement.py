# -*- coding: utf-8 -*-
#
# 	Advertisement 
# 
#
from openerp import models, fields, api

class Advertisement(models.Model):
	
	_name = 'openhealth.advertisement'

	_inherit='openhealth.sale_proof'



	name = fields.Char(
			string="Canje #", 
		)

	family = fields.Char(
			default='advertisement', 
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
	
		counter = self.env['openhealth.counter'].search([('name', '=', 'advertisement')])		
		counter.increase()


		#Write your logic here
		res = super(Advertisement, self).create(vals)
		#Write your logic here

		return res

		