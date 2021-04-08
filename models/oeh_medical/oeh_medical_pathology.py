##############################################################################
#    Copyright (C) 2015 oeHealth (<http://oehealth.in>). All Rights Reserved
#    oeHealth, Hospital Management Solutions
##############################################################################

import openerp
from openerp import SUPERUSER_ID
from openerp import pooler, tools, api
from openerp.osv import osv, fields
from openerp.tools.translate import _

class OeHealthPathologyCategory(osv.osv):
        def name_get(self, cr, uid, ids, context={}):
                if not len(ids):
                        return []
                reads = self.read(cr, uid, ids, ['name','parent_id'], context)
                res = []
                for record in reads:
                        name = record['name']
                        if record['parent_id']:
                                name = record['parent_id'][1]+' / '+name
                        res.append((record['id'], name))
                return res

        def _name_get_fnc(self, cr, uid, ids, prop, foo, faa):
                res = self.name_get(cr, uid, ids)
                return dict(res)
        def _check_recursion(self, cr, uid, ids):
                level = 100
                while len(ids):
                        cr.execute('select distinct parent_id from oeh_medical_pathology_category where id in ('+','.join(map(str,ids))+')')
                        ids = filter(None, map(lambda x:x[0], cr.fetchall()))
                        if not level:
                                return False
                        level -= 1
                return True

        _description='Disease Categories'
        _name = 'oeh.medical.pathology.category'
        _columns = {
                'name': fields.char('Category Name', required=True, size=128),
                'parent_id': fields.many2one('oeh.medical.pathology.category', 'Parent Category', select=True),
                'complete_name': fields.function(_name_get_fnc, method=True, type="char", string='Name'),
                'child_ids': fields.one2many('oeh.medical.pathology.category', 'parent_id', 'Children Category'),
                'active' : fields.boolean('Active'),
        }
        _constraints = [
                (_check_recursion, 'Error ! You can not create recursive categories.', ['parent_id'])
        ]
        _defaults = {
                'active' : lambda *a: 1,
        }
        _order = 'parent_id,id'


class OeHealthPathology(osv.osv):
    _name = "oeh.medical.pathology"
    _description = "Diseases"
    _columns = {
        'name' : fields.char ('Disease Name', size=128, help="Disease name",required=True),
        'code' : fields.char ('Code', size=32, help="Specific Code for the Disease (eg, ICD-10, SNOMED...)"),
        'category' : fields.many2one('oeh.medical.pathology.category','Disease Category'),
        'chromosome' : fields.char ('Affected Chromosome', size=128, help="chromosome number"),
        'protein' : fields.char ('Protein involved', size=128, help="Name of the protein(s) affected"),
        'gene' : fields.char ('Gene', size=128, help="Name of the gene(s) affected"),
        'info' : fields.text ('Extra Info'),
    }

    _sql_constraints = [
            ('code_uniq', 'unique (code)', 'The disease code must be unique')]


    def name_search(self, cr, uid, name, args=[], operator='ilike', context={}, limit=80):
            args2 = args[:]
            if name:
                    args += [('name', operator, name)]
                    args2 += [('code', operator, name)]
            ids = self.search(cr, uid, args, limit=limit)
            ids += self.search(cr, uid, args2, limit=limit)
            res = self.name_get(cr, uid, ids, context)
            return res