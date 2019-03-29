# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g
from mongoengine import connect
from . import Resource
from .. import schemas
from ..models import Dentist
from mongoengine.queryset.visitor import Q


class Dentists(Resource):

    def get(self):
        # print(g.args)
        offset = g.args['offset']
        limit = g.args['limit']
        max_rec = offset + limit
        
        condition = None
        if 'name' in g.args:
            if g.args['name'] is not '':
                condition = Q(name__icontains=g.args['name'])
        
        if 'location' in g.args:
            if g.args['location'] is not '':
                if condition is None:
                    condition = Q(location__iexact=g.args['location'])
                else:
                    condition &= Q(location__iexact=g.args['location'])
        connect(host='mongodb://user1:abc123@ds040877.mlab.com:40877/db_01')

        return Dentist.objects(condition)[offset:max_rec], 200, None