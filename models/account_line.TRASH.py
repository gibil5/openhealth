

# 21 Aug 2018


# ----------------------------------------------------------- Deprecated ------------------------------------------------------
	
	# Codigo Unico Ope
	#cuo_mes = fields.Char(
	#		'MES', 
	#	)


	#cuo_sd = fields.Char(
	#		'SD', 
	#	)

	#cuo_asi = fields.Char(
	#		'ASI', 
	#	)


		#self.cuo_asi = 
		#self.cuo_sd = '02'




	# Update Fields
	@api.multi
	def update_fields(self):  

		# Dates	- Must be converteed to a datetime object, before converting to the proper format. 
		#DATETIME_FORMAT = "%Y-%m-%d"
		#self.fecha  = datetime.datetime.strptime(self.date, DATETIME_FORMAT).strftime('%d/%m/%Y')
		#self.fechavencimiento  = datetime.datetime.strptime(self.date, DATETIME_FORMAT).strftime('%d/%m/%Y')
		#self.fechavencimiento2 = self.fechavencimiento


		# Month 
		#self.cuo_mes =  datetime.datetime.strptime(self.date, DATETIME_FORMAT).strftime('%m')


		# Constants 
		#self.EXPortacion = '0.00'
		#self.exonerad = '0.00'
		#self.inafecto = '0.00'
		#self.isc = '0.00'
		#self.otros = '0.00'
		#self.tipor = '00'
		#self.tipocambio = '3.2100'




			#self.total = 0
			#self.neto = 0 
			#self.igv = 0 
			#self.porigv = 0


			#self.amount_net = self.amount/1.18
			#self.amount_tax = self.amount_net * 0.18


			#self.total = self.amount
			#self.neto = self.amount_net 
			#self.igv = self.amount_tax 			
			#self.porigv = self.igv

			#self.neto = str(float(self.amount)/1.18)
			#self.igv = str(float(self.neto) * 0.18)



