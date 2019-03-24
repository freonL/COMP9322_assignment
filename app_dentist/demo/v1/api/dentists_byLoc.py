# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g
from mongoengine import connect
from ..models import Dentist
from . import Resource
from .. import schemas


class DentistsByloc(Resource):

    def get(self):
        # print(g.args)
        location = g.args['location']
        offset = g.args['offset']
        limit = g.args['limit']

        connect(host='mongodb://user1:abc123@ds040877.mlab.com:40877/db_01')
        result = Dentist.objects(Q(location__exact=location))
        return result[offset:offset+limit], 200, None