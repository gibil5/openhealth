# -*- coding: utf-8 -*-
#
#
# 		*** OPEN HEALTH - Card 
# 
# Created: 				25 Aug 2017
# Last mod: 			16 Jun 2018
#
from datetime import datetime
from openerp import models, fields, api

#from . import count_funcs
#from libs import count_funcs
from openerp.addons.openhealth.models.libs import count_funcs


class Card(models.Model):

	_name = 'openhealth.card'		

	_order = 'name desc'





# ----------------------------------------------------------- Primitives ------------------------------------------------------


	active = fields.Boolean(
			string="Activa", 
			default=True, 
		)
	



# ----------------------------------------------------------- Defaults ------------------------------------------------------

	@api.model
	def _get_default_name(self):

		name_ctr = 'vip'
 		counter = self.env['openhealth.counter'].search([
																('name', '=', name_ctr), 
															],
																#order='write_date desc',
																limit=1,
															)

		name = count_funcs.get_name(self, counter.prefix, counter.separator, counter.padding, counter.value)

		counter.increase()

		return name





# ----------------------------------------------------------- Primitives ------------------------------------------------------

	# Name 
	name = fields.Char(		
			"Tarjeta Vip #", 

			default=_get_default_name, 

			#required=True, 
			required=False, 
		)





	date_created = fields.Date(
			"Fecha de Creación",

			default = fields.Date.today, 
			#readonly = True, 
			required=True, 
		)


	patient_name = fields.Char(
			"Paciente nombre",
			
			default = "", 
			#readonly=True
			required=True, 
			)







	categ_id = fields.Many2one(
			'product.category',
			string="Categoria",
		)




	patient = fields.Many2one(
			'oeh.medical.patient',
			"Paciente", 	
			#required=True, 
			compute='_compute_patient', 

			#store=True, 
		)


	#@api.multi
	@api.depends('patient_name')

	def _compute_patient(self):
		for record in self:

			patient = record.env['oeh.medical.patient'].search([
															#('name','like', record.patient.name),
															#('name','like', record.patient),
															('name','=', record.patient_name),
														],
														#order='appointment_date desc',
														limit=1,)

			record.patient = patient

	# 









	partner_id = fields.Many2one(
			'res.partner',
			string = "Cliente", 	
			#required=True, 
			compute='_compute_partner_id', 
		)


	#@api.multi
	@api.depends('patient_name')

	def _compute_partner_id(self):
		#print 'jx'
		#print 'compute partner_id'

		for record in self:

			partner_id = record.env['res.partner'].search([
															#('name','like', record.patient.name),
															#('name','like', record.patient),
															('name','=', record.patient_name),
														],
														#order='appointment_date desc',
														limit=1,)

			record.partner_id = partner_id


			pl = record.env['product.pricelist'].search([
																('name','=', 'VIP'),
															],
															#order='appointment_date desc',
															limit=1,)

			#print pl 
			#print pl.id



			#partner_id.property_product_pricelist = pl
			#print partner_id.property_product_pricelist.name 


			#partner_id.save 
	# 







	date_product = fields.Date(
			string = "Fecha de Servicio",
			default = fields.Date.today, 
			#readonly = True, 
			#required=True, 
			required=False, 
		)

	product = fields.Char(
			string = "Servicio",
			default = "", 
			#readonly=True
			#required=True, 
			required=False, 
			)

	days_after = fields.Integer(
			string = "Días después",
			default = 0, 
			#readonly=True
			#required=True, 
			required=False, 
			)



	vspace = fields.Char(
			' ', 
			readonly=True
		)




# ----------------------------------------------------------- Actions ------------------------------------------------------
	
	# Removem
	@api.multi
	def remove_myself(self):  
				
		self.unlink()





# ----------------------------------------------------------- CRUD - Deprecated ? -----------------
	@api.multi
	def unlink(self):
		#print 'jx'
		#print 'CRUD - Card - Unlink'
		#print 


		# Partner - Pricelist 
		pl = self.env['product.pricelist'].search([
															('name','=', 'Public Pricelist'),
													],
													#order='appointment_date desc',
													limit=1,)
		
		self.partner_id.property_product_pricelist = pl



		# Put your logic here 
		#res = models.Model.unlink(self)
		#res = super(openhealth.Card, self).unlink()
		res = super(models.Model, self).unlink()



		# Or here 
				
		return res 

