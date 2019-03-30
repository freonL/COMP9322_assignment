# -*- coding: utf-8 -*-
from __future__ import absolute_import

import flask_restful as restful
from flask import request
from ..validators import request_validate, response_filter


def authenticate(func):
    # @wraps(func)
    def wrapper(*args, **kwargs):
        if not getattr(func, 'authenticated', True):
            return func(*args, **kwargs)
        # acct = True  # custom account lookup function

        if request.headers.get("API_KEY") == 'a3b23d9d511e81d63115d21af049cf1f':
            return func(*args, **kwargs)

        restful.abort(401)
    return wrapper

class Resource(restful.Resource):
    method_decorators = [request_validate, response_filter,authenticate]