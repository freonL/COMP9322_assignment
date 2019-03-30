# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas
from ..models import Appointment
from mongoengine import connect
from mongoengine.queryset.visitor import Q
from datetime import datetime 

class AppointmentsBydoctor(Resource):

    def get(self):
        print(g.args)
        doctor = g.args['name'].lower()
        try:
            connect(host='mongodb://user2:abc123@ds012889.mlab.com:12889/db_02')
            appointments = Appointment.objects(Q(doctor__iexact=doctor) & Q(status="reserved") & Q(date__gte=datetime.now().strftime('%Y-%m-%d') ))

        except:
            return [], 405, None
        return appointments, 200, None