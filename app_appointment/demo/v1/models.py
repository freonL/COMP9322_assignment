from mongoengine import StringField, DateTimeField, IntField, Document, ListField, BooleanField


class Appointment(Document):
    id = StringField(required=True, primary_key=True)    
    date = DateTimeField(required=True)
    time = StringField(required=True, max_length=4)
    doctor = StringField(max_length=50, required=True)
    customer = StringField(max_length=50, required=True)
    status = StringField(max_length=10, default="reserved")
    def __init__(self,id, date, time, doctor, customer, *args, **kwargs):
        super().__init__(*args, **kwargs) 
        self.id = id
        self.date = date
        self.time = time
        self.doctor = doctor
        self.customer = customer