# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas
from requests import get, post

class Appointments(Resource):

    def get(self):
        # print(g.args)
        customer = "{} {}".format(g.args['first_name'], g.args['last_name'])
        url ="http://0.0.0.0:3000/v1/appointments/byCustomer?name={}".format(customer)
        resp = get(url)

        ls = list()
        for res in resp.json():
            ls.append({
                "title": "{} {}".format(res['date'][:10],res['time']),
                "set_attributes": {
                    "booking_time": res['time'], 
                    "booking_date": res['date'][:10]
                }
            })
            pass
        output = {
            "messages": [{
                "text": "Choose your upcoming appointment",
                "quick_replies": ls,
                "quick_reply_options": {
                    "process_text_by_ai": True,
                }
            }]
        }
        return output, 200, None

    def post(self):
        
        customer = "{} {}".format(g.args['first_name'], g.args['last_name'])
        url ="http://0.0.0.0:3000/v1/appointments"

        body = {
            'date': g.args['booking_date'],
            'time': g.args['booking_time'],
            'customer': customer,
            'doctor': g.args['dentist_name']
        }
        

        resp = post(url, json=body)
        if resp.status_code == 200:
            output = {"redirect_to_blocks": ["book.success"]}
        else:
            output = {"redirect_to_blocks": ["book.failed"]}

        return output, 200, None