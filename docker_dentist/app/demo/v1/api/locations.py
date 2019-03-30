# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g
from mongoengine import connect
from . import Resource
from .. import schemas
from ..models import Dentist


class Locations(Resource):

    def get(self):
        connect(host='mongodb://user1:abc123@ds040877.mlab.com:40877/db_01')
        result = list()
        for dentist in Dentist.objects():
            if dentist.location not in result:
                result.append(dentist.location)
        return result, 200, None