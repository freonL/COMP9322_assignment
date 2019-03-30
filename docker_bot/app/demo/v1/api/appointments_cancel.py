# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource, TIMESLOT
from .. import schemas

from requests import get, patch

class AppointmentsCancel(Resource):

    def post(self):
        # print(g.args)
        customer = "{} {}".format(g.args['first_name'], g.args['last_name'])
        url = TIMESLOT.url + "/appointments/byCustomer?name={}".format(customer)
        responses = get(url, headers={'API_KEY': TIMESLOT.apiKey})
        output = {"redirect_to_blocks": ["cancel.fail"]}
        for res in responses.json():
            if g.args['booking_time'] == res['time'][:10] and g.args['booking_date']:
                url = TIMESLOT.url+"/appointments/{}/cancel".format(res['id'])
                cancel = patch(url)
                if cancel.status_code == 200:
                    output = {"redirect_to_blocks": ["cancel.success"]}
                break
        return output, 200, None