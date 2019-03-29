# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas


class DentistsDentistNameTimeslots(Resource):

    def get(self, dentist_name):
        print(g.args)

        return {}, 200, None