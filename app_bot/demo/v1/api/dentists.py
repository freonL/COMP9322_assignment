# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource, DENTIST
from .. import schemas

from requests import get
from datetime import datetime


class Dentists(Resource):

    def get(self):

        ls = list()
        
        url = DENTIST.url+"/dentists?offset={}&limit={}".format(0,10)

        try:
            url = url + "&location={}".format(g.args['location'])
        except :
            pass
        try:
            url = url + "&name={}".format(g.args['dentist_name'])
        except :
            pass

        resp = get(url)
        try:
            day = datetime.strptime(g.args['booking_date'],'%Y-%m-%d').strftime('%A')
        except :
            day = datetime.now().strftime('%A')
        
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
                'text': "There are our results\nWhich dentist you want to choose?",
                "quick_replies": ls,
                "quick_reply_options": {
                    "process_text_by_ai": True,
                    "text_attribute_name": "dentist_name"
                }
            }]
        }
        return output, 200, None