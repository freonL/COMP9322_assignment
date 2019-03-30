from mongoengine import StringField, DateTimeField, IntField, Document, ListField, BooleanField


class Dentist(Document):
    id = StringField(required=True, primary_key=True)
    name = StringField(max_length=50)
    location = StringField(max_length=50)
    work_days = ListField(StringField(max_length=15))
    specialities = ListField(StringField(max_length=30))
    def __init__(self, name, location, work_days=[], specialities=[], *args, **kwargs):
        super().__init__(*args, **kwargs) 
        self.name = name
        self.location = location
        self.work_days = work_days
        self.specialities = specialities