# -*- coding: utf-8 -*-
from openerp import http

# class Dmhealth(http.Controller):
#     @http.route('/dmhealth/dmhealth/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dmhealth/dmhealth/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('dmhealth.listing', {
#             'root': '/dmhealth/dmhealth',
#             'objects': http.request.env['dmhealth.dmhealth'].search([]),
#         })

#     @http.route('/dmhealth/dmhealth/objects/<model("dmhealth.dmhealth"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dmhealth.object', {
#             'object': obj
#         })