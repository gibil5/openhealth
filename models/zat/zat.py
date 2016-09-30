
#from openerp.oeh import models, fields, api 
#from openerp.addons.oehealth.oeh.medical import models, fields, api 
#from openerp.addons.oehealth import models, fields, api 

#from openerp.addons.oehealth import models # , fiels #, api

# class openhealth(models.Model):
#     _name = 'openhealth.openhealth'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100





	# Active domain 
	_domain_array = [
				[
					('type', '=', 'service'), 
					('x_treatment', '=', 'laser_co2'), 
				], 

				[
					('type', '=', 'service'), 
					('x_treatment', '=', 'laser_excilite'), 
				], 

				[
					('type', '=', 'service'), 
					('x_treatment', '=', 'laser_ipl'), 
				], 

				[
					('type', '=', 'service'), 
					('x_treatment', '=', 'laser_ndyag'), 
				]
			]


	_domain_dic= {

			'laser_co2' : 
				[
					('type', '=', 'service'), 
					('x_treatment', '=', 'laser_co2'), 
				]
				, 

			'laser_excilite' : 
				[
					('type', '=', 'service'), 
					('x_treatment', '=', 'laser_excilite'), 
				]
				, 

			'laser_ipl' : 
				[
					('type', '=', 'service'), 
					('x_treatment', '=', 'laser_ipl'), 
				]
				, 

			'laser_ndyag' : 
				[
					('type', '=', 'service'), 
					('x_treatment', '=', 'laser_ndyag'), 
				]

			}




	#_active_domain = _domain_array[3]
	#active_domain = _domain_dic['laser_ipl']

	# Active domain 
	#active_domain = fields.Array(
	#		compute='_compute_ad', 
	#		string='')

	#@api.depends('laser')

	#def _compute_ad(self):
	#	for record in self:
	#		#record.active_domain = _domain_dic[record.laser] 
	#		record.active_domain = _domain_dic['laser_ndyag'] 





	_laser_dic = {

			'laser_co2' : 'laser_co2'   
			, 

			'laser_excilite':'laser_excilite' 
			, 

			'laser_ipl':'laser_ipl' 
			, 

			'laser_ndyag':'laser_ndyag' 

			}












	# On change
	#_jx_laser_type = ''

	#@api.onchange('laser')
	#def _activate_domain(self):

	#	l_type = 'nil'

	#	if self.laser == 'laser_co2':
			#self.laser_type = 'laser_co2'
	#		_jx_laser_type = 'laser_co2'
	#		l_type = 'Laser Co2'

	#	if self.laser == 'laser_ipl':
	#		_jx_laser_type = 'laser_ipl'
	#		l_type = 'Laser IPL'

	#	if self.laser == 'laser_excilite':
	#		_jx_laser_type = 'laser_excilite'
	#		l_type = 'Laser Excilite'

	#	if self.laser == 'laser_ndyag':
	#		_jx_laser_type = 'laser_ndyag'
	#		l_type = 'Laser NDYAG'



		#service = fields.Many2one('product.template',

		#	domain = [
		#				('type', '=', 'service'),
		#				('x_treatment', '=', _jx_laser_type),
		#			],

		
		#string="jx Service", 
		#)

		#return {
		#	'warning': {
		#		'title': "Laser",
		#		'message': "Laser " + l_type,
		#	}
		#}


	# Laser type 
	#_jx_laser_type = 'laser_ipl'

	#_jx_laser_type = _laser_dic['laser_ipl'] 
	#_jx_laser_type = _laser_dic[self.laser] 
	#_jx_laser_type = laser



	#laser_type = fields.Char(
	#		default='laser_co2',
	#		)
			#compute='_compute_laser_type', 

	#@api.depends('laser')
	#@api.multi

	#def _compute_laser_type(self):
	#	for record in self:
			#record.active_domain = _laser_dic['laser_ndyag'] 
			#record.laser_type = record.laser.name
	#		record.laser_type = record.laser
			#record.laser_type = _jx_laser_type

	#def _compute_code(self):
	#	for record in self:
	#		record.code= record.service.name 


			#domain = _domain_array[3], 
			#domain = active_domain, 
			#			('x_treatment', '=', self.laser_type),
			#			('x_treatment', '=', laser_type),
			#			('x_treatment', '=', _jx_laser_type),
