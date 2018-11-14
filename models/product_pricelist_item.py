# -*- coding: utf-8 -*-
"""
 		*** Product Pricelist Item

 		Created: 			 13 Nov 2018
		Last up: 	 		 13 Nov 2018
"""


from openerp import models, fields, api

#class product_pricelist_item(osv.osv):
class ProductPricelistItem(models.Model):
    
    #_name = "product.pricelist.item"
    _inherit = "product.pricelist.item"
    
    _description = "Pricelist item"
    
    _order = "applied_on, min_quantity desc, categ_id desc"



    x_type = fields.Selection(
			[
				('product', 'product'),
				('consultation', 'consultation'),
				
                ('laser_co2', 'laser_co2'),
                ('laser_excilite', 'laser_excilite'),
                ('laser_ipl', 'laser_ipl'),
                ('laser_ndyag', 'laser_ndyag'),
                
                ('laser_quick', 'laser_quick'),
			],
    	)


# ----------------------------------------------------------- Handle ------------------------------
    
    corrector_id = fields.Many2one(
    		'openhealth.corrector',
			ondelete='cascade',    		
    	)


