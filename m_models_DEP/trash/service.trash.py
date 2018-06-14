#------------------------------------ Classes -----------------------------------------

class ServiceExcilite(models.Model):
	#_name = 'openhealth.service.laserexcilite'
	_name = 'openhealth.service.excilite'

	_inherit = 'openhealth.service'
	
	
	

class ServiceIpl(models.Model):
	#_name = 'openhealth.service.laseripl'
	_name = 'openhealth.service.ipl'

	_inherit = 'openhealth.service'



class ServiceNdyag(models.Model):
	#_name = 'openhealth.service.laserndyag'
	_name = 'openhealth.service.ndyag'

	_inherit = 'openhealth.service'





# 19 Jan 2017


	# Quotation - Deprecated
	#quotation = fields.Many2one('openhealth.quotation',
	#		ondelete='cascade', 
			#string="Treatment", 
	#		string="Quotation", 
	#		)



	# Treatment - Deprecated 
	#treatment = fields.Selection(
	#		selection = prodvars._treatment_list, 
	#	)



	# Treatment 
	#treatment_id = fields.Many2one('openextension.treatment',






# Deprecated
	def get_domain_service(self,cr,uid,ids,context=None):
		mach = []
		lids = self.pool.get('product.template').search(cr,uid,[
																('x_treatment', '=', context)
																])
		return {'domain':{'service':[('id','in',lids)]}}


	def get_domain_service_multi(self,cr,uid,ids,context_1=None,context_2=None,context_3=None):
		#print context
		#print 'jx'
		#print context_1, context_2, context_3
		#print 'jx'
		
		mach = []
		lids = self.pool.get('product.template').search(cr,uid,[
																	('x_treatment', '=', 	context_1), 
																	('x_zone', '=', 		context_2), 
																	('x_pathology', '=', 	context_3), 
																])
		return {'domain':{'service':[('id','in',lids)]}}








