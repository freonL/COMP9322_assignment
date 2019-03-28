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
from .api.dentists_byDay import DentistsByday
from .api.dentists_byLoc import DentistsByloc
from .api.dentists_dentistId import DentistsDentistid
from .api.dentists_dentistId_timeslots import DentistsDentistidTimeslots


routes = [
    dict(resource=Locations, urls=['/locations'], endpoint='locations'),
    dict(resource=Dentists, urls=['/dentists'], endpoint='dentists'),
    dict(resource=DentistsByday, urls=['/dentists/byDay'], endpoint='dentists_byDay'),
    dict(resource=DentistsByloc, urls=['/dentists/byLoc'], endpoint='dentists_byLoc'),
    dict(resource=DentistsDentistid, urls=['/dentists/<dentistId>'], endpoint='dentists_dentistId'),
    dict(resource=DentistsDentistidTimeslots, urls=['/dentists/<dentistId>/timeslots'], endpoint='dentists_dentistId_timeslots'),
]