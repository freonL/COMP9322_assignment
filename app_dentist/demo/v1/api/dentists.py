# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g
from mongoengine import connect
from . import Resource
from .. import schemas
from ..models import Dentist


class Dentists(Resource):

    def get(self):
        # print(g.args)
        offset = g.args['offset']
        limit = g.args['limit']
        max_rec = offset + limit
        
        for key in g.args: 
            print(key)
        
        connect(host='mongodb://user1:abc123@ds040877.mlab.com:40877/db_01')
        

        return Dentist.objects[offset:max_rec], 200, None