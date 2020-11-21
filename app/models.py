from flask_mongoengine import MongoEngine
import mongoengine_goodjson as gj

db = MongoEngine()


class Goods(gj.Document):
    name = db.StringField(required=True)
    description = db.StringField(required=True)
    parameters = db.DictField()

