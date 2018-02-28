# -*- coding: utf-8 -*-
#
# 	*** Leg Funcs
# 
# Created: 				 26 Feb 2017
# Last updated: 	 	 id

from openerp import models, fields, api

#from datetime import timedelta
import datetime



#------------------------------------------------ Functions ---------------------------------------------------

def correct_time(self, date):

	print 'jx'
	print 'Correct'
	print date 


	if date != False: 

		DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"

		date_field1 = datetime.datetime.strptime(date, DATETIME_FORMAT)


		date_corr = date_field1 + datetime.timedelta(hours=+5,minutes=0)


		return date_corr




def get_date_from_char(self, date_char):

	print 'jx'
	print 'Get date from c'

	print date_char



	if date_char != False: 


		a = date_char


		e = a.split()

		#b = a.split('/')
		b = e[0].split('/')


		#c = b[2] + '-' + b[1] + '-' + b[0] #+ ' ' + e[1]
		#c = b[2].zfill(4) + '-' + b[1].zfill(2) + '-' + b[0].zfill(2) 
		c = b[2].zfill(4) + '-' + b[1].zfill(2) + '-' + b[0].zfill(2) + ' ' + e[1]
	 	

		#c = c +  timedelta(hour=5)

	 	#+ ' ' + e[1]
		#.zfill()



		#date_d = date_char
		date_d = c


		print date_d
		return date_d
