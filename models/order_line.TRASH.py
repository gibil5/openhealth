# -*- coding: utf-8 -*-
#
# 	Order Line
# 
#

from openerp import models, fields, api
import math





class sale_order_line(models.Model):

	_inherit='sale.order.line'
	#_name = 'openhealth.order_line'



	name = fields.Text(
			string='Descripción', 
			required=True
		)



	product_id = fields.Many2one(

			'product.product', 		
		
			string='Producto', 

			#domain=[('sale_ok', '=', True)], 

			
			domain=[
						('sale_ok', '=', True), 
					], 


			change_default=True, 
			ondelete='restrict', 
			required=True
		)



	product_uom_qty = fields.Float(
			string='Cantidad', 

			#digits=dp.get_precision('Product Unit of Measure'), 
			#required=True, 
			#default=1.0
		)


	#price_unit = fields.Float('Unit Price', required=True, digits=dp.get_precision('Product Price'), default=0.0)
	price_unit = fields.Float(
			'Precio', 
			required=True, 
			#digits=dp.get_precision('Product Price'), 
			default=0.0
		)

	#price_subtotal = fields.Monetary(compute='_compute_amount', string='Subtotal', readonly=True, store=True)
	#price_tax = fields.Monetary(compute='_compute_amount', string='Taxes', readonly=True, store=True)
	#price_total = fields.Monetary(compute='_compute_amount', string='Total', readonly=True, store=True)








	order_id=fields.Many2one(

		'sale.order',
		
		string='Order',
		)



	consultation = fields.Many2one('openhealth.consultation',
			ondelete='cascade', 
		)



	procedure_created = fields.Boolean(
			default=False,
		)



	_state_list = [
        			#('pre-draft', 'Pre-Quotation'),

        			('draft', 'Quotation'),
        			('sent', 'Quotation Sent'),
        			('sale', 'Sale Order'),
        			('done', 'Done'),
        			('cancel', 'Cancelled'),
        		]

	state = fields.Selection(
				selection = _state_list, 
				
				string="State",

				)







# ---------------------------------------------- Prices --------------------------------------------------------





	x_price_vip = fields.Float(
			string="Precio Vip",
		)





	#x_partner_vip = fields.Boolean(
	#		'Vip', 
			#readonly=True
	#		default=False, 
			#compute="_compute_partner_vip",
	#		)

	# Price total - Deprecated ? 
	#price_total = fields.Float(	
	#		string="Total",
	#		compute="_compute_price_total",
	#	)

	#@api.multi
	#@api.depends('price_unit', 'x_price_vip')
	
	#def _compute_price_total(self):
		
	#	for record in self:
	#		if record.order_id.x_partner_vip  	and  	record.x_price_vip != 0.0:
	#			record.price_total = record.x_price_vip * record.product_uom_qty
	#		else: 
	#			record.price_total = record.price_unit * record.product_uom_qty





	# Price subtotal 
	price_subtotal = fields.Float(	
			string="jx Sub-Total",
			compute="_compute_price_subtotal",
		)


	#@api.multi
	@api.depends('price_unit', 'x_price_vip')
	
	def _compute_price_subtotal(self):

		#print 
		#print 'Compute - Price Subtotal'
		
		for record in self:
		
			#if True: 
			#if record.x_partner_vip  	and  	record.x_price_vip != 0.0:
			if record.order_id.x_partner_vip  	and  	record.x_price_vip != 0.0:

					record.price_subtotal = record.x_price_vip * record.product_uom_qty


			else: 
				record.price_subtotal = record.price_unit * record.product_uom_qty












# ---------------------------------------------- Type --------------------------------------------------------

	# Type - Deprecated ?

	_x_type_list = [
						('service','Servicio'), 
						('consu','Producto'), 
					]


	x_type = fields.Selection(
			selection = _x_type_list, 

			string="Tipo",			
			compute='_compute_x_type', 			
			)
	
	#@api.multi
	@api.depends('product_id')

	def _compute_x_type(self):
		for record in self:
			record.x_type = record.product_id.type




#sale_order_line













# 31 Dec 2017


	@api.depends('product_uom_qty', 'discount', 'price_unit', 'tax_id')
	def _compute_amount(self):
		"""
		Compute the amounts of the SO line.
		"""
		for line in self:
			

			if line.x_comeback == True: 
				
				#price = line.price_unit * (1 - (line.discount or 0.0) / 100.0)
				price = line.x_price_vip_return * (1 - (line.discount or 0.0) / 100.0)
			
			else: 
				#price = line.price_unit * (1 - (line.discount or 0.0) / 100.0)
				price = 55
			



			taxes = line.tax_id.compute_all(price, line.order_id.currency_id, line.product_uom_qty, product=line.product_id, partner=line.order_id.partner_id)
			
			line.update({
				'price_tax': taxes['total_included'] - taxes['total_excluded'],
				'price_total': taxes['total_included'],
				'price_subtotal': taxes['total_excluded'],
			})






	@api.depends('product_uom_qty', 'discount', 'price_unit', 'tax_id')
	def _compute_amount(self):
		"""
		Compute the amounts of the SO line.
		"""
		for line in self:
			
			if line.x_comeback == True: 
				
				#price = line.price_unit * (1 - (line.discount or 0.0) / 100.0)
				price = line.x_price_vip_return * (1 - (line.discount or 0.0) / 100.0)
			
			else: 
				#price = line.price_unit * (1 - (line.discount or 0.0) / 100.0)
				price = 77
			



			taxes = line.tax_id.compute_all(price, line.order_id.currency_id, line.product_uom_qty, product=line.product_id, partner=line.order_id.partner_id)
			
			line.update({
				'price_tax': taxes['total_included'] - taxes['total_excluded'],
				'price_total': taxes['total_included'],
				'price_subtotal': taxes['total_excluded'],
			})




	#price_subtotal = fields.Monetary(compute='_compute_amount', string='Subtotal - jx', readonly=True, store=True)
	
	price_subtotal = fields.Monetary(
		compute='_compute_amount', 
		string='Subtotal - jx', 
		readonly=True, 
		#store=True
	)



			
# 22 May 2018

# ----------------------------------------------------------- Sale Order Report - Deprecated ------------------------------------------------------

	#order_report_id = fields.Many2one(

	#	'openhealth.order.report.nex', 
		
	#	string='Order Report Reference', 		
	#	required=False, 
	#	ondelete='cascade', index=True, copy=False
	#)






# 17 Jun 2018 
# ----------------------------------------------------------- Patient Lines - Extremely Dangerous !!! ------------------------------------------------------

	# Patient Line  
	#patient_line_id = fields.Many2one(
			
	#		'openhealth.patient.line',
			
	#		ondelete='cascade', 
			
			#string="Tratamiento",
			#readonly=False, 
	#	)


	# Correct
	#@api.multi
	#def x_reset(self):  
	#	print 
	#	print 'Order Line Reset'
	#	self.product_uom_qty = 0 







# 25 Oct 2017 

# ----------------------------------------------------------- Update ------------------------------------------------------

	# Update Recommendations 
	@api.multi
	def update_recos(self):  
		#print 
		#print 'Update - Recommendations'

		# Init 
		family = self.product_id.x_family
		treatment = self.product_id.x_treatment
		if family in ['laser', 'consultation', 'consultation_gyn']: 
			categ = treatment
		else: 
			categ = family


		# Print 
		#print family
		#print treatment
		#print categ
		#print self.service_co2_id 
		#print self.service_co2_id.state 
		#print hasattr(self.service_co2_id, 'state')
		#print self.service_co2_id is None



		#if categ == 'laser_co2'		and 	self.service_co2_id.state != False: 								
		#if categ == 'laser_co2'		and 	self.service_co2_id != False: 								
			#self.service_co2_id.state = 'sale'
		#elif categ == 'laser_excilite'		and 	self.service_excilite_id.state != False: 
			#self.service_excilite_id.state = 'sale'
		#elif categ == 'laser_ipl'		and 	self.service_ipl_id.state != False: 
			#self.service_ipl_id.state = 'sale'
		#elif categ == 'laser_ndyag'		and 	self.service_ndyag_id.state != False: 
			#self.service_ndyag_id.state = 'sale'
		#elif categ == 'laser_quick'		and 	self.service_quick_id.state != False: 
			#self.service_quick_id.state = 'sale'
		#elif categ == 'medical'			and 	self.service_medical_id.state != False: 
			#self.service_medical_id.state = 'sale'
		#elif categ == 'cosmetology'		and 	self.service_cosmetology_id.state != False: 
			#self.service_cosmetology_id.state = 'sale'
			#if self.service_product_id.state != False: 
			#	self.service_product_id.state = 'sale'



		# Co2
		if categ == 'laser_co2': 									
			lib.change_state(self.service_co2_id, 'sale')


		# Exc
		elif categ == 'laser_excilite': 
			lib.change_state(self.service_excilite_id, 'sale')


		# Ipl
		elif categ == 'laser_ipl': 
			lib.change_state(self.service_ipl_id, 'sale')


		# Ndyag
		elif categ == 'laser_ndyag': 
			lib.change_state(self.service_ndyag_id, 'sale')


		# Quick
		elif categ == 'laser_quick': 
			lib.change_state(self.service_quick_id, 'sale')


		# Medical
		elif categ == 'medical': 
			lib.change_state(self.service_medical_id, 'sale')


		# Cosmetology
		elif categ == 'cosmetology': 
			lib.change_state(self.service_cosmetology_id, 'sale')



		# Consultation
		elif categ == 'consultation': 
			#self.service_consultation_id.state = 'sale'
			print 


		# Products 
		else:
			lib.change_state(self.service_product_id, 'sale')



# ----------------------------------------------------------- On Changes ------------------------------------------------------

    # Product  
    #@api.onchange('product_id')
    #def _onchange_product_id(self):
    #   print 'jx'
    #   print 'Change Product'
        #if self.product_id.description != False: 
    #   self.name = self.product_id.description 



# ----------------------------------------------------------- Price Unit ------------------------------------------------------
    # Price Unit
    price_unit = fields.Float(
        #'Unit Price', 
        'Precio', 
        required=True, 
        digits=dp.get_precision('Product Price'), 
        default=0.0, 
    
        #compute='_compute_price_unit', 
    )

    @api.multi
    def _compute_price_unit(self):
        for record in self:
            if record.x_price_manual != False:                      # Manual                
                record.price_unit = record.x_price_manual
            else: 
                if      not record.order_id.x_partner_vip       and     not record.x_vip_inprog:                # Not VIP
                    record.price_unit = record.x_price_std
                else:                                               # VIP
                    if record.x_comeback    and     record.x_price_vip_return != 0: 
                        record.price_unit = record.product_id.x_price_vip_return
                    else: 
                        if record.x_price_vip != 0: 
                            record.price_unit = record.x_price_vip
                        else:
                            record.price_unit = record.x_price_std



# ----------------------------------------------------------- Price Manual ------------------------------------------------------

    # Price manual
    x_price_manual = fields.Float(
            string="Precio manual",
            required=False, 

            default=-1, 

            #compute='_compute_price_manual', 
        )

    #@api.multi
    #def _compute_price_manual(self):
    #   for record in self:
    #       record.x_price_manual = record.product_id.list_price





# ----------------------------------------------------------- Deprecated --------------------------
    # Date Created
    #x_date_created = fields.Datetime(
    #       string='Fecha',
    #    )

    #order_id = fields.Many2one('sale.order', string='Order Reference',
    #   required=False,
    #    ondelete='cascade', index=True, copy=False
    #)


# ----------------------------------------------------------- Actions -----------------------------
    # Create Myself
    #@api.multi
    #def create_myself(self):
    #    print
    #    print 'jx'
    #    print 'Create Myself'
    #    print


# ----------------------------------------------------------- Standard  - Dep ? -------------------

    #product_uom = fields.Many2one(
    #    'product.uom',
    #    string='Unit of Measure',
    #    required=False,
    #)

    #customer_lead = fields.Float(
    #    'Delivery Lead Time',
    #    required=False,
    #    default=0.0,
    #    help="Number of days between the order confirmation and
    #          the shipping of the products to the customer",
    #    oldname="delay"
    #)

    #order_id = fields.Many2one('sale.order', string='Order Reference',
    #    required=False,
    #    ondelete='cascade', index=True, copy=False
    #)







# ----------------------------------------------------------- Blocked - Dep ?----------------------
	# Product
	#product_id = fields.Many2one(
	#		'product.product',
	#		string='Product',
	#		domain=[('sale_ok', '=', True)],
	#		change_default=True,
			#default=lambda self: user._get_default_id(self, 'product'),
	#		ondelete='restrict',
	#		required=True
	#	)


# ----------------------------------------------------------- Primitives --------------------------

	# Name
	#name = fields.Text(
	#		string='Description',
	#		required=True,
	#	)

	# Patient
	#patient_id = fields.Many2one(
	#		'oeh.medical.patient',
	#		string='Paciente',
	#	)


	#x_qty = fields.Integer(
	#		compute='_compute_x_qty',
	#	)

	#@api.multi
	#def _compute_x_qty(self):
	#	for record in self:
	#		record.x_qty = record.product_uom_qty



# ----------------------------------------------------------- Comeback - Dep ---------------------------------
	# Comeback
	#x_comeback = fields.Boolean(
	#		string='Regreso',

	#		compute='_compute_comeback',
	#	)

	#@api.multi
	#def _compute_comeback(self):
	#	for record in self:
	#		record.x_comeback = False
	#		for service in record.order_id.patient.x_service_quick_ids:
	#			if service.service.name == record.name      and     service.comeback:
	#				record.x_comeback = True


