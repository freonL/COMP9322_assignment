# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas

from mongoengine import connect
from ..models import Dentist
from mongoengine.queryset.visitor import Q

class DentistsDentistName(Resource):

    def get(self, dentist_name):
        connect(host='mongodb://user1:abc123@ds040877.mlab.com:40877/db_01')
        
        try:
            result = Dentist.objects.get(id=dentistId)
        except expression as identifier:
            return {}, 404, None
        return result, 200, None