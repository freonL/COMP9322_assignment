# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas

from requests import get
from datetime import datetime

class Dentists(Resource):

    def get(self):
        # print(g.args)
        url = "http://0.0.0.0:5000/v1/dentists?offset={}&limit={}&location={}&name={}".format(0,10,g.args['location'],g.args['dentist_name'])
        ls = list()
        resp = get(url)
        day = datetime.strptime(g.args['booking_date'],'%Y-%m-%d').strftime('%A')
        for res in resp.json():
            if day in res['work_days']:
                ls.append({
                    "title": res['name'],
                    "set_attributes": {
                        "dentist_name": res['name']
                    }
                })

        output = {
            "messages":[{
                'text': "There are our results\nWhich you want to choose?",
                "quick_replies": ls,
                "quick_reply_options": {
                    "process_text_by_ai": True,
                    "text_attribute_name": "dentist_name"
                }
            }]
        }
        return output, 200, None