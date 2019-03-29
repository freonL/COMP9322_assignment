# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas
from requests import get

class DentistsDentistName(Resource):

    def get(self, dentist_name):
        url = "http://0.0.0.0:5000/v1/dentists/{}".format(dentist_name)
        resp = get(url)
        print(resp)
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