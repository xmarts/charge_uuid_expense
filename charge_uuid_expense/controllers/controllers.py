# -*- coding: utf-8 -*-
from odoo import http

# class ChargeUuidExpense(http.Controller):
#     @http.route('/charge_uuid_expense/charge_uuid_expense/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/charge_uuid_expense/charge_uuid_expense/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('charge_uuid_expense.listing', {
#             'root': '/charge_uuid_expense/charge_uuid_expense',
#             'objects': http.request.env['charge_uuid_expense.charge_uuid_expense'].search([]),
#         })

#     @http.route('/charge_uuid_expense/charge_uuid_expense/objects/<model("charge_uuid_expense.charge_uuid_expense"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('charge_uuid_expense.object', {
#             'object': obj
#         })