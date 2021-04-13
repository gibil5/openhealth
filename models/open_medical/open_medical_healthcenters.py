"""
    Open Pathology
    Created:    12 apr 2021 
    Last:       12 apr 2021     
"""

from __future__ import print_function
from openerp import models, fields, api


# Health Center Management
class OeHealthCenters(models.Model):
    _name = 'oeh.medical.health.center'
    _description = "Information about the health centers"
    _inherits={
        'res.partner': 'partner_id',
    }
    #_defaults={
    #        'is_institution': True,
    #        'is_company': True
    #    }
    HEALTH_CENTERS = [
        ('Hospital', 'Hospital'),
        ('Nursing Home', 'Nursing Home'),
        ('Clinic', 'Clinic'),
        ('Community Health Center', 'Community Health Center'),
        ('Military Medical Facility', 'Military Medical Facility'),
        ('Other', 'Other'),
    ]

    partner_id = fields.Many2one('res.partner', 'Related Partner', required=True,ondelete='cascade', help='Partner-related data of the hospitals')
    health_center_type = fields.Selection(HEALTH_CENTERS, 'Type', help="Health center type", select=True)
    info = fields.Text('Extra Information')


    # Computes 
    #building_count = fields.function(_building_count, string="Buildings", type="integer")
    building_count = fields.Integer(
        string="Buildings",
    	compute='_building_count',
        )   
    @api.multi
    def _building_count(self):
        for record in self:
            record.complete_name = 0

    #pharmacy_count = fields.function(_pharmacy_count, string="Pharmacies", type="integer")
    pharmacy_count = fields.Integer(
        string="Pharmacies",
    	compute='_pharmacy_count',
    )   
    @api.multi
    def _pharmacy_count(self):
        for record in self:
            record.complete_name = 0


    @api.multi
    def onchange_state(self, state_id):
        if state_id:
            state = self.env['res.country.state'].browse(state_id)
            return {'value': {'country_id': state.country_id.id}}
        return {}


# Health Center Building
class OeHealthCentersBuilding(models.Model):
    _name = 'oeh.medical.health.center.building'
    _sql_constraints = [
        ('name_uniq', 'unique (name)', 'The building name must be unique !')
    ]

    name = fields.Char ('Name', size=128, required=True, help="Name of the building within the institution")
    institution = fields.Many2one ('oeh.medical.health.center','Health Center',required=True)
    code = fields.Char ('Code', size=64)
    info = fields.Text ('Extra Info')


    # Computes 
    #ward_count = fields.function(_ward_count, string="Wards", type="integer")
    ward_count = fields.Integer(
        string="Beds", 
    	compute='_ward_count',
        )   
    @api.multi
    def _ward_count(self):
        for record in self:
            record.ward_count = 0

    #bed_count = fields.function(_bed_count, string="Beds", type="integer")
    bed_count = fields.Integer(
        string="Beds", 
    	compute='_bed_count',
        )   
    @api.multi
    def _bed_count(self):
        for record in self:
            record.complete_name = 0



# Health Center Wards Management
class OeHealthCentersWards(models.Model):
    _name = "oeh.medical.health.center.ward"
    #_defaults = {
    #        'gender': lambda *a: 'Unisex',
    #        'state':'Beds Available',
    #    }
    _sql_constraints = [
            ('name_ward_uniq', 'unique (name,building)', 'The ward name is already configured in selected building !')]
    GENDER = [
                ('Men Ward','Men Ward'),
                ('Women Ward','Women Ward'),
                ('Unisex','Unisex'),
            ]
    WARD_STATES = [
                ('Beds Available','Beds Available'),
                ('Full','Full'),
            ]

    name = fields.Char ('Name', size=128, required=True, help="Ward / Room code")
    building = fields.Many2one ('oeh.medical.health.center.building','Building',required=True)
    floor = fields.Integer ('Floor Number')
    private = fields.Boolean ('Private Room',help="Check this option for private room")
    bio_hazard = fields.Boolean ('Bio Hazard',help="Check this option if there is biological hazard")
    telephone = fields.Boolean ('Telephone access')
    ac = fields.Boolean ('Air Conditioning')
    private_bathroom = fields.Boolean ('Private Bathroom')
    guest_sofa = fields.Boolean ('Guest sofa-bed')
    tv = fields.Boolean ('Television')
    internet = fields.Boolean ('Internet Access')
    refrigerator = fields.Boolean ('Refrigerator')
    microwave = fields.Boolean ('Microwave')
    gender = fields.Selection (GENDER,'Gender')
    state = fields.Selection(WARD_STATES,'Status')
    info = fields.Text ('Extra Info')

    # Computes 
    #bed_count = fields.function(_bed_count, string="Beds", type="integer")
    bed_count = fields.Integer(
        string="Beds", 
    	compute='_bed_count',
    )
    @api.multi
    def _bed_count(self):
        for record in self:
            record.complete_name = 0
    


# Beds Management
class OeHealthCentersBeds(models.Model):
    _name = 'oeh.medical.health.center.beds'
    _description = "Information about the health centers beds"
    _inherits={
        'product.product': 'product_id',
    }
    #_defaults = {
    #        'is_bed': True,
    #        'bed_type': lambda *a: 'Gatch Bed',
    #        'state': 'Free',
    #    }
    #_sql_constraints = [
    #        ('name_bed_uniq', 'unique (name,ward)', 'The bed name is already configured in selected ward !')]

    BED_TYPES = [
        ('Gatch Bed','Gatch Bed'),
        ('Electric','Electric'),
        ('Stretcher','Stretcher'),
        ('Low Bed','Low Bed'),
        ('Low Air Loss','Low Air Loss'),
        ('Circo Electric','Circo Electric'),
        ('Clinitron','Clinitron'),
    ]

    BED_STATES = [
        ('Free', 'Free'),
        ('Reserved', 'Reserved'),
        ('Occupied', 'Occupied'),
        ('Not Available', 'Not Available'),
    ]

    CHANGE_BED_STATUS = [
        ('Mark as Reserved', 'Mark as Reserved'),
        ('Mark as Not Available', 'Mark as Not Available'),
    ]

    product_id = fields.Many2one('product.product', 'Related Product', required=True,ondelete='cascade', help='Product-related data of the hospital beds')
    building = fields.Many2one ('oeh.medical.health.center.building','Building')
    ward = fields.Many2one ('oeh.medical.health.center.ward','Ward',domain="[('building', '=', building)]",help="Ward or room", ondelete='cascade')
    bed_type = fields.Selection(BED_TYPES,'Bed Type', required=True)
    telephone_number = fields.Char ('Telephone Number',size=128, help="Telephone Number / Extension")
    info = fields.Text ('Extra Info')
    state = fields.Selection(BED_STATES,'Status')
    change_bed_status = fields.Selection(CHANGE_BED_STATUS,'Change Bed Status')


    # Preventing deletion of a beds which is not in draft state
    #def unlink(self, cr, uid, ids, context=None):

    #def create(self, cr, uid, vals, context=None):

    #def write(self, cr, uid, ids, vals, context=None):

    def onchange_bed_status(self, cr, uid, ids, change_bed_status, state, context=None):
        res = {}
        if state and change_bed_status:
            if state=="Occupied":
                raise osv.except_osv(_('Error'), _('Bed status can not change if it already occupied!'))
            else:
                if change_bed_status== "Mark as Reserved":
                    res = self.write(cr, uid, ids, {'state': 'Reserved'}, context=context)
                else:
                    res = self.write(cr, uid, ids, {'state': 'Not Available'}, context=context)
        return res

