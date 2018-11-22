'''
Author: Kris Shin
Edit Time: 18-11-11 16:32:04
'''
# Create your models here.
import mongoengine


class NamesModel(mongoengine.Document):
    first_name = mongoengine.StringField(max_length=3)
    f_url = mongoengine.StringField(max_length=512)
    name = mongoengine.StringField(max_length=50)
    name_url = mongoengine.StringField(max_length=512)
    detail = mongoengine.StringField(max_length=1024)