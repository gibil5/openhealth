# -*- coding: utf-8 -*-
"""
 		*** Product Template

 		Created: 			   Nov 2016
		Last up: 	 		 5 Nov 2018
"""
from openerp import models, fields, api
from openerp.exceptions import ValidationError
import prodvars
import lib
import gen
import gen_tic

class Product(models.Model):
	"""
	high level support for doing this and that.
	"""
	_inherit = 'product.template'

	_order = 'x_name_short'



# ----------------------------------------------------------- Unfix  --------------------------------
	# Fix Name
	@api.multi
	def unfix_name(self):
		"""
		high level support for doing this and that.
		"""
		print
		print 'Unfix Name'

		self.name = self.x_name_unfixed




# ----------------------------------------------------------- Fix  --------------------------------
	# Fix Name
	@api.multi
	def fix_name(self):
		"""
		high level support for doing this and that.
		"""
		print
		print 'Fix Name'


		# Array Name
		name_arr = self.name.split('-')


		# Co2
		if self.x_treatment in ['laser_co2']:

			# To avoid repetition
			if len(name_arr) == 4:

				# Unfixed
				if self.x_name_unfixed in [False, '']:
					self.x_name_unfixed = self.name

				# Fix
				self.name = self.name.replace(" - 1", "")


		# Exc
		if self.x_treatment in ['laser_excilite', 'laser_ipl', 'laser_ndyag']:

			# Unfixed
			if self.x_name_unfixed in [False, '']:
				self.x_name_unfixed = self.name

			# Fix
			self.name = self.x_generated




		# Cosmetolgy
		if self.x_family in ['cosmetology']:

			# Unfixed
			if self.x_name_unfixed in [False, '']:
				self.x_name_unfixed = self.name

			# Fix
			self.name = self.x_generated






# ----------------------------------------------------------- Codes -------------------------------

	x_name_unfixed = fields.Char()


	# Name Short
	x_name_short = fields.Char()


	# Counter
	x_counter = fields.Integer(
			'Counter',
		)

	# Code
	x_code = fields.Char(
			'Code',
		)


	# For Tickets
	x_name_ticket = fields.Char(
			default="x",

			compute='_compute_x_name_ticket',
		)

	@api.multi
	#@api.depends('state')
	def _compute_x_name_ticket(self):
		"""
		high level support for doing this and that.
		"""
		for record in self:
			record.x_name_ticket = gen_tic.gen_ticket_name(self, record.x_treatment, record.x_zone, record.x_pathology, record.x_family, record.type, record.x_name_short)







# Relaxed ! - For Prod
# ----------------------------------------------------------- Constraints - Sql -------------------

	#_sql_constraints = [
	#						('name_unique','unique(name)', 'SQL Warning: name must be unique !'),
	#						('x_name_short_unique','unique(x_name_short)', 'SQL Warning: x_name_short must be unique !'),
	#						('x_code_unique','unique(x_code)', 'SQL Warning: x_code must be unique !'),
	#					]




# ----------------------------------------------------------- Constraints - Python ----------------
	# Check Name
	@api.constrains('name')
	def _check_name(self):
		"""
		high level support for doing this and that.
		"""

		if False:
		#if True:
			for record in self:

				#if record.name == '0':
				#	raise ValidationError("C Warning: Default code not valid: %s" % record.name)

				# Count
				if record.name != False:
					count = self.env['product.template'].search_count([
																		('name', '=', record.name),
												])
					if count > 1:
						raise ValidationError("Rec Warning: NAME already exists: %s" % record.name)

			# all records passed the test, don't return anything



	# Check Default Code
	@api.constrains('default_code')
	def _check_default_code(self):
		"""
		high level support for doing this and that.
		"""

		if False:
		#if True:
			for record in self:

				if record.default_code == '0':
					raise ValidationError("C Warning: Default code not valid: %s" % record.default_code)

				# Count
				if record.default_code != False:
					count = self.env['product.template'].search_count([
																		('default_code', '=', record.default_code),
												])
					if count > 1:
						raise ValidationError("Rec Warning: DEFAULT CODE already exists: %s" % record.default_code)

		# all records passed the test, don't return anything




	# Check Type
	@api.constrains('type')
	def _check_type(self):

		if False:
		#if True:
			for record in self:
				if record.type == 'consu':
					raise ValidationError("Rec Warning: TYPE not valid: %s" % record.type)

				# Count
				#if record.type != False:
				#	count = self.env['product.template'].search_count([
				#														('type', '=', 'consu'),
				#								])
				#	if count > 0:
				#		raise ValidationError("C Warning: Type already exists: %s" % record.type)

			# all records passed the test, don't return anything





	# Check Code
	@api.constrains('x_code')
	def _check_x_code(self):

		if False:
		#if True:
			for record in self:

				#if record.name == '0':
				#	raise ValidationError("C Warning: Default code not valid: %s" % record.name)

				# Count
				if record.x_code != False:
					count = self.env['product.template'].search_count([
																		('x_code', '=', record.x_code),
												])
					if count > 1:
						raise ValidationError("Rec Warning: CODE already exists: %s" % record.x_code)

			# all records passed the test, don't return anything






# ----------------------------------------------------------- Checksum ----------------------------

	# Checksum 1 - Generated vs Name
	x_checksum_1 = fields.Char(
			'Checksum 1',

			compute='_compute_checksum_1',
		)
	@api.multi
	def _compute_checksum_1(self):
		for record in self:
			record.x_checksum_1 = lib.get_checksum_gen(record.x_generated, record.name)




	# Checksum 2 - Ticket Compact Name
	x_checksum_2 = fields.Char(
			'Checksum 2',

			compute='_compute_checksum_2',
		)
	@api.multi
	def _compute_checksum_2(self):
		for record in self:
			record.x_checksum_2 = lib.get_checksum_tic(record.x_name_ticket)





	# Generated
	x_generated = fields.Char(
			'Generated',

			compute='_compute_generated',
		)
	@api.multi
	def _compute_generated(self):

		treatments = ['laser_excilite', 'laser_ipl', 'laser_ndyag']

		for record in self:

			# Co2
			if record.x_treatment in ['laser_co2']:
				record.x_generated = gen.get_generated_co2(record.x_name_short)

			# Exc, Ipl Ndyag
			elif record.x_treatment in treatments:
				record.x_generated = gen.get_generated_exc(record.x_name_short)

			# Consultation
			elif record.x_treatment in ['consultation']:
				record.x_generated = gen.get_generated_con(record.x_name_short)

			# Medical
			elif record.x_family in ['medical']:
				record.x_generated = gen.get_generated_med(record.x_name_short)

			# Cosmeto
			elif record.x_family in ['cosmetology']:
				record.x_generated = gen.get_generated_exc(record.x_name_short)

			# Products
			elif record.type in ['product']:
				record.x_generated = gen.get_generated_prod(record.x_name_short)

			# Quick
			elif record.x_treatment in ['laser_quick']:
				record.x_generated = gen.get_generated_quick(record.x_name_short)








# ----------------------------------------------------------- Relational --------------------------
	# Coder
	x_coder = fields.Many2one(
			'openhealth.coder',
			'Coder',
		)

	# Categ
	categ_id = fields.Many2one(
			'product.category',
			'Internal Category',
			#required=True,
			required=False,
			change_default=True,
			domain="[('type','=','normal')]",
			help="Select category for the current product"
		)






# ----------------------------------------------------------- Canonical ---------------------------
	# Unit of measure
	uom = fields.Many2one(
			'product.uom',
			required=False,
		)

	# Origin
	x_origin = fields.Selection(
		[
			('legacy', 'Legacy'),
			('test', 'Test'),
			('production', 'Production'),
		],
			required=False,
		)

	# Price Vip
	x_price_vip = fields.Float(
			required=False,
		)


	# Price Vip Return
	x_price_vip_return = fields.Float(
			required=False,
		)

	# Level
	x_level = fields.Selection(
			selection=prodvars._level_list,
			required=False,
		)

	# Family
	x_family = fields.Selection(
			selection=prodvars._family_list,
			required=False,
		)

	# Treatment
	x_treatment = fields.Selection(
			selection=prodvars._treatment_list,
			required=False,
		)

	# Zone
	x_zone = fields.Selection(
			selection=prodvars._zone_list,
			required=False,
		)

	# Pathology
	x_pathology = fields.Selection(
			selection=prodvars._pathology_list,
			required=False,
		)

	# Sessions
	x_sessions = fields.Char(
			default="",
			required=False,
		)

	# Time
	x_time = fields.Char(
			selection=prodvars._time_list,
			required=False,
		)







# ----------------------------------------------------------- Actions -----------------------------
	# Update
	@api.multi
	def update_level(self):
		"""
		high level support for doing this and that.
		"""
		#print 'jx'
		#print 'Update Product'
		self.x_level = self.x_pathology[-1]
		#print self.x_level
	# update_level
