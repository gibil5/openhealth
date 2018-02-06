# -*- coding: utf-8 -*-
#
# 	sale_note 
# 
from openerp import models, fields, api

class SaleNote(models.Model):
	
	_name = 'openhealth.sale_note'

	_inherit='openhealth.sale_proof'



	# ----------------------------------------------------------- Defaults ------------------------------------------------------
	@api.model
	def _get_default_serial_nr(self):

		print 'jx'
		print 'Get Default Serial Number - Sale Note'

		name = 'sale_note'
 		counter = self.env['openhealth.counter'].search([
																('name', '=', name), 
															],
																#order='write_date desc',
																limit=1,
														)
		default_serial_nr = '13'

		if counter.total != False: 
			default_serial_nr = counter.total
			counter.increase()

		return default_serial_nr


	# ----------------------------------------------------------- Primitives ------------------------------------------------------

	# Serial Number 
	serial_nr = fields.Char(
			default=_get_default_serial_nr, 
		)


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
	

		# Counter - Deprecated 
		#counter = self.env['openhealth.counter'].search([('name', '=', 'sale_note')])		
		#vals['serial_nr'] = counter.total
		#counter.increase()



		#Write your logic here
		res = super(SaleNote, self).create(vals)
		#Write your logic here

		return res

