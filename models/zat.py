	#a_jx = a_treatment_id.a_jx 
	#a_jx = fields.Char(
	#		)



	#chief_complaint = fields.Char(
			#default = a_jx, 
	#		required=True, 
	#		)

	#ur_field = fields.Many2one('Your model', 
	#		string="Your specified name",
	#		default=lambda self: self.env['Your model'].search([('file_type','=','company_user')])
	#		)

	#name_def = a_treatment_id.patient.name 
	#name_def = super.patient.name 









	#def default_get(self, cr, uid, fields, context=None):
	#	product_obj = self.pool.get('product.product')
	#	record_ids = context and context.get('active_ids', []) or []
	#	res = super(product_product, self).default_get(cr, uid, fields, context=context)

	#	for product in product_obj.browse(cr, uid, record_ids, context=context):
	#		if 'default_code' in fields:
				#in 'default_code' is a field name of that pop-up window
	#			res.update({'default_code': product.default_code})

	#	return res


	#def __init__( self, a, b ):
	#		self.parentNumber = 5


	#print self._haircolor
	#print 'jx message'
	#print models.Model.patient.name 
	#print models.Model









	# Test 
	def some_method(self):
			return {"msg" : "Message from the server"}

	def get_patient(self):
			return self.patient 

	def get_patient_name(self):
			return 'Javier Revilla' 









	# Button 1 
	@api.one
	def generate_record_name(self):
		print
		print 'jx:Button'
		print 










	# Test fields 
	#jx_char = fields.Char() 
	#jx_int = fields.Integer() 
	#jx_float = fields.Float() 











	#def action_evaluation_form(self, cr, uid, ids, context=None):
	def evaluation_form_action(self, cr, uid, ids, context=None):
		ctx.update({
			'default_model': 'sale.order',
			'default_res_id': ids[0],
			'default_use_template': bool(template_id),
			'default_template_id': template_id,
			'default_composition_mode': 'comment',
			'mark_so_as_sent': True
		})
		return {
			'type': 'ir.actions.act_window',
			'view_type': 'form',
			'view_mode': 'form',
			'res_model': 'mail.compose.message',
			'views': [(compose_form_id, 'form')],
			'view_id': compose_form_id,
			'target': 'new',
			'context': ctx,
		}

	#default_patient = self.patient  







	#def _get_physician(self, cr, uid, context=None):
	#	"""Return default physician value"""
	#	therapist_id = []
	#	therapist_obj = self.pool.get('oeh.medical.physician')
	#	domain = [('oeh_user_id', '=', uid)]
	#	user_ids = therapist_obj.search(cr, uid, domain, context=context)
	#	if user_ids:
	#		return user_ids[0] or False
	#	else:
	#		return False


	#def_physician = _get_physician


	#physician = def_physician 
	#physician = fields.Many2one(
	#		'oeh.medical.physician',
			#string="Patient", 
	#		string = "jx Physician", 
	#		required = False, 
	#		default = def_physician, 
			#index=True
	#		)


	#default_physician = fields.Many2one(
	#		'oeh.medical.physician',
			#string="Physician", 
			#string="Médico", 
			#required=True, 
			#index=True
	#		)



