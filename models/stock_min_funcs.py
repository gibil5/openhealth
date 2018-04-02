# -*- coding: utf-8 -*-

from openerp import models, fields, api
#import datetime



# ----------------------------------------------------------- Funcs ------------------------------------------------------

_hac = {
	
	#'ACNETOPIC WASH': 'acnetopic_wash', 
	#'PROTECTOR SOLAR': 'solar_protector_inv', 

	'ESPARADRAPO COLOR PIEL': 					'tape_color_skin', 
	'PERFORADOR P/10 HOJAS 2/3/4HUECOS M-99A': 	'perforator_p10', 
	'VITAMINA C ENDOVENOSA': 					'vitamin_c_intra', 
	'CLIP MARIPOSA CHICO CJTAX50 CAJA DE 50': 	'clip_butterfly_small_50', 
	'PAPEL FOTOCOPIADORA A4': 					'paper_a4', 



	'CAJA DE CLORURO POR LITRO DE 12 UNIDADES': 	'chloride_lt_12', 
	'EQUIPO DE VENOCLISIS': 			'venoclisis_equip', 
	'VENDAS ELASTICAS 12*5 YARDAS' : 	'bandages_12x5', 
	'JERINGAS 20ML'	: 					'hypodermic_20_ml', 
	'JERINGA 10ML' : 					'hypodermic_10_ml', 

	'CAJA DE GUANTES TALLA M': 	'gloves_m_box', 
	'TOALLAS DE 65 X150': 		'towels_65x150', 
	'LIDOCAINA 2%': 			'lydocaine_2%', 
	'AGUJA N. 18': 				'needle_nr_18', 
	'GASAS X 100YDAS': 			'gause_yd_100', 



	'LIDOCAINA CON EPENIFRINA':		'lidocaine_w_epineprine', 
	'PLUMERO DE TELLA':				'duster_cloth', 
	'CAFÉ':							'coffee', 
	'ALGODON DE 500GR':				'cotton_500gr', 
	'AMBIENTADOR EN EPRAY GLADE':	'air_refreshener_spray_glade', 
	'BAJA LENGUA':					'tongue_spatula', 
	'VENDAS ELASTICAS 3*5 YARDAS':	'bandages_3x5', 
	'VENDAS ELASTICAS 6*5 YARDAS':	'bandages_6x5', 
	'LAPISERO BOLIGRAFOS CAJA DE 12':	'pen_box_12', 

	'ENGRAMPADOR DE METALICO':		'stapler_metal', 
	'PAPEL ELIITE 250':				'toilette_paper_elite', 
	'CREMA ANESTESICA X LITRO':		'topical_anesthesia_lt', 
	'DETERGENTE ARIEL X 7KLS':		'detergent_ariel_kg_7', 
	'AGUJA N30':					'needle_nr_30', 




	'JERINGA TUBERCULINA 1ML':	'hypodermic_tuberculine_1_ml', 
	'LIMPIATODO ARIM':			'clean_all_arim', 
	'HIBICLEN ESPUMA 4%':		'hibiclen_foam_4%', 
	'LEJIA CLOROX LIMON':		'bleach_clorox_lemon', 
	'NACL /0;9%':				'nacl', 
	'CATETER N24':				'catheter_nr_24', 
	'GLUCONATO DE CALCIO 10%':	'gluconate_calcium_10%', 

	'VACUETTE AZUL':			'vacuette_blue', 
	'CAJA DE GUANTES# (S)':		'gloves_s_box', 
	'VITAMINA "C" 20% AMP':		'vitamin_c_20%_amp', 
	'SILICIO ORGANICO AMP. 1%':	'silicium_organic_1%_amp', 
	'CREMA PEELING X 500GR.':	'topical_peeling_gr_500', 
	'GOMAGE CON AHA X 250 GR.':	'gomage_aha_gr_250', 
	'JERINGA 0,5ML':			'hypodermic_0.5_ml', 
	'VACUETTE':					'vacuette', 




}




@api.multi
#def get_product_id(self, code):
#def get_product_id(self, code, name):
def get_product_id(self, code, name, categ):

	
	# Clean 
	name = name.upper()
	name = " ".join(name.split())




	print 
	print 'get product id'
	print code 
	print name 
	print categ 


	product_id = False 



	# Search if exists
	product = self.env['product.template'].search([
														('default_code', '=', code),
											],
												#order='code asc',
												limit=1,
											)

	

	# Create 
	#if product.id == False: 
	if product.name != False: 
		print 'Prod exists'
		print 'Found'


	else:
		print 'Prod does not exist'



		#if name not in _hac:			
		if False: 
			print 'not in hac'


		else: 
			name_short = False
			#print 'in hac'
			#name_short = _hac[name]
			
			print name_short




			# Categ 

			purchase_ok = True

			if categ == 'topical': 
				categ_name = 'Cremas'
				sale_ok = True
			else: 
				categ_name = 'Consumibles'
				sale_ok = False



			categ = self.env['product.category'].search([
																('name', '=', categ_name),
											],
												#order='code asc',
												limit=1,
											)
			categ_id = categ.id



			# Prod 
			product = self.env['product.template'].create({
															'name': name,
															'default_code': code,
															'x_name_short': name_short, 

															'categ_id': categ_id, 

															'type': 'product', 
															'sale_ok': sale_ok, 
															'purchase_ok': purchase_ok, 													
											})


			print 'Created'

	print product
	print product.id


	
	#if product.id != False: 
	product_id = product.id

	return product_id

