# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas
from ..models import Appointment
from mongoengine import connect
from mongoengine.queryset.visitor import Q
from datetime import datetime 

class AppointmentsIdCancel(Resource):

    def patch(self, id):
        try:
            connect(host='mongodb://user2:abc123@ds012889.mlab.com:12889/db_02')
            
            Appointment.objects.get(id=id).update(set__status='Available')
        except:
            return {}, 401, None

        return {}, 200, None