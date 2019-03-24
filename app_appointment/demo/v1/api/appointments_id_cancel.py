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
            timeslot = Appointment.objects.get(id=id) 
            if timeslot is None:
                return {}, 404, None
            timeslot.update_one(set__status=True)
        except expression as identifier:
            return {}, 404, None

        return {}, 200, None