class ServiceBase(models.Model):
	#_name = 'openhealth.service'
	_inherit = 'product.template'


	def get_domain_servicebase(self,cr,uid,ids,context=None):

		context='laser_co2'
		print
		print context
		print 
		
		#return {
		#	'warning': {
		#		'title': "Laser",
		#		'message': context,
		#}}

		mach = []
		lids = self.pool.get('product.template').search(cr,uid,[
																('x_treatment', '=', context)
																])
		return {'domain':{'service':[('id','in',lids)]}}

