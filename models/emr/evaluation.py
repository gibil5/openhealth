# -*- coding: utf-8 -*-
"""
		Evaluation

		Created: 			 1 Nov 2016
		Last updated: 	 	02 Aug 2020
"""
from __future__ import print_function
import datetime
from openerp import models, fields, api
from openerp.addons.openhealth.models.patient import pat_vars

#from openerp.addons.openhealth.models.libs import eval_vars
#from openerp.addons.openhealth.models.commons.libs import eval_vars
from . import eval_vars

from openerp.addons.openhealth.models.commons import prodvars


class Evaluation(models.Model):
	"""
	Evaluation Class
	Inherited from: OeHealth
	Used by: Consultation, Procedure, Session and Control
	"""
	_inherit = 'oeh.medical.evaluation'

# ----------------------------------------------------------- Inactive Bug -------------------------
	# Doctor
	doctor = fields.Many2one(
			'oeh.medical.physician',
			string="Médico",

			required=True, 		# Important - To avoid losing data with invalid doctors
			#required=False,			# To avoid DB inconsistencies in Lima !
		)

# ----------------------------------------------------------- Getters -------------------------
	# Get Treatment
	#@api.multi
	def get_treatment(self):
		"""
		Get Product Treatment
		Used by: Session, Control
		Respects the LOD
		"""
		return self.product.get_treatment()


# ----------------------------------------------------------- Laser ------------------------
	# Laser
	laser = fields.Selection(
			selection=prodvars._laser_type_list,
			string="Láser",

			compute='_compute_laser',
		)

	#@api.multi
	@api.depends('product')
	def _compute_laser(self):
		for record in self:
			#record.laser = record.product.x_treatment  	# 2018
			#record.laser = record.product.pl_treatment  	# 2019
			record.laser = record.get_treatment()  			# RLOD


# ----------------------------------------------------------- Dates - OK ------------------------------------------------------
	# Date
	evaluation_start_date = fields.Datetime(
			#string="Fecha y hora",
			string="Evaluation Start Date",
			#default = fields.Date.today,
			required=True,
			#readonly=True,
		)

# ----------------------------------------------------------- Configurator ------------------------

	# Default Configurator
	@api.model
	def _get_default_configurator(self):

		configurator = self.env['openhealth.configurator.emr'].search([
																			#('name', 'in', ['Historias']),
																			('x_type', 'in', ['emr']),
																		],
																			#order='date_begin,name asc',
																			limit=1,
														)
		return configurator



	#configurator = fields.Char()
	
	# Configurator
	configurator = fields.Many2one(
			'openhealth.configurator.emr',
			string="Configuracion",
			domain=[
						#('name', '=', 'Historias'),
						('x_type', '=', 'emr'),
					],

			#default=_get_default_configurator,
		)

# ----------------------------------------------------------- Relationals -------------------------
	# Treatment
	treatment = fields.Many2one(
			'openhealth.treatment',
			ondelete='cascade',
			required=True,
			readonly=True,
		)

	# Patient
	patient = fields.Many2one(
			'oeh.medical.patient',
			string="Paciente",
			ondelete='cascade',
			required=True,
			readonly=True,
		)

	# Product
	product = fields.Many2one(
			'product.template',
			string="Producto",
			domain=[
						('x_origin', '=', False),
					],
		)

# --------------------------------------------------------- Consultation First --------------------

	x_diagnosis = fields.Text(
			string='Diagnóstico',
			required=False,
			default = 'x', 
		)

	x_antecedents = fields.Text(
			string='Antecedentes médicos',
			required=False,
			default = 'x', 
		)

	x_allergies_medication = fields.Text(
			string='Alergias a medicamentos',
			required=False,
			default = 'x', 
		)

	x_observations = fields.Text(
			string='Observaciones',
			required=False,
			default = 'x', 
		)

	x_indications = fields.Text(
			string='Indicaciones',
			required=False,
			default = 'x', 
		)

	x_analysis_lab = fields.Boolean(
			string='Análisis de laboratorio',
			default=False,
			#default = 'x', 
		)

	x_examination = fields.Text(
			string='Examen clínico',
			required=False,
			default = 'x', 
		)

# ----------------------------------------------------------- Patient -------------------------
	# Sex
	patient_sex = fields.Char(
			string="Sexo",

			compute='_compute_patient_sex',
		)

	@api.multi
	def _compute_patient_sex(self):
		for record in self:
			if record.patient.sex != False:
				record.patient_sex = record.patient.sex[0]


	# Age
	patient_age = fields.Char(
			string="Edad",

			compute='_compute_patient_age',
		)

	@api.multi
	def _compute_patient_age(self):
		for record in self:
			if record.patient.age != False:
				record.patient_age = record.patient.age.split()[0]

	# City
	patient_city = fields.Char(
			string="Lugar de procedencia",
			compute='_compute_patient_city',
		)

	@api.multi
	def _compute_patient_city(self):
		for record in self:
			if record.patient.city_char != False:
				city = record.patient.city_char
				record.patient_city = city.title()










# ----------------------------------------------------------- Primitives --------------------------


	# Space
	vspace = fields.Char(
			' ',
			readonly=True
		)

	# Autofill
	x_autofill = fields.Boolean(
			string="Autofill",
			default=False,
		)

	# Done
	x_done = fields.Boolean(
			default=False,
			string="Realizado",
		)

	# State
	state = fields.Selection(
			selection=eval_vars._state_list,
			string='Estado',
			default='draft',
		)



	# Evaluation Nr
	evaluation_nr = fields.Integer(
			string="Evaluation #",
			default=1,
			required=True,
		)











# ----------------------------------------------------------- Computed ----------------------------

	# Zone
	zone = fields.Selection(
			selection=prodvars._zone_list,
			string="Zona",

			compute='_compute_zone',
		)

	#@api.multi
	@api.depends('product')
	def _compute_zone(self):
		for record in self:
			record.zone = record.product.x_zone



	# Pathology
	pathology = fields.Selection(
			selection=prodvars._pathology_list,
			string="Patología",

			compute='_compute_pathology',
		)

	#@api.multi
	@api.depends('product')
	def _compute_pathology(self):
		for record in self:
			record.pathology = record.product.x_pathology


	# Level
	level = fields.Selection(
			selection=prodvars._level_list,
			string="Nivel",

			compute='_compute_level',
		)

	#@api.multi
	@api.depends('product')
	def _compute_level(self):
		for record in self:
			record.level = record.product.x_level



	# Nr images
	nr_images = fields.Integer(
			string="Nr Visia",

			compute="_compute_nr_images",
		)

	@api.multi
	def _compute_nr_images(self):
		for record in self:
			ctr = 0
			for image in record.image_ids:
				ctr = ctr + 1
			record.nr_images = ctr



# ----------------------------------------------------------- Primitive ---------------------------

	# Chief complaint
	chief_complaint = fields.Selection(
			string='Motivo de consulta',
			selection=eval_vars._chief_complaint_list,
			required=True,
		)

	# Evaluation type
	evaluation_type = fields.Selection(
			selection=eval_vars.EVALUATION_TYPE,
			string='Tipo',
			required=True,
		)


# ----------------------------------------------------------- Actions -----------------------------

	# Open Procedure
	@api.multi
	def open_procedure(self):
		"""
		Goes Back to Procedure
		Used by: Control and Session
		"""
		print()
		print('Eval - Open Treatment')

		ret = self.procedure.open_myself()

		return ret
	# open_procedure


	# Open Treatment
	@api.multi
	def btn_open_treatment(self):
		"""
		Goes Back to Treatment
		Used by: Procedure
		"""
		#print
		#print 'Open Treatment'
		treatment = self.env['openhealth.treatment'].search([('id', '=', self.treatment.id)])
		treatment_id = treatment.id
		ret = treatment.open_myself()
		return ret
	# open_treatment

# ----------------------------------------------------------- Open Myself -------------------------
	# Open Myself
	@api.multi
	def open_myself(self):
		print()
		print('Eval - Open Myself')

		return {
			# Mandatory
			'type': 'ir.actions.act_window',
			'name': 'Open Consultation Current',
			# Window action


			#'res_model': 'openhealth.treatment',
			#'res_id': treatment_id,

			'res_model': self._name,
			'res_id': self.id,


			# Views
			"views": [[False, "form"]],
			'view_mode': 'form',
			'target': 'current',
			#'view_id': view_id,
			#"domain": [["patient", "=", self.patient.name]],
			#'auto_search': False,
			'flags': {
					#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
					'form': {'action_buttons': True, }
			},
			'context':   {}
		}
	# open_myself

