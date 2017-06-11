# -*- coding: utf-8 -*-
#
# 	Receipt 
# 
#

from openerp import models, fields, api



class Receipt(models.Model):
	
	_name = 'openhealth.receipt'

	#_inherit='openhealth.sale_document'
	_inherit='openhealth.sale_proof'






	name = fields.Char(
			string="Boleta #", 
			required=True, 
			compute='_compute_name', 
			)

	#@api.depends()
	@api.multi

	def _compute_name(self):
		for record in self:

			#record.name = 'BO-' + str(record.id) 
			record.name = 'BO-1-' + record.counter.rjust(4, '0')






	# ----------------------------------------------------------- CRUD ------------------------------------------------------

 	#@api.model
	#def create(self, values):
	#	new_id = super(res_partner, self).create(vals)
	#	print values



	# Create 
	@api.model
	def create(self,vals):

		print 
		print 'jx'
		print 'Receipt - Create Override'
		print 
		print vals
		print 
	


		counter = self.env['openhealth.counter'].search([('name', 'like', 'receipt')])
		counter.increase()


		#Write your logic here
		res = super(Receipt, self).create(vals)
		#Write your logic here

		return res



