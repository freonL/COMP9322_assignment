# -*- coding: utf-8 -*-
from __future__ import absolute_import

import flask_restful as restful

from ..validators import request_validate, response_filter



class Resource(restful.Resource):
    method_decorators = [request_validate, response_filter]

class MicroServices():
    def __init__(self, url = 'http://0.0.0.0', key=''):
        self.url = url
        self.apiKey = key

DENTIST = MicroServices("http://127.0.0.1:5000/v1","d279e9604a129f48f5ff39dc6bee6546")
TIMESLOT = MicroServices("http://127.0.0.1:3000/v1","a3b23d9d511e81d63115d21af049cf1f")