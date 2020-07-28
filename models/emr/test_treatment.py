# -*- coding: utf-8 -*-
"""
	*** Test Treatment - openhealth
		Created: 			14 Aug 2018
		Last up: 	 		28 Jul 2020
		Used by:			treatment.py
"""
from __future__ import print_function
from openerp.addons.price_list.models.lib import test_funcs
from openerp import _
from openerp.exceptions import Warning as UserError
#from . import exc_tre

# ----------------------------------------------------------- First Level - Buttons ---------------------------------------------

# ----------------------------------------------- Test Integration --------------------------------
def test_integration_treatment(self):
	"""
 	Integration Tests for the Treatment Class.
	"""
	print()
	#print('Test Integration Function')
	print('OH - test_treatment.py - test_integration_treatment')

	# Handle Exceptions
	#exc_tre.handle_exceptions(self)

	# Create Consultation
	create_consultation(self)

	# Create Credit Note
	if self.x_test_scenario in ['credit_note']:
		create_credit_note(self)

	# Create Block Flow
	elif self.x_test_scenario in ['block_flow']:
		create_block_flow(self)

	# Recommendations and Sale
	else:
		create_recommentations_and_procedure_sale(self)

# test_integration_treatment


# ----------------------------------------------- 2nd level --------------------------------

# ----------------------------------------------- Consultation ------------------------------------
def create_consultation(self):
	"""
	Create Consultation
	"""
	msg = 'OH - test_treatment - create_consultation'
	print()
	print(msg)

	#test_funcs.disablePrint()

	# Create Consultation Sale
	self.create_order_con()			# Actual Button
	for order in self.order_ids:
		if order.state in ['draft']:
			order.pay_myself()

	# Create and Fill Consultation
	self.create_consultation()
	for consultation in self.consultation_ids:
		consultation.autofill()

	#test_funcs.enablePrint()


def create_credit_note(self):
	"""
	Create Credit Note
	"""
	msg = 'Create Credit Note'
	print()
	print(msg)
	for order in self.order_ids:
		if order.state in ['sale']:
			order.create_credit_note()
			order.cancel_order()

def create_block_flow(self):
	"""
	Create Block Flow
	"""
	msg = 'Create Block Flow'
	print()
	print(msg)
	print('Create Block Flow')
	for order in self.order_ids:
		if order.state in ['sale']:
			order.block_flow()

def create_recommentations_and_procedure_sale(self):
	"""
	Create Recommendations and Procedure Sale
	"""
	msg = 'Create Recommendations and Procedure Sale'
	print()
	print(msg)

	# 2019
	if self.test_pricelist_2019:
		create_recommendations_2019(self)
		self.create_order_pro()				# Actual Button - 2019

	# 2018
	if self.test_pricelist_2018:
		create_recommendations_2018(self)
		#test_funcs.disablePrint()
		print()
		print()
		self.create_order_pro_2018()		# Actual Button - 2018
		#test_funcs.enablePrint()

	# Pay Order Procedure
	test_funcs.disablePrint()

	#print()
	#print('Create Order - Procedure')
	for order in self.order_ids:
		if order.state in ['draft']:
			#print('mark 10')
			try:
				order.pay_myself()
			except:
				print("An exception occurred")
			#print('mark 11')
	test_funcs.enablePrint()

# ----------------------------------------------- 3nd level --------------------------------


# ----------------------------------------------- Test Cycle --------------------------------
def test_create_budget_consultation(self):
	"""
	Test
	"""
	print()
	print('Test Create Budget Consultation')

	# Create Budget Consultation
	self.create_order_con()			# Actual Button

def test_create_sale_consultation(self):
	"""
	Test
	"""
	print()
	print('Test Create Sale Consultation')

	# Pay Budget Consultation
	for order in self.order_ids:
		if order.state in ['draft']:
			order.pay_myself()

def test_create_recommendations(self):
	"""
	Test
	"""
	print()
	print('Test Create Recommendations')

	name_dic = {
					# Lasers
					'co2': 		'LASER CO2 FRACCIONAL - Cuello - Rejuvenecimiento - Grado 1 - 1 sesion',	# Co2
		}


	model_dic = {
					'co2': 		'price_list.service_co2',
		}



	tst_list = [
					'co2',
	]

	# Loop
	for tst in tst_list:

		# Init
		name = name_dic[tst]
		model = model_dic[tst]

		# Search
		product = self.env['product.template'].search([
															('name', '=', name),
															('pl_price_list', 'in', ['2019']),
											],
												#order='date_order desc',
												limit=1,
									)
		# Manage Exception
		try:
			product.ensure_one()

		except:
			#print("An exception occurred")
			msg_name = "ERROR: Record Must be One Only."
			class_name = type(product).__name__
			obj_name = name
			msg =  msg_name + '\n' + class_name + '\n' + obj_name
			raise UserError(_(msg))



		product_id = product.id

		print()
		print(product)
		print(product.name)


		# Create
		service = self.env[model].create({
														'service': 			product_id,
														'family': 			product.pl_family,
														'subfamily': 		product.pl_subfamily,
														'zone': 			product.pl_zone,
														'pathology': 		product.pl_pathology,
														'sessions': 		product.pl_sessions,
														'level': 			product.pl_level,
														'time': 			product.pl_time,
														'price_applied': 	product.list_price,
														'sel_zone': 		product.pl_zone,
														'pl_treatment': 	product.pl_treatment,

														'treatment': 		self.id,
											})
# test_create_recommendations


def test_create_budget_procedure(self):
	"""
	Test
	"""
	print()
	print('Test Create Budget Procedure')

	# Pay Budget Procedures
	self.create_order_pro()				# Actual Button - 2019


def test_create_sale_procedure(self):
	"""
	Test
	"""
	print()
	print('Test Create Sale Procedure')

	# Pay Budget Procedures
	for order in self.order_ids:
		if order.state in ['draft']:
			try:
				order.pay_myself()
			except:
				print("An exception occurred")


def test_create_procedure(self):
	"""
	Test
	"""
	print()
	print('Test Create Procedure')

	# Create Procedure
	self.create_procedure_man()



def test_create_sessions(self):
	"""
	Test
	"""
	print()
	print('Test Create Sessions')

	# Create Sessions
	for procedure in self.procedure_ids:
		print(procedure)
		#for _ in range(2):
		for _ in range(1):
			print('create sesion')
			procedure.create_sessions_manual()



def test_create_controls(self):
	"""
	Test
	"""
	print()
	print('Test Create Controls')

	# Create Controls
	for procedure in self.procedure_ids:
		print(procedure)
		#for _ in range(1):
		for _ in range(6):
			print('create control')
			procedure.create_controls_manual()








# ----------------------------------------------------------- Second Level ---------------------------------------------










# ----------------------------------------------- Sessions -------------------------------------
def create_sessions(self):
	"""
	Create Sessions
	"""
	#print('Create Sessions')
	for procedure in self.procedure_ids:
		#for _ in range(2):
		for _ in range(1):
			procedure.create_sessions()


# ----------------------------------------------- Controls -------------------------------------
def create_controls(self):
	"""
	Create Controls
	"""
	#print('Create Controls')
	for procedure in self.procedure_ids:
		#for _ in range(1):
		for _ in range(6):
			procedure.create_controls()



# ----------------------------------------------------------- Create Recommendations - 2019 --------------
def create_recommendations_2019(self):
	"""
	Create Recommendations 2019
	Test Cases
	Be sure to cover:
		- All Families.
		- All Sub Families.
		- All Sub sub Families.
	"""
	print()
	print('Create Recommendations 2019')

	# Init

	#price_list = '2019'

	name_dic = {
					# Products
					'prod_0':		'ACNETOPIC 200ML',				# Topic
					'prod_1':		'KIT POST LASER CO2 COOPER',	# Kit
					'prod_2':		'TARJETA VIP',					# Card
					'prod_3':		'OTROS',						# Other
					'prod_4':		'COMISION DE ENVIO',			# Comission


					# Lasers
					'co2': 		'LASER CO2 FRACCIONAL - Cuello - Rejuvenecimiento - Grado 1 - 1 sesion',	# Co2
					'exc':		'LASER EXCILITE - Abdomen - Alopecias - 1 sesion - 15 min',					# Excilite
					'ipl':		'LASER M22 IPL - Abdomen - Depilacion - 1 sesion - 15 min',					# Ipl
					'ndy':		'LASER M22 ND YAG - Localizado Cuerpo - Hemangiomas - 1 sesion - 15 min',	# Ndyag
					'qui':		'QUICKLASER - Cuello - Rejuvenecimiento - Grado 1 - 1 sesion',				# Quick


					# Cosmetology
					'cos_0':		'CARBOXITERAPIA - Cuerpo - Rejuvenecimiento - 1 sesion - 30 min',				# Carboxitherapy
					'cos_1':		'PUNTA DE DIAMANTES - Rostro - Limpieza profunda - 1 sesion - 30 min',			# Diamond Tip
					'cos_2':		'LASER TRIACTIVE + CARBOXITERAPIA - Rostro + Papada + Cuello - Reafirmacion - 10 sesiones - 30 min',	# Laser Triactive + Carbo
					#'cos_1':		'',			# Carboxitherapy


					# Medical
					'med_0':		'BOTOX - 1 Zona - Rejuvenecimiento Zona - 1 sesion',										# Botox
					'med_1':		'CRIOCIRUGIA - Todo Rostro - Acne - 1 sesion',												# Cryo
					'med_2':		'ACIDO HIALURONICO - 1 Jeringa - Rejuvenecimiento Facial - 1 sesion - FILORGA UNIVERSAL',	# Hialuronic

					'med_3':		'INFILTRACIONES',																			# Infil
					'med_4':		'MESOTERAPIA NCTF - Todo Rostro - Rejuvenecimiento Facial - 5 sesiones',					# Meso
					'med_5':		'PLASMA - Todo Rostro - Rejuvenecimiento Facial - 1 sesion',								# Plasma

					'med_6':		'REDUX - 1 Zona - Rejuvenecimiento Zona - 1 sesion',										# Redux
					'med_7':		'ESCLEROTERAPIA - Piernas - Varices - 1 sesion',											# Sclero


					'med_8':		'VITAMINA C ENDOVENOSA',																	# Vitamin
					#'med_8':		'VICTAMINA C ENDOVENOSA',																	# Vitamin


					#'med_1':		'',			# Plasma



					# New Services
					'gyn':		'LASER CO2 FRACCIONAL - Monalisa Touch / Revitalizacion',
					'echo':		'ECOGRAFIAS ESPECIALES - Cadera Pediatrica (Bilateral) - 1 sesion',
					'prom':		'CARBOXITERAPIA - Localizado Cuerpo - Rejuvenecimiento Facial - 6 sesiones',
					#'gyn':		'ANALISIS - Vagina - Biopsias',
		}


	model_dic = {
					'prod_0': 	'price_list.service_product',
					'prod_1': 	'price_list.service_product',
					'prod_2': 	'price_list.service_product',
					'prod_3': 	'price_list.service_product',
					'prod_4': 	'price_list.service_product',


					'co2': 		'price_list.service_co2',
					'exc': 		'price_list.service_excilite',
					'ipl': 		'price_list.service_ipl',
					'ndy': 		'price_list.service_ndyag',
					'qui': 		'price_list.service_quick',

					'cos_0': 		'price_list.service_cosmetology',
					'cos_1': 		'price_list.service_cosmetology',
					'cos_2': 		'price_list.service_cosmetology',



					'med_0': 		'price_list.service_medical',
					'med_1': 		'price_list.service_medical',
					'med_2': 		'price_list.service_medical',

					'med_3': 		'price_list.service_medical',
					'med_4': 		'price_list.service_medical',
					'med_5': 		'price_list.service_medical',

					'med_6': 		'price_list.service_medical',
					'med_7': 		'price_list.service_medical',
					'med_8': 		'price_list.service_medical',



					'gyn': 		'price_list.service_gynecology',
					'echo': 	'price_list.service_echography',
					'prom': 	'price_list.service_promotion',
		}



	tst_list_all = [
					'prod_0',
					'prod_1',
					'prod_2',
					'prod_3',
					'prod_4',

					'co2',
					'exc',
					'ipl',
					'ndy',
					'qui',

					#'cos',
					'cos_0',
					'cos_1',
					'cos_2',


					'med_0',
					'med_1',
					'med_2',

					'med_3',
					'med_4',
					'med_5',

					'med_6',
					'med_7',
					'med_8',


					'gyn',
					'echo',
					'prom',
	]



	tst_list_product = [
					'prod_0',
					'prod_1',
					'prod_2',
					'prod_3',
					'prod_4',
	]

	tst_list_laser = [
					'co2',
					#'exc',
					#'ipl',
					#'ndy',
					#'qui',
	]

	tst_list_cosmetology = [
					#'cos',
					'cos_0',
					'cos_1',
					'cos_2',
	]

	tst_list_medical = [
					'med_0',
					'med_1',
					'med_2',

					'med_3',
					'med_4',
					'med_5',

					'med_6',
					'med_7',
					'med_8',
	]

	tst_list_new = [
					'gyn',
					'echo',
					'prom',
	]



	tst_list_empty = []



	if self.x_test_scenario in ['all']:
		tst_list = tst_list_all

	elif self.x_test_scenario in ['product']:
		tst_list = tst_list_product

	elif self.x_test_scenario in ['laser']:
		tst_list = tst_list_laser

	elif self.x_test_scenario in ['cosmetology']:
		tst_list = tst_list_cosmetology

	elif self.x_test_scenario in ['medical']:
		tst_list = tst_list_medical

	elif self.x_test_scenario in ['new']:
		tst_list = tst_list_new


	elif self.x_test_scenario in [False]:
		tst_list = tst_list_empty



	# Loop
	#for tst in tst_list_all:
	for tst in tst_list:

		# Init
		name = name_dic[tst]

		model = model_dic[tst]

		# Search
		product = self.env['product.template'].search([
															('name', '=', name),
															('pl_price_list', 'in', ['2019']),
															#('pl_price_list', 'in', [price_list]),
											],
												#order='date_order desc',
												limit=1,
									)
		# Manage Exception
		try:
			product.ensure_one()

		except:
			#print("An exception occurred")
			msg_name = "ERROR: Record Must be One Only."

			class_name = type(product).__name__

			#obj_name = product.name
			obj_name = name

			msg =  msg_name + '\n' + class_name + '\n' + obj_name
			#msg =  msg_name + '\n' + class_name + '\n'

			raise UserError(_(msg))



		product_id = product.id

		print()
		print(product)
		print(product.name)

		#print(tst)
		#print(product_id)
		#print(product.pl_price_list)
		#print(product.pl_treatment)

		#if False:
		#	print(product.pl_family)
		#	print(product.pl_subfamily)
		#	print(product.pl_treatment)
		#	print(product.pl_zone)
		#	print(product.pl_pathology)
		#	print(product.pl_sessions)
		#	print(product.pl_level)
		#	print(product.pl_time)


		# Create
		service = self.env[model].create({
														'service': 			product_id,
														'family': 			product.pl_family,
														'subfamily': 		product.pl_subfamily,
														'zone': 			product.pl_zone,
														'pathology': 		product.pl_pathology,
														'sessions': 		product.pl_sessions,
														'level': 			product.pl_level,
														'time': 			product.pl_time,
														'price_applied': 	product.list_price,
														'sel_zone': 		product.pl_zone,
														'pl_treatment': 	product.pl_treatment,

														'treatment': 		self.id,
											})
# create_recommendations_2019



# ----------------------------------------------------------- Reset Treatment ---------------------

def test_reset_treatment(self):
	"""
	Test Reset - For Treatment
	"""
	print()
	print('Test Reset Function')

	# Consultation
	self.consultation_ids.unlink()

	# Recos
	self.service_co2_ids.unlink()
	self.service_excilite_ids.unlink()
	self.service_ipl_ids.unlink()
	self.service_ndyag_ids.unlink()
	self.service_quick_ids.unlink()
	self.service_product_ids.unlink()
	self.service_medical_ids.unlink()
	self.service_cosmetology_ids.unlink()
	self.service_gynecology_ids.unlink()
	self.service_echography_ids.unlink()
	self.service_promotion_ids.unlink()

	# Procedures
	self.procedure_ids.unlink()
	self.session_ids.unlink()
	self.control_ids.unlink()

	# App
	#self.appointment_ids.unlink()			# Dep !

	# Alta
	self.treatment_closed = False

	# Orders - Keep them !
	#for order in self.order_ids:
	#	order.remove_myself_force()
# reset
