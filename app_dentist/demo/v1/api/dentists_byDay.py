# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g
from mongoengine import connect
from ..models import Dentist

from . import Resource
from .. import schemas


class DentistsByday(Resource):

    def get(self):
        # print(g.args)
        limit = g.args['limit']
        offset = g.args['offset']
        max_record = offset + limit
        day = g.args['day']

        days = ('monday','tuesday','wednesday','thurday','friday','saturday','sunday')
        if day.lower() not in days:
            return [], 404, None
        result = list()
        
        connect(host='mongodb://user1:abc123@ds040877.mlab.com:40877/db_01')
        for dentist in Dentist.objects():
            print(dentist.work_days)
            
            if len(result) >= max_record:
                break

            if day.lower() in (work_day.lower() for work_day in dentist.work_days):
                print(dentist)
                result.append(dentist)

        return result[offset:max_record], 200, None