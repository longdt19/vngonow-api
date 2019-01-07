from api.common.base_models import BaseDocument, db, STRING_LENGTH

class Product(BaseDocument):
    name = db.StringField(max_length=STRING_LENGTH['LONG'], required=True)
    price = db.IntField()
    category = db.StringField(max_length=STRING_LENGTH['LONG'], required=True)
    image_id = db.ObjectIdField()
    country = db.StringField(max_length=STRING_LENGTH['LONG'], required=True)


class Sim(Product):
    owned = db.StringField(max_length=STRING_LENGTH['LONG'], required=True)
    day_used = db.IntField()


class Wifi(Product):
    internet_name = db.StringField(max_length=STRING_LENGTH['LONG'], required=True)
    connections = db.IntField()
    download_speed = db.StringField(max_length=STRING_LENGTH['LONG'], required=True)
    upload_speed = db.StringField(max_length=STRING_LENGTH['LONG'], required=True)
    information = db.StringField(max_length=STRING_LENGTH['LONG'], required=True)
    prepayment = db.IntField()
    continent = db.StringField(max_length=STRING_LENGTH['LONG'], required=True)
