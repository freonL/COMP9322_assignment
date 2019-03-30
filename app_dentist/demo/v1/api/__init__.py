# -*- coding: utf-8 -*-
from __future__ import absolute_import
from flask import request
import flask_restful as restful

from ..validators import request_validate, response_filter
import functools

def authenticate(func):
    # @wraps(func)
    def wrapper(*args, **kwargs):
        if not getattr(func, 'authenticated', True):
            return func(*args, **kwargs)
        # acct = True  # custom account lookup function

        if request.headers.get("API_KEY") == 'd279e9604a129f48f5ff39dc6bee6546':
            return func(*args, **kwargs)

        restful.abort(401)
    return wrapper


class Resource(restful.Resource):
    method_decorators = [request_validate, response_filter,authenticate]

