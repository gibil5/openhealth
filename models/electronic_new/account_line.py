# -*- coding: utf-8 -*-
"""
 	Account Line

 	Created: 				23 April 2019
 	Last up: 				23 April 2019
"""
from openerp import models, fields, api
from . import acc_lib
from . import acc_vars

from . import pl_acc_lib

class AccountLine(models.Model):
	"""
	high level support for doing this and that.
	"""
	_inherit = 'openhealth.account.line'

	_order = 'date_time asc'



# ----------------------------------------------------------- Relational -----------------------------

	product = fields.Many2one(

			'product.product',
		
			string="Producto",
		)


	account_id = fields.Many2one(
			'openhealth.account.contasis'
		)


	patient = fields.Many2one(
			'oeh.medical.patient',
			string="Nombre",
		)



# ----------------------------------------------------------- Update -----------------------------

	# Update Fields
	@api.multi
	def update_fields(self):
		"""
		high level support for doing this and that.
		"""
		#print
		#print 'Update Contasis'


		# Product
		self.product_type = self.product.type

		# Type Doc
		self.tipodocumento = acc_vars._sale_type[self.x_type]

		# Cuentab
		#self.cuentab = acc_vars._cuentab[self.product_type]
		self.cuentab = pl_acc_lib.get_cuentab(self, self.product_type)






		# Dates
		#self.date_time_corr, date_time_str = acc_funcs.correct_time(self, self.date_time, -5)
		self.date_time_corr, date_time_str = acc_lib.AccFuncs.correct_time(self.date_time, -5)
		self.date_char = date_time_str.split()[0]
		self.time_char = date_time_str.split()[1]
		self.fecha = self.date_char
		self.fechavencimiento = self.date_char
		self.fechavencimiento2 = self.date_char


		# Name
		if self.x_type in ['invoice', 'ticket_invoice']:			# Ruc
			self.nombre = self.patient.x_firm
		else: 														# Other
			self.nombre = self.patient.name


		# Id Doc
		self.tipodoc = self.document_type
		self.numdoc = self.document



		# Serial number
		#if self.serial_nr != False:
		if self.serial_nr != False and len(self.serial_nr.split('-')) == 2:
			self.numeroserie = self.serial_nr.split('-')[0]
			self.numerofactura = self.serial_nr.split('-')[1]
			self.glosa = self.glosa + self.serial_nr





		# Actual amount
		if self.state == 'cancel':
			self.amount = 0
			self.amount_net = 0
			self.amount_tax = 0

		else:
			# Net
			net = self.amount/1.18
			self.amount_net = round(net, 2)

			# Tax
			tax = net * 0.18
			self.amount_tax = round(tax, 2)


		# Other
		self.total = self.amount
		self.neto = self.amount_net
		self.igv = self.amount_tax
		self.porigv = self.igv

	# update_fields





# ----------------------------------------------------------- Dates -------------------------------

	# Date
	date = fields.Date(
			#string="Fecha",
		)

	# Datetime
	date_time = fields.Datetime(
			string="Fecha y hora",
		)

	# Corr
	date_time_corr = fields.Datetime(
			#string="Fecha",
		)

	# Date
	date_char = fields.Char(
			string="Fecha",
		)

	# Time
	time_char = fields.Char(
			string="Hora",
		)






# ----------------------------------------------------------- Contasis - 1 ------------------------

	# Name
	nombre = fields.Char(
			'nombre',
		)


	# Fechas
	fecha = fields.Char(
			'fecha',
		)

	fechavencimiento = fields.Char(
			'fechavencimiento',
		)


	# Comprobante de pago
	tipodocumento = fields.Char(
			'tipodocumento',
		)

	numeroserie = fields.Char(
			'numeroserie',
		)

	numerofactura = fields.Char(
			'numerofactura',
		)


	# Documento de identidad
	tipodoc = fields.Char(
			'tipodoc',
		)

	numdoc = fields.Char(
			'numdoc',
		)



# ----------------------------------------------------------- Contasis - 2 ------------------------

	# Exportacion
	EXPortacion = fields.Char(
			'EXPortacion',
			default='0',
		)


	# Importe
	neto = fields.Char(
			'neto',
		)

	exonerado = fields.Char(
			'exonerado',
			default='0',
		)

	inafecto = fields.Char(
			'inafecto',
			default='0',
		)

	isc = fields.Char(
			'isc',
			default='0',
		)

	igv = fields.Char(
			'igv',
		)

	otros = fields.Char(
			'otros',
			default='0',
		)


	# Total
	total = fields.Char(
			'total',
		)

	tipocambio = fields.Char(
			'tipocambio',
			default='3.3',
		)


# ----------------------------------------------------------- Contasis - 3 ------------------------

	# Referencia modificada
	fechar = fields.Char(
			'fechar',
		)

	tipor = fields.Char(
			'tipor',
		)

	serier = fields.Char(
			'serier',
		)

	numr = fields.Char(
			'numr',
		)


	moneda = fields.Char(
			'moneda',
			default='S',
		)

	dolares = fields.Char(
			'dolares',
			default='0',
		)

	fechavencimiento2 = fields.Char(
			'fechavencimiento2',
		)

	condicion = fields.Char(
			'condicion',
			default='CON',
		)

	ccosto = fields.Char(
			'ccosto',
		)

	ccosto2 = fields.Char(
			'ccosto2',
		)


# ----------------------------------------------------------- Contasis - 4 ------------------------
	cuentab = fields.Char(
			'cuentab',
			#default='701101001',
		)

	cuentao = fields.Char(
			'cuentao',
			#default='CON',
		)

	cuentacontable = fields.Char(
			'cuentacontable',
			default='121210001',
		)


	regimen = fields.Char(
			'regimen',
			default='0',
		)

	porcen = fields.Char(
			'porcen',
			default='0',
		)

	importer = fields.Char(
			'importer',
			default='0',
		)


# ----------------------------------------------------------- Contasis - 5 ------------------------

	seried = fields.Char(
			'seried',
			#default='0',
		)

	numdocr = fields.Char(
			'numdocr',
			#default='CON',
		)

	fechad = fields.Char(
			'fechad',
			#default='CON',
		)

	codigop = fields.Char(
			'codigop',
			#default='CON',
		)

	porigv = fields.Char(
			'porigv',
			#default='CON',
		)

	glosa = fields.Char(
			'glosa',
			default='POR VENTA DE 01-',
		)

	mediop = fields.Char(
			'mediop',
			#default='CON',
		)

	comd = fields.Char(
			'comd',
			#default='CON',
		)

	importec = fields.Char(
			'importec',
			default='0',
		)




# ----------------------------------------------------------- Meta --------------------------------

	# Id Document
	document = fields.Char(
			string="Documento",
		)

	document_type = fields.Char(
			#string="Tipo Documento",
			string="Tipo Doc",
		)

	name = fields.Char(
			'Nr',
		)


	qty = fields.Integer(
			string="Cantidad",
		)


	product_type = fields.Selection(
			[
				('service', 'Servicio'),
				('product', 'Producto'),
				('consu', 'Consumible'),
			],
			string='Tipo Prod',
			#required=False,
		)

	state = fields.Selection(
			[
				('sale', 'Venta'),
				('cancel', 'Anulado'),
			],
			string='Estado',
			#required=False,
		)

	serial_nr = fields.Char(
			string="Nr. de serie",
		)

	x_type = fields.Selection(
			[
				('receipt', 'Boleta'),
				('invoice', 'Factura'),
				('advertisement', 'Canje Publicidad'),
				('sale_note', 'Canje NV'),
				('ticket_receipt', 'Ticket Boleta'),
				('ticket_invoice', 'Ticket Factura'),
			],
			string='Tipo',
			#required=False,
		)


	# Amount
	amount = fields.Float(
			string="Total",
		)

	amount_net = fields.Float(
			string="Neto",
		)

	amount_tax = fields.Float(
			string="Impuesto",
		)
