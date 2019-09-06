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




# ----------------------------------------------------------- Encode Error ------------------------

	@api.multi
	def encode_error(self):
		print()
		print('Encode Error')

		#name = "ECOGRAFIAS MUSCULOESQUELETICAS - Muñeca (Unilateral) - 1 sesion"

		print(self.name)


	@api.multi
	def fix_encode_error(self):
		"""
		Fix Encode Error
		"""
		print()
		print('Fix Encode Error')

		#self.name.replace("ñ", "nh")
		#self.name.replace(u"ñ", "nh")
		self.name = self.name.replace(u"ñ", "nh")

		print('Finished !')




# ----------------------------------------------------------- Fix ------------------------

	@api.multi
	def fix_procurements(self):
		"""
		Fix Procurements
		Set State to Cancel. For Manual Cancellation.
		"""
		print()
		print('Fix Procurements')


		procs = self.env['procurement.order'].search([
															#('type', 'in', ['product']),
															#('sale_ok', 'in', [True]),
												],
													#order='name asc',
													#limit=1,
												)

		for procurement in procs:
			#print()
			#print(procurement)
			#print(procurement.name)
			#print(procurement.state)
			#procurement.unlink()
			procurement.state = 'cancel'
		
		print('Finished !')



	@api.multi
	def fix_stock(self):
		"""
		Cancels stock moves
		Remove manually
		"""
		print('Fix fstock')

		# Search
		moves = self.env['stock.move'].search([
													#('x_name_short', 'in', [name]),
												],
												#order='date_begin asc',
												#limit=10,
											)
		for stock_move in moves:
			#print()
			#print(stock_move)
			#print(stock_move.name)
			#print(stock_move.state)
			#stock_move.unlink()
			stock_move.state = 'cancel'

		print('Finished !')

	# clean_stock_moves




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
