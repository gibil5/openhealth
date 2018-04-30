# -*- coding: utf-8 -*-
#
# 	Account Line Contasis
# 
# Created: 				19 April 2018
#

from openerp import models, fields, api

import datetime

import acc_funcs



class AccountLineContasis(models.Model):
	
	#_inherit='openhealth.account.line'
	_name = 'openhealth.account.line.contasis'
	_order = 'date_time asc'






# ----------------------------------------------------------- Contasis ------------------------------------------------------


	# Codigo Unico Ope
	cuo_mes = fields.Char(
			'MES', 
		)

	cuo_sd = fields.Char(
			'SD', 
		)

	cuo_asi = fields.Char(
			'ASI', 
		)




	# Fechas 
	fecha_emi = fields.Char(
			'FECHA DE EMISIÓN DEL CdP', 
		)

	fecha_ven = fields.Char(
			'FECHA DE VEN. Y/O PAGO.', 
		)




	# Comprobante de pago 
	cdp_t = fields.Char(
			'T CP', 
		)

	cdp_ser = fields.Char(
			#'N° SERIE O N° DE SERIE DE LA  MAQ. REGIS.', 
			'N° SERIE', 
		)

	cdp_num = fields.Char(
			'NUMERO', 
		)






	# Documento de identidad
	doc_t = fields.Char(
			'T', 
		)

	doc_num = fields.Char(
			'NÚMERO', 
		)


	ape_nom = fields.Char(
			#'APELLIDOS Y NOMBRES,  DENOMINACIÓN O RAZÓN SOCIAL', 
			'APELLIDOS Y NOMBRES', 
		)





	# Exportacion
	val_exp = fields.Char(
			'VALOR FACT. DE LA EXPORT.', 
		)




	# Importe
	bas_imp = fields.Char(
			'BASE IMPONIBLE DE LA OPERACIÓN GRAVADA', 
		)


	imp_tot_exo = fields.Char(
			'EXONERADA', 
		)

	imp_tot_ina = fields.Char(
			'INAFECTA', 
		)





	isc = fields.Char(
			'ISC', 
		)


	igv = fields.Char(
			'IGV Y/O IPM', 
		)

	otr = fields.Char(
			'OTROS TRIB. Y CARG. NO PART.  B. IMPONIBLE', 
		)






	imp_tot = fields.Char(
			'IMPORTE TOTAL DEL CdP', 
		)

	tc = fields.Char(
			'T/C', 
		)





	# Referencia modificada
	refmod_fecha = fields.Char(
			'FECHA', 
		)

	refmod_t = fields.Char(
			'T', 
		)

	refmod_ser = fields.Char(
			'SERIE', 
		)

	refmod_num = fields.Char(
			'N° DEL CdP', 
		)




# ----------------------------------------------------------- Actions ------------------------------------------------------



	# Update 
	@api.multi
	def update_fields(self):  

		print 'jx'
		print 'Update Contasis'



		# Names 
		if self.x_type == 'ticket_invoice':
			self.ape_nom = self.patient.x_firm 

		else: 
			self.ape_nom = self.patient.name 



		# Doc 
		self.doc_num = self.document
		self.doc_t = '0'




		# Serial number 
		if self.serial_nr != False: 
			self.cdp_ser = self.serial_nr.split('-')[0]
			self.cdp_num = self.serial_nr.split('-')[1]


		self.cdp_t = acc_funcs._h_type[self.x_type]




		# Dates	- Must be converteed to a datetime object, before converting to the proper format. 
		DATETIME_FORMAT = "%Y-%m-%d"
		self.fecha_emi  = datetime.datetime.strptime(self.date, DATETIME_FORMAT).strftime('%d/%m/%Y')
		self.fecha_ven  = datetime.datetime.strptime(self.date, DATETIME_FORMAT).strftime('%d/%m/%Y')


		self.cuo_mes =  datetime.datetime.strptime(self.date, DATETIME_FORMAT).strftime('%m')
		#self.cuo_asi = 


		# Constants 
		self.val_exp = '0.00'
		self.imp_tot_exo = '0.00'
		self.imp_tot_ina = '0.00'
		self.isc = '0.00'
		self.otr = '0.00'
		self.refmod_t = '00'
		self.tc = '3.2100'
		self.cuo_sd = '02'



		# Actual amount
		self.imp_tot = self.amount
		self.bas_imp = self.amount_net 
		self.igv = self.amount_tax 




# ----------------------------------------------------------- Relational ------------------------------------------------------

	account_id = fields.Many2one(
			'openhealth.account.contasis'
		)


# ----------------------------------------------------------- Primitives ------------------------------------------------------

	serial_nr = fields.Char(
			string="Nr. de serie", 
		)


	x_type = fields.Selection(
			[	('receipt', 			'Boleta'),
				('invoice', 			'Factura'),
				('advertisement', 		'Canje Publicidad'),
				('sale_note', 			'Canje NV'),
				('ticket_receipt', 		'Ticket Boleta'),
				('ticket_invoice', 		'Ticket Factura'),	], 

			string='Tipo', 
			
			#required=False,
		)

	document = fields.Char(
			string="Documento", 
		)



	date = fields.Date(
		)

	date_time = fields.Datetime(
			string="Fecha", 
		)



	patient = fields.Many2one(
			'oeh.medical.patient', 
			string="Nombre", 
		)




	amount = fields.Float(
			string="Total", 
		)

	amount_net = fields.Float(
			string="Neto", 
		)

	amount_tax = fields.Float(
			string="Impuesto", 
		)




