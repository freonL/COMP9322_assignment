# -*- coding: utf-8 -*-

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###
from __future__ import absolute_import

from .api.appointments import Appointments
from .api.appointments_byCustomer import AppointmentsBycustomer
from .api.appointments_byDoctor import AppointmentsBydoctor
from .api.appointments_id_cancel import AppointmentsIdCancel


routes = [
    dict(resource=Appointments, urls=['/appointments'], endpoint='appointments'),
    dict(resource=AppointmentsBycustomer, urls=['/appointments/byCustomer'], endpoint='appointments_byCustomer'),
    dict(resource=AppointmentsBydoctor, urls=['/appointments/byDoctor'], endpoint='appointments_byDoctor'),
    dict(resource=AppointmentsIdCancel, urls=['/appointments/<id>/cancel'], endpoint='appointments_id_cancel'),
]