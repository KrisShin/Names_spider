'''
Author: Kris Shin
Edit Time: 18-11-11 16:32:04
'''

# Create your models here.
from mongoengine import connect, Document, StringField
from namesdj.settings import DBNAME

connect(DBNAME,host='127.0.0.1')


class NamesModel(Document):
    first_name = StringField(max_length=3)
    f_url = StringField(max_length=512)
    name = StringField(max_length=50)
    name_url = StringField(max_length=512)
    detail = StringField(max_length=1024)
