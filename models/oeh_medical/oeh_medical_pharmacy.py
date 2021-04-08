##############################################################################
#    Copyright (C) 2015 oeHealth (<http://oehealth.in>). All Rights Reserved
#    oeHealth, Hospital Management Solutions
##############################################################################

from openerp import pooler, tools, api
from openerp.osv import osv, fields
import openerp.addons.decimal_precision as dp
import datetime
from openerp.tools.translate import _

# Pharmacy Management

class OeHealthPharmacy(osv.osv):
    _name = 'oeh.medical.health.center.pharmacy'
    _description = "Information about the pharmacy"
    _inherits={
        'res.partner': 'partner_id',
    }

    _columns = {
        'partner_id': fields.many2one('res.partner', 'Related Partner', required=True,ondelete='cascade', help='Partner-related data of the hospitals'),
        'pharmacist_name': fields.many2one('oeh.medical.physician','Pharmacist Name', domain=[('is_pharmacist','=',True)], required=True),
        'institution' : fields.many2one ('oeh.medical.health.center','Health Center'),
        'pharmacy_lines': fields.one2many('oeh.medical.health.center.pharmacy.line', 'pharmacy_id', 'Pharmacy Lines'),
        'info':fields.text('Extra Information'),
    }
    _defaults={
        'is_pharmacy': lambda *a: True,
        'is_company': lambda *a: True
    }

    @api.multi
    def onchange_state(self, state_id):
        if state_id:
            state = self.env['res.country.state'].browse(state_id)
            return {'value': {'country_id': state.country_id.id}}
        return {}

class OeHealthPharmacyLines(osv.osv):
    _name = 'oeh.medical.health.center.pharmacy.line'
    _description = 'Pharmacy Lines'

    STATES = [
        ('Draft', 'Draft'),
        ('Invoiced', 'Invoiced'),
    ]

    def _amount_all(self, cr, uid, ids, field_name=None, arg=None, context=None):
        res = {}
        for order in self.browse(cr, uid, ids, context=context):
            res[order.id] = {
                'amount_total': 0.0,
            }
            val = 0.0
            for line in order.prescription_lines:
                val += line.price_subtotal
            res[order.id]['amount_total'] = val
        return res

    _columns = {
        'name': fields.many2one('oeh.medical.prescription', 'Prescription #', required=True, ondelete='cascade', readonly=True, states={'Draft': [('readonly', False)]}),
        'patient': fields.many2one('oeh.medical.patient','Patient', help="Patient Name", required=True, readonly=True, states={'Draft': [('readonly', False)]}),
        'doctor': fields.many2one('oeh.medical.physician','Physician', help="Current primary care / family doctor", domain=[('is_pharmacist','=',False)], readonly=True, states={'Draft': [('readonly', False)]}),
        'prescription_lines': fields.one2many('oeh.medical.health.center.pharmacy.prescription.line', 'prescription_id', 'Prescription Lines', readonly=True, states={'Draft': [('readonly', False)]}),
        'pharmacy_id': fields.many2one('oeh.medical.health.center.pharmacy', 'Pharmacy Reference', readonly=True, states={'Draft': [('readonly', False)]}),
        'amount_total': fields.function(_amount_all, digits_compute=dp.get_precision('Account'), string='Total',
            store=True, multi='sums', help="The total amount."),
        'pricelist_id': fields.many2one('product.pricelist', 'Pricelist', help="Pricelist for current prescription", readonly=True, states={'Draft': [('readonly', False)]}),
        'currency_id': fields.related('pricelist_id', 'currency_id', type="many2one", relation="res.currency", string="Currency", readonly=True),
        'info':fields.text('Extra Information', readonly=True, states={'Draft': [('readonly', False)]}),
        'state': fields.selection(STATES, 'State',readonly=True),
    }
    _defaults={
        'state': lambda *a: 'Draft',
    }

    # Fetching prescription lines values
    def onchange_prescription_id(self, cr, uid, ids, prescription_id=False,context=None):
        phar_pres_line_obj = self.pool.get('oeh.medical.health.center.pharmacy.prescription.line')
        pres_line_obj = self.pool.get('oeh.medical.prescription.line')
        pres_obj = self.pool.get('oeh.medical.prescription')
        med_obj = self.pool.get('oeh.medical.medicines')
        prescription_ids =[]


        if context is None:
            context = {}
        #delete old prescription lines
        old_pres_line_ids = ids and phar_pres_line_obj.search(cr, uid, [('prescription_id', '=', ids[0])], context=context) or False
        if old_pres_line_ids:
            phar_pres_line_obj.unlink(cr, uid, old_pres_line_ids, context=context)


        #defaults
        res = {'value':{
                      'prescription_lines':[],
                      'doctor':'',
                      'patient':'',
                }
            }

        if (not prescription_id):
            return res

        # Getting prescription values
        pr = pres_obj.browse(cr, uid, prescription_id, context=context)
        res['value'].update({
                'patient': pr.patient.id,
                'doctor':pr.doctor.id,
        })

        # Getting prescription lines values
        pres_line_ids1 = pres_line_obj.search(cr, uid, [('prescription_id', '=', prescription_id)], context=context)
        if pres_line_ids1:
            for pr_line_id in pres_line_obj.browse(cr, uid, pres_line_ids1, context=context):

                    # Getting item pricing
                    med_price = 0.0
                    med_price_ids1 = med_obj.search(cr, uid, [('id', '=', pr_line_id.name.id)], context=context)
                    if med_price_ids1:
                        for med_id in med_obj.browse(cr, uid, med_price_ids1, context=context):
                            med_price = med_id.lst_price
                    pres = {
                              'name': pr_line_id.name.id,
                              'indication':pr_line_id.indication.id,
                              'qty': pr_line_id.qty,
                              'actual_qty': pr_line_id.qty,
                              'price_unit': med_price,
                              'price_subtotal': pr_line_id.qty * med_price,
                            }
                    prescription_ids += [pres]

            res['value'].update({
                        'prescription_lines': prescription_ids,
            })
        return res

    def button_compute(self, cr, uid, ids,context=None):
        self._amount_all(cr, uid, ids, context=context)
        return True


    # Create Prescription invoice

    def _default_account(self,cr,uid,ids,context=None):
        journal_ids = self.pool.get('account.journal').search(cr,uid,[('type', '=', 'sale')],context=context, limit=1)
        journal = self.pool.get('account.journal').browse(cr, uid, journal_ids, context=context)
        return journal.default_credit_account_id.id

    def action_prescription_invoice_create(self, cr, uid, ids, context=None):
        if context is None:
            context = {}
        invoice_obj = self.pool.get("account.invoice")
        invoice_line_obj = self.pool.get("account.invoice.line")
        inv_ids = []

        for pres in self.browse(cr, uid, ids, context=context):
            # Create Invoice
            if pres.patient:
                curr_invoice = {
                    'partner_id': pres.patient.partner_id.id,
                    'account_id': pres.patient.partner_id.property_account_receivable_id.id,
                    'patient': pres.patient.id,
                    'state': 'draft',
                    'type':'out_invoice',
                    'date_invoice': datetime.datetime.now(),
                    'origin': pres.name.name,
                }

                inv_ids = invoice_obj.create(cr, uid, curr_invoice, context)

                if inv_ids:
                    prd_account_id = self._default_account(cr,uid,ids,context)
                    if pres.prescription_lines:
                        for ps in pres.prescription_lines:

                            # Create Invoice line
                            curr_invoice_line = {
                                'name': ps.name.product_id.name,
                                'product_id': ps.name.product_id.id,
                                'price_unit': ps.price_unit,
                                'quantity': ps.actual_qty,
                                'account_id':prd_account_id,
                                'invoice_id':inv_ids,
                            }

                            inv_line_ids = invoice_line_obj.create(cr, uid, curr_invoice_line, context)

                            #invoice_obj.button_compute(cr, uid, [inv_ids], context=context, set_total=('type' in ('in_invoice', 'in_refund')))

                res = self.write(cr, uid, [pres.id], {'state': 'Invoiced'})

        return res

    # Preventing deletion of a prescription which is not in draft state
    def unlink(self, cr, uid, ids, context=None):
        stat = self.read(cr, uid, ids, ['state'], context=context)
        unlink_ids = []
        for t in stat:
            if t['state'] in ('Draft'):
                unlink_ids.append(t['id'])
            else:
                raise osv.except_osv(_('Invalid Action!'), _('You can not delete a prescription which is in "Invoiced" state !!'))
        osv.osv.unlink(self, cr, uid, unlink_ids, context=context)
        return True

class OeHealthPharmacyMedicineLines(osv.osv):
    _name = 'oeh.medical.health.center.pharmacy.prescription.line'
    _description = 'Pharmacy Medicine Lines'

    def _amount_line(self, cr, uid, ids, field_name, arg, context=None):
        res = {}
        if context is None:
            context = {}
        for line in self.browse(cr, uid, ids, context=context):
            price = line.price_unit * line.actual_qty
            res[line.id] = price
        return res

    _columns = {
        'name': fields.many2one('oeh.medical.medicines','Medicines',help="Prescribed Medicines",domain=[('medicament_type','=','Medicine')], required=True),
        'indication': fields.many2one('oeh.medical.pathology','Indication',help="Choose a disease for this medicament from the disease list. It can be an existing disease of the patient or a prophylactic."),
        'qty': fields.integer('Prescribed Qty',help="Quantity of units (eg, 2 capsules) of the medicament"),
        'actual_qty': fields.integer('Actual Qty Given', help="Actual quantity given to the patient"),
        'prescription_id': fields.many2one('oeh.medical.health.center.pharmacy.line', 'Pharmacy Prescription Reference'),
        'price_unit': fields.float('Unit Price', required=True, digits_compute= dp.get_precision('Product Price')),
        'price_subtotal': fields.function(_amount_line, string='Subtotal', digits_compute= dp.get_precision('Account')),
    }
    _defaults={
        'price_unit': lambda *a: 0.0,
        'price_subtotal': lambda *a: 0.0,
    }

    # Autopopulate selected medicine values
    def onchange_medicine_id(self, cr, uid, ids, medicine=False,context=None):
        if context is None:
            context = {}
        result = {}
        if medicine:
            med_obj = self.pool.get('oeh.medical.medicines')
            med_price_ids1 = med_obj.search(cr, uid, [('id', '=', medicine)], context=context)
            if med_price_ids1:
                for med_id in med_obj.browse(cr, uid, med_price_ids1, context=context):
                    result['price_unit'] = med_id.lst_price
        return {'value': result}

    # Change subtotal pricing
    def onchange_qty_and_price(self, cr, uid, ids, qty=False,price_unit=False,context=None):
        if context is None:
            context = {}
        result = {}
        if qty and price_unit:
            result['price_subtotal'] = price_unit * qty
        return {'value': result}
