# -*- coding: utf-8 -*-
"""

 	Electronic Order - Sunat compatible

 	Created:          13 sep 2018
	Last up: 	 		29 mar 2021
"""

from __future__ import print_function  # Only needed for Python 2
import io

from openerp import models, fields, api
from openerp.addons.openhealth.models.order import ord_vars
from .lib import chk_electronic, lib_coeffs, pl_lib_exp

#from openerp.addons.openhealth.models.libs import lib
#from openerp.addons.openhealth.models.commons.libs import lib
from openerp.addons.openhealth.models.commons.libs import commons_lib as lib

class ElectronicOrder(models.Model):
	"""
	Electronic Order used by Accounting TXT generator
	"""
	_name = 'openhealth.electronic.order'
	_description = "Sunat Electronic Order"
	_order = 'serial_nr asc'

	_inherit = 'openhealth.line'


# ----------------------------------------------------------- Handles -----------------------------
	# Treatment
	treatment_id = fields.Many2one(
			'openhealth.treatment',
			ondelete='cascade',
		)

	# Container
	container_id = fields.Many2one(
			'openhealth.container',
			ondelete='cascade',
		)

	# Management
	management_id = fields.Many2one(
			'openhealth.management',
			ondelete='cascade',
		)


# ----------------------------------------------------------- Relational --------------------------
	# CN Owner
	credit_note_owner = fields.Many2one(
			'sale.order',
		)

	# Lines
	electronic_line_ids = fields.One2many(
			'openhealth.electronic.line',
			'electronic_order_id',
		)



# ----------------------------------------------------------- Members -----------------------------

# ----------------------------------------------------------- Required ---------
	# Patient
	id_doc_type = fields.Char(
			string='Doc Id Tipo',
			default=".",
			required=True,
		)

	id_doc_type_code = fields.Char(
			string='Codigo',
			default=".",
			required=True,
		)

	# Order
	x_type = fields.Char(
			'Tipo',
			required=True,
		)

	type_code = fields.Char(
			'Codigo',
			required=True,
		)

	serial_nr = fields.Char(
			'Serial Nr',
			required=True,
		)

	receptor = fields.Char(
			string='Receptor',
			required=True,
		)


# ----------------------------------------------------------- Emitter ----------
	# Firm
	firm = fields.Char(
			'Firm',
			#default='SERVICIOS MÉDICOS ESTÉTICOS S.A.C',
		)

	# Ruc
	ruc = fields.Char(
			'Ruc',
			#default='20523424221',
		)

	# Ubigeo
	ubigeo = fields.Char(
			'Ubigeo',
			#default='150101',	# Verify
		)

	# Address
	address = fields.Char(
			'Address',
			#default='Av. La Merced 161',
		)

	# Country
	country = fields.Char(
			'Country',
			#default='PE',
		)

# ----------------------------------------------------------- Receptor ---------
	id_doc = fields.Char(
			'Doc Id',
			default=".",
		)

	patient = fields.Many2one(
			'oeh.medical.patient',
			string="Paciente",
		)


# ----------------------------------------------------------- Credit Note ------
	credit_note_type = fields.Selection(
			selection=ord_vars._credit_note_type_list,
			string='Motivo',
			default='cancel',
		)

	def get_credit_note_type(self):
		"""
        Gets credit note type
		"""
		_dic_cn_type = {
							'cancel': 					'Anulacion de la operacion',
							'cancel_error_ruc': 		'Anulacion por error en el RUC',
							'correct_error_desc': 		'Correccion por error en la descripcion',
							'discount': 				'Descuento global',
							'discount_item': 			'Descuento por item',
							'return': 					'Devolucion total',
							'return_item': 				'Devolucion por item',
							'bonus': 					'Bonificacion',
							'value_drop': 				'Disminucion en el valor',
							'other': 					'Otros',
							False: 						'',
					}
		return _dic_cn_type[self.credit_note_type].upper()






# ----------------------------------------------------------- Sale -------------
	currency_code = fields.Char(
			'Moneda',
			default="PEN",
		)

	state = fields.Selection(
			selection=ord_vars._state_list,
			string='Estado',
			readonly=False,
			default='draft',
		)

	# Counter Value
	counter_value = fields.Integer(
			string="Contador",
		)

	# Delta
	delta = fields.Integer(
			'Delta',
		)

	# Amount total
	amount_total = fields.Float(
			string="Total",
			digits=(16, 2),
		)

	# Amount total - Net
	amount_total_net = fields.Float(
			string="Net",
			digits=(16, 2),
		)

	# Amount total - Tax
	amount_total_tax = fields.Float(
			string="Tax",
			digits=(16, 2),
		)

	export_date = fields.Char(
			'Export Date',

			compute='_compute_export_date',
		)
	@api.multi
	def _compute_export_date(self):
		for record in self:
			record.export_date = lib.correct_date(record.x_date_created).split()[0]



# ----------------------------------------------------------- Methods ------------------------

# --------------------------------------------------------- Configurator -------
	def _get_default_configurator(self):
		# Search
		configurator = self.env['openhealth.configurator.emr'].search([
																		#('active', 'in', [True]),
											],
												#order='x_serial_nr asc',
												limit=1,
											)
		print(configurator)
		print(configurator.name)
		return configurator

	# Configurator
	configurator = fields.Many2one(
			'openhealth.configurator.emr',
			string="Configuracion",
			default=_get_default_configurator,
		)


# ----------------------------------------------------------- Electronic -------
	def get_coeff(self):
		"""
		Used by Txt Generation
		From containers.lib_exp
		"""
		coeff = lib_coeffs.get_coeff(self.state)
		return coeff


# --------------------------------------------- Constraints - Python - Dep ------
	# Check
	@api.constrains('serial_nr')
	def check_serial_nr(self):
		"""
		high level support for doing this and that.
		"""
		chk_electronic.check_serial_nr(self, self.container_id.id)




# ----------------------------------------------------------- From electronic_order_new ---------------------

# ----------------------------------------------------------- Fields ------------------------------


# ----------------------------------------------------------- Native -----------
	content = fields.Text()

	path = fields.Char()

	file_name = fields.Char()

	# Id
	id_serial_nr = fields.Char(
			'Id Serial Nr',
		)


# -------------------------------------------------------------- Required ------
	# Patient
	id_doc_type = fields.Char(
			string='Doc Id Tipo',
			default=".",
			required=True,
		)

	id_doc_type_code = fields.Char(
			string='Codigo',
			default=".",
			required=True,
		)

	# Order
	x_type = fields.Char(
			'Tipo',
			required=True,
		)

	type_code = fields.Char(
			'Codigo',
			required=True,
		)

	serial_nr = fields.Char(
			'Serial Nr',
			required=True,
		)

	receptor = fields.Char(
			string='Receptor',
			required=True,
		)



# ----------------------------------------------------------- Methods ------------------------

# ------------------------------------------------ Electronic - Create File ----
	def pl_create_file(self):
		"""
		Used by Txt Generation
		From pl_export
		"""
		print()
		print('Create File')

		# Create File
		fname = self.path + '/' + self.file_name + '.txt'
		f = io.open(fname, mode="w", encoding="utf-8")
		print(self.content, file=f)
		f.close()

		# Create Txt Line
		self.container_id.txt_ids.create({
											'name': 			self.file_name,
											'content': 			self.content,
											'container_id': 	self.container_id.id,
			})


# -------------------------------------------------------- Update Constants ----
	def update_constants(self):
		"""
		Update Electronic Order Constants:
			- Firm
		Used by Txt Generation
		"""
		print()
		print('update_constants')
        
		# Firm
		self.firm = self.configurator.company_name
		self.ruc = self.configurator.company_ruc
		self.address = self.configurator.company_address
		self.ubigeo = self.configurator.company_ubigeo
		self.country = self.configurator.company_country


# ----------------------------------------------------------- Init -------------
	def pl_init(self, id_serial_nr, path, file_name):
		"""
		Used by Txt Generation
		From pl_export
		"""
		print()
		print('Pl - Init')

		#print(self)
		#print(id_serial_nr)
		#print(path)
		#print(file_name)
		self.id_serial_nr = id_serial_nr
		self.path = path
		self.file_name = file_name
		self.configurator = self.container_id.configurator


# ------------------------------------------------- Electronic - Create TXT ----
	def pl_create_txt(self):
		"""
		Used by Txt Generation
		From pl_export
		"""
		print()
		print('pl_create_txt')

		# Content - This !!!
		self.content = pl_lib_exp.get_file_content(self)
		#print(self.content)
