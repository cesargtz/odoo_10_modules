# -*- coding: utf-8 -*-
from odoo import http

# class StockMoveSum(http.Controller):
#     @http.route('/stock_move_sum/stock_move_sum/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/stock_move_sum/stock_move_sum/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('stock_move_sum.listing', {
#             'root': '/stock_move_sum/stock_move_sum',
#             'objects': http.request.env['stock_move_sum.stock_move_sum'].search([]),
#         })

#     @http.route('/stock_move_sum/stock_move_sum/objects/<model("stock_move_sum.stock_move_sum"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('stock_move_sum.object', {
#             'object': obj
#         })