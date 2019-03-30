# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource, DENTIST
from .. import schemas
from requests import get

class Locations(Resource):

    def get(self):
        url = DENTIST.url + "/locations"
        response = get(url,headers={'API_KEY': DENTIST.apiKey})
        ls = list()
        for loc in response.json():
            ls.append({
                'title': loc,
                'set_attributes': {
                    "location": loc
                }
            })

        result = {'messages': [{
            'text' : "There are our clinics location. Which's one near to you?",
            'quick_replies': ls,
            'quick_reply_options': {
                'process_text_by_ai': True,
                'text_attribute_name': "location"
            }
        }]}
        # print(result)
        return result, 200, None