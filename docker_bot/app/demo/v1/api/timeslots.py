# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource, TIMESLOT
from .. import schemas
from requests import get

class Timeslots(Resource):

    def get(self):
        print(g.args)
        
        url = TIMESLOT.url + "/appointments/byDoctor?name={}".format(g.args['dentist_name'].replace("%20"," "))
        output = {"redirect_to_blocks": ["book.confirm"]}
        resp = get(url,headers={'API_KEY': TIMESLOT.apiKey})
        # print(resp)
        for res in resp.json():
            # print(res)
            if res['date'][:10] == g.args['booking_date'] and res['time'] == g.args['booking_time']:
                output = {"redirect_to_blocks": ["book.timeslot_fail"]}
                break

        return output, 200, None