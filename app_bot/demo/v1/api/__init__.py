# -*- coding: utf-8 -*-
from __future__ import absolute_import

import flask_restful as restful

from ..validators import request_validate, response_filter



class Resource(restful.Resource):
    method_decorators = [request_validate, response_filter]

class MicroServices():
    def __init__(self, url = 'http://0.0.0.0', key=''):
        self.url = url
        self.key = key

DENTIST = MicroServices("http://0.0.0.0:5000/v1")
TIMESLOT = MicroServices("http://0.0.0.0:3000/v1")