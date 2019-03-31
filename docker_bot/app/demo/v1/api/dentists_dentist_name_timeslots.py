# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource,DENTIST,TIMESLOT
from .. import schemas
from requests import get

class DentistsDentistNameTimeslots(Resource):

    def get(self, dentist_name):
        print(g.args)
        dentist_name = dentist_name.replace("%20"," ")
        print(dentist_name)
        # url = DENTIST.url + "/dentists/{}/timeslots?start_date={}".format(dentist_name,g.args['booking_date'])
        # resp = get(url, headers={'API_KEY': DENTIST.apiKey})
        
        # ls = list()
        # for res in resp.json():
        #     print(res)
        #     if res['status'] == 'Available':
        #         ls.append(res['time'])

        url = TIMESLOT.url + "/appointments/byDoctor?name={}".format(dentist_name)
        resp = get(url, headers={'API_KEY': TIMESLOT.apiKey})
        if len(resp.json()) == 0:
            msg ="{} available the whole day on {}\nDo you want to change?".format(dentist_name,g.args['booking_date'])
        else:
            app_ls = resp.json()
            tm_ls = list(filter(lambda tm: tm['date'] == g.args['booking_date'], app_ls))
            if len(tm_ls) == 0:
                msg ="{} available the whole day on {}\nDo you want to change?".format(dentist_name,g.args['booking_date'])
            else:
                avail = ['09AM','10AM','11AM', '12PM','01PM','02PM','03PM','04PM','05PM']
                for tm in tm_ls:
                    avail.remove(tm['time'])
                
                if len(avail) == 0:
                    msg ="{} not available on {}\nDo you want to change?".format(dentist_name,g.args['booking_date'])
                else:
                    msg ="{} available on {} at : {}\nDo you want to change?".format(dentist_name,g.args['booking_date'], ", ".join(avail))

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