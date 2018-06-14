# -*- coding: utf-8 -*-
#
# 	Patient Line
# 
# Created: 				16 May 2018
#

from openerp import models, fields, api

import pat_vars

import eval_vars

import prodvars


class PaitentLine(models.Model):
	
	_name = 'openhealth.patient.line'

	_order = 'date_create asc'





# ----------------------------------------------------------- Inheritable ------------------------------------------------------

	# Patient 
	patient = fields.Many2one(
			'oeh.medical.patient', 
			string="Paciente", 
		)


	# Doctor 
	doctor = fields.Many2one(
			'oeh.medical.physician',
			string = "Médico", 	
		)




	# Treatment 
	treatment = fields.Many2one(
			'openhealth.treatment', 
			string="Tratamiento", 
		)


	# Consultation 
	consultation = fields.Many2one(
			'openhealth.consultation', 
			string="Consulta", 
		)



	# Mkt 
	emr = fields.Char(
			'HC', 
		)


	phone_1 = fields.Char(
			'Tel 1', 
		)


	phone_2 = fields.Char(
			'Tel 2', 
		)


	email = fields.Char(
			'Email', 
		)



	#chief_complaint = fields.Char(
	#		'Motivo', 
	#	)



	chief_complaint = fields.Selection(
			string = 'Motivo de consulta', 						
			selection = eval_vars._chief_complaint_list, 
			#required=False, 
			#readonly=True, 
		)




	diagnosis = fields.Char(
			'Diagnóstico', 
		)



	budget_date = fields.Datetime(
			'Pres. Fecha', 
		)



	#budget_amount = fields.Float(
	budget_amount = fields.Char(
			'Pres. Monto', 
		)



	budget_flag = fields.Boolean(
			'Flag', 
		)



	budget_prod = fields.Char(
			'Pres. Proc.', 
		)



# ----------------------------------------------------------- Relational ------------------------------------------------------


	# Budgets
	budget_line = fields.One2many(
			'openhealth.marketing.order.line', 
			'patient_line_budget_id',
		)




	# Sales
	sale_line = fields.One2many(
			'openhealth.marketing.order.line', 
			'patient_line_sale_id',
		)



	# Consus
	consu_line = fields.One2many(
			'openhealth.marketing.order.line', 
			'patient_line_consu_id',
		)



	# Products
	product_line = fields.One2many(
			'openhealth.marketing.order.line', 

			'patient_line_product_id',
		)



	# Procedures
	procedure_line = fields.One2many(
			'openhealth.marketing.order.line', 
			
			#'patient_line_id_proc',
			'patient_line_proc_id',
		
			string="Procedimientos", 
		)







	# Vip Sales
	order_line = fields.One2many(
			'openhealth.marketing.order.line', 
			'patient_line_id',
		)


	# Vip Sales - With Vip Card
	order_line_vip = fields.One2many(
			'openhealth.marketing.order.line', 
			'patient_line_id_vip',
		)





	# Recommendations
	reco_line = fields.One2many(
			'openhealth.marketing.recom.line', 
			'patient_line_id',
			string="Recom.", 
		)


# ----------------------------------------------------------- Dates ------------------------------------------------------

	# Date Created 
	date_create = fields.Datetime(
			string="Fecha de Creación", 
		)

	# Date Record 
	date_record = fields.Datetime(
			string="Fecha de Registro", 
			#string="Fecha creación", 
		)






# ----------------------------------------------------------- Reco ------------------------------------------------------
	# Nr Reco 
	nr_reco = fields.Integer(
			#'Nr Recomendaciones', 
			'Nr Recom', 
			#default=-1, 
		)



# ----------------------------------------------------------- Sales ------------------------------------------------------


	# Nr Budgets 
	nr_budget = fields.Integer(
			#'Nr Presupuestos', 
			'Nr Presupuestos pendientes', 
			#default=-1, 
		)




	# Nr Sales 
	nr_sale = fields.Integer(
			'Nr Ventas', 
			#default=-1, 
		)

	# Nr Consus 
	nr_consu = fields.Integer(
			'Nr Consultas', 
			#default=-1, 
		)



	# Nr Products 
	nr_products = fields.Integer(
			'Nr Productos', 
			#default=-1, 
		)



	# Nr Proc
	nr_proc = fields.Integer(
			'Nr Procedimientos', 
			#default=-1, 
		)




	# Nr lines Vip 
	nr_lines_vip = fields.Integer(
			#'Ventas Usando la tarjeta Vip', 
			'Compras Con Tarjeta Vip', 
			default=-1, 
		)





# ----------------------------------------------------------- Primitives ------------------------------------------------------

	# Date Vip card 
	vip_date = fields.Datetime(
			string="Fecha Vip", 
		)


	# Marketing Id 
	marketing_id = fields.Many2one(
			#'openhealth.account.contasis'
			'openhealth.marketing', 

			ondelete='cascade', 
		)





	# Age 
	age = fields.Char(
			string = "Edad", 		
		)

	age_years = fields.Integer(
			string = "Edad", 		
			#default=0, 
			default=-1, 
		)

	dob = fields.Date(
			string="Fecha nacimiento",
			required=False, 
		)



	# Sex 
	sex = fields.Selection(

			selection = pat_vars._sex_type_list, 
		
			string="Sexo",
			#required=False, 
		)

	mea_m = fields.Integer(
			'M', 
		)

	mea_f = fields.Integer(
			'F', 
		)

	mea_u = fields.Integer(
			'U', 
		)



	# First Contact 
	first_contact = fields.Selection(

			selection = pat_vars._first_contact_list, 
		
			string = 'Primer contacto',
		)
	
	mea_recommendation = fields.Integer(
			'Pri Recomendación', 
		)

	mea_tv = fields.Integer(
			'Pri Tv', 
		)

	mea_radio = fields.Integer(
			'Pri Radio', 
		)

	mea_internet = fields.Integer(
			'Pri Internet', 
		)

	mea_website = fields.Integer(
			'Pri Website', 
		)

	mea_mail_campaign = fields.Integer(
			'Pri Mail', 
		)

	mea_how_none = fields.Integer(
			'Pri Ninguno', 
		)

	mea_how_u = fields.Integer(
			'Pri Ind', 
		)




	# Education 
	education = fields.Selection(
			selection = pat_vars._education_level_type,
			string = 'Grado de instrucción',
		)

	mea_first = fields.Integer(
			'Edu Primaria', 
		)

	mea_second = fields.Integer(
			'Edu Secundaria', 
		)
	
	mea_technical = fields.Integer(
			'Edu Instituto', 
		)
	
	mea_university = fields.Integer(
			'Edu Universidad', 
		)
	
	mea_masterphd = fields.Integer(
			'Edu Posgrado', 
		)

	mea_edu_u = fields.Integer(
			'Edu Ind', 
		)
	




	# Vip 
	vip = fields.Boolean(
			string = 'Vip',
		)

	mea_vip = fields.Integer(
			'Vip', 
		)

	mea_vip_no = fields.Integer(
			'No Vip', 
		)





	# Address
	country = fields.Char(
			'Pais', 
		)

	city = fields.Char(
			'Ciudad', 
		)

	district = fields.Char(
			'Distrito', 
		)






# ----------------------------------------------------------- Update Fields ------------------------------------------------------

	# Update Fields
	@api.multi
	def update_fields_mkt(self):  


		#print
		#print 'Update Fields - Mkt'


		self.emr = self.patient.x_id_code

		self.phone_2 = self.patient.phone 

		self.phone_1 = self.patient.mobile

		self.email = self.patient.email




		self.treatment = self.env['openhealth.treatment'].search([
																	('patient','=', self.patient.name),
														],
														#order='create_date desc',
														order='start_date desc',
														limit=1,)





		self.consultation = self.env['openhealth.consultation'].search([
																		#('name','=', self.patient.name),
																		('treatment','=', self.treatment.id),
														],
														#order='create_date desc',
														order='evaluation_start_date desc',
														limit=1,)




		self.chief_complaint = self.treatment.chief_complaint

		self.diagnosis = self.consultation.x_diagnosis



		#self.budget_amount = 

		#self.budget_date = 







# ----------------------------------------------------------- Update Fields ------------------------------------------------------

	# Update Fields
	@api.multi
	def update_fields(self):  


		#print
		#print 'Update Fields - Patient'


		# Age 
		if self.age.split()[0] != 'No': 
			self.age_years = self.age.split()[0]
			ret = 1
		else:
			ret = -1



		# Places
		if self.city != False: 
			self.city = self.city.title()

		if self.district != False: 
			self.district = self.district.title()


		

		# Measures

		# Sex 
		if self.sex == 'Male': 
			self.mea_m = 1
		elif self.sex == 'Female':
			self.mea_f = 1
		else:
			self.mea_u = 1

		# Vip 
		if self.vip: 
			self.mea_vip = 1
		else: 
			self.mea_vip_no	= 1


		# Education
		if self.education == 'first': 
			self.mea_first = 1

		elif self.education == 'second': 
			self.mea_second = 1

		elif self.education == 'technical': 
			self.mea_technical = 1

		elif self.education == 'university': 
			self.mea_university = 1

		elif self.education == 'masterphd': 
			self.mea_masterphd = 1 

		else: 
			self.mea_edu_u = 1			


		# First Contact 
		if self.first_contact == 'recommendation': 
			self.mea_recommendation = 1

		elif self.first_contact == 'tv': 
			self.mea_tv = 1

		elif self.first_contact == 'radio': 
			self.mea_radio = 1

		elif self.first_contact == 'internet': 
			self.mea_internet = 1

		elif self.first_contact == 'website': 
			self.mea_website = 1

		elif self.first_contact == 'mail_campaign': 
			self.mea_mail_campaign = 1

		elif self.first_contact == 'none': 
			self.mea_how_none = 1

		else: 
			self.mea_how_u = 1

	
		return ret 

	# update_fields






# ----------------------------------------------------------- Update Fields Vip ------------------------------------------------------

	# Update fields Vip
	@api.multi
	def update_fields_vip(self):  
		
		#print 
		#print 'Update fields - Vip'
		

		# Nr Lines Vip 
		count = self.env['openhealth.marketing.order.line'].search_count([
																				('patient_line_id_vip','=', self.id),
																			]) 
		self.nr_lines_vip = count

	# update_fields_vip






# ----------------------------------------------------------- Update Fields Proc ------------------------------------------------------

	# Update fields Proc
	@api.multi
	def update_nrs(self):  

		#print 
		#print 'Update fields - Nrs'
		#print 



		# Sales 
		for line in self.sale_line: 
			# Doctor 
			if self.doctor.name == False: 
				self.doctor = line.doctor.id 





		# Budgets
		self.budget_amount = ''
		self.budget_prod = ''
		for line in self.budget_line: 


			# Doctor 
			if self.doctor.name == False: 
				self.doctor = line.doctor.id 



		
			# Budget Amount 
			self.budget_amount = self.budget_amount + str(line.price_total) + ', '

			# Budget Flag 
			if line.price_total >= 1500: 
				self.budget_flag = True



			# Budget Prod
			if line.product_id.x_treatment != False: 
				if line.product_id.x_treatment in prodvars._h_subfamily: 
					self.budget_prod = self.budget_prod + prodvars._h_subfamily[line.product_id.x_treatment] + ', '
				else: 
					self.budget_prod = self.budget_prod + line.product_id.x_treatment + ', '




		# Amount and Prod 
		self.budget_amount = self.budget_amount[:-2]
		self.budget_prod = self.budget_prod[:-2]




		# Nr Budgets
		count = self.env['openhealth.marketing.order.line'].search_count([
																				('patient_line_budget_id','=', self.id),
																			]) 
		self.nr_budget = count




		# Nr Sale
		count = self.env['openhealth.marketing.order.line'].search_count([
																				('patient_line_sale_id','=', self.id),
																			]) 
		self.nr_sale = count




		# Nr Consu 
		count = self.env['openhealth.marketing.order.line'].search_count([
																				('patient_line_consu_id','=', self.id),
																			]) 
		self.nr_consu = count




		# Nr Product
		count = self.env['openhealth.marketing.order.line'].search_count([
																				('patient_line_product_id','=', self.id),
																			]) 
		self.nr_products = count





		# Nr Proc 
		count = self.env['openhealth.marketing.order.line'].search_count([
																				('patient_line_proc_id','=', self.id),
																			]) 
		self.nr_proc = count





		# Nr Reco 
		count = self.env['openhealth.marketing.recom.line'].search_count([
																				('patient_line_id','=', self.id),
																			]) 
		self.nr_reco = count

	# update_nrs

