

# 9 May 2018


#def onchange_product(self,cr,uid,ids,context=None):
#   #you can do something here
#   return {'value':{},'warning':{'title':'warning','message':'Your message'}}


	#@api.onchange('co2_power')
	#def _onchange_co2_power(self):
	#	print 'jx'
	#	print 'onchange co2_power'
	#	print self.co2_power
	#	ret = session_vars.test_for_zero(self, self.co2_power)
	#	return ret
		#if self.co2_power == 0.0: 
		#	return {'value':{},'warning':{'title':'warning','message':'Valor nulo'}}


	#@api.onchange('co2_energy')
	#def _onchange_co2_energy(self):
	#	if self.co2_energy == 0.0: 
	#		return {'value':{},'warning':{'title':'warning','message':'Valor nulo'}}



	#error=fields.Boolean(
			#default = False, 
	#		compute='_compute_error', 
	#	)
	#@api.multi
	#def _compute_error(self):
	#	print 'jx'
	#	print 'compute error'
	#	for record in self:
	#		print record.co2_power
	#		if record.co2_power == 0.0: 
	#			print 'true'
	#			record.error = True
	#		else: 
	#			print 'false'
	#			record.error = False




# 20 Aug 2018 

# From session_vars.py

def test_for_zero(self, token):
	#print 'test_for_zero'
	#print token 

	#if token and (not token.isdigit()):
	#if token and token == 0.0:
	if token == 0.0:
		#print 'Error'
		#return {
		#		'warning': {
		#			'title': 	"Error: Valor Nulo.",
		#			'message': 	token,
		#		}}
		return {'value':{},'warning':{'title':'warning','message':'Valor nulo'}}

	else:
		return 0
# test_for_digits





#import jxvars
#import jrfuncs
#import time_funcs



