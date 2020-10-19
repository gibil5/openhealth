# -*- coding: utf-8 -*-
"""
	Configurator - EMR
	Created: 			25 jan 2019
	Last updated: 		11 oct  2020
"""
from __future__ import print_function
from openerp import models, fields, api

class ConfiguratorEmr(models.Model):
	"""
	Permits Multi Company behavior.
	Configuration can be done for:
		- Ticket content.
		- Electronic Billing,
		- Laser procedures,
		- Error validation,
		- CSV path for product input,
		- Holidays,
		- Opening hours.
	"""
	_name = 'openhealth.configurator.emr'
	_description = 'Configurator Emr'

# ----------------------------------------------------------- Getters ----------
	def get_number(self, laser, evaluation):
		"""
		Get nr controls, for controls and sessions.
		Used by procedure.
		"""

		dic_control = {	
				'laser_co2': self.nr_controls_co2, 
				'laser_quick': self.nr_controls_quick, 
				'laser_exc': self.nr_controls_exc, 
				'laser_ipl': self.nr_controls_ipl, 
				'laser_ndyag': self.nr_controls_ndyag 
				}
		dic_session = {	
				'laser_co2': self.nr_sessions_co2, 
				'laser_quick': self.nr_sessions_quick, 
				'laser_exc': self.nr_sessions_exc, 
				'laser_ipl': self.nr_sessions_ipl, 
				'laser_ndyag': self.nr_sessions_ndyag 
				}

		number = 0
		
		if evaluation == 'control':
			if laser in dic_control:
				number = dic_control[laser]

		elif evaluation == 'session':
			if laser in dic_session:
				number = dic_session[laser]

		return number

# --------------------------------------------- Companuy - Ticket and TXT ------
	# Company
	company_name = fields.Char(
			required=True,
			default="SERVICIOS MÉDICOS ESTÉTICOS S.A.C",
		)

	company_address = fields.Char(
			required=True,
			default="Av. La Merced 161",
		)

	company_phone = fields.Char(
			required=True,
			default="Teléfono: (051) 321 2394",
		)

	company_ruc = fields.Char(
			required=True,
			default="20523424221",
		)

	company_ubigeo = fields.Char(
			required=True,
			default="150101",
		)

	company_country = fields.Char(
			required=True,
			default="PE",
		)

	company_account = fields.Char(
			required=True,
			default="6",
		)

	# Ticket
	company_website = fields.Char(
			required=True,
			default="https://www.clinicachavarri.com/",
		)

	company_email = fields.Char(
			required=True,
			default="info@clinicachavarri.com",
		)

	ticket_company_address = fields.Char(
			required=True,
			default="Av. La Merced 161 Miraflores - Lima",
		)

	ticket_company_ruc = fields.Char(
			required=True,
			default="R.U.C.: 20523424221",
		)

	ticket_note = fields.Text(
			required=True,
			default="Esto es una nota para el ticket.",
		)

	ticket_description = fields.Text(
			required=True,
			default="Representación impresa generada por SERVICIOS MÉDICOS ESTÉTICOS S.A.C.",
		)

	ticket_warning = fields.Text(
			required=True,
			default="Por medio del presente, se informa que en caso de cancelación de tratamiento o de la consulta por parte del paciente, ya sea de manera expresa o tácita, este autoriza a la empresa la retención del 15%% del costo del tratamiento o el 25%% de la consulta, sea el caso, por concepto de gastos administrativos y gastos operativos. (Art. 67 Ley 29571, Art 40 Ley General de Salud",
		)

	#warning = fields.Text(			# dep
			#required=True,
	#	)

# ----------------------------------------------------------- Order Admin ------
	order_admin = fields.Many2one(
			'openhealth.order.admin',
			#string='Venta',
		)

# ----------------------------------------------------------- PL - Paths -------
	path_account_txt = fields.Char(
			required=True,
			default='/Users/gibil/mssoft/ventas/'
		)

	path_csv_pricelist = fields.Char(
			required=True,
			default='/Users/gibil/cellar/github/price_list/csv/',
		)

# ----------------------------------------------------------- Patients ---------
	# Patient Limit
	patient_limit = fields.Integer(
		)

# ----------------------------------------------------------- Relational -------
	# Doctor Line
	doctor_line = fields.One2many(
			'openhealth.doctor',
			'configurator_id',
		)

# ----------------------------------------------------------- Fix --------------
	@api.multi
	def config_doctors(self):
		"""
		Configure Doctors
		Using configurator data
		"""
		print()
		print('Configure Doctors')
		print(self.name)

		#procs = self.env['procurement.order'].search([
															#('sale_ok', 'in', [True]),
		#										],
													#order='name asc',
													#limit=1,
		#										)

		count = 0
		for doctor in self.doctor_line:
			#print()
			#print(doctor.physician.name)
			#print(doctor.physician.active)
			doctor.physician.active = doctor.x_active
			count = count + 1
			#print(count)
		print('Finished !')
	# config_doctors

# ----------------------------------------------------------- PL - Redefined -------------------------------

	name = fields.Selection(
			[
				('Lima', 'Sede Lima'),
				('Tacna', 'Sede Tacna'),
			],
			string="Nombre",
			required=True,

			default="Lima",
		)

	x_type = fields.Selection(
			[
				('emr', 'Clinica'),
			],
			string="Tipo",
			required=True,

			default="emr",
		)

	vspace = fields.Char(
			' ',
			readonly=True,
		)

# ----------------------------------------------------------- PL - Account Contasis ---------------
	cuentab_services = fields.Char(
			'Cuentab Servicios',
			#required=True,
		)

	cuentab_products = fields.Char(
			'Cuentab Productos',
			#required=True,
		)

	cuentab_consu = fields.Char(
			'Cuentab Consumibles',
			#required=True,
		)

# ----------------------------------------------------------- PL - Error Validation -----------------

	error_validation_electronic = fields.Boolean(
			'Validacion de Errores Electronico',
			default=True,
		)

	error_validation_patient = fields.Boolean(
			'Validacion de Errores Paciente',
			default=True,
		)

	error_validation_order = fields.Boolean(
			'Validacion de Errores Venta',
			default=True,
		)

	error_validation_product = fields.Boolean(
			'Validacion de Errores Producto',
			default=True,
		)

	error_validation_management = fields.Boolean(
			'Validacion de Errores Reporte MGT',
			default=True,
		)

	error_validation_marketing = fields.Boolean(
			'Validacion de Errores Reporte MKT',
			default=True,
		)

# ----------------------------------------------------------- Relational - Holidays ----------------
	# Day Line
	#day_line = fields.One2many(
	#		'openhealth.management.day.line',
	#		'configurator_emr_id',
	#	)


# ----------------------------------------------------------- Medical ------------------------------

	# Nr Controls
	nr_controls_co2 = fields.Integer(
			'Co2',
			default=-1,
		)

	nr_controls_quick = fields.Integer(
			'Quick',
			default=-1,
		)

	nr_controls_exc = fields.Integer(
			'Exc',
			default=-1,
		)

	nr_controls_ipl = fields.Integer(
			'Ipl',
			default=-1,
		)

	nr_controls_ndyag = fields.Integer(
			'Ndyag',
			default=-1,
		)

	# Nr Sessions
	nr_sessions_co2 = fields.Integer(
			'Co2',
			default=-1,
		)

	nr_sessions_quick = fields.Integer(
			'Quick',
			default=-1,
		)

	nr_sessions_exc = fields.Integer(
			'Exc',
			default=-1,
		)

	nr_sessions_ipl = fields.Integer(
			'Ipl',
			default=-1,
		)

	nr_sessions_ndyag = fields.Integer(
			'Ndyag',
			default=-1,
		)

# ----------------------------------------------------------- Opening Hours ------------------------------
	# Dates
	date_open = fields.Datetime(
			'Hora Apertura',
			default=fields.Date.today,
		)

	date_close = fields.Datetime(
			'Hora Cierre',
			default=fields.Date.today,
		)

# ----------------------------------------------------------- Get Inactive Days -------------------------------
	def get_inactive_days(self):
		"""
		LOD friendly.
		Gets Inactive Days. From Configurator. 
		"""
		#print()
		#print('Configurator - Get Inactive Days')
		days_inactive = []
		if self.name not in [False]:		
			for day in self.day_line:								# Respects the LOD
				if day.holiday:
					days_inactive.append(day.date)
		return days_inactive
