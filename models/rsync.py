# -*- coding: utf-8 -*-
#
#	Rsync. 
# 
#	Created: 			 1 Oct 2018
# 	Last up: 	 		 1 Oct 2018
#
import os
import shutil
import io




# ----------------------------------------------------------- Create Services  ------------------------------------------------------
#def synchronize(export_date): 
def synchronize(): 
	print 
	print "Synchronize"
	
	# Init 
	#base_dir = '/Users/gibil/Virtualenvs/Odoo9-min/odoo'
	#path = base_dir + "/mssoft/ventas/" + export_date

	source = '/Users/gibil/Virtualenvs/Odoo9-min/odoo/mssoft/ventas/'
	#destination = 'root@165.227.25.8:/root/mssoft/ventas'
	destination = 'root@165.227.25.8:/var/www/html/ventas'


	# Rsync 
	#os.system("rsync -rtv /opt/data/filename root@ip:/opt/data/file")
	#os.system("rsync -rtv /Users/gibil/Virtualenvs/Odoo9-min/odoo/mssoft/ventas/ root@165.227.25.8:/root/mssoft/ventas")
	#os.system("rsync -rv /Users/gibil/Virtualenvs/Odoo9-min/odoo/mssoft/ventas/ root@165.227.25.8:/root/mssoft/ventas")
	os.system("rsync -rv " + source + " " + destination)



	# List 
	#ret = os.listdir(path)  
	#print ret 
