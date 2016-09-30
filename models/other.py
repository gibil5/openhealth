
# -----------------------------------------------------------------------------
class oehEvaluation(models.Model):
	_name =	'openhealth.evaluation3'
	#_inherit = 'oeh.medical.evaluation'


	#@api.model
	#def create(self, values):
	#		print 
	#		print 'jx: This is a message...'
	#		print 
	#		res_id = super(oehEvaluation, self).create(values)
	#		return res_id




	#def a_fun(self):
	#		#return self.do_something()
	#		return '77'

	name = fields.Char(
			#compute='_compute_name', 
			default=77,
			)

	#@api.multi
	#@api.depends('start_date')
	#def _compute_name(self):
	#	for record in self:
			#record.name = record.patient.name
	#		record.name = '7'




	#a_treatment_id = fields.Many2one('openextension.treatment',
	treatment_id = fields.Many2one('openextension.treatment',
			ondelete='cascade', 
			)

	#a_jx = a_treatment_id._get_ajx 





	#evaluation = fields.Many2one(
	#		'oeh.medical.evaluation',
	#		)





	patient = fields.Many2one(
			'oeh.medical.patient',
			#default = lambda self: self.env['oeh.medical.patient'].search([('id','=','3025')]), 
			#default = lambda self: self.env['oeh.medical.patient'].search([('name','=','Javier Revilla')]), 
			required=True, 
			)

	doctor = fields.Many2one(
			'oeh.medical.physician',
			#default = lambda self: self.env['oeh.medical.patient'].search([('name','=','Javier Revilla')]), 
			required=True, 
			)








# -----------------------------------------------------------------------------
class Evaluation(models.Model):
	_name =	'openhealth.evaluation'


	# Name 
	name = fields.Char(
			default='x',
			#string='Name',
			string='Nombre',
			#required=True, 
			)

	# Name 
	#name = fields.Char(
	#		#string="Treatment #", 
	#		string="Evaluación #", 
	#		compute='_compute_name', 
	#		default='.', 
	#		required=True, 
	#		)

	#@api.multi
	#@api.depends('start_date')
	#def _compute_name(self):
	#	for record in self:
	#		record.name = record.patient.name



	treatment_id = fields.Many2one('openextension.treatment',
			ondelete='cascade', 
			#string="Treatment", 
			string="Tratamiento", 
			)



	# Evaluation  
	evaluation = fields.Many2one(
			'oeh.medical.evaluation',
			string="Evaluación", 
			#domain = [
			#			('patient', '=', 'Javier Revilla'),
			#			('patient', '=', PATIENT),
			#			('patient', '=', self.patient),
			#			('doctor', '=', 'Fernando Chavarri'),
			#			('doctor', '=', PHYSICIAN),
			#		],

			)



	# Type evaluation 
	evaluation_type = fields.Char(
			compute='_compute_evaluation_type', 
			string='Tipo', 
			)

	@api.depends('evaluation')

	def _compute_evaluation_type(self):
		for record in self:
			record.evaluation_type = record.evaluation.evaluation_type  





	# Evaluation date  
	#evaluation_date= fields.Datetime(
	#evaluation_date= fields.Date(
	#		compute='_compute_evaluation_date', 
	#		string='Fecha', 
	#		)

	#@api.depends('evaluation')

	#def _compute_evaluation_date(self):
	#	for record in self:
	#		record.evaluation_date = record.evaluation.evaluation_start_date




	#def get_domain_evaluation(self,cr,uid,ids,context=None):
	#	print 'jx'
	#	print context
	#	mach = []
	#	lids = self.pool.get('oeh.medical.evaluation').search(cr,uid,[('patient', '=', context)])
	#	return {'domain':{'evaluation':[('id','in',lids)]}}






# -----------------------------------------------------------------------------
class Invoice(models.Model):
	_name =	'openhealth.invoice'

	# Name 
	name = fields.Char(
			default='x',
			#string='Name',
			string='Nombre',
			required=True, 
			)

	# Invoice 
	invoice = fields.Many2one(
			'account.invoice',
			#string="Invoice", 
			string="Presupuesto", 
			)

	# Treatment 
	#treatment_id = fields.Many2one('openhealth.treatment',
	treatment_id = fields.Many2one('openextension.treatment',
			ondelete='cascade', 
			#string="Treatment", 
			string="Tratamiento", 
			)

	#Price 
	price = fields.Float(
			#compute='_compute_price', 
			#string='Price', 
			string='Precio', 
			default=55, 
			) 











# -----------------------------------------------------------------------------
class Service(models.Model):
	_name = 'openhealth.service'


	# Name 
	name = fields.Char(
			default='Laser Co2',
			#string='Name',
			string='Nombre',
			required=True, 
			)


	# Service 
	service = fields.Many2one(
			'product.template',
			#domain = [
			#			('type', '=', 'service'),
			#			('x_treatment', '=', _jx_laser_type),
			#		],
			#string="Service", 
			string="Servicio", 
			)


	# Treatment 
	treatment_id = fields.Many2one('openextension.treatment',
			ondelete='cascade', 
			#string="Treatment", 
			string="Tratamiento", 
			)
	#required=True,





	# Laser type 
	_laser_type_list = [
			('laser_co2','Laser Co2'), 
			('laser_excilite','Laser Excilite'), 
			('laser_ipl','Laser Ipl'), 
			('laser_ndyag','Laser Ndyag'), 
			]

	laser = fields.Selection(
			selection = _laser_type_list, 
			#string="Treatment",  
			string="Tratamiento",  
			default='laser_co2',
			required=True, 
			index=True
			)



	def get_domain_service(self,cr,uid,ids,context=None):

		#print context

		#return {
		#	'warning': {
		#		'title': "Laser",
		#		'message': context,
		#}}

		mach = []
		lids = self.pool.get('product.template').search(cr,uid,[('x_treatment', '=', context)])
		return {'domain':{'service':[('id','in',lids)]}}





	# Code 
	code = fields.Char(
			compute='_compute_code', 
			string='Code'
			)

	@api.depends('service')

	def _compute_code(self):
		for record in self:
			record.code= record.service.name 






	# Name short 
	name_short = fields.Char(
			compute='_compute_name_short', 
			#string='Short name'
			string='Código'
			)

	@api.depends('service')

	def _compute_name_short(self):
		for record in self:
			record.name_short = record.service.x_name_short 




	#Price 
	price = fields.Float(
			compute='_compute_price', 
			#string='Price'
			string='Precio'
			) 

	#@api.multi
	@api.depends('service')

	def _compute_price(self):
		for record in self:
			record.price= (record.service.list_price)




