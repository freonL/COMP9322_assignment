# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas
from mongoengine import connect
from mongoengine.queryset.visitor import Q
from ..models import Appointment
from datetime import datetime 
from uuid import uuid4

class Appointments(Resource):

    def post(self):
        print(g.json)
        connect(host='mongodb://user2:abc123@ds012889.mlab.com:12889/db_02')
        try:
            customer = g.json['customer'].lower()
            doctor = g.json['doctor'].lower()
            time = g.json['time']
            dt = g.json['date']
            dt = datetime.strptime(dt, '%Y-%m-%d')
            # check other appointment by date time and doctor
            # timeslot = Appointment.objects.get( Q(doctor=doctor) & Q(date=dt) & Q(time=time) & Q(status=False) ) 
            # if timeslot:
            #     return {}, 405, None
        except :
            return {}, 405, None
        
        appointment = Appointment(id = str(uuid4()),date=dt, time=time, doctor=doctor, customer=customer)
        appointment.save()

        output = {
            'id': str(appointment.id),
            'date': str(appointment.date)[:10],
            'time': appointment.time,
            'doctor': appointment.doctor,
            'customer': appointment.customer,
            'status': "reserved"
        }

        return appointment, 200, None