# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas

from mongoengine import connect
from ..models import Dentist
from mongoengine.queryset.visitor import Q
from datetime import date, timedelta

class DentistsDentistNameTimeslots(Resource):

    def get(self, dentist_name):
        print(g.args)
        connect(host='mongodb://user1:abc123@ds040877.mlab.com:40877/db_01')
        result = list()
        try:
            dentist = Dentist.objects.get(id=dentistId)
        except expression as identifier:
            return {}, 404, None
            
        today_dt = date.today()
        weekdays = ('Monday','Tuesday','Wednesday','Thurday','Friday','Saturday','Sunday')
        print(dentist.work_days)
        for dt in (today_dt + timedelta(n) for n in range(14)): 
            if weekdays[dt.weekday()] in dentist.work_days:
                print(dt, dt.weekday(), weekdays[dt.weekday()])
                pass

        return {}, 200, None