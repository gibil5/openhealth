

# 26 Oct 2016

	def test_dni(self,cr,uid,ids,context=None):
		print context

		if context and (not context.isdigit()):
			return {
					'warning': {
						'title': "Error: DNI no es número",
						'message': context,
					}}

		if context and (len(str(context))!= 8):
			return {
					'warning': {
						'title': "Error: DNI no tiene 8 cifras",
						'message': context,
					}}
					
		return {}