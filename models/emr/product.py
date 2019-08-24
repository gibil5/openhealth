# -*- coding: utf-8 -*-
"""
		*** Product Template

		Created: 			    Nov 2016
		Last up: 	 		  9 Apr 2019
"""
from __future__ import print_function
from openerp import models, fields, api
from openerp.exceptions import ValidationError
from openerp.addons.openhealth.models.libs import lib
from . import prodvars
#from . import gen  		# Dep 2019
#from . import gen_tic   	# Dep 2019

class Product(models.Model):
	"""
	high level support for doing this and that.
	"""
	_inherit = 'product.template'

	_order = 'name'




# ----------------------------------------------------------- Price List ------------------------

	pl_price_list = fields.Selection(
			[
				('2019', '2019'),
				('2018', '2018'),
			],
			string='Lista de Precios',
		)




# ----------------------------------------------------------- Canonical -------------------------------
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

	# Level
	x_level = fields.Selection(
			selection=prodvars._level_list,
			required=False,
		)

	# Time
	x_time = fields.Char(
			selection=prodvars._time_list,
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


# ----------------------------------------------------------- Test -------------------------------
	x_test = fields.Boolean(
			'Test',
		)

# ----------------------------------------------------------- Account -----------------------------

	x_name_account = fields.Char(
			'Name Account',
		)

	x_code_account = fields.Char(
			'Code Account',
		)

	vspace = fields.Char(
			' ',
			readonly=True
		)

# ----------------------------------------------------------- Codes -------------------------------
	# Code
	x_code_acc = fields.Char(
			'Code Acc',
		)

	# Get Code
	@api.multi
	def get_code(self):
		"""
		high level support for doing this and that.
		"""
		#print
		#print 'Get Code'

		coder = self.env['openhealth.coder'].search([
															('type', 'in', ['product']),
															('sale_ok', 'in', [True]),
												],
													order='name asc',
													#limit=1,
												)




# ----------------------------------------------------------- Unfix  ------------------------------
	@api.multi
	def unfix_name(self):
		"""
		high level support for doing this and that.
		"""
		#print
		#print 'Unfix Name'

		if self.x_name_unfixed not in [False, '']:
			self.name = self.x_name_unfixed

		if self.x_treatment in ['laser_quick']:
			if self.x_short_unfixed not in [False, '']:
				self.x_name_short = self.x_short_unfixed




# ----------------------------------------------------------- Fix  --------------------------------
	@api.multi
	def fix_name(self):
		"""
		high level support for doing this and that.
		"""
		#print
		#print 'Fix Name'

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
				if self.x_go_flag:
					self.name = self.name.replace(" - 1", "")


		# Exc
		if self.x_treatment in ['laser_excilite', 'laser_ipl', 'laser_ndyag']:

			# Unfixed
			if self.x_name_unfixed in [False, '']:
				self.x_name_unfixed = self.name

			# Fix
			if self.x_go_flag:
				self.name = self.x_generated



		# Cosmetolgy
		if self.x_family in ['cosmetology']:

			# Unfixed
			if self.x_name_unfixed in [False, '']:
				self.x_name_unfixed = self.name

			# Fix
			if self.x_go_flag:
				self.name = self.x_generated




		# Quick
		if self.x_treatment in ['laser_quick']:

			# Unfixed
			if self.x_name_unfixed in [False, '']:
				self.x_name_unfixed = self.name


			# Init
			short_arr = self.x_name_short.split('_')

			# Correct the Short Name
			if short_arr[0] in ['quick']:	# To avoid repetition

				# Unfixed
				if self.x_short_unfixed in [False, '']:
					self.x_short_unfixed = self.x_name_short

				short = self.x_name_short
				short_old = short

				for tup in [
								('quick', 'qui'),
								('face_all_hands', 'faa-han'), ('face_all_neck', 'faa-nec'), ('neck_hands', 'nec-han'),
								('body_local', 'bol'), ('face_local', 'fal'), ('face_all', 'faa'),
								('hands', 'han'), ('neck', 'nec'), ('cheekbones', 'che'),
								('rejuvenation', 'rej'), ('acne_sequels', 'acs'), ('scar', 'sca'),
								('mole', 'mol'), ('stains', 'sta'), ('keratosis', 'ker'), ('cyst', 'cys'),
								('tatoo', 'tat'), ('wart', 'war'),
								('1', '5m_one'),
								('2', '15m_one'),
								('3', '30m_one'),
								('4', '45m_one'),
							]:

					old = tup[0]
					new = tup[1]
					short = short.replace(old, new)

				# Fix Short
				if self.x_go_flag:
					self.x_name_short = short


			# Fix
			if self.x_go_flag:
				self.name = self.x_generated




# ----------------------------------------------------------- Codes -------------------------------
	# Go Flag
	x_go_flag = fields.Boolean()

	# Name Unfixed
	x_name_unfixed = fields.Char()

	# Short Name Unfixed
	x_short_unfixed = fields.Char()

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




# ----------------------------------------------------------- Test Computes --------------------------------
	# Test 
	@api.multi 
	def test_computes(self):
		#print()
		print('Product - Test Computes')

		print(self.x_name_ticket)
		print(self.x_generated)
		print(self.x_checksum_1)
		print(self.x_checksum_2)




# ----------------------------------------------------------- Test --------------------------------
	# Test 
	@api.multi 
	def test(self):
		#print()
		print('Product - Test')

		# Test Unit
		self.test_computes()
		#self.test_actions()
		#self.test_services()

	# test 




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
