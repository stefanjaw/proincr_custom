# -*- coding: utf-8 -*-
from odoo import http

# class Fields(http.Controller):
#     @http.route('/fields/fields/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fields/fields/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('fields.listing', {
#             'root': '/fields/fields',
#             'objects': http.request.env['fields.fields'].search([]),
#         })

#     @http.route('/fields/fields/objects/<model("fields.fields"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fields.object', {
#             'object': obj
#         })