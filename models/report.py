# -*- coding: utf-8 -*-
#
#
# 		Report
# 
#

from openerp import models, fields, api



class Report(models.Model):
	
	#_inherit = 'sale.report'

	_name = 'openhealth.report'

	_description = 'Base Report'

	#_order = 'write_date desc'






# ----------------------------------------------------------- Actions ------------------------------------------------------

	# Update 
	@api.multi
	def update_report(self):  

		print
		print 'Update report'











# ----------------------------------------------------------- Primitives ------------------------------------------------------

	name = fields.Char(
		)




	total_qty = fields.Integer(
			string="Cantidad", 
		)

	total = fields.Float(
			string="Total", 
		)




	date = fields.Datetime(
			string="Fecha", 
			default = fields.Date.today, 
			#readonly=True,
			#required=True, 
		)



	#date_begin = fields.Datetime(
	date_begin = fields.Date(
			string="Fecha Inicio", 
			default = fields.Date.today, 
			#readonly=True,
			#required=True, 
		)


	#date_end = fields.Datetime(
	date_end = fields.Date(
			string="Fecha Fin", 
			default = fields.Date.today, 
			#readonly=True,
			#required=True, 
		)






	vspace = fields.Char(
			' ', 
			readonly=True
		)
