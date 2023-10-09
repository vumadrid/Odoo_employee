# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
# from odoo.tools.safe_eval import json
# from bson import json_util
import json
class EvEmployeeController(http.Controller):

    @http.route('/api/ev_employees', auth='public', type='http', methods=['GET'])
    def get_ev_employees(self, **kw):
        employees = request.env['id.card'].sudo().search([])
        employee_list = []
        for employee in employees:
            employee_data = {
                'name': employee.name,
                'id_no': employee.id_no,
                'sex': employee.sex,
                'age': employee.age,
                'birth': employee.birth_place,
                #'birth_date': employee.birth_date,
                'image': employee.image,
                # 'department_id': employee.department_id,
                # 'features_ids': employee.features_ids,
                'reference': employee.reference,

            }
            employee_list.append(employee_data)
            json_obj = json.dumps(employee_list)
            return request.make_response(
                headers=[('Content-Type', 'application/json')],
                content_type='application/json',
                content=json_obj
            )