# -*- coding: utf-8 -*-

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###
from __future__ import absolute_import

from .api.locations import Locations
from .api.dentists import Dentists
from .api.dentists_dentist_name import DentistsDentistName
from .api.dentists_dentist_name_timeslots import DentistsDentistNameTimeslots


routes = [
    dict(resource=Locations, urls=['/locations'], endpoint='locations'),
    dict(resource=Dentists, urls=['/dentists'], endpoint='dentists'),
    dict(resource=DentistsDentistName, urls=['/dentists/<dentist_name>'], endpoint='dentists_dentist_name'),
    dict(resource=DentistsDentistNameTimeslots, urls=['/dentists/<dentist_name>/timeslots'], endpoint='dentists_dentist_name_timeslots'),
]