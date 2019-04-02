# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas

from requests import get
from datetime import datetime

class Datetime(Resource):

    def get(self):
        print(g.args)
        AUTH = 'Bearer 2RDKA3BKYCEZ55IBFL4NIYNFSSEXF5OD'
        url = "https://api.wit.ai/message?v=20190330&q={}".format(g.args['datetime_exp'])

        result = get(url, headers={'Authorization': AUTH}).json()
        output = None
        try:
            print(result['entities']['datetime'][0]['value'][:13])
            output_dt = datetime.strptime(result['entities']['datetime'][0]['value'][:13], '%Y-%m-%dT%H')
            booking_date = output_dt.strftime('%Y-%m-%d')
            booking_time = output_dt.strftime('%I%p')
            
            
            time_ls = ['09AM','10AM','11AM', '12PM','01PM','02PM','03PM','04PM','05PM']
            if booking_time in time_ls:
                output = {
                    'set_attributes': {
                        'booking_date' : booking_date,
                        'booking_time' : booking_time
                    }
                }

            else:
                
                ls = list()
                print('21')
                for tm in time_ls:

                    ls.append({
                        'title': tm,
                        'set_attributes': {
                            "booking_time": tm
                        },
                    })

                
                output = {
                    'set_attributes': {
                        'booking_date' : booking_date,
                    },
                    'messages': [{
                        'text': "What's time you like?",
                        'quick_replies': ls,
                        'quick_reply_options': {
                            'process_text_by_ai': True,
                            'text_attribute_name': "booking_time"
                        }
                    }]
                }
                pass
            
        except :
            output = {"redirect_to_blocks": ["book.datetime"]}
        print(output)
        return output, 200, None