# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function
from mongoengine.queryset.visitor import Q
from flask import request, g
from mongoengine import connect
from ..models import Dentist
from . import Resource
from .. import schemas


class DentistsDentistid(Resource):

    def get(self, dentistId):
        connect(host='mongodb://user1:abc123@ds040877.mlab.com:40877/db_01')
        
        try:
            result = Dentist.objects.get(id=dentistId)
        except expression as identifier:
            return {}, 404, None
        return result, 200, None