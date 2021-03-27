# -*- coding: utf-8 -*-
"""
	Container

	Separate Structure and Business Logic

	Created: 				30 Sep 2018
	Last mod: 				16 Dec 2019
"""
from __future__ import print_function
import base64
import io
import os
import shutil
import datetime
from openerp import models, fields, api

from openerp.addons.openhealth.models.management import mgt_funcs

from openerp.addons.openhealth.models.management import mgt_vars

#from openerp.addons.openhealth.models.containers import export

from openerp import _
from openerp.exceptions import Warning as UserError

from . import pl_export



class ElectronicContainer(models.Model):
	"""
	Electronic Container
	Uses
		Electronic Orders
		TXT Lines
	Migrated to PL
	"""

	_inherit = 'openhealth.container'

	_description = 'Electronic Container'




# ----------------------------------------------------- Django Interface --------------------------

	@api.multi
	def get_date_begin(self):
		"""
		Django interface
		"""
		print()
		print('Get date begin')
		return self.export_date_begin


	@api.multi
	def get_date_end(self):
		"""
		Django interface
		"""
		print()
		print('Get date end')
		return self.export_date_end





	@api.multi
	def get_total(self):
		"""
		Django interface
		"""
		print()
		print('Get total')
		if self.amount_total not in [False]:
			return self.amount_total
		else:
			return 0



	@api.multi
	def get_count(self):
		"""
		Django interface
		"""
		print()
		print('Get count')

		if self.total_count not in [False]:
			return self.total_count

		else:
			return 0



# ----------------------------------------------------------- Relational - New --------------------------

	# Txt Line - New
	txt_line = fields.One2many(

			'openhealth.account.txt.line',

			'container_id',
		)




# ----------------------------------------------------------- Relational --------------------------

	# Electronic Line
	electronic_order_ids = fields.One2many(
			'openhealth.electronic.order',

			'container_id',
		)



	# Txt Line
	txt_ids = fields.One2many(
			'openhealth.texto',

			'container_id',
		)





# ----------------------------------------------------------- Fields --------------------------

	# Total count
	total_count = fields.Integer(
			'Total Nr',
		)


	# Receipt count
	receipt_count = fields.Integer(
			'Recibos Nr',
		)


	# Invoice count
	invoice_count = fields.Integer(
			'Facturas Nr',
		)



	export_date = fields.Char(
			'Export Date',
			readonly=True,
		)




	# Txt File Name
	txt_pack_name = fields.Char(
			#'Paquete TXT - Name',
			'Nombre Archivo TXT',
		)


	# Download
	txt_pack = fields.Binary(
			'Descargar TXT',
		)



	# Total
	amount_total = fields.Float(
			'Total',
			digits=(16, 2),
		)









# ----------------------------------------------------------- Relational ---------------------------------------------



# ----------------------------------------------------------- First Level - Buttons ---------------------------------------------

# ----------------------------------------------------------- Export TXT - Button - Step 2 ---------------------------

	@api.multi
	def create_txt_line(self):
		"""
		Create TXT Line - Button
		"""
		print()
		print('X - Create - Txt Line')


		# Clean 
		self.txt_line.unlink()


		# Path
		path = self.configurator.path_account_txt + self.export_date
		#print(path)



		# Loop - For all Electronic Lines
		for order in self.electronic_order_ids:


			# Instantiate Txt Line
			#txt_line = TxtLine()

			#name = order.name			

			txt_line = self.txt_line.create({
												#'name': name,
												'name': self.name,

												'path': path,

												'order': order.id,

												'container_id': self.id,
											})


			# Get File Name
			txt_line.get_file_name()



			# Init Electronic
			txt_line.complete_order()


			# Create Content 
			txt_line.generate_content()


			# Create File
			txt_line.create_file()



		# For Django
		self.total_count = self.receipt_count + self.invoice_count

		self.state = 'stable'
		self.date_test = datetime.datetime.now() 
		return 1

	# create_txt_line





# ----------------------------------------------------------- Create Electronic - Button - Step 1 ----------------------
	# Create Electronic
	@api.multi
	def create_electronic(self):
		"""
		Create Electronic Orders - Button
		"""
		print()
		print('X - Create - Electronic - Button')


		# Init Configurator
		self.init_configurator()


		# Clean
		self.electronic_order_ids.unlink()


		# Init Dates
		date_format = "%Y-%m-%d"
		date_dt = datetime.datetime.strptime(self.export_date_begin, date_format) + datetime.timedelta(hours=+5, minutes=0)
		self.export_date = date_dt.strftime(date_format).replace('-', '_')


		# Init
		self.state_arr = 'sale,cancel,credit_note'
		self.type_arr = 'ticket_receipt,ticket_invoice'


		# Create Electronic
		self.amount_total, self.receipt_count, self.invoice_count = self.update_electronic()



		return 1	# For Django

	# create_electronic



# ----------------------------------------------------------- Export TXT - Button - Step 2 ---------------------------
	@api.multi
	#def pl_export_txt(self):
	def create_txt(self):
		"""
		Create TXT - Button
		"""
		print()
		print('X - Create - Txt')


		# Clean
		self.txt_ids.unlink()


		# Init
		path = self.configurator.path_account_txt + self.export_date
		#print(path)



		# Remove and Create Dir

		# Remove dir if it already exists
		if os.path.isdir(path) and not os.path.islink(path):
			shutil.rmtree(path)		
		
		# Create
		os.mkdir(path)  			



		# Create and Write into a file
		fname = pl_export.create_txt_for_all_electronic_orders(self, self.electronic_order_ids, path)




		# Download file
		fname_txt = fname.split('/')[-1]

		# Read Binary
		f = io.open(fname, mode="rb")
		out = f.read()
		f.close()

		# Update
		self.write({
					'txt_pack': base64.b64encode(out),
					'txt_pack_name': fname_txt,
				})
	# export_txt


# ----------------------------------------------------------- Clear - Button  -----------------------------
	@api.multi
	def clear(self):
		"""
		Cleans all variables - Button
		"""

		#self.txt_pack.unlink()
		self.txt_pack = False

		# Electronic
		self.electronic_order_ids.unlink()
		# Txt
		self.txt_ids.unlink()
		# Stats
		self.amount_total = 0
		self.invoice_count = 0
		self.receipt_count = 0
	# clear








# ----------------------------------------------------------- Second Level - Services ---------------------------------------------


# ----------------------------------------------------------- Update Sales Electronic -----------

	# Update Electronic
	@api.multi
	def update_electronic(self):
		"""
		high level support for doing this and that.
		"""
		print()
		#print('Pl - Update - Electronic')
		print('Update - Electronic')


		# Clean
		self.electronic_order_ids.unlink()


		# Init
		if not self.several_dates:
			self.export_date_end = self.export_date_begin



		# Get Orders
		print(self.state_arr)
		print(self.type_arr)
		orders, count = mgt_funcs.get_orders_filter(self, self.export_date_begin, self.export_date_end, self.state_arr, self.type_arr)
		print(orders)
		print(count)



		# Init
		amount_total = 0
		receipt_count = 0
		invoice_count = 0

		# Loop
		for order in orders:
			#print order
			#print order.x_type

			# Generate Id Doc
			if order.x_type in ['ticket_invoice', 'invoice']:
				order.pl_receptor = order.patient.x_firm.upper()
				id_doc = order.patient.x_ruc
				id_doc_type = 'ruc'
				id_doc_type_code = '6'
			else:
				order.pl_receptor = order.patient.name
				id_doc = order.patient.x_id_doc
				id_doc_type = order.patient.x_id_doc_type
				id_doc_type_code = order.patient.x_id_doc_type_code

			# Patch
			#if order.patient.x_id_doc == False and order.patient.x_id_doc_type == False:
			if not order.patient.x_id_doc and not order.patient.x_id_doc_type:
				if order.patient.x_dni != False:
					id_doc = order.patient.x_dni
					id_doc_type = 'dni'
					id_doc_type_code = 1


			#print(receptor)
			#print(order.pl_receptor)
			#print(id_doc)
			#print(id_doc_type)
			#print(id_doc_type_code)



			# Validate Errors
			#if self.configurator.validate_errors_electronic():
			if self.configurator.error_validation_electronic:


				# Validate Order Patient
				#error, msg = order.patient.validate()				# Train Wreck ! - Does not respect the LOD
				#order.validate_patient()							

				if order.x_type in ['ticket_invoice', 'invoice']:
					order.validate_patient_for_invoice()							# Good - Respects the LOD




				# Validate Order 	
				order.validate_electronic()							# Good - Respects the LOD
				#error, msg = order.validate_electronic()   		# # Train Wreck !




			# Create Electronic Order
			electronic_order = self.electronic_order_ids.create({
																# Required

																# Electronic order
																'name': 				order.name,
																'x_date_created': 		order.date_order,


																# Firm ?


																# Patient
																'receptor': 			order.pl_receptor,
																'patient': 				order.patient.id,
																'id_doc': 				id_doc,
																'id_doc_type': 			id_doc_type,
																'id_doc_type_code': 	id_doc_type_code,


																# Sale
																'doctor': 				order.x_doctor.id,
																'x_type': 				order.x_type,
																'type_code': 			order.x_type_code,
																'serial_nr': 			order.x_serial_nr,
																'amount_total': 		order.x_amount_flow,
																'amount_total_net': 	order.x_total_net,
																'amount_total_tax': 	order.x_total_tax,
																'state': 				order.state,
																'counter_value': 		order.x_counter_value,
																'delta': 				order.x_delta,
																'credit_note_owner': 	order.x_credit_note_owner.id,
																'credit_note_type': 	order.x_credit_note_type,


																# Handles
																'container_id': 		self.id,
			})


			# Update constants (Firm)
			electronic_order.update_constants()



			#print(electronic_order)
			#print(electronic_order.container_id)
			#print(electronic_order.name)


			# Create Lines
			for line in order.order_line:
				# Create
				electronic_order.electronic_line_ids.create({
																					# Line
																					'product_id': 			line.product_id.id,
																					'product_uom_qty': 		line.product_uom_qty,
																					'price_unit': 			line.price_unit,

																					# Handle
																					'electronic_order_id': 	electronic_order.id,
					})


			# Update Amount Total
			if order.state in ['sale', 'cancel', 'credit_note']:
				# Total
				amount_total = amount_total + order.x_amount_flow
				# Count
				if order.x_type in ['ticket_receipt']:
					receipt_count = receipt_count + 1
				elif order.x_type in ['ticket_invoice']:
					invoice_count = invoice_count + 1

		return amount_total, receipt_count, invoice_count
	# update_electronic


# ----------------------------------------------------------- Init Configurator -----------
	def init_configurator(self):
		"""
		Init Configurator
		"""
		print()
		print('Init Configurator')

		# Configurator
		if self.configurator.name in [False]:
			self.configurator = self.env['openhealth.configurator.emr'].search([
																					('x_type', 'in', ['emr']),
															],
															#order='date_begin,name asc',
															limit=1,
														)
			#print(self.configurator)
			#print(self.configurator.name)
	# init_configurator



# ----------------------------------------------------------- Third Level - Fields ---------------------------------------------




# ----------------------------------------------------------- Configurator --------------
	# Configurator
	configurator = fields.Many2one(
			'openhealth.configurator.emr',
			string="Configuracion",
			required=True,
			#required=False,
		)

# ----------------------------------------------------------- Dates ---------------------
	# Dates
	export_date_begin = fields.Date(
			string="Fecha Inicio",
			default=fields.Date.today,
			required=True,
		)

	# Dates
	export_date_end = fields.Date(
			string="Fecha Final",
			default=fields.Date.today,
			required=True,
		)

	several_dates = fields.Boolean(
			'Varias Fechas',
		)

# ----------------------------------------------------------- Electronic ----------------
	# Name
	name = fields.Char(
			'Nombre',
			default='Generador',
			required=True,
		)

	# State Array
	state_arr = fields.Selection(
			selection=mgt_vars._state_arr_list,
			string='State Array',
			default='sale,cancel,credit_note',
			required=True,
		)

	# Type Array
	type_arr = fields.Selection(
			selection=mgt_vars._type_arr_list,
			string='Type Array',
			default='ticket_receipt,ticket_invoice',
			required=True,
		)

# ----------------------------------------------------------- Common ----------------
	vspace = fields.Char(
			' ',
		)



# ----------------------------------------------------------- Download --------------------------

	@api.multi
	def export_file( self ):
	    return {
		        'type' : 'ir.actions.act_url',
		        
		        #'url':   '/web/binary/saveas?model=ir.attachment&field=datas&filename_field=self.file_name&id=%s' % ( self.excel_file.id ),
		        #'url':   '/web/binary/saveas?model=ir.attachment&field=datas&filename_field=self.file_name&id=%s' % ( self.txt_pack_name ),
		        #'url':   ' /Users/gibil/mssoft/ventas/saveas?model=ir.attachment&field=datas&filename_field=self.file_name&id=%s' % ( self.txt_pack_name ),
			    #"url": "http://odoo.com/saveas?model=ir.attachment&field=datas&filename_field=self.file_name&id=%s' % ( self.txt_pack_name ),",
			    "url": "http://localhost:8069/saveas?model=ir.attachment&field=datas&filename_field=self.file_name&id=%s' % ( self.txt_pack_name ),",

		        'target': 'self',
	        }

