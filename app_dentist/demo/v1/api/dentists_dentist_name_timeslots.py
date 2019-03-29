# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas

from mongoengine import connect
from ..models import Dentist
from mongoengine.queryset.visitor import Q
from datetime import date, timedelta, datetime
from requests import get

def daterange(start_date, end_date):
    for n in range(int (( (end_date +  timedelta(1) )- start_date).days)):
        yield start_date + timedelta(n)

class DentistsDentistNameTimeslots(Resource):

    def get(self, dentist_name):
        # print(g.args)
        connect(host='mongodb://user1:abc123@ds040877.mlab.com:40877/db_01')
        result = list()
        try:
            dentist = Dentist.objects.get(name__iexact = dentist_name)
        except expression as identifier:
            return {}, 404, None
            
        today_dt = date.today()
        start_dt = datetime.strptime( g.args['start_date'],'%Y-%m-%d').date()
        try:
            end_dt = datetime.strptime( g.args['end_date'],'%Y-%m-%d' ).date()
        except:
            end_dt = start_dt
        

        if start_dt < today_dt:
            start_dt = today_dt
        
        if end_dt < start_dt:
            end_dt = start_dt + timedelta(1)
        try:
            url = "http://0.0.0.0:3000/v1/appointments/byDoctor?name={}".format(dentist_name)
            responses = get(url)
            
            
            
        except :
            return {}, 501, None
        reserved_set = list()
        # result.append({'date':'2019-03-30', 'time':'07AM','status':'Reserved'})
        for A in responses.json():
            reserved_set.append((A['date'][:10], A['time']))
            result.append({
                'date': A['date'][:10],
                'time': A['time'],
                'status': "Reserved",
            })
        time_ls = ['09AM','10AM','11AM', '12PM','01PM','02PM','03PM','04PM','05PM']
        # print(today_dt, start_dt, end_dt)
        
        for single_date in daterange(start_dt, end_dt  ):
            if single_date.strftime("%A")  in dentist.work_days:
                for tm in time_ls:
                    if (single_date.strftime("%Y-%m-%d"), tm) not in reserved_set:
                        result.append({
                            'date': single_date.strftime("%Y-%m-%d"),
                            'time': tm,
                            'status': "Available",
                        })
                    
                    
                    # print (single_date.strftime("%Y-%m-%d"), tm)
        
        return result, 200, None