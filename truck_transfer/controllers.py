# -*- coding: utf-8 -*-
from odoo import http

# class TruckTransfer(http.Controller):
#     @http.route('/truck_transfer/truck_transfer/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/truck_transfer/truck_transfer/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('truck_transfer.listing', {
#             'root': '/truck_transfer/truck_transfer',
#             'objects': http.request.env['truck_transfer.truck_transfer'].search([]),
#         })

#     @http.route('/truck_transfer/truck_transfer/objects/<model("truck_transfer.truck_transfer"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('truck_transfer.object', {
#             'object': obj
#         })