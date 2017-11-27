# -*- coding: utf-8 -*-



from openerp import models, fields, api


class AccountInvoice(models.Model):
	
	_inherit = 'account.invoice'
	_description = "Account Invoice"


	# Commons 
	vspace = fields.Char(
			' ', 
			readonly=True
			)



# ----------------------------------------------------------- Actions ------------------------------------------------------

	# Removem
	@api.multi
	def remove_myself(self):  
		
		self.state = 'cancel'
		
		self.unlink()



