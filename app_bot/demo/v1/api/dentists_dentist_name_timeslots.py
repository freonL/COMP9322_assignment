# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource,DENTIST
from .. import schemas
from requests import get

class DentistsDentistNameTimeslots(Resource):

    def get(self, dentist_name):
        print(g.args)
        url = DENTIST.url + "/dentists/{}/timeslots?start_date={}".format(dentist_name,g.args['booking_date'])
        resp = get(url)

        ls = list()
        for res in resp.json():
            print(res)
            if res['status'] == 'Available':
                ls.append(res['time'])

        msg ="{}'s available on {} at these time: {}\nDo you want to change?".format(dentist_name,g.args['booking_date'], ', '.join(ls))
        output = {
            "messages": [{
                'text': msg,
                "quick_replies": [
                    {
                        "title": "Yes",
                        "block_names": [
                            "book.datetime"
                        ]
                    },
                    {
                        "title": "No",
                        "block_names": [
                            "book.confirm"
                        ]
                    }
                ]
            }]
        }
        return output, 200, None