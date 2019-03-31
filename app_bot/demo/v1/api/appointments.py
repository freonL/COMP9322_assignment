# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource, TIMESLOT
from .. import schemas
from requests import get, post

class Appointments(Resource):

    def get(self):
        # print(g.args)
        customer = "{} {}".format(g.args['first_name'], g.args['last_name'])
        url = TIMESLOT.url + "/appointments/byCustomer?name={}".format(customer)
        resp = get(url, headers={'API_KEY': TIMESLOT.apiKey})

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
        url =TIMESLOT.url+"/appointments"
        
        body = {
            'date': g.args['booking_date'],
            'time': g.args['booking_time'],
            'customer': customer,
            'doctor': g.args['dentist_name'].replace("%20"," ")
        }
        

        resp = post(url, json=body,  headers={'API_KEY': TIMESLOT.apiKey})
        if resp.status_code == 200:
            output = {"redirect_to_blocks": ["book.success"]}
        else:
            print(body)
            print(resp.status_code)
            print(resp)
            output = {"redirect_to_blocks": ["book.failed"]}

        return output, 200, None