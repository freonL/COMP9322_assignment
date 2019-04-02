# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource,DENTIST
from .. import schemas
from requests import get

class DentistsDentistName(Resource):

    def get(self, dentist_name):
        url = DENTIST.url+"/dentists/{}".format(dentist_name)
        resp = get(url, headers={'API_KEY': DENTIST.apiKey})
        
        res = resp.json()
        temp = "{} work on {} has specialities in: {}.\nWorking days: {}\nDo you want to make appointment with {}?".format(res['name'], res['location'], ", ".join(res['specialities']), ", ".join(res['work_days']), format(res['name']))


        output = {
            'messages': [{
                "text": temp,
                "quick_replies": [
                    {
                        "title": "Yes",
                        "block_names": [
                            "book.check"
                        ]
                    },
                    {
                        "title": "His/er Avaiblity",
                        "block_names": [
                            "dentist.timeslot"
                        ]
                    },
                    {
                        "title": "No, search again",
                        "block_names": [
                            "book.dentist"
                        ]
                    }
                ]
            }]
        }
        return output, 200, None