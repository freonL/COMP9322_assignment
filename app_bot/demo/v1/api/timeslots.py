# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas
from requests import get

class Timeslots(Resource):

    def get(self):
        # print(g.args)
        
        url = "http://0.0.0.0:3000/v1/appointments/byDoctor?name={}".format(g.args['dentist_name'])
        output = {"redirect_to_blocks": ["book.confirm"]}
        resp = get(url)
        # print(resp)
        for res in resp.json():
            # print(res)
            if res['date'][:10] == g.args['booking_date'] and res['time'] == g.args['booking_time']:
                output = {"redirect_to_blocks": ["book.timeslot_fail"]}
                break

        return output, 200, None