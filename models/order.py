# -*- coding: utf-8 -*-
#
# 	Order 
# 
#


from openerp import models, fields, api

import jxvars
import appfuncs



class sale_order(models.Model):
	
	#_name = 'openhealth.order'
	_inherit='sale.order'
	



	x_appointment = fields.Many2one(
			'oeh.medical.appointment',
			
			#string='Appointment #'
			string='Cita', 

			#required=False, 
			#required=True, 
			)




	# Machine 
	x_machine = fields.Selection(
			#string="Máquina", 
			string="Sala", 
			selection = jxvars._machines_list, 
			
			#required=True, 
		)



	# Doctor 
	x_doctor = fields.Many2one(
			'oeh.medical.physician',
			string = "Médico", 	
			
			#required=True, 
			)



	x_appointment_date = fields.Datetime(
			string="Fecha", 
			#readonly=True,

			#required=True, 
			)


	x_duration = fields.Float(
			string="Duración (h)", 
			#readonly=True, 

			#required=True, 		
			)






	# Chief complaint 
	x_chief_complaint = fields.Selection(
			string = 'Motivo de consulta', 

			selection = jxvars._chief_complaint_list, 
			)







	x_vip = fields.Boolean(
			'Vip', 
			#readonly=True
			)




	_state_list = [
        			#('pre-draft', 'Pre-Quotation'),

        			#('draft', 'Quotation'),
        			#('sent', 'Quotation Sent'),
        			#('sale', 'Sale Order'),
        			#('done', 'Done'),
        			#('cancel', 'Cancelled'),


        			('pre-draft', 	'Presupuesto consulta'),

        			('draft', 		'Presupuesto'),
        			
        			('sent', 		'Presupuesto enviado'),
        			('sale', 		'Facturado'),
        			('done', 		'Completo'),
        			('cancel', 		'Cancelado'),
        		]


	state = fields.Selection(
			selection = _state_list, 

			#string='Status', 			
			string='Estado',	
			
			#readonly=True, 
			readonly=False, 

			#default='draft'
			#copy=False, 
			#index=True, 
			#track_visibility='onchange', 
			)


	#jxx
	@api.onchange('state')

	def _onchange_state(self):

		print 
		print 
		print 'On change State'

		if self.state == 'sale':	

			print 'Gotcha !!!'

		print 
		print 











	vspace = fields.Char(
			' ', 
			readonly=True
			)
	
	
	order_line = field_One2many=fields.One2many(
		'sale.order.line',
		'order_id',

		#string='Order',
		#compute="_compute_order_line",
		)


	#@api.multi
	#@api.depends('x_vip')
	
	#def _compute_order_line(self):
	#	for record in self:
	#		print 'compute_order_line'
	#		print record.x_vip 
	#		ret = record.update_order_lines()
	#		print ret 





	# Indexes 
	consultation = fields.Many2one('openhealth.consultation',
		string="Consulta",
		ondelete='cascade', 
	)


	treatment = fields.Many2one('openextension.treatment',
		ondelete='cascade', 
	)



	
	patient = fields.Many2one(
			'oeh.medical.patient',
	)
	
	
	
	x_state = fields.Char(
		default='a',
	)
	

	#x_copy_created = fields.Boolean(
	#	default=False,
	#)

		

	
	
	
	
	
	
	# Nr lines 
	nr_lines = fields.Integer(
			
			default=0,

			string='Nr líneas',
			
			compute='_compute_nr_lines', 
			#required=True, 
			)

	@api.multi
	#@api.depends('order_line')
	
	def _compute_nr_lines(self):
		for record in self:
			#record.name = 'SE00' + str(record.id) 
			#record.nr_lines = 0
			
			ctr = 0
			for l in record.order_line:
				ctr = ctr + 1
			record.nr_lines = ctr 
			
	
	
	
	
	
	# Order lines 

	@api.multi 
	def clean_order_lines(self):
		
		if self.state == 'draft':
			ret = self.remove_order_lines()







	# On change - Vip 

	#@api.onchange('x_vip')
	
	#def _onchange_x_vip(self):
		#print 'onchange'

		#name = self.name 		
		#order_id = self.env['sale.order'].search([('name', 'like', name)]).id

		#print self.id
		#print self.name
		#print order_id 

		#ret = self.update_order_lines(order_id)
		#print ret 

		#print 




	# Update Lines 
	@api.multi 
	def update_order_lines(self):

		print 
		print 'update_order_lines'

		#ret = self.remove_order_lines()

		ret = self.x_create_order_lines()

		return 1



	# Remove 
	@api.multi 
	def remove_order_lines(self):
		ret = self.order_line.unlink()
		return ret 





	# Create Line 

	@api.multi 
	def create_line(self, order_id, se):
		print 'create line'

		product_id = se.service.id
		name = se.name_short


		# Consultation 
		consultation = self.consultation
		print consultation 
		print consultation.id



		x_price_vip = se.service.x_price_vip
		x_price = se.service.list_price

		#if self.x_vip and se.service.x_price_vip != 0.0:
		if self.x_vip and x_price_vip != 0.0:
			#price_unit = se.service.x_price_vip
			price_unit = x_price_vip
		else:
			#price_unit = se.service.list_price
			price_unit = x_price


		#print product_id
		#print order_id
		#print name
		#print price_unit
		#print se.service.uom_id.id
		#print 



		if self.nr_lines == 0:
			print 'create new'

			ol = self.order_line.create({

										'product_id': product_id,
										
										'order_id': order_id,

										
										'consultation':consultation.id,
										'state':'pre-draft',


										'name': name,

										'price_unit': price_unit,

										'x_price_vip': x_price_vip,
										
										'x_price': x_price,

										'product_uom': se.service.uom_id.id, 
									})

		else:
			print 'update existing'

			order_line_id = self.env['sale.order.line'].search([
																('order_id', 'like', order_id),
																('name', 'like', name),
																]).id
			print order_line_id


			rec_set = self.env['sale.order.line'].browse([
															order_line_id																
														])
			print rec_set 

			#ol = self.order_line.create({
			#ol = self.order_line.write(1, order_line_id, 
			
			ol = rec_set.write({
									#'product_id': product_id,
									#'order_id': order_id,
									#'name': name,
									'price_unit': price_unit,
									#'product_uom': se.service.uom_id.id, 
								})


		return 1




	# Create 
	@api.multi 
	def x_create_order_lines(self):
		print 
		print 'Create order lines'
		
		
		order_id = self.id


		print 
		print 'co2'
		for se in self.consultation.service_co2_ids:
			print se 
			
			ret = self.create_line(order_id, se)



		print 
		print 'excilite'
		for se in self.consultation.service_excilite_ids:
			print se 

			ret = self.create_line(order_id, se)


		
		print 
		print 'ipl'
		for se in self.consultation.service_ipl_ids:
			print se 

			ret = self.create_line(order_id, se)



		print 
		print 'ndyag'
		for se in self.consultation.service_ndyag_ids:
			print se 

			ret = self.create_line(order_id, se)



		print 
		print 'medical'
		for se in self.consultation.service_medical_ids:
			print se 
			#print se.service.id
			#print order_id
			#print se.name_short

			ret = self.create_line(order_id, se)



		print 'out'

		return self.nr_lines

	



	# Total 
	x_price_total = fields.Float(
			string="Total",
			default=5.0,

			compute="_compute_x_price_total",
		)

	x_price_vip_total = fields.Float(
			string="Total Vip",
			default=3.0,

			compute="_compute_x_price_vip_total",
		)

	

	@api.multi
	#@api.depends('x_price')
	
	def _compute_x_price_total(self):
		for record in self:			
			total = 0 

			for line in record.order_line:
				#total = total + line.price_total 
				total = total + line.x_price_wigv 

			record.x_price_total = total 



	@api.multi
	#@api.depends('x_price_vip')
	
	def _compute_x_price_vip_total(self):
		for record in self:			
			total = 0 

			for line in record.order_line:
				total = total + line.x_price_vip_wigv

			record.x_price_vip_total = total 






# ----------------------------------------------------------- Button - Update Lines ------------------------------------------------------

	@api.multi 
	def update_order_lines_app(self):


		for line in self.order_line:

			product_id = line.product_id


			# If Service 
			if product_id.type == 'service':

				appointment = self.env['oeh.medical.appointment'].search([ 	
															('doctor', 'like', self.x_doctor.name), 	
															('patient', 'like', self.patient.name),		
															('x_type', 'like', 'procedure'), 

															#('state', 'like', 'pre_scheduled'), 
														], 
														order='appointment_date desc', limit=1)

				appointment_id = appointment.id
				#print appointment  
				#print appointment_id  



				# Self 
				line.x_appointment_date = appointment.appointment_date
				line.x_doctor_name = appointment.doctor.name
				line.x_duration = appointment.duration 

				line.x_machine = appointment.x_machine


				self.x_appointment = appointment
				self.x_doctor = appointment.doctor
				self.x_appointment_date = appointment.appointment_date
				self.x_duration = appointment.duration

				#self.x_machine = appointment.x_machine 







# ----------------------------------------------------------- Button - Update Lines ------------------------------------------------------

	@api.multi 
	def reserve_machine(self):

		self.x_machine = 'laser_co2_1'





# ----------------------------------------------------------- CRUD ------------------------------------------------------

# Create 
	@api.model
	def create(self,vals):

		print 
		print 'Order - Create - Override'
		print 
		print vals
		print 
	


		#Write your logic here
		res = super(sale_order, self).create(vals)
		#Write your logic here

		return res




# Write 
	@api.multi
	def write(self,vals):

		print 
		print 'Order - Write - Override'
		#print 
		#print vals
		#print 
		#print 



		#if 'x_machine' in vals:
		#	x_machine = vals['x_machine']
		#	print x_machine
		#else:
		#	print 'Error !'
		#	return {
		#				'warning': {
		#							'title': "Error: Sala no Reservada !",
		#							'message': 'jx',
												#'Cita ya existente, con el ' + doctor_name + ": " + start + ' - ' + end + '.',
		#						}}
		print 





		res = super(sale_order, self).write(vals)
		#Write your logic here

		print 
		print 

		return res




# ----------------------------------------------------------- Buttons - Order  ------------------------------------------------------

	@api.multi
	def remove_myself(self):  

		print 
		print 'Remove Order'

		order_id = self.id
		print "id: ", order_id
		

		# Search 
		rec_set = self.env['sale.order'].browse([order_id])
		print "rec_set: ", rec_set


		# Write
		ret = rec_set.write({
								'state': 'draft',
							})

		
		# Unlink 
		ret = rec_set.unlink()
		print "ret: ", ret
		print 


#sale_order()

