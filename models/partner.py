from openerp import models, fields, api
#from datetime import datetime



class Partner(models.Model):
	
	_inherit = 'res.partner'
	#_name = 'openhealth.patient'	#The best solution ? So that impact is minimal ?	- Deprecated


	# Function 
	function = fields.Selection(

			[	
				('reception', 	'Plataforma'),
				('cash', 		'Caja'),
				('assistant', 	'Asistente Medico'),
				('physician', 	'Medico'),
				('inventory', 	'Almacen'),
				('hc', 			'Personal'),
				('marketing', 	'Marketing'),
				('accounting', 	'Contabilidad'),
				('manager', 	'Gerente'),
				('lawyer', 		'Abogado'),
			], 
		)


	# Vip 
	x_vip = fields.Boolean(
		string="Vip",
		default=False, 

		compute='_compute_x_vip', 
	)




	@api.multi
	#@api.depends('x_card')
	def _compute_x_vip(self):
		for record in self:
			x_card = record.env['openhealth.card'].search([
															('patient_name','=', record.name),
														],
														#order='appointment_date desc',
														limit=1,)
			if x_card.name != False:
				record.x_vip = True 



