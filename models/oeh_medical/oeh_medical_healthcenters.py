##############################################################################
#    Copyright (C) 2015 oeHealth (<http://oehealth.in>). All Rights Reserved
#    oeHealth, Hospital Management Solutions
##############################################################################

from openerp import pooler, tools, api
from openerp.osv import osv, fields
from openerp.tools.translate import _

# Health Center Management

class OeHealthCenters(osv.osv):
    _name = 'oeh.medical.health.center'
    _description = "Information about the health centers"
    _inherits={
        'res.partner': 'partner_id',
    }

    HEALTH_CENTERS = [
            ('Hospital', 'Hospital'),
            ('Nursing Home', 'Nursing Home'),
            ('Clinic', 'Clinic'),
            ('Community Health Center', 'Community Health Center'),
            ('Military Medical Facility', 'Military Medical Facility'),
            ('Other', 'Other'),
            ]

    def _building_count(self, cr, uid, ids, field_name, arg, context=None):
        result = {}
        oe_buildings = self.pool.get('oeh.medical.health.center.building')
        for hec in self.browse(cr, uid, ids, context=context):
            domain = [('institution', '=', hec.id)]
            buildings_ids = oe_buildings.search(cr, uid, domain, context=context)
            buildings = oe_buildings.browse(cr, uid, buildings_ids, context=context)
            bu_count = 0
            for bul in buildings:
                bu_count+=1
            result[hec.id] = bu_count
        return result

    def _pharmacy_count(self, cr, uid, ids, field_name, arg, context=None):
        result = {}
        oe_pharmacies = self.pool.get('oeh.medical.health.center.pharmacy')
        for hec in self.browse(cr, uid, ids, context=context):
            domain = [('institution', '=', hec.id)]
            pharmacies_ids = oe_pharmacies.search(cr, uid, domain, context=context)
            pharmacies = oe_pharmacies.browse(cr, uid, pharmacies_ids, context=context)
            pha_count = 0
            for pha in pharmacies:
                pha_count+=1
            result[hec.id] = pha_count
        return result

    _columns = {
        'partner_id': fields.many2one('res.partner', 'Related Partner', required=True,ondelete='cascade', help='Partner-related data of the hospitals'),
        'health_center_type': fields.selection(HEALTH_CENTERS, 'Type', help="Health center type", select=True),
        'info':fields.text('Extra Information'),
        'building_count': fields.function(_building_count, string="Buildings", type="integer"),
        'pharmacy_count': fields.function(_pharmacy_count, string="Pharmacies", type="integer"),
    }
    _defaults={
            'is_institution': True,
            'is_company': True
        }

    @api.multi
    def onchange_state(self, state_id):
        if state_id:
            state = self.env['res.country.state'].browse(state_id)
            return {'value': {'country_id': state.country_id.id}}
        return {}

# Health Center Building

class OeHealthCentersBuilding(osv.osv):
    def _ward_count(self, cr, uid, ids, field_name, arg, context=None):
        result = {}
        oe_wards = self.pool.get('oeh.medical.health.center.ward')
        for building in self.browse(cr, uid, ids, context=context):
            domain = [('building', '=', building.id)]
            wards_ids = oe_wards.search(cr, uid, domain, context=context)
            wards = oe_wards.browse(cr, uid, wards_ids, context=context)
            wa_count = 0
            for war in wards:
                wa_count+=1
            result[building.id] = wa_count
        return result

    def _bed_count(self, cr, uid, ids, field_name, arg, context=None):
        result = {}
        oe_beds = self.pool.get('oeh.medical.health.center.beds')
        for building in self.browse(cr, uid, ids, context=context):
            domain = [('building', '=', building.id)]
            beds_ids = oe_beds.search(cr, uid, domain, context=context)
            beds = oe_beds.browse(cr, uid, beds_ids, context=context)
            be_count = 0
            for bed in beds:
                be_count+=1
            result[building.id] = be_count
        return result

    _name = 'oeh.medical.health.center.building'
    _columns = {
        'name' : fields.char ('Name', size=128, required=True, help="Name of the building within the institution"),
        'institution' : fields.many2one ('oeh.medical.health.center','Health Center',required=True),
        'code' : fields.char ('Code', size=64),
        'info' : fields.text ('Extra Info'),
        'ward_count': fields.function(_ward_count, string="Wards", type="integer"),
        'bed_count': fields.function(_bed_count, string="Beds", type="integer"),
        }
    _sql_constraints = [
            ('name_uniq', 'unique (name)', 'The building name must be unique !')]

# Health Center Wards Management

class OeHealthCentersWards(osv.osv):

    GENDER = [
                ('Men Ward','Men Ward'),
                ('Women Ward','Women Ward'),
                ('Unisex','Unisex'),
            ]

    WARD_STATES = [
                ('Beds Available','Beds Available'),
                ('Full','Full'),
            ]

    def _bed_count(self, cr, uid, ids, field_name, arg, context=None):
        result = {}
        oe_beds = self.pool.get('oeh.medical.health.center.beds')
        for ward in self.browse(cr, uid, ids, context=context):
            domain = [('ward', '=', ward.id)]
            beds_ids = oe_beds.search(cr, uid, domain, context=context)
            beds = oe_beds.browse(cr, uid, beds_ids, context=context)
            be_count = 0
            for bed in beds:
                be_count+=1
            result[ward.id] = be_count
        return result

    _name = "oeh.medical.health.center.ward"
    _columns = {
            'name' : fields.char ('Name', size=128, required=True, help="Ward / Room code"),
            'building' : fields.many2one ('oeh.medical.health.center.building','Building',required=True),
            'floor' : fields.integer ('Floor Number'),
            'private' : fields.boolean ('Private Room',help="Check this option for private room"),
            'bio_hazard' : fields.boolean ('Bio Hazard',help="Check this option if there is biological hazard"),
            'telephone' : fields.boolean ('Telephone access'),
            'ac' : fields.boolean ('Air Conditioning'),
            'private_bathroom' : fields.boolean ('Private Bathroom'),
            'guest_sofa' : fields.boolean ('Guest sofa-bed'),
            'tv' : fields.boolean ('Television'),
            'internet' : fields.boolean ('Internet Access'),
            'refrigerator' : fields.boolean ('Refrigerator'),
            'microwave' : fields.boolean ('Microwave'),
            'gender' : fields.selection (GENDER,'Gender'),
            'state': fields.selection(WARD_STATES,'Status'),
            'info' : fields.text ('Extra Info'),
            'bed_count': fields.function(_bed_count, string="Beds", type="integer"),
        }

    _defaults = {
            'gender': lambda *a: 'Unisex',
            'state':'Beds Available',
        }
    _sql_constraints = [
            ('name_ward_uniq', 'unique (name,building)', 'The ward name is already configured in selected building !')]

# Beds Management
class OeHealthCentersBeds(osv.osv):

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
    _name = 'oeh.medical.health.center.beds'
    _description = "Information about the health centers beds"
    _inherits={
        'product.product': 'product_id',
    }
    _columns = {
            'product_id': fields.many2one('product.product', 'Related Product', required=True,ondelete='cascade', help='Product-related data of the hospital beds'),
            'building': fields.many2one ('oeh.medical.health.center.building','Building'),
            'ward': fields.many2one ('oeh.medical.health.center.ward','Ward',domain="[('building', '=', building)]",help="Ward or room", ondelete='cascade'),
            'bed_type': fields.selection(BED_TYPES,'Bed Type', required=True),
            'telephone_number': fields.char ('Telephone Number',size=128, help="Telephone Number / Extension"),
            'info': fields.text ('Extra Info'),
            'state': fields.selection(BED_STATES,'Status'),
            'change_bed_status': fields.selection(CHANGE_BED_STATUS,'Change Bed Status'),
        }
    _defaults = {
            'is_bed': True,
            'bed_type': lambda *a: 'Gatch Bed',
            'state': 'Free',
        }
    _sql_constraints = [
            ('name_bed_uniq', 'unique (name,ward)', 'The bed name is already configured in selected ward !')]

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

    # Preventing deletion of a beds which is not in draft state
    def unlink(self, cr, uid, ids, context=None):
        stat = self.read(cr, uid, ids, ['state'], context=context)
        unlink_ids = []
        for t in stat:
            if t['state'] in ('Free','Not Available'):
                unlink_ids.append(t['id'])
            else:
                raise osv.except_osv(_('Invalid Action!'), _('You can not delete bed(s) which is in "Reserved" or "Occupied" state !!'))
        osv.osv.unlink(self, cr, uid, unlink_ids, context=context)
        return True

    def create(self, cr, uid, vals, context=None):
        if vals.get('change_bed_status') and vals.get('state') and vals.get('state')=="Occupied":
            raise osv.except_osv(_('Error'), _('Bed status can not change if it already occupied!'))
        return super(OeHealthCentersBeds, self).create(cr, uid, vals, context=context)

    def write(self, cr, uid, ids, vals, context=None):
        if 'change_bed_status' in vals:
            if vals['change_bed_status'] in ('Mark as Reserved','Mark as Not Available'):
                for bd in self.browse(cr,uid,ids):
                    if bd.state=="Occupied":
                        raise osv.except_osv(_('Error'), _('Bed status can not change if it already occupied!'))
        return super(OeHealthCentersBeds, self).write(cr, uid, ids, vals, context=context)
