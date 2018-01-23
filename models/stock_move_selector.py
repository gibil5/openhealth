
from openerp import models, fields, api




class StockMoveSelector(models.Model):
	
	_name = 'stock.move.selector'

	_description = "Stock Move Selector"




	sms_active_id = fields.Integer(
			default=7,
		)




	name = fields.Char(

			'Name',

			required="0", 

			compute="_compute_name",
		)

	@api.multi
	#@api.depends('')

	def _compute_name(self):
		for record in self:
			record.name = 'SMS-' + str(record.id).zfill(8)





	product_id = fields.Many2one(
			
			'product.product',
			#'product.template',

			'Producto', 



			domain = [
						('type', '=', 'product'),
						('x_origin', '=', False),
						('sale_ok', '=', True),
					],



			required=True, 
		)


# ----------------------------------------------------------- Actions ------------------------------------------------------

	# Create Kardex 
	#@api.multi 
	#def create_kardex_platform(self):




	# Create Kardex 
	@api.multi 
	#def create_kardex_general(self):
	def create_kardex(self):


		print 'jx'
		print 'Create Kardex'


		context = self._context.copy()


		print 
		#print context
		#print context['params']
		location = context['location']
		print location
		print 



		product_name = self.product_id.name
		product_id = self.product_id.id

			
		kardex = self.env['openhealth.kardex'].search([

														#('state', '=', 'done'),			
														('product', '=', product_name),			

														('location', '=', location),			
			
												],
												#order='start_date desc',
												limit=1,
												)
		
		if kardex.name == False: 
		
			#print 'Create'

			kardex = self.env['openhealth.kardex'].create({
															'product': product_id, 
															'location': location, 
														})




		# Generate 
		kardex.generate_kardex()


		kardex_id = kardex.id



		return {

			'type': 'ir.actions.act_window',

			'name': 'Open Kardex',
			
			'res_model': 'openhealth.kardex',
			
			'res_id': kardex_id,


			# Views 

			"views": [[False, "form"]],
			#"views": [[False, "tree"]],

			'view_mode': 'form',
			#'view_mode': 'tree',

			'target': 'current',
			
			#'view_id': view_id,
			
			#'auto_search': False, 


			'flags': {
						'form': {'action_buttons': True, }
						#'form': {'action_buttons': True, 'options': {'mode': 'edit'}}
			},			


			#"domain": [
			#			["product_id", "=", self.product_id.id], 
						#['state', '=', 'done'],
			#		],

			'context':   {}
		}
	# create_kardex



